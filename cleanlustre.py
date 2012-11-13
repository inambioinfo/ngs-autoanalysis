#!/usr/bin/env python
# encoding: utf-8
"""
cleanlustre.py

Created by Anne Pajon on 2012-11-13.
"""

import sys, os, glob
import optparse
import logging

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import lims

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from sqlalchemy.orm.exc import NoResultFound
except ImportError:
    print '''
 --------------------------------------------------------------------------------
 --- Use this python on the sols to call the script
 > /home/mib-cri/software/python2.7/bin/python
 --------------------------------------------------------------------------------
 --- Or locally install these python modules { mysql-python | sqlalchemy | suds } first 
 --- and activate your python virtual environment
 > wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py --no-check-certificate
 > python virtualenv.py `pwd`
 > source bin/activate
 > pip install mysql-python sqlalchemy suds
 '''
    sys.exit()

################################################################################
# CONSTANTS
################################################################################
# Default filenames
DONT_DELETE_FILENAME = 'dont.delete'

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'")
    parser.add_option("--trashdir", dest="trashdir", action="store", help="trash directory e.g. '/lustre/mib-cri/solexa/Trash_Runs'")
    parser.add_option("--dburl", dest="dburl", action="store", default=lims.DB_SOLEXA, help="database url [read only access] - default set to '%s'" % lims.DB_SOLEXA)
    parser.add_option("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_option("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_option("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    (options, args) = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
                  
    for option in ['basedir', 'trashdir']:
        if getattr(options, option) == None:
            print "Please supply a --%s parameter.\n" % (option)
            parser.print_help()
            sys.exit()
            
    if not os.path.exists(options.basedir):
        log.error("%s does not exists - check your '--basedir' option" % options.basedir)
        sys.exit(1)

    if not os.path.exists(options.trashdir):
        log.error("%s does not exists - check your '--trashdir' option" % options.trashdir)
        sys.exit(1)
    
    # lims db
    solexa_db = SqlSoup(options.dburl)
    
    run_folders = glob.glob("%s/??????_*_*_*" % options.basedir)
    for run_folder in run_folders:
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run_folder)
        log.info('--------------------------------------------------------------------------------')
        # check dont.delete is not present - stop cleaning if present
        dont_delete = os.path.join(run_folder, DONT_DELETE_FILENAME)
        if not os.path.exists(dont_delete):
            try:
                run = solexa_db.solexarun.filter_by(pipelinePath=os.path.basename(run_folder)).one()
                log.info('Sequencing status %s and analysis status %s' % (run.status, run.analysisStatus))
                if (run.status == 'COMPLETE' and (run.analysisStatus == 'COMPLETE' or run.analysisStatus == 'SECONDARY COMPLETE')) or ('ABORTED' in run.status):
                    log.info('*** run folder will be moved to trash')
                    cmd = ['mv', run_folder, options.trashdir]
                    utils.run_bg_process(cmd, options.dry_run)
            except (NoResultFound):
                log.info('No result found in lims for pipelinePath %s' % os.path.basename(run_folder))
            except:
                log.error("Unexpected error:", sys.exc_info()[0])
                raise
        else:
            log.debug('%s is present' % dont_delete)
            
    
if __name__ == '__main__':
    main()

