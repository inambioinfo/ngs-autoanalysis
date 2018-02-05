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

from datetime import date
from subprocess import CalledProcessError

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils

# constants and configurations
from autoanalysis.config import cfg


"""
usage: manageglsevents.py [-h] [--days DAYS] [--runfolder RUN_FOLDER]
                          [--dry-run] [--logfile LOGFILE]

optional arguments:
  -h, --help            show this help message and exit
  --days DAYS           Number of days files stays on lims servers before
                        being deleted, default is 3
  --runfolder RUN_FOLDER
                        run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'
  --dry-run             use this option to not do any shell command execution,
                        only report actions
  --logfile LOGFILE     File to print logging information

----------
gls_events_xxxx needs to be created at the destination prior to run the script
----------
"""

LIMS_SERVER = "glsjboss@genomicsequencing.cruk.cam.ac.uk"
RUNFOLDER_GLOB = "%s/??????_*_*_*"
RUN_HEADER = """
================================================================================
=== RUN: %(run_folder)s
================================================================================"""
EVENT_HEADER = """
================================================================================
=== EVENT: %s
================================================================================"""
THREE_DAYS = 3

TECHNOLOGIES = ['4000', 'hiseq', 'miseq', 'nextseq']


def sync_runfolder(log, run_folder, to_path_rsync, dry_run):
    run_folder_name = os.path.basename(run_folder)
    # Sync runfolder to lims server
    log.info('Synchronising run folder...')
    try:
        rsync_files_cmd = ["rsync", "-avm", "--include=RunInfo.xml", "--include=runParameters.xml", "--include=RunParameters.xml", "--include=First_Base_Report.htm", "--exclude=/*/*/", "--exclude=/*/*", run_folder, to_path_rsync]
        utils.run_process(rsync_files_cmd, dry_run)
        rsync_bin_cmd = ["rsync", "-avm", "%s/InterOp" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)]
        if os.path.exists(os.path.join(run_folder, 'InterOp')):
            utils.run_process(rsync_bin_cmd, dry_run)
        else:
            log.warning('%s/InterOp no such directory' % run_folder)
        rsync_ga_cmd = ["rsync", "-avrm", "--include=*/", "--include=Data/Intensities/RTAConfiguration.xml", "--include=ReadPrep1/RunInfo.xml", "--exclude=*", run_folder, to_path_rsync]
        utils.run_process(rsync_ga_cmd, dry_run)
    except CalledProcessError, e:
        if e.returncode == 24:
            # This return code means "Partial transfer due to vanished source files"
            # See https://lxadm.com/Rsync_exit_codes
            # We get these errors if things are cleaned or moved while one of the rsync
            # commands above is taking place, and is harmless.
            log.warn("rsync had run files removed underneath it during copy to Clarity server:\n%s" % e.output.strip())
        else:
            raise e

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
    parser.add_argument("--days", dest="days", action="store", default=THREE_DAYS, help="Number of days files stays on lims servers before being deleted, default is %s" % THREE_DAYS)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
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

    server = socket.gethostname()

    # setting-up time
    present = time.time()

    # location of run folders on sequencing server and lims server
    from_path = "/processing/"
    to_path = "/runs/%s/" % server
    to_path_for_rsync = "%s:%s" % (LIMS_SERVER, to_path)

    # Manage run folders
    run_folders = glob.glob(RUNFOLDER_GLOB % from_path)
    for run_folder in run_folders:
        log.info(RUN_HEADER % {'run_folder': run_folder})
        run_folder_name = os.path.basename(run_folder)
        ignore_me = os.path.join(run_folder, cfg['IGNORE_ME'])
        try:
            if run_folder_name == options.run_folder:
                sync_runfolder(log, run_folder, to_path_for_rsync, options.dry_run)
            else:
                if not os.path.exists(ignore_me):
                    sync_runfolder(log, run_folder, to_path_for_rsync, options.dry_run)
                else:
                    log.info('%s is present - run ignored' % ignore_me)
        except CalledProcessError, e:
            log_calledprocesserror(log, "rsync command", e)
        except Exception, e:
            log.exception("Unexpected error")
            log.exception(e)
            continue

    # location of processed run folders on sequencing server
    processed_runs_path = "/processing/ProcessedRuns/"

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
                log.info('Deleting run folder older than 3 days...')
                # ssh username@domain.com 'rm /some/where/some_file.war'
                delete_runfolder_cmd = ['ssh', LIMS_SERVER, 'rm -rf %s/%s' % (to_path, run_folder_name)]
                log.info(delete_runfolder_cmd)
                try:
                    utils.run_process(delete_runfolder_cmd, options.dry_run)
                except CalledProcessError, e:
                    log_calledprocesserror(log, "Remote run folder clean up", e)
                except Exception, e:
                    log.exception("Unexpected error")
                    log.exception(e)
                    continue

    today = date.today() 

    # Copy event files to lims server
    for technology in TECHNOLOGIES:
        from_events = "%s/gls_events_%s/" % (from_path, technology)
        to_events_archive = "%s/archive/%04d/%02d/%02d/" % (from_events, today.year, today.month, today.day)
        to_events_new_lims = "%s/gls_events_%s/" % (to_path_for_rsync, technology)
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
