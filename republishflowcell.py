#!/usr/bin/env python
# encoding: utf-8
"""
republishflowcell.py

Created by Anne Pajon on 2013-08-01.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import argparse

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.pipelines as auto_pipelines
import autoanalysis.glslims as auto_glslims

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--runfolders", dest="runfolders", action="store", nargs='+', help="list of run folders e.g. '--runfolders 121019_HWI-ST230_957_D18DUACXX 121011_HWI-ST230_952_D19D3ACXX'", required=True)
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--publish", dest="publish", action="store_true", default=False, help="use this option to assign flowcells to publishing workflow")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    # get list of run folders from command line
    log.debug("List of runfolders to process: " % options.runfolders)
    # connect to lims
    glslims = auto_glslims.GlsLims(options.use_limsdev)
    for runfolder in options.runfolders:
        log.info(auto_runfolders.RUN_HEADER % {'run_folder': runfolder})
        # find runfolder in basedir
        runfolder_path = utils.locate_run_folder(runfolder, options.basedir, False)
        run = auto_runfolders.RunDefinition(runfolder_path)
        if os.path.exists(run.analysis_completed):
            log.info('Analysis completed')
            if options.publish:
                if not os.path.exists(run.publishing_assigned):
                    # publish flow-cell and update sample status
                    glslims.publishFlowCell(run, False)
                else:
                    log.info('%s already exists' % run.publishing_assigned)
            else:
                log.info('use --publish to publish the flowcell')
        else:
            log.info('Analysis not completed')
                  

if __name__ == '__main__':
    main()

