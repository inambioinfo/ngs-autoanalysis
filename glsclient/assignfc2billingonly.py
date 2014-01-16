#!/usr/bin/env python
# encoding: utf-8
"""
assignfc2billing.py

Created by Anne Pajon on 2013-07-05.
"""

import sys
import os
import logging
import argparse

# import custom modules
import log as logger
import glsclient

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to preform the update and not only report action")
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    try:
        # connect to lims
        if options.use_limsdev:
            lims_server = 'limsdev'
        else:
            #lims_server = 'lims'
            lims_server = 'lims'
        glsutil = glsclient.GlsUtil(server=lims_server)
        
        # query list of flow-cell ready for billing and assign to billing only workflow
        runs = glsutil.getRunProcessByFinishDate('2013-06-01', '2013-07-01')
        for run in runs:
            try:
                glsutil.assignFlowcellToBillingOnlyWorkflow(run['flowcellid'], run['name'], options.update)
            except:
                log.exception("Unexpected error")
                continue
        if not options.update:
            log.info('use --update to perform the operation in the lims')

    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()
