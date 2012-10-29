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

# Default filenames
SEQUENCING_COMPLETED_FILENAME = "Run.completed"

# rsync exclude list
RSYNC_EXCLUDE = { 
    "primary" : "--exclude=Data/Intensities/*_pos.txt --exclude=Data/Intensities/L00? --exclude=Data/Intensities/BaseCalls --exclude=*/temp/* --exclude=fastqc --exclude=mga --exclude=demultiplex --exclude=secondary",
    "mga" : "",
    "demultiplex" : "",
    "fastqc" : "",
    "secondary" : "",                   
}

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
        dest_pipeline_directory = os.path.join(dest_run_folder, pipeline_name)
        
        # create rsync-pipeline script 
        if os.path.exists(pipeline_directory):
            if not os.path.exists(rsync_script_path):    
                rsync_script_file = open(rsync_script_path, 'w')
                if pipeline_name is 'primary':
                    rsync_options = "-av %s %s %s > %s 2>&1" % (RSYNC_EXCLUDE[pipeline_name], run_folder, dest_basedir, rsync_log)
                else:
                    rsync_options = "-av %s %s %s > %s 2>&1" % (RSYNC_EXCLUDE[pipeline_name], pipeline_directory, dest_run_folder, rsync_log)
                copy_finished = "%s %s/." % (rsync_finished, dest_pipeline_directory)
                command = "touch %s; touch %s; rsync %s; touch %s; cp %s; rm %s" % (rsync_started, rsync_lock, rsync_options, rsync_finished, copy_finished, rsync_lock)
                rsync_script_file.write(LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
                rsync_script_file.close()
                log.info('%s created' % rsync_script_path)
            else:
                log.debug('%s already exists' % rsync_script_path)
        else:
            log.error('%s is missing' % pipeline_directory)

def _rsync_run(run_folder, dry_run=True):
    rsync_script_path = os.path.join(run_folder, RSYNC_SCRIPT_FILENAME)
    pipeline_started = os.path.join(run_folder, PIPELINE_STARTED_FILENAME)
    pipeline_finished = os.path.join(run_folder, PIPELINE_FINISHED_FILENAME)
    rsync_started = os.path.join(run_folder, RSYNC_STARTED_FILENAME)
    rsync_finished = os.path.join(run_folder, RSYNC_FINISHED_FILENAME)
    rsync_lock = os.path.join(os.path.dirname(run_folder), RSYNC_LOCK_FILENAME)

    # run rsync-pipeline script to synchronise data from lustre to lbio03
    # rsync primary first
    if os.path.exists(rsync_script_path):            
        if os.path.exists(pipeline_started) and os.path.exists(pipeline_finished):
            if not os.path.exists(rsync_started):
                if not os.path.exists(rsync_lock):
                    if not pipeline_name is 'primary':
                        if process_completed(run_folder, ['primary']):
                            touch(rsync_lock)
                            run_bg_process(['sh', '%s' % rsync_script_path], dry_run)
                        else:
                            log.debug("nothing to rsync yet - primary pipeline not complete")
                    else:
                        touch(rsync_lock)
                        run_bg_process(['sh', '%s' % rsync_script_path], dry_run)
                else:
                    log.info('%s presents - another rsync process is running' % rsync_lock)
            else:
                if not os.path.exists(rsync_finished):
                    log.info('%s pipeline is currently being synchronised' % pipeline_name)
                else:
                    log.info('%s pipeline has been synchronised' % pipeline_name)
        else:
            log.debug("nothing to rsync yet - %s and/or %s missing" % (PIPELINE_STARTED_FILENAME, PIPELINE_FINISHED_FILENAME))
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
    parser.add_option("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'")
    parser.add_option("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'")
    parser.add_option("--dburl", dest="dburl", action="store", default=DB_URL, help="database url [read only access] - default set to '%s'" % DB_URL)
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
                  
    for option in ['basedir', 'archivedir']:
        if getattr(options, option) == None:
            print "Please supply a --%s parameter.\n" % (option)
            parser.print_help()
            sys.exit()
            
    if not os.path.exists(options.basedir):
        log.error("%s does not exists - check your '--basedir' option" % options.basedir)
        sys.exit(1)
    
    if not glob.glob(options.archivedir):
        log.error("%s does not exists - check your '--archivedir' option" % options.archivedir)
        sys.exit(1)
        
    # get completed runs that needs to be synchronised
    runs = Runs(options.dburl, options.run_number)
    for run in runs.runs:
        # check run folder in basedir for analysis
        run_folder = os.path.join(options.basedir, run.pipelinePath)
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run_folder)
        log.info('--------------------------------------------------------------------------------')
        if os.path.exists(run_folder):
            # check sequencing process has finished - do not just rely on lims status
            sequencing_completed = os.path.join(run_folder, SEQUENCING_COMPLETED_FILENAME)
            # check analysis.ignore is not present - stop running autopipe if present
            analysis_ignore = os.path.join(run_folder, ANALYSIS_IGNORE_FILENAME)
            if os.path.exists(sequencing_completed) and not os.path.exists(analysis_ignore):
                # get/create dest folder to synchronize run folder
                dest_run_folder = locate_archive_run_folder(os.path.basename(run_folder), options.archivedir)

                # get list of pipeline names for processing and completion
                if run.multiplexed == 1:
                    pipelines = MULTIPLEX_PIPELINES
                    pipelines_for_completion = MULTIPLEX_PIPELINES
                else:
                    pipelines = PIPELINES
                    pipelines_for_completion = PIPELINES
                if options.step:
                    pipelines = {options.step : ""}
                
                log.info('--- SETUP PIPELINES ------------------------------------------------------------')
                _setup_pipelines(run_folder, run.runNumber, pipelines, options.softdir, options.soapurl, options.dry_run)
                log.info('--- SETUP RSYNC ----------------------------------------------------------------')
                _setup_rsync_pipelines(dest_run_folder, run_folder, pipelines, options.dry_run)
                log.info('--- RUN PIPELINES --------------------------------------------------------------')
                _run_pipelines(run_folder, run.runNumber, pipelines, options.softdir, options.cluster, options.dry_run)
                log.info('--- RUN RSYNC ------------------------------------------------------------------')
                _rsync_pipelines(run_folder, pipelines, options.dry_run)
                log.info('--- UPDATE STATUS --------------------------------------------------------------')
                _register_process_completed(options.update_status, options.soapurl, run, run_folder, dest_run_folder, pipelines_for_completion)
            else:
                if not os.path.exists(sequencing_completed):
                    log.warning('%s does not exists' % sequencing_completed)
                if os.path.exists(analysis_ignore):
                    log.info('%s is present' % analysis_ignore)
        else:
            log.error('%s does not exists' % run_folder)
        

if __name__ == "__main__":
	sys.exit(main())

