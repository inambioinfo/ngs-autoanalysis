#!/usr/bin/env python
# encoding: utf-8
"""
set_status.py

$Id$

Created by Anne Pajon on 2012-10-29.
"""

import sys, os
import optparse
import logging

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils

try:
    from suds.client import Client
except ImportError:
    print '''
 --------------------------------------------------------------------------------
 --- Use this python on the sols to call the script
 > /home/mib-cri/software/python2.7/bin/python
 --------------------------------------------------------------------------------
 --- Or locally install 'suds' python module first 
 --- and activate your python virtual environment
 > wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py --no-check-certificate
 > python virtualenv.py `pwd`
 > source bin/activate
 > pip install suds
 '''
    sys.exit()

# Soap url
SOAP_URL = "http://uk-cri-ldmz02.crnet.org/solexa-ws/SolexaExportBeanWS"

################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--soapurl", dest="soapurl", action="store", default=SOAP_URL, help="soap url - default set to '%s'" % SOAP_URL)
    parser.add_option("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_option("--status", dest="status", action="store", help="analysis status to set e.g. 'COMPLETE'")
    parser.add_option("--update", dest="update", action="store_true", default=False, help="use this option to do a status update and not only report action")
    parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_option("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    (options, args) = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
                  
    for option in ['run_number', 'status']:
        if getattr(options, option) == None:
            print "Please supply a --%s parameter.\n" % (option)
            parser.print_help()
            sys.exit(1)
            
    # create soap client
    soap_client = Client("%s?wsdl" % options.soapurl)

    # get run
    run = soap_client.service.getSolexaRunForRunNumber(options.run_number, 'true')
    log.debug(run)
    
    if run.runStatus == 'COMPLETE':
        log.info('--- UPDATE STATUS --------------------------------------------------------------')
        if (options.update):
            utils.set_analysis_status(soap_client, run, options.status)
            log.info('update status of run %s from %s to %s' % (options.run_number, run.analysisStatus, options.status))
        else:
            log.info('use --update to update the status of %s from %s to %s' % (options.run_number, run.analysisStatus, options.status))
    else:
        log.warning('sequencing status of run %s is not COMPLETE' % options.run)
        

if __name__ == "__main__":
	sys.exit(main())


        

