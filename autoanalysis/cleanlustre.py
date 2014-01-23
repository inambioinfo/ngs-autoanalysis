#!/usr/bin/env python
# encoding: utf-8
"""
cleanlustre.py

$Id$

Created by Anne Pajon on 2012-11-13.

--------------------------------------------------------------------------------

Analysis server script that cleans runs after being analysed on lustre.

Usage:
> python cleanlustre.py --basedir=/lustre/mib-cri/solexa/Runs --trashdir=/lustre/mib-cri/solexa/TrashRuns --debug
"""

###############################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging
import time

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.pipelines as auto_pipelines

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--trashdir", dest="trashdir", action="store", help="trash directory e.g. '/lustre/mib-cri/solexa/Trash_Runs'", required=True)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # loop over all runs that have a Analysis.completed and Publishing.completed and not dont.delete files in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, '', options.run_folder)
        for run in runs.published_runs:
            try:
                log.info(run.getHeader())
                log.info('*** run folder move to trash')
                if os.path.exists(run.dont_delete):
                    log.info('%s is present' % run.dont_delete)
                else:
                    cmd = ['mv', run.run_folder, options.trashdir]
                    utils.run_bg_process(cmd, options.dry_run)
            except:
                log.exception("Unexpected error")
                continue
    
        # delete all run folders older than 3 days in options.trashdir
        trash_run_folders = glob.glob("%s/??????_*_*_*" % options.trashdir)
        older = 60*60*24*3 # convert 3 days to seconds
        present = time.time()
        for run_folder in trash_run_folders:
            log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            log.info('~~~ TRASH RUN: %s' % run_folder)
            log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            try:
                if (present - os.path.getmtime(run_folder)) > older:
                    log.info('*** run folder removed')
                    cmd = ['rm', '-rf', run_folder]
                    utils.run_bg_process(cmd, options.dry_run)
            except:
                log.exception("Unexpected error")
                continue  
    except:
        log.exception("Unexpected error")
        raise        
    
if __name__ == '__main__':
    main()

