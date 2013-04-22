#!/usr/bin/env python
# encoding: utf-8
"""
set_status.py

$Id$

Created by Anne Pajon on 2012-10-29.
"""

import sys
import os
import argparse
import logging

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
import autoanalysis.lims as lims

################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--soapurl", dest="soapurl", action="store", default=lims.SOAP_URL, help="soap url - default set to '%s'" % lims.SOAP_URL)
    parser.add_argument("--run", dest="run_number", action="store", help="run number e.g. '948'", required=True)
    parser.add_argument("--status", dest="status", action="store", help="analysis status to set e.g. 'COMPLETE'", required=True)
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to do a status update and not only report action")
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
        # create soap client
        soap_client = lims.SoapLims(options.soapurl)

        # get run
        run = soap_client.getRun(options.run_number)
        log.debug(run)
    
        if run.runStatus == 'COMPLETE':
            log.info('--- UPDATE STATUS --------------------------------------------------------------')
            if (options.update):
                soap_client.setAnalysisStatus(soap_client, run, options.status)
                log.info('update status of run %s from %s to %s' % (options.run_number, run.analysisStatus, options.status))
            else:
                log.info('use --update to update the status of %s from %s to %s' % (options.run_number, run.analysisStatus, options.status))
        else:
            log.warning('sequencing status of run %s is not COMPLETE' % options.run)
    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
	sys.exit(main())


        

