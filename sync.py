#!/usr/bin/env python
# encoding: utf-8
"""
sync.py

$Id$

Created by Anne Pajon on 2012-10-26.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import optparse

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from suds.client import Client
except ImportError:
    sys.exit("""
--------------------------------------------------------------------------------
>>> modules { mysql-python | sqlalchemy | suds } not installed.
--------------------------------------------------------------------------------
[on sols] use /home/mib-cri/software/python2.7/bin/python
[locally] install virtualenv; source bin/activate and pip install modules
--------------------------------------------------------------------------------
    """)

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import lims

################################################################################
# CONSTANTS
################################################################################
# Instrument names with their run completed dependencies
INSTRUMENTS = {
    'HWI-ST230' : ['RTAComplete.txt'],
#    'M00225' : ['RTAComplete.txt'], # old MiSeq
    'M01214' : ['RTAComplete.txt'], # new MiSeq
    'HWI-EAS350' : ['Basecalling_Netcopy_complete.txt'],
    'HWI-EAS202' : ['Basecalling_Netcopy_complete.txt']
}

# Default filenames
SEQUENCING_COMPLETED_FILENAME = "Run.completed"

RSYNC_FOLDERNAME = "rsync"
RSYNC_SCRIPT_FILENAME = "rsync.sh"
RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_FINISHED_FILENAME = "rsync.ended"
RSYNC_FAIL_FILENAME = "rsync.fail"
RSYNC_LOCK_FILENAME = "rsync.lock"
RSYNC_LOG_FILENAME = "rsync.log"
RSYNC_IGNORE_FILENAME = 'rsync.ignore'

# rsync exclude list
RSYNC_EXCLUDES = [
    "--exclude=Data/Intensities/L00?/C*/*.tif", # images - not generated anymore by sequencers
    "--exclude=Thumbnail_Images", # thumbnail images
    "--exclude=Data/Intensities/L00?/C*/*.cif", # intensitites
    "--exclude=%s" % SEQUENCING_COMPLETED_FILENAME
]

################################################################################
# METHODS
################################################################################
def setup_rsync(run_folder, dest_run_folder): 
    rsync_directory = os.path.join(run_folder, RSYNC_FOLDERNAME)
    rsync_script_path = os.path.join(rsync_directory, RSYNC_SCRIPT_FILENAME)
    rsync_started = os.path.join(rsync_directory, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(rsync_directory, RSYNC_FINISHED_FILENAME)
    rsync_log = os.path.join(rsync_directory, RSYNC_LOG_FILENAME)
    rsync_fail = os.path.join(rsync_directory, RSYNC_FAIL_FILENAME)
    rsync_lock = os.path.join(os.path.dirname(run_folder), RSYNC_LOCK_FILENAME)
    run_completed = os.path.join(run_folder, SEQUENCING_COMPLETED_FILENAME)

    dest_basedir = os.path.dirname(dest_run_folder)
    dest_rsync_directory = os.path.join(dest_run_folder, RSYNC_FOLDERNAME)

    # create rsync folder
    if not os.path.exists(rsync_directory):
        os.makedirs(rsync_directory)
        log.info('%s created' % rsync_directory)
    else:
        log.debug('%s already exists' % rsync_directory)
        
    # create rsync script 
    if not os.path.exists(rsync_script_path):    
        rsync_script_file = open(rsync_script_path, 'w')
        rsync_options = "-av %s %s %s > %s 2>&1" % (" ".join(RSYNC_EXCLUDES), run_folder, dest_basedir, rsync_log)
        copy_finished = "%s %s/." % (rsync_finished, dest_rsync_directory)
        copy_run_completed = "%s %s/." % (run_completed, dest_run_folder)
        command = """
touch %s
touch %s

if ( rsync %s )
then 
    touch %s
    cp %s
    cp %s
else 
    touch %s 
fi

