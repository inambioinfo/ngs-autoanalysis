#!/usr/bin/env python
# encoding: utf-8
"""
autoanalysis.py

$Id$

Created by Anne Pajon on 2012-10-05.

--------------------------------------------------------------------------------

This script has firstly been made to replace the old Perl solexa_autoanalysis.pl 
written by Kevin Howe and modified by Ben Davis mainly because all steps of the 
sequencing pipeline have been standardised and are now using the workflow engine 
written by Richard Bowers.

This script automatised the creation of the run-meta.xml needed for the pipeline
to run; runs the pipeline; synchronises the data back to the archive; publishes 
external data onto the ftp server; and updates the analysis status in the lims. 
The list of runs is obtained from the lims when sequencing has finished and
status set to COMPLETE.
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
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import lims
import pipelines

################################################################################
# CONSTANTS
################################################################################
# Cluster host
CLUSTER_HOST = "uk-cri-lcst01"

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--dburl", dest="dburl", action="store", default=lims.DB_URL, help="database url [read only access] - default set to '%s'" % lims.DB_URL)
    parser.add_argument("--soapurl", dest="soapurl", action="store", default=lims.SOAP_URL, help="soap url [for updating status only] - default set to '%s'" % lims.SOAP_URL)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % CLUSTER_HOST)
    parser.add_argument("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_argument("--step", dest="step", action="store", choices=list(pipelines.MULTIPLEX_PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(pipelines.MULTIPLEX_PIPELINES.viewkeys()))
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--update-status", dest="update_status", action="store_true", default=False, help="use this option to update the status of a run in lims when process completed")
    parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
                  
    if not os.path.exists(options.basedir):
        sys.exit("%s does not exists - check your '--basedir' option" % options.basedir)
    
    if not glob.glob(options.archivedir):
        sys.exit("%s does not exists - check your '--archivedir' option" % options.archivedir)
    
    # turn off update-status for dry-run
    if options.dry_run:
        options.update_status = False
        
    # create soap client
    soap_client = lims.SoapLims(options.soapurl)
    # create lims client
    runs = lims.Runs(options.dburl)
    # loop over all completed runs that have not been analysed or just one run
    for run in runs.findAllCompleteRuns(options.run_number):
        # create run definition
        run_definition = pipelines.RunDefinition(options.basedir, options.archivedir, run)
        # create list of external samples for this run
        external_samples = runs.findExternalSampleIds(run)
        
        if run_definition.ready_to_process():
            # create pipelines
            analysis_pipelines = pipelines.Pipelines(run_definition, external_samples, options.step, options.update_status, soap_client, options.softdir, options.cluster, options.dry_run)
            analysis_pipelines.execute()
        else:
            log.warn('run folder %s does not exists - autoanalysis will not run' % run_definition.run_folder)
    
if __name__ == "__main__":
	main()


        

