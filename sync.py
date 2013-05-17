#!/usr/bin/env python
# encoding: utf-8
"""
sync.py

$Id$

Created by Anne Pajon on 2012-10-26.

--------------------------------------------------------------------------------

Sequencing server script that synchronizes data to lustre

Usage:
> python sync.py --basedir=/solexa0[1-3]/data/Runs --lustredir=/lustre/mib-cri/solexa/Runs --debug
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging

# import logging module first
import autoanalysis.log as logger
log = logger.set_custom_logger()
# then import other custom modules
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.pipelines as auto_pipelines

################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
                              
    try:
        # loop over all runs that have a Sequencing.completed file in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, options.lustredir, options.run_folder)
        for run in runs.completed_runs:
            try:
                log.info(run.getHeader())
                # create sync 
                sync = auto_pipelines.Sync(run, options.dry_run)
                # execute pipelines
                sync.execute()
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
	sys.exit(main())
