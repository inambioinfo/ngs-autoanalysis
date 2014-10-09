#!/usr/bin/env python
# encoding: utf-8
"""
autoassignsamples.py

Created by Anne Pajon on 2013-05-14.

"""

import sys
import os
import logging
import argparse
# email modules
import smtplib
from email.mime.text import MIMEText
# time module
import datetime

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient
import glsclient.glssql as glssql


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to preform the update and not only report action")
    parser.add_argument("--limsdev", dest="limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    try:
        # connect to lims
        if options.limsdev:
            lims_server = 'limsdev'
        else:
            lims_server = 'lims'
        glsutil = glsclient.GlsUtil(server=lims_server)
        results = glsutil.db.execute(glssql.SAMPLES_WITH_NODATE_QUERY).fetchall()
        
        for row in results:
            # artifactid,samplename,submissiondate,acceptancedate
            try:                
                # update sample date received if empty
                if row.submissiondate is None or row.submissiondate == '':
                    log.info('No date received on sample %s. It will be set to %s.' % (row.samplename, row.acceptancedate))
                    if options.update:
                        artifact = glsutil.api.load('artifact', row.artifactid)
                        sample = glsutil.api.load('sample', artifact.sample[0].limsid)
                        sample.date_received = row.acceptancedate
                        log.debug(sample.toxml('utf-8'))
                        updated_sample = glsutil.api.update(sample)
                        log.info('Date set to %s on sample %s' % (updated_sample.date_received, updated_sample.name))
                        log.debug(updated_sample.toxml('utf-8'))
            except:
                log.exception("Unexpected error")
                continue

    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()
