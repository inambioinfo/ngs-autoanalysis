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
import argparse

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.data as auto_data
import autoanalysis.pipelines as auto_pipelines
import autoanalysis.glslims as auto_glslims


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--processingdir", dest="processingdir", action="store", help="processing base directories e.g. '/processing'", required=True)
    parser.add_argument("--stagingdir", dest="stagingdir", action="store", help="staging base directories e.g. '/staging'", required=True)

    parser.add_argument("--softdir", dest="softdir", action="store", default=auto_pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % auto_pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--step", dest="step", action="store", choices=list(auto_pipelines.Pipelines.PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(auto_pipelines.Pipelines.PIPELINES.viewkeys()))
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--donot-run-pipelines", dest="donot_run_pipelines", action="store_true", default=False, help="use this option to DO NOT run the pipelines")
    parser.add_argument("--logfile", dest="logfile", action="store", default=None, help="File to print logging information")
    parser.add_argument("--nologemail", dest="nologemail", action="store_true", default=False, help="turn off sending log emails on error")

    options = parser.parse_args()

    # logging configuration
    log = logger.get_custom_logger(options.logfile, options.nologemail)
                  
    try:
        # loop over all runs that have a Sequencing.completed file in options.basedir
        runs = auto_data.RunFolderList(options.processingdir, options.stagingdir, None, options.run_folder)
        # connect to lims
        glslims = auto_glslims.GlsLims(options.use_limsdev)
        for run in runs.completed_runs:
            try:
                log.info(run.get_header())
                # create pipelines
                pipelines = auto_pipelines.Pipelines(run, options.step, options.softdir, options.cluster, options.dry_run, options.use_limsdev)
                if not options.donot_run_pipelines:
                    # run pipelines
                    pipelines.execute()
                # register pipelines completion
                pipelines.register_completion()
                
                # create lims processes
                glslims.create_analysis_processes(run.flowcell_id)

                # get all flow-cell sample fastq files when attached in lims
                all_data = glslims.is_fastq_files_found(run.run_folder_name)
                # get external data when lane and sample fastq files are attached in lims
                external_data = glslims.find_external_data(run.run_folder_name)
                
                # create external
                external = auto_pipelines.External(run, all_data, external_data, options.dry_run)
                # synchronise external data to ftp server
                external.sync()

                # add flow-cell into the publishing queue
                if run.is_analysis_completed_present() and not run.is_publishing_assigned_present() and external.is_external_data_synchronised():
                    glslims.publish_flowcell(run.run_folder_name, run.flowcell_id, run.publishing_assigned)
                
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
    main()


        

