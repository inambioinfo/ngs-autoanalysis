#!/usr/bin/env python
# encoding: utf-8
"""
sync.py

Created by Anne Pajon on 2012-10-26.

"""

import sys, os, glob
import optparse
import logging

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from suds.client import Client
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
 > pip install mysql-python sqlalchemy
 '''
    sys.exit()

# Database url
DB_URL = "mysql://readonly@uk-cri-lbio04/cri_solexa"

# Soap url
SOAP_URL = "http://uk-cri-ldmz02.crnet.org/solexa-ws/SolexaExportBeanWS"

# Instrument names with their run completed dependencies
INSTRUMENTS = {
    'HWI-ST230' : ['RTAComplete.txt'],
    'M00225' : ['RTAComplete.txt'],
    'HWI-EAS350' : ['Basecalling_Netcopy_complete.txt'],
    'HWI-EAS202' : ['Basecalling_Netcopy_complete.txt']
}

# Default filenames
SEQUENCING_COMPLETED_FILENAME = "Run.completed"

RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_FINISHED_FILENAME = "rsync.ended"
RSYNC_LOCK_FILENAME = "rsync.lock"
RSYNC_LOG_FILENAME = "rsync.log"
RSYNC_IGNORE_FILENAME = 'rsync.ignore'

# rsync exclude list
RSYNC_EXCLUDE_LIST = [
    "--exclude=Data/Intensities/L00?/C*/*.tif", # images - not generated anymore by sequencers
    "--exclude=Data/Thumbnail_Images", # thumbnail images
    "--exclude=Data/Intensities/L00?/C*/*.cif" # intensitites
]

# Template for rsync.sh
LOCAL_SCRIPT_TEMPLATE = '''
#!/bin/bash
#
# Shell script for running command(s) locally
#

echo "%(cmd)s"

%(cmd)s

'''


################################################################################
# METHODS
################################################################################
def _setup_rsync_run(dest_run_folder, run_folder, dry_run=True): 
    rsync_script_path = os.path.join(run_folder, RSYNC_SCRIPT_FILENAME)
    rsync_started = os.path.join(run_folder, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(run_folder, RSYNC_FINISHED_FILENAME)
    rsync_log = os.path.join(run_folder, RSYNC_LOG_FILENAME)
    rsync_lock = os.path.join(os.path.dirname(run_folder), RSYNC_LOCK_FILENAME)

    if dest_run_folder:
        dest_basedir = os.path.dirname(dest_run_folder)
        # create rsync-pipeline script 
        if not os.path.exists(rsync_script_path):    
            rsync_script_file = open(rsync_script_path, 'w')
            rsync_options = "-av %s %s %s > %s 2>&1" % (RSYNC_EXCLUDE[pipeline_name], run_folder, dest_basedir, rsync_log)
            copy_finished = "%s %s/." % (rsync_finished, dest_pipeline_directory)
            command = "touch %s; touch %s; rsync %s; touch %s; cp %s; rm %s" % (rsync_started, rsync_lock, rsync_options, rsync_finished, copy_finished, rsync_lock)
            rsync_script_file.write(LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
            rsync_script_file.close()
            log.info('%s created' % rsync_script_path)
        else:
            log.debug('%s already exists' % rsync_script_path)

def _rsync_run(run_folder, dry_run=True):
    rsync_script_path = os.path.join(run_folder, RSYNC_SCRIPT_FILENAME)
    rsync_started = os.path.join(run_folder, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(run_folder, RSYNC_FINISHED_FILENAME)
    rsync_lock = os.path.join(os.path.dirname(run_folder), RSYNC_LOCK_FILENAME)

    # run rsync script to synchronise data from sequencing servers to lustre
    if os.path.exists(rsync_script_path):            
        if not os.path.exists(rsync_started):
            if not os.path.exists(rsync_lock):
                if run_completed(run_folder):
                    utils.touch(rsync_lock)
                    utils.run_bg_process(['sh', '%s' % rsync_script_path], dry_run)
                else:
                    log.debug("nothing to rsync yet - sequencing not complete")
            else:
                log.info('%s presents - another rsync process is running' % rsync_lock)
        else:
            if not os.path.exists(rsync_finished):
                log.info('%s is currently being synchronised' % run_folder)
            else:
                log.info('%s has been synchronised' % run_folder)
    else:
        log.warn('%s is missing' % rsync_script_path)

################################################################################
# UTILITY METHODS
################################################################################


################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'")
    parser.add_option("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'")
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
                  
    for option in ['basedir', 'lustredir']:
        if getattr(options, option) == None:
            print "Please supply a --%s parameter.\n" % (option)
            parser.print_help()
            sys.exit()
            
    if not glob.glob(options.basedir):
        log.error("%s does not exists - check your '--basedir' option" % options.basedir)
        sys.exit(1)

    if not os.path.exists(options.lustredir):
        log.error("%s does not exists - check your '--lustredir' option" % options.lustredir)
        sys.exit(1)
        
    # get list of run folders on disk
    runs = get_runs(options.basedir)
    for run_folder in runs:
        # check run folder in basedir for analysis
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run_folder)
        log.info('--------------------------------------------------------------------------------')
        if os.path.exists(run_folder):
            # check sequencing process has finished
            sequencing_completed = process_completed(instrument_name)
            # check rsync.ignore is not present
            rsync_ignore = os.path.join(run_folder, RSYNC_IGNORE_FILENAME)
            if os.path.exists(sequencing_completed) and not os.path.exists(analysis_ignore):
                # get/create dest folder to synchronize run folder
                dest_run_folder = os.path.join(options.lustredir, run_folder)
                log.info('--- RUN RSYNC ------------------------------------------------------------------')
                _rsync_pipelines(run_folder, pipelines, options.dry_run)
                log.info('--- UPDATE STATUS --------------------------------------------------------------')
                _register_process_completed(options.update_status, options.soapurl, run, run_folder, dest_run_folder, pipelines_for_completion)
            else:
                if not os.path.exists(sequencing_completed):
                    log.warning('%s does not exists' % sequencing_completed)
                if os.path.exists(rsync_ignore):
                    log.info('%s is present' % rsync_ignore)
        else:
            log.error('%s does not exists' % run_folder)
        

if __name__ == "__main__":
	sys.exit(main())