rm %s
        """ % (rsync_started, rsync_lock, rsync_options, rsync_finished, copy_finished, copy_run_completed, rsync_fail, rsync_lock)
        rsync_script_file.write(utils.LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
        rsync_script_file.close()
        os.chmod(rsync_script_path, 0755)
        log.info('%s created' % rsync_script_path)
    else:
        log.debug('%s already exists' % rsync_script_path)

def rsync(run_folder, dry_run=True):
    rsync_directory = os.path.join(run_folder, RSYNC_FOLDERNAME)
    rsync_script_path = os.path.join(rsync_directory, RSYNC_SCRIPT_FILENAME)
    rsync_started = os.path.join(rsync_directory, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(rsync_directory, RSYNC_FINISHED_FILENAME)
    rsync_fail = os.path.join(rsync_directory, RSYNC_FAIL_FILENAME)
    rsync_lock = os.path.join(os.path.dirname(run_folder), RSYNC_LOCK_FILENAME)
    run_completed = os.path.join(run_folder, SEQUENCING_COMPLETED_FILENAME)

    # run rsync script to synchronise data from sequencing servers to lustre
    if os.path.exists(rsync_script_path):            
        if not os.path.exists(rsync_started):
            if not os.path.exists(rsync_lock):
                if sequencing_completed(run_folder) and os.path.exists(run_completed):
                    utils.touch(rsync_lock)
                    utils.run_bg_process(['sh', '%s' % rsync_script_path], dry_run)
                else:
                    log.debug("nothing to rsync yet - sequencing not completed")
            else:
                log.info('%s presents - another rsync process is running' % rsync_lock)
        else:
            if not os.path.exists(rsync_finished):
                if os.path.exists(rsync_fail):
                    log.warn("[***FAIL***] rsync for %s has failed." % run_folder)
                    log.warn("please investigate %s." % rsync_log)
                else:
                    log.info('%s is currently being synchronised' % run_folder)
            else:
                log.info('%s has been synchronised successfully' % run_folder)
    else:
        log.warn('%s is missing' % rsync_script_path)

def register_run_completed(run_folder):
    run_completed = os.path.join(run_folder, SEQUENCING_COMPLETED_FILENAME)
    if sequencing_completed(run_folder):
        if not os.path.exists(run_completed):
            utils.touch(run_completed)
            log.info("%s created" % run_completed)
        else:
            log.debug("%s already exists" % run_completed)
            
def update_status(update_status, soap_url, run, run_folder, dest_run_folder):
    # create soap client
    soap_client = Client("%s?wsdl" % soap_url)

    # update lims status when sequencing completed and rsynced
    if rsync_and_run_completed(run_folder) and rsync_and_run_completed(dest_run_folder):
        log.info('*** RSYNC AND RUN COMPLETED ****************************************************')
        # update status in lims
        if update_status:
            utils.set_run_complete(soap_client, run, lims.SEQUENCING_COMPLETE_STATUS)
        else:
            log.debug('lims status not updated - use --update-status option to turn it on')
    else:
        log.debug('lims status not updated - run/rsync not finished yet')

################################################################################
# UTILITY METHODS
################################################################################
def sequencing_completed(run_folder):
    instrument_match = False
    files_found = True
    for instrument in list(INSTRUMENTS.viewkeys()):
        if instrument in run_folder:
            for filename in INSTRUMENTS[instrument]:
                if not os.path.exists(os.path.join(run_folder, filename)):
                    files_found = False
            instrument_match = True
    return instrument_match and files_found

def rsync_and_run_completed(run_folder):
    rsync_directory = os.path.join(run_folder, RSYNC_FOLDERNAME)
    run_completed = os.path.join(run_folder, SEQUENCING_COMPLETED_FILENAME)
    rsync_started = os.path.join(rsync_directory, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(rsync_directory, RSYNC_FINISHED_FILENAME)
    # sequencing not finished
    if not os.path.exists(run_completed):
        return False
    # rsync not finished or started
    if not os.path.exists(rsync_finished) or not os.path.exists(rsync_started):
        return False
    return True    

################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'")
    parser.add_option("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'")
    parser.add_option("--dburl", dest="dburl", action="store", default=lims.DB_SOLEXA, help="database url [read only access] - default set to '%s'" % lims.DB_SOLEXA)
    parser.add_option("--soapurl", dest="soapurl", action="store", default=lims.SOAP_URL, help="soap url [for updating status only] - default set to '%s'" % lims.SOAP_URL)
    parser.add_option("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_option("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_option("--update-status", dest="update_status", action="store_true", default=False, help="use this option to update the status of a run in lims when process completed")
    parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_option("--email", dest="email", action="store_true", default=False, help="Send WARN logs by email")
    parser.add_option("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    (options, args) = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
    if options.email:
        log.addHandler(logger.set_smtp_handler('sync.py logs'))
                  
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
        
    # get all started runs
    runs = lims.StartedRuns(options.dburl, options.run_number)
    for run in runs.filtered_runs:
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run.runNumber)
        log.info('--------------------------------------------------------------------------------')
        # check run folder in basedir for analysis
        run_folder = utils.locate_run_folder(run.pipelinePath, options.basedir, False)
        if run_folder:
            # check rsync.ignore is not present
            rsync_ignore = os.path.join(run_folder, RSYNC_IGNORE_FILENAME)
            if not os.path.exists(rsync_ignore):
                # get/create dest folder to synchronize run folder
                dest_run_folder = utils.locate_run_folder(run.pipelinePath, options.lustredir)
                log.info('--- REGISTER RUN COMPLETED -----------------------------------------------------')
                register_run_completed(run_folder)
                log.info('--- SETUP RSYNC ----------------------------------------------------------------')
                setup_rsync(run_folder, dest_run_folder)
                log.info('--- RUN RSYNC ------------------------------------------------------------------')
                rsync(run_folder, options.dry_run)
                log.info('--- UPDATE STATUS --------------------------------------------------------------')
                update_status(options.update_status, options.soapurl, run, run_folder, dest_run_folder)
            else:
                log.info('%s is present' % rsync_ignore)
        else:
            log.debug('%s does not exists in %s' % (run.pipelinePath, options.basedir))

if __name__ == "__main__":
	sys.exit(main())

