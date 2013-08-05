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
THREE_DAYS = 60*60*24*3

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", dest="server", action="store", help="server name e.g. 'sol02'", required=True)
    parser.add_argument("--volumes", dest="volumes", action="store", nargs='+', help="list of volumes e.g. '--volumes solexa01 solexa02 solexa03'", required=True)
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

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
            if os.path.exists(sequencing_completed):
                runfolder_age = present - os.path.getmtime(sequencing_completed)
            elif os.path.exists(sequencing_failed):
                runfolder_age = present - os.path.getmtime(sequencing_failed)
            else:
                log.warning('No run status found')
                runfolder_age = None
                
            if runfolder_age:
                ### Delete runfolder on lims server if older than 3 days
                if runfolder_age > THREE_DAYS:
                    log.info('run folder older than 3 days will be deleted')
                    # ssh username@domain.com 'rm /some/where/some_file.war'
                    delete_runfolder_cmd = ['ssh', LIMS, 'rm -rf %s/%s' % (to_path, run_folder_name)]
                    log.info(delete_runfolder_cmd)
                    utils.run_process(delete_runfolder_cmd, options.dry_run)
            else:
                ### Sync runfolder to lims server
                log.info('run folder will be synchronised')
                rsync_files_cmd = ["rsync", "-av", "--include=RunInfo.xml", "--include=runParameters.xml", "--include=First_Base_Report.htm", "--exclude=/*/*/", "--exclude=/*/*", run_folder, to_path_rsync]
                utils.run_process(rsync_files_cmd, options.dry_run)
                rsync_bin_cmd = ["rsync", "-av", "%s/InterOp" % run_folder, "%s/%s" % (to_path_rsync, run_folder_name)] 
                utils.run_process(rsync_bin_cmd, options.dry_run)
                ### Copy event files to lims server

                
                

                
                


if __name__ == '__main__':
	main()

