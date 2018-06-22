#!/usr/bin/env python
# encoding: utf-8
"""
manageglsevents.py

Created by Anne Pajon on 2013-08-05.
"""

################################################################################
# IMPORTS
################################################################################
import os
import glob
import argparse
import time
import socket
import shutil
import errno
import re
import lxml.etree as et

from datetime import date
from subprocess import CalledProcessError

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
# import genologics client library
import glsclient.glsclient as glsclient

# constants and configurations
from autoanalysis.config import cfg

LIMS_USER = 'glsjboss'
RUNFOLDER_GLOB = "%s/??????_*_*_*"
NOVASEQ_RUNFOLDER = re.compile("^[0-9]{6}_.+_[0-9]+_[AB]?[A-Z0-9]{5}D[MRS]XX$", re.IGNORECASE)
RUN_HEADER = """
================================================================================
=== RUN: %(run_folder)s
================================================================================"""
EVENT_HEADER = """
================================================================================
=== EVENT: %s
================================================================================"""
NB_DAYS = 3
RSYNC_FLAGS = "-rtm"

TECHNOLOGIES = ['4000', 'hiseq', 'miseq', 'nextseq']


def sync_runfolder(log, lims_server, seq_server, run_folder, dry_run):
    run_folder_name = os.path.basename(run_folder)
    to_path_rsync = "%s:/%s/" % (lims_server, get_destination_path(seq_server, run_folder))
    # Sync runfolder to lims server
    log.info('Synchronising run folder...')
    try:
        rsync_files_cmd = ["rsync", RSYNC_FLAGS, "--include=RunInfo.xml", "--include=runParameters.xml", "--include=RunParameters.xml", "--include=First_Base_Report.htm", "--include=CopyComplete.txt", "--exclude=/*/*/", "--exclude=/*/*", run_folder, to_path_rsync]
        utils.run_process(rsync_files_cmd, dry_run)

        rsync_interop_cmd = ["rsync", RSYNC_FLAGS, "%s/InterOp" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)]
        if os.path.exists(os.path.join(run_folder, 'InterOp')):
            utils.run_process(rsync_interop_cmd, dry_run)
        else:
            log.warning('%s/InterOp no such directory' % run_folder)

        rsync_ga_cmd = ["rsync", RSYNC_FLAGS, "--include=*/", "--include=Data/Intensities/RTAConfiguration.xml", "--include=ReadPrep1/RunInfo.xml", "--exclude=*", run_folder, to_path_rsync]
        utils.run_process(rsync_ga_cmd, dry_run)

        if is_novaseq(run_folder):
            # NovaSeq runs work in a different way, and thanks to the integration not
            # allowing more than one run folder base, they are not per server. They
            # need the "OutputRunFolder" element changing to be the single path registered
            # in Clarity regardless of which server processed them.
            run_parameters = "%s/RunParameters.xml" % run_folder
            run_parameters_server = "%s/RunParameters_LIMS.xml" % run_folder
            if os.path.exists(run_parameters):
                if not os.path.exists(run_parameters_server):
                    mangle_runparameters(log, seq_server, run_parameters, run_parameters_server)
                copy_params_cmd = ["scp", run_parameters_server, "%s/%s/RunParameters.xml" % (to_path_rsync, run_folder_name)]
                utils.run_process(copy_params_cmd, dry_run)
            else:
                log.warning('%s no such file' % run_parameters)

            rsync_lims_cmd = ["rsync", RSYNC_FLAGS, "%s/LIMS" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)]
            utils.run_process(rsync_lims_cmd, dry_run)

    except CalledProcessError, e:
        if e.returncode in [23, 24]:
            # These return codes mean "Partial transfer due to error" and
            # "Partial transfer due to vanished source files" respectively.
            # See https://lxadm.com/Rsync_exit_codes
            # We get these errors if things are cleaned or moved while one of the rsync
            # commands above is taking place, and is harmless. If necessary any missing
            # files will be transferred next time.
            log.warn("rsync had run files removed underneath it during copy to Clarity server:\n%s" % e.output.strip())
        else:
            raise e


# Supports the NovaSeq cludging of RunParameters.xml. Loads the true
# file up, replaces the OutputRunFolder value to be what Clarity wants,
# and saves it to a modified file.
def mangle_runparameters(log, seq_server, run_parameters, run_parameters_server):
    run_folder = os.path.dirname(run_parameters)
    run_folder_name = os.path.basename(run_folder)
    if os.path.exists(run_parameters):
        doc = et.parse(run_parameters)
        for output_folder in doc.xpath('//RunParameters/OutputRunFolder'):
            output_folder.text = "\\\\%s\\solexa\\%s\\" % (seq_server, run_folder_name)
        doc.write(run_parameters_server, xml_declaration=True)
        return run_parameters_server
    else:
        log.warning('%s does not exist' % run_parameters)


# Check if the run folder is NovaSeq, based on its name.
def is_novaseq(run_folder):
    run_folder_name = os.path.basename(run_folder)
    print run_folder_name
    return NOVASEQ_RUNFOLDER.search(run_folder_name) is not None


# Destination folder on LiMS server has the name of the originate folder, except for NovaSeq
def get_destination_path(seq_server, run_folder=None):
    if not run_folder:
        return "/runs/%s/" % seq_server
    if is_novaseq(run_folder):
        return "/runs/novaseq/"
    return "/runs/%s/" % seq_server


