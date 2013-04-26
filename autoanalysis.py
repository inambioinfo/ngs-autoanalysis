#!/usr/bin/env python
# encoding: utf-8
"""
autoanalysis.py

$Id$

Created by Anne Pajon on 2012-10-05.

--------------------------------------------------------------------------------

Analysis server script that automatically runs the different steps of the sequencing 
pipeline and rsync them to the archive.

Usage:
> python autoanalysis.py --basedir=/lustre/mib-cri/solexa/Runs/ --archivedir=/solexa0[1-6]/data/Runs --cluster=uk-cri-lcst01 --debug
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import argparse

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
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=auto_pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % auto_pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--step", dest="step", action="store", choices=list(auto_pipelines.PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(auto_pipelines.PIPELINES.viewkeys()))
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
        runs = auto_runfolders.RunFolders(options.basedir, options.archivedir, options.run_folder)
        for run in runs.completed_runs:
            try:
                log.info(run.getHeader())
                # create pipelines
                pipelines = auto_pipelines.Pipelines(run, options.step, options.softdir, options.cluster, options.dry_run)
                # execute pipelines
                pipelines.execute()
                # register completion
                pipelines.registerCompletion()
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()


        

