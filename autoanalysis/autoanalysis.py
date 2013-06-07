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
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=auto_pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % auto_pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--step", dest="step", action="store", choices=list(auto_pipelines.PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(auto_pipelines.PIPELINES.viewkeys()))
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--lims", dest="lims", action="store", default=auto_glslims.LIMS_SERVERS['dev'], help="lims servers to choose from %s - default set to %s" % (list(auto_glslims.LIMS_SERVERS.viewkeys()), auto_glslims.LIMS_SERVERS['dev']))
    parser.add_argument("--update-lims", dest="update_lims", action="store_true", default=False, help="use this option to update the lims")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    log = logger.get_custom_logger()
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
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
                if options.update_lims:
                    glslims = auto_glslims.GlsLims(options.lims)
                    glslims.createAnalysisProcesses(run.flowcell_id)
                    #glslims.publishFlowCell()
                    #glslims.updateSampleProgressStatus()
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()


        

