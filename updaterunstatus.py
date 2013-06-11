#!/usr/bin/env python
# encoding: utf-8
"""
updaterunstatus.py

$Id$

Created by Anne Pajon on 2013-06-11.

"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging

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
    parser.add_argument("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--lims", dest="lims", action="store", choices=list(auto_glslims.LIMS_SERVERS.viewkeys()), default='dev', help="lims servers to choose from %s - default set to 'dev'" % list(auto_glslims.LIMS_SERVERS.viewkeys()))
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # lims connection
        glslims = auto_glslims.GlsLims(auto_glslims.LIMS_SERVERS[options.lims])
        # loop over all runs in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, options.lustredir, options.run_folder)
        for run in runs.getAllRuns():
            try:
                log.info(run.getHeader())
                run.updateSequencingStatus(glslims.isSequencingRunComplete(run.run_folder_name), options.dry_run)
                run.updateAnalysisStatus(options.dry_run)
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise


if __name__ == '__main__':
	main()