def log_calledprocesserror(log, what, cpe):
    message = ["%s failed with exit code %d:" % (what, cpe.returncode), " ".join(cpe.cmd)]
    if cpe.output:
        message.append(cpe.output.strip())
    log.exception("\n".join(message))


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", dest="days", action="store", default=NB_DAYS, help="Number of days files stays on lims servers before being deleted, default is %s" % NB_DAYS)
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # time files stay on lims server
    delete_time = 60 * 60 * 24 * options.days

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    # lims server
    lims_server = '%s@%s' % (LIMS_USER, glsclient.SERVER)
    if options.use_limsdev:
        lims_server = '%s@%s' % (LIMS_USER, glsclient.TEST_SERVER)

    # sequencing server on which this script is running
    seq_server = socket.gethostname()

    # setting-up time
    present = time.time()

    # location of run folders & processed run folders on sequencing server
    from_path = "/processing/"
    processed_runs_path = "/processing/ProcessedRuns/"

    # Sync part of the run folder onto LiMS server
    run_folders = glob.glob(RUNFOLDER_GLOB % from_path)
    for run_folder in run_folders:
        log.info(RUN_HEADER % {'run_folder': run_folder})
        run_folder_name = os.path.basename(run_folder)
        try:
            sync_runfolder(log, lims_server, seq_server, run_folder, options.dry_run)
        except CalledProcessError, e:
            log_calledprocesserror(log, "rsync command", e)
        except Exception, e:
            log.exception("Unexpected error")
            log.exception(e)
            continue

    # Delete run folders on LiMS when runs are in 'ProcessedRuns' and older than x days
    processed_run_folders = glob.glob(RUNFOLDER_GLOB % processed_runs_path)
    for run_folder in processed_run_folders:
        log.info(RUN_HEADER % {'run_folder': run_folder})
        run_folder_name = os.path.basename(run_folder)
        sequencing_completed = os.path.join(run_folder, cfg['SEQUENCING_COMPLETED'])
        sequencing_failed = os.path.join(run_folder, cfg['SEQUENCING_FAILED'])
        if os.path.exists(sequencing_completed):
            run_age = present - os.path.getmtime(sequencing_completed)
            log.info('%s is %s old' % (sequencing_completed, run_age))
        elif os.path.exists(sequencing_failed):
            run_age = present - os.path.getmtime(sequencing_failed)
            log.info('%s is %s old' % (sequencing_failed, run_age))
        else:
            log.warning('No run status found')
            run_age = None
        if run_age:
            if run_age > delete_time:
                log.info('Deleting run folder older than %s days...' % NB_DAYS)
                # ssh username@domain.com 'rm /some/where/some_file.war'
                delete_runfolder_cmd = ['ssh', lims_server, 'rm -rf %s/%s' % (get_destination_path(seq_server, run_folder), run_folder_name)]
                log.info(delete_runfolder_cmd)
                try:
                    utils.run_process(delete_runfolder_cmd, options.dry_run)
                except CalledProcessError, e:
                    if e.errno != 255:
                        # Error code 255 mostly happens when the run folder does not exist on the server.
                        log_calledprocesserror(log, "Remote run folder clean up", e)
                except Exception, e:
                    log.exception("Unexpected error")
                    log.exception(e)
                    continue

    today = date.today()

    # Copy event files to lims server (no event file for NovaSeq)
    for technology in TECHNOLOGIES:
        from_events = "%s/gls_events_%s/" % (from_path, technology)
        to_events_archive = "%s/archive/%04d/%02d/%02d/" % (from_events, today.year, today.month, today.day)
        to_events_new_lims = "%s:%s/gls_events_%s/" % (lims_server, get_destination_path(seq_server), technology)
        if os.path.exists(from_events):
            event_files = glob.glob("%s/event-*.txt" % from_events)
            log.info('List of events file to sync: %s' % event_files)
            # create archive folder if it does not exist
            if len(event_files) > 0 and not os.path.exists(to_events_archive):
                os.makedirs(to_events_archive)
            for event_file in event_files:
                log.info(EVENT_HEADER % event_file)
                try:
                    attempt = 4
                    while attempt > 0:
                        try:
                            # copy event file to lims server
                            scp_cmd = ["scp", "-r", "-p", event_file, to_events_new_lims]
                            utils.run_process(scp_cmd, options.dry_run)
                            # move event file into archive
                            shutil.move(event_file, "%s%s" % (to_events_archive, os.path.basename(event_file)))
                            # If the copy has worked, all done here. Stop the loop.
                            break
                        except CalledProcessError, e:
                            if not os.path.exists(event_file):
                                log.info("Event file %s no longer exists." % os.path.basename(event_file))
                                break
                            else:
                                attempt -= 1
                                if attempt <= 0:
                                    # No retries left. Allow the error out.
                                    raise e
                                # Otherwise, log a warning, pause, then try again.
                                if e.output:
                                    log.warn("scp command failed, but can retry.")
                                else:
                                    log.warn("scp command failed, but can retry: %s" % e.output.strip())
                                time.sleep(0.5)
                        except IOError, e:
                            # Error number 2 is "file not found". Can happen if things clean up while this
                            # script is iterating. So ignore errors with that error number.
                            if e.errno != errno.ENOENT:
                                raise e
                except CalledProcessError, e:
                    log_calledprocesserror(log, "scp command", e)
                except Exception, e:
                    log.exception("Unexpected error")
                    log.exception(e)

if __name__ == '__main__':
    main()
