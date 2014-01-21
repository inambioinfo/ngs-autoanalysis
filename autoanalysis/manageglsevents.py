#!/usr/bin/env python
# encoding: utf-8
"""
manageglsevents.py

Created by Anne Pajon on 2013-08-05.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging
import time
import datetime

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders

"""
----------
Usage: $0 -s sol02 -v "solexa01 solexa02 solexa03"
Options: 
 -s   server name
 -v   List of volumes
----------
gls_events needs to be created at the destination prior to run the script
----------
"""

LIMS="glsadmin@lims.cri.camres.org"
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

def sync_runfolder(log, run_folder, to_path_rsync, dry_run):
    run_folder_name = os.path.basename(run_folder)
    ### Sync runfolder to lims server
    log.info('Synchronising run folder...')
    rsync_files_cmd = ["rsync", "-av", "--include=RunInfo.xml", "--include=runParameters.xml", "--include=First_Base_Report.htm", "--exclude=/*/*/", "--exclude=/*/*", run_folder, to_path_rsync]
    utils.run_process(rsync_files_cmd, dry_run)
    rsync_bin_cmd = ["rsync", "-av", "%s/InterOp" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)] 
    utils.run_process(rsync_bin_cmd, dry_run)
    rsync_ga_cmd = ["rsync", "-avr", "--include=*/", "--include=Data/Intensities/RTAConfiguration.xml", "--include=ReadPrep1/RunInfo.xml", "--exclude=*", run_folder, to_path_rsync]
    utils.run_process(rsync_ga_cmd, dry_run)
    
################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", dest="server", action="store", help="server name e.g. 'sol02'", required=True)
    parser.add_argument("--volumes", dest="volumes", action="store", nargs='+', help="list of volumes e.g. '--volumes solexa01 solexa02 solexa03'", required=True)
    parser.add_argument("--days", dest="days", action="store", default=THREE_DAYS, help="Number of days files stays on lims servers before being deleted, default is %s" % THREE_DAYS)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()
    
    # time files stay on lims server
    delete_time = 60*60*24*options.days

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
        
    # check server
    if not options.server in os.uname()[1]:
        log.error("Server names do not match, check argument --server=%s when running on %s" % (options.server, os.uname()[1]))
        exit(1)
        
    # setting-up time
    present = time.time()
                      
    # get list of volumes from command line
    log.debug("List of volumes to sync: %s" % options.volumes)

    ### Manage run folders
    for volume in options.volumes:
        from_path="/%s/data/Runs/" % volume
        to_path="/runs/%s/%s/" % (options.server, volume)
        to_path_rsync="%s:/runs/%s/%s/" % (LIMS, options.server, volume)
        run_folders =  glob.glob(RUNFOLDER_GLOB % from_path)
        for run_folder in run_folders:
            log.info(RUN_HEADER % {'run_folder': run_folder})
            run_folder_name = os.path.basename(run_folder)
            sequencing_completed = os.path.join(run_folder, auto_runfolders.SEQUENCING_COMPLETED)
            sequencing_failed = os.path.join(run_folder, auto_runfolders.SEQUENCING_FAILED)
            analysis_ignore = os.path.join(run_folder, auto_runfolders.ANALYSIS_IGNORE)
            
            if run_folder_name == options.run_folder:
                sync_runfolder(log, run_folder, to_path_rsync, options.dry_run)
            else:
                if not os.path.exists(analysis_ignore):
                    if os.path.exists(sequencing_completed):
                        runfolder_age = present - os.path.getmtime(sequencing_completed)
                    elif os.path.exists(sequencing_failed):
                        runfolder_age = present - os.path.getmtime(sequencing_failed)
                    else:
                        log.warning('No run status found')
                        runfolder_age = None
                
                    if runfolder_age:
                        ### Delete runfolder on lims server if older than x days usually 3
                        if runfolder_age > delete_time:
                            log.info('Deleting run folder older than 3 days...')
                            # ssh username@domain.com 'rm /some/where/some_file.war'
                            delete_runfolder_cmd = ['ssh', LIMS, 'rm -rf %s/%s' % (to_path, run_folder_name)]
                            log.info(delete_runfolder_cmd)
                            utils.run_process(delete_runfolder_cmd, options.dry_run)
                    else:
                        sync_runfolder(log, run_folder, to_path_rsync, options.dry_run)
                else:
                    log.info('%s is present - run ignored' % analysis_ignore)

    ### Copy event files to lims server
    for volume in options.volumes:
        from_path="/%s/data/Runs/" % volume
        to_path="/runs/%s/%s/" % (options.server, volume)
        to_path_rsync="%s:/runs/%s/%s/" % (LIMS, options.server, volume)
        from_events="%s/gls_events/" % from_path
        from_events_archive="%s/archive/" % from_events
        to_events="%s/gls_events/" % to_path_rsync
        if os.path.exists(from_events):
            event_files = glob.glob("%s/event-*.txt" % from_events)
            log.info('List of events file to sync: %s' % event_files)
            # create archive folder if it does not exist
            if not os.path.exists(from_events_archive):
                os.makedirs(from_events_archive)
            for event_file in event_files:
                log.info(EVENT_HEADER % event_file)
                # copy event files to lims server and move them to archive
                scp_cmd = ["scp", "-r", "-p", event_file, to_events]
                utils.run_process(scp_cmd, options.dry_run)
                mv_cmd = ["mv", event_file, from_events_archive]
                utils.run_process(mv_cmd, options.dry_run)

if __name__ == '__main__':
	main()

