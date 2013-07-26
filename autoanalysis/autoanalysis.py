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
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--donot-run-pipelines", dest="donot_run_pipelines", action="store_true", default=False, help="use this option to DO NOT run the pipelines")
    parser.add_argument("--updatelims", dest="update_lims", action="store_true", default=False, help="use this option to update the lims")
    parser.add_argument("--publish", dest="publish", action="store_true", default=False, help="use this option to assign flowcells to publishing workflow")
    parser.add_argument("--ftp", dest="ftp", action="store_true", default=False, help="use this option to sync external data to ftp server")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # loop over all runs that have a Sequencing.completed file in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, options.archivedir, options.run_folder)
        # connect to lims
        glslims = auto_glslims.GlsLims(options.use_limsdev)
        for run in runs.completed_runs:
            try:
                log.info(run.getHeader())
                # create pipelines
                pipelines = auto_pipelines.Pipelines(run, options.step, options.softdir, options.cluster, options.dry_run, options.use_limsdev)
                # get external data
                external_data = glslims.findExternalData(run.run_folder_name)
                if not options.donot_run_pipelines:
                    # run pipelines
                    pipelines.execute()
                # register completion
                pipelines.registerCompletion(external_data)
                if options.update_lims:
                    # create lims processes and update sample status
                    glslims.createAnalysisProcesses(run.flowcell_id)
                    glslims.updateSampleProgressStatus(run.flowcell_id)
                else:
                    log.info('use --update-lims option to update the lims')
                if options.publish:
                    # publish flow-cell
                    if run.isAnalysed():
                        glslims.publishFlowCell(run.flowcell_id)
                else:
                    log.info('use --publish option to assign flowcells to publishing workflow')
                if options.ftp:
                    # publish external data
                    external = auto_pipelines.External(run, external_data, options.dry_run)
                    external.publish()
                else:
                    log.info('use --ftp option to sync external data to ftp server')
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()


        

