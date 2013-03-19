#!/usr/bin/env python
# encoding: utf-8
"""
autoanalysis.py

$Id$

Created by Anne Pajon on 2012-10-05.

--------------------------------------------------------------------------------

This script automatised the creation of the run-meta.xml needed for the pipeline
to run; runs the pipeline; synchronises the data back to the archive; publishes 
external data onto the ftp server; and updates the analysis status in the lims. 
The list of runs is obtained from the lims when sequencing has finished and
status set to COMPLETE.

This script has been made firstly to replace the old Perl solexa_autoanalysis.pl 
written by Kevin Howe and modified by Ben Davis mainly because all steps of the 
sequencing pipeline have been standardised and are now using the workflow engine 
written by Richard Bowers.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import argparse

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from suds.client import Client
except ImportError:
    sys.exit('''
--------------------------------------------------------------------------------
>>> modules { mysql-python | sqlalchemy | suds } not installed.
--------------------------------------------------------------------------------
[on sols] use /home/mib-cri/software/python2.7/bin/python
[locally] install virtualenv; source bin/activate and pip install modules
--------------------------------------------------------------------------------
''')

# import logging module first
import autoanalysis.log as logger
log = logger.set_custom_logger()
# then import other custom modules
import autoanalysis.utils as utils
import autoanalysis.runfolders as runfolders
import autoanalysis.pipelines as pipelines

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_argument("--step", dest="step", action="store", choices=list(pipelines.MULTIPLEX_PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(pipelines.MULTIPLEX_PIPELINES.viewkeys()))
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
        # loop over all run folders that have a Run.completed file in options.basedir
        runs = runfolders.RunFolders(options.basedir, options.archivedir)
        for run in runs.run_folders:
            try:
                # create run definition
                run_definition = runfolders.RunDefinition(run)
                
                ### TODO
                # create list of external samples for this run
                #external_samples = runs.findExternalSampleIds(run)
        
                if run_definition.is_ready_for_analysis():
                    # create pipelines and execute
                    analysis_pipelines = pipelines.Pipelines(run_definition, external_samples, options.step, options.update_status, soap_client, options.softdir, options.cluster, options.dry_run)
                    analysis_pipelines.execute()
                else:
                    log.warn('run folder %s does not exists - autoanalysis will not run' % run_definition.run_folder)
            except:
                log.exception("Unexpected error")
                continue
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()


        

