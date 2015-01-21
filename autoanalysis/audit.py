#!/usr/bin/env python
# encoding: utf-8
"""
audit

Created by Anne Pajon on 2015-01-21.
"""
################################################################################
# IMPORTS
################################################################################
import os
import argparse
import glob
import time
import datetime
import logging

# import custom modules
import autoanalysis.log as logger
import glsclient.glssql as glssql
import glsclient.glsclient as glsclient

import autoanalysis.data as auto_data
import autoanalysis.glslims as auto_glslims
import autoanalysis.utils as utils


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()

    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--dev-lims", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False,  help="File to print logging information")
    parser.add_argument("--nologemail", dest="nologemail", action="store_true", default=False, help="turn off sending log emails on error")

    options = parser.parse_args()

    # logging configuration
    log = logger.get_custom_logger(options.logfile, options.nologemail)

    # connect to lims
    lims_server = 'lims'
    if options.use_limsdev:
        lims_server = 'limsdev'
    glsutil = glsclient.GlsUtil(server=lims_server)

    glsutil.db.execute(glssql.PUBLISHED_RUNS_WITHOUT_FASTQ_ATTACHED)
    results = glsutil.db.fetchall()
    
    if results:
        for r in results:
            log.error("Published run id %s without attached files onto 'FASTQ Sample Pipeline' process" % r['run_id'])

    glsutil.close_db_connection()


if __name__ == '__main__':
    main()

