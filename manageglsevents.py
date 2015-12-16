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

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.data as auto_data

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

TECHNOLOGIES = [ '4000', 'hiseq', 'miseq', 'nextseq' ]

def sync_runfolder(log, run_folder, to_path_rsync, dry_run):
    run_folder_name = os.path.basename(run_folder)
    ### Sync runfolder to lims server
    log.info('Synchronising run folder...')
    rsync_files_cmd = ["rsync", "-avm", "--include=RunInfo.xml", "--include=runParameters.xml", "--include=RunParameters.xml", "--include=First_Base_Report.htm", "--exclude=/*/*/", "--exclude=/*/*", run_folder, to_path_rsync]
    utils.run_process(rsync_files_cmd, dry_run)
    rsync_bin_cmd = ["rsync", "-avm", "%s/InterOp" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)]
    if os.path.exists(os.path.join(run_folder, 'InterOp')):
        utils.run_process(rsync_bin_cmd, dry_run)
    else:
        log.warning('%s/InterOp no such directory' % run_folder)
    rsync_ga_cmd = ["rsync", "-avrm", "--include=*/", "--include=Data/Intensities/RTAConfiguration.xml", "--include=ReadPrep1/RunInfo.xml", "--exclude=*", run_folder, to_path_rsync]
    utils.run_process(rsync_ga_cmd, dry_run)
    

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

    ### Manage run folders
    run_folders = glob.glob(RUNFOLDER_GLOB % from_path)
    for run_folder in run_folders:
        log.info(RUN_HEADER % {'run_folder': run_folder})
        run_folder_name = os.path.basename(run_folder)
        sequencing_completed = os.path.join(run_folder, auto_data.SEQUENCING_COMPLETED)
        sequencing_failed = os.path.join(run_folder, auto_data.SEQUENCING_FAILED)
        ignore_me = os.path.join(run_folder, auto_data.IGNORE_ME)

        if run_folder_name == options.run_folder:
            sync_runfolder(log, run_folder, to_path_for_rsync, options.dry_run)
        else:
            if not os.path.exists(ignore_me):
                if os.path.exists(sequencing_completed):
                    run_age = present - os.path.getmtime(sequencing_completed)
                elif os.path.exists(sequencing_failed):
                    run_age = present - os.path.getmtime(sequencing_failed)
                else:
                    log.warning('No run status found')
                    run_age = None

                if run_age:
                    ### Delete run folder on lims server if older than x days usually 3
                    if run_age > delete_time:
                        log.info('Deleting run folder older than 3 days...')
                        # ssh username@domain.com 'rm /some/where/some_file.war'
                        delete_runfolder_cmd = ['ssh', LIMS_SERVER, 'rm -rf %s/%s' % (to_path, run_folder_name)]
                        log.info(delete_runfolder_cmd)
                        utils.run_process(delete_runfolder_cmd, options.dry_run)
                else:
                    sync_runfolder(log, run_folder, to_path_for_rsync, options.dry_run)
            else:
                log.info('%s is present - run ignored' % ignore_me)

    ### Copy event files to lims server
    for technology in TECHNOLOGIES:
        from_events = "%s/gls_events_%s/" % (from_path, technology)
        to_events_archive = "%s/archive/" % from_events
        to_events_new_lims = "%s/gls_events_%s/" % (to_path_for_rsync, technology)
        if os.path.exists(from_events):
            event_files = glob.glob("%s/event-*.txt" % from_events)
            log.info('List of events file to sync: %s' % event_files)
            # create archive folder if it does not exist
            if not os.path.exists(to_events_archive):
                os.makedirs(to_events_archive)
            for event_file in event_files:
                log.info(EVENT_HEADER % event_file)
                # copy event files to lims server
                scp_cmd = ["scp", "-r", "-p", event_file, to_events_new_lims]
                utils.run_process(scp_cmd, options.dry_run)
                # move event files into archive
                mv_cmd = ["mv", event_file, to_events_archive]
                utils.run_process(mv_cmd, options.dry_run)

if __name__ == '__main__':
    main()

