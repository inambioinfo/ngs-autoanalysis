#!/usr/bin/env python
# encoding: utf-8
"""
solexa_autopipe.py

Made as a temporary replacement of solexa_autoanalysis.pl

Created by Anne Pajon on 2012-10-05.

-----------------------------------------------
INFO TO INSTALL DEPENDENCIES ON SOLs
-----------------------------------------------
cd /home/mib-cri/software/Python-2.7.3/

wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz
tar -zxvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
/home/mib-cri/software/python2.7/bin/python setup.py install

cd ..
wget http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz
tar -zxvf MySQL-python-1.2.3.tar.gz
cd MySQL-python-1.2.3
emacs site.cfg # change threadsafe = True to threadsafe = False
/home/mib-cri/software/python2.7/bin/python setup.py build
/home/mib-cri/software/python2.7/bin/python setup.py install

cd ..
wget http://prdownloads.sourceforge.net/sqlalchemy/SQLAlchemy-0.7.9.tar.gz
cd SQLAlchemy-0.7.9
/home/mib-cri/software/python2.7/bin/python setup.py install

cd ..
wget https://fedorahosted.org/releases/s/u/suds/python-suds-0.4.tar.gz
tar -zxvf python-suds-0.4.tar.gz
/home/mib-cri/software/python2.7/bin/python setup.py install

cd /home/mib-cri/bin/
ln -s /home/mib-cri/software/python2.7/bin/python python
"""

import sys, os, glob
import optparse
import logging
import logging.handlers
import subprocess 
from collections import OrderedDict

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

# logging definition
log = logging.getLogger("autopipe")
formatter = logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s: %(message)s')
log.setLevel(logging.DEBUG)

# Database url
DB_URL = "mysql://readonly@uk-cri-lbio04/cri_solexa"

# Soap url
SOAP_URL = "http://uk-cri-ldmz02.crnet.org/solexa-ws/SolexaExportBeanWS"

# Pipeline definitions
PIPELINES = {
    "primary": [],
    "mga": ["primary"],
    "fastqc": ["primary"],
    "secondary": ["primary"]}
    
MULTIPLEX_PIPELINES = {
    "primary": [],
    "mga": ["primary"],
    "demultiplex": ["primary"],
    "fastqc": ["primary"],
    "secondary": ["primary","demultiplex"]}

# Pipeline create-metafile extra options
PIPELINES_SETUP_OPTIONS = {
    "primary": "",
    "mga": "--create-sample-sheet",
    "demultiplex": "--index-files",
    "fastqc": "",
    "secondary": "--demultiplexed"}
        
# Software pipeline path
SOFT_PIPELINE_PATH = "/home/mib-cri/software/pipelines"

# Cluster host
CLUSTER_HOST = "uk-cri-lcst01"

# Default filenames
SETUP_SCRIPT_FILENAME = "setup-pipeline.sh"
RUN_SCRIPT_FILENAME = "run-pipeline.sh"
RSYNC_SCRIPT_FILENAME = "rsync.sh"

CREATE_METAFILE_FILENAME = "create-metafile"
RUN_META_FILENAME = "run-meta.xml"
RUN_PIPELINE_FILENAME = "run-pipeline"

PIPELINE_STARTED_FILENAME = "pipeline.started"
PIPELINE_FINISHED_FILENAME = "pipeline.ended"
PIPELINE_FAILED_FILENAME = "pipeline.failed"

RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_FINISHED_FILENAME = "rsync.ended"
RSYNC_LOCK_FILENAME = "rsync.lock"
RSYNC_LOG_FILENAME = "rsync.log"

SEQUENCING_COMPLETED_FILENAME = "Run.completed"
PRIMARY_COMPLETED_FILENAME = "Run.primary.completed"
PROCESS_COMPLETED_FILENAME = "Run.all.completed"
ANALYSIS_IGNORE_FILENAME = "analysis.ignore"

# Default lims status
PRIMARY_COMPLETE = 'PRIMARY COMPLETE'
ALL_COMPLETE = 'COMPLETE'

# Template for setup-pipeline.sh
LOCAL_SCRIPT_TEMPLATE = '''
#!/bin/bash
#
# Shell script for running command(s) locally
#

echo "%(cmd)s"

%(cmd)s

'''

# Template for run-pipeline.sh
LSF_SCRIPT_TEMPLATE = '''
#!/bin/bash
# 
# Shell script for executing run-pipeline on the cluster
#

export MEM_VALUE=2048
export MEM_LIMIT=$[${MEM_VALUE}*1024]
export JAVA_OPTS="-Xmx$[${MEM_VALUE}-512]M -Xms$[${MEM_VALUE}-512]M"

echo "ssh %(cluster)s \\"cd %(work_dir)s; touch pipeline.started; bsub -M ${MEM_LIMIT} -R 'select[mem>=${MEM_VALUE}] rusage[mem=${MEM_VALUE}]' -J %(job_name)s -o %(job_name)s_%%J.out -q solexa %(cmd)s\\""

ssh %(cluster)s "cd %(work_dir)s; touch pipeline.started; bsub -M ${MEM_LIMIT} -R 'select[mem>=${MEM_VALUE}] rusage[mem=${MEM_VALUE}]' -J %(job_name)s -o %(job_name)s_%%J.out -q solexa %(cmd)s"

'''

# rsync exclude list
RSYNC_EXCLUDE = { 
    "primary" : "--exclude=Data/Intensities/*_pos.txt --exclude=Data/Intensities/L00? --exclude=Data/Intensities/BaseCalls --exclude=*/temp/* --exclude=fastqc --exclude=mga --exclude=demultiplex --exclude=secondary",
    "mga" : "",
    "demultiplex" : "",
    "fastqc" : "",
    "secondary" : "",                   
}

################################################################################
# PIPELINE METHODS
################################################################################

def _setup_pipelines(run_folder, run_number, pipelines, soft_path, soap_url, dry_run=True):        
    for pipeline_name in list(pipelines.viewkeys()):
        log.info('--- %s' % pipeline_name.upper())
        pipeline_directory = os.path.join(run_folder, pipeline_name)
        setup_script_path = os.path.join(pipeline_directory, SETUP_SCRIPT_FILENAME)
        run_meta = os.path.join(pipeline_directory, RUN_META_FILENAME)  
        
        # create pipeline folder
        if not os.path.exists(pipeline_directory):
            os.makedirs(pipeline_directory)
            log.info('%s created' % pipeline_directory)
        else:
            log.debug('%s already exists' % pipeline_directory)
            
        # create setup-pipeline script 
        if not os.path.exists(setup_script_path):    
            setup_script_file = open(setup_script_path, 'w')
            command = "%s/%s/bin/%s --basedir=%s --queue=solexa --url=%s --notifications %s %s %s" % (soft_path, pipeline_name, CREATE_METAFILE_FILENAME, os.path.dirname(run_folder), soap_url, PIPELINES_SETUP_OPTIONS[pipeline_name], run_number, run_meta)
            setup_script_file.write(LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
            # TODO: copy pipeline definition
            setup_script_file.close()
            log.info('%s created' % setup_script_path)
        else:
            log.debug('%s already exists' % setup_script_path)
        
        # run setup-pipeline script to create meta data 
        if not os.path.exists(run_meta):
            if dependencies_satisfied(run_folder, pipeline_name, pipelines):
                run_process(['sh', '%s' % setup_script_path], dry_run)
            else:
                log.info('%s pipeline dependencies not satisfied' % pipeline_name)
        else:
            # TODO: check output file for errors
            log.debug('%s already exists' % run_meta)
            
def _run_pipelines(run_folder, run_number, pipelines, soft_path, cluster_host, dry_run=True):
    for pipeline_name in list(pipelines.viewkeys()):
        log.info('--- %s' % pipeline_name.upper())
        pipeline_directory = os.path.join(run_folder, pipeline_name)
        run_script_path = os.path.join(pipeline_directory, RUN_SCRIPT_FILENAME)
        job_name = "%s_%s_pipeline" % (run_number, pipeline_name)
        pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
        pipeline_finished = os.path.join(pipeline_directory, PIPELINE_FINISHED_FILENAME)
        run_meta = os.path.join(pipeline_directory, RUN_META_FILENAME)  
        
        # create run-pipeline script
        if not os.path.exists(run_script_path):
            run_script_file = open(run_script_path, 'w')
            if cluster_host:
                command = "%s/%s/bin/%s --mode=lsf %s" % (soft_path, pipeline_name, RUN_PIPELINE_FILENAME, RUN_META_FILENAME)
                run_script_file.write(LSF_SCRIPT_TEMPLATE % {'cluster': cluster_host, 'work_dir':pipeline_directory, 'job_name':job_name, 'cmd':command})
            else:
                command = "cd %s; touch %s; %s/%s/bin/%s --mode=local %s" % (pipeline_directory, PIPELINE_STARTED_FILENAME, soft_path, pipeline_name, RUN_PIPELINE_FILENAME, RUN_META_FILENAME)
                run_script_file.write(LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
            run_script_file.close()
            log.info('%s created' % run_script_path)
        else:
            log.debug('%s already exists' % run_script_path)
        
        # run run-pipeline script to run the pipeline
        if os.path.exists(run_meta):
            # pipeline not started
            if not os.path.exists(pipeline_started):
                # no pipeline.finished file, then run-pipeline
                if not os.path.exists(pipeline_finished):
                    if dependencies_satisfied(run_folder, pipeline_name, pipelines):
                        run_process(['sh', '%s' % run_script_path], dry_run)
                    else:
                        log.info('%s pipeline dependencies not satisfied' % pipeline_name)
                else:
                    log.error("%s presents with no %s" % (pipeline_finished, PIPELINE_STARTED_FILENAME))
            # pipeline started
            else:
                # pipeline not finished
                if not os.path.exists(pipeline_finished):
                    job_output = glob.glob(os.path.join(pipeline_directory, '%s_*.out' % job_name))
                    # output file presents - check for errors
                    if job_output:
                        if pipeline_success(job_output):
                            log.info("%s pipeline finished successfully. %s do not exist yet." % (pipeline_name, pipeline_finished))
                        else:
                            log.error(">>> %s pipeline in %s has failed." % (pipeline_name, run_folder))
                            log.error(">>> please investigate %s." % job_output)
                    else:
                        log.info("%s pipeline in %s has not finished." % (pipeline_name, run_folder))
                # pipeline finished
                else:
                    log.info("%s pipeline finished successfully." % pipeline_name)
        else:
            log.warn("%s is missing" % run_meta)
            
def _setup_rsync_pipelines(dest_run_folder, run_folder, pipelines, dry_run=True): 
    for pipeline_name in list(pipelines.viewkeys()):       
        pipeline_directory = os.path.join(run_folder, pipeline_name)
        rsync_script_path = os.path.join(pipeline_directory, RSYNC_SCRIPT_FILENAME)
        rsync_started = os.path.join(pipeline_directory, RSYNC_STARTED_FILENAME)
        rsync_finished = os.path.join(pipeline_directory, RSYNC_FINISHED_FILENAME)
        rsync_log = os.path.join(pipeline_directory, RSYNC_LOG_FILENAME)
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

def _rsync_pipelines(run_folder, pipelines, dry_run=True):
    for pipeline_name in list(pipelines.viewkeys()):
        log.info('--- %s' % pipeline_name.upper())
        pipeline_directory = os.path.join(run_folder, pipeline_name)
        rsync_script_path = os.path.join(pipeline_directory, RSYNC_SCRIPT_FILENAME)
        pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
        pipeline_finished = os.path.join(pipeline_directory, PIPELINE_FINISHED_FILENAME)
        rsync_started = os.path.join(pipeline_directory, RSYNC_STARTED_FILENAME)
        rsync_finished = os.path.join(pipeline_directory, RSYNC_FINISHED_FILENAME)
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

def _register_process_completed(update_status, soap_url, run, run_folder, dest_run_folder, pipelines):
    primary_completed_path = os.path.join(run_folder, PRIMARY_COMPLETED_FILENAME)
    dest_primary_completed_path = os.path.join(dest_run_folder, PRIMARY_COMPLETED_FILENAME)
    process_completed_path = os.path.join(run_folder, PROCESS_COMPLETED_FILENAME)
    dest_process_completed_path = os.path.join(dest_run_folder, PROCESS_COMPLETED_FILENAME)
    # create soap client
    soap_client = Client("%s?wsdl" % soap_url)
    
    # touch Run.primary.complete when process completed
    if process_completed(run_folder, ['primary']):
        if not os.path.exists(primary_completed_path):
            touch (primary_completed_path)
        if not os.path.exists(dest_primary_completed_path):
            touch (dest_primary_completed_path)
        log.info('*** PRIMARY COMPLETED **********************************************************')
    else:
        # remove Run.primary.complete when primary not complete and file exists
        if os.path.exists(primary_completed_path):
            os.remove(primary_completed_path)
        if os.path.exists(dest_primary_completed_path):
            os.remove(dest_primary_completed_path)
        
    # update lims analysis status when all processes completed and rsynced
    if process_completed(run_folder, list(pipelines.viewkeys())):
        if not os.path.exists(process_completed_path):
            touch(process_completed_path)
        if not os.path.exists(dest_process_completed_path):
            touch(dest_process_completed_path)
        log.info('*** PROCESS COMPLETED **********************************************************')
        # update analysis status in lims
        if update_status:
            set_analysis_status(soap_client, run, ALL_COMPLETE)
        else:
            log.debug('lims not updated - use --update-status option to turn it on')
    else:
        # update lims analysis status when just primary completed and rsynced
        if process_completed(run_folder, ['primary']):
            # update analysis status in lims
            if update_status:
                set_analysis_status(soap_client, run, PRIMARY_COMPLETE)
            else:
                log.debug('lims not updated - use --update-status option to turn it on')
        # remove Run.all.complete when process not completed and file exists
        if os.path.exists(process_completed_path):
            os.remove(process_completed_path)
        if os.path.exists(dest_process_completed_path):
            os.remove(dest_process_completed_path)
    
################################################################################
# UTILITY METHODS
################################################################################
def run_process(cmd, dry_run=True):
    if not dry_run:
        process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = process.communicate()
        log.info("command '%s' executed" % " ".join(cmd))
        if stdout:
            log.debug(stdout)
        if stderr:
            log.error(stderr)
        return stdout
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def run_bg_process(cmd, dry_run=True):
    if not dry_run:
        subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.info("command '%s' executed" % " ".join(cmd))
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def touch(fname, times=None):
    with file(fname, 'wa'):
        os.utime(fname, times)

def pipeline_success(output_files):
    for output_file in output_files:
        with open(output_file) as output:
            head=[output.next() for x in xrange(50)]
            for line in head:
                if 'Successfully completed' in line:
                    return True
    return False
        
def dependencies_satisfied(run_folder, pipeline_name, pipelines):
    pipeline_dependencies = pipelines[pipeline_name]
    log.debug('%s pipeline dependencies: [%s]' % (pipeline_name, ",".join(pipeline_dependencies)))
    for dep_pipeline_name in pipeline_dependencies:
        pipeline_directory = os.path.join(run_folder, dep_pipeline_name)
        if not os.path.exists("%s/%s" % (pipeline_directory, PIPELINE_FINISHED_FILENAME)):
            return False
    return True

def process_completed(run_folder, list_pipelines):
    for pipeline_name in list_pipelines:
        pipeline_directory = os.path.join(run_folder, pipeline_name)
        pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
        pipeline_finished = os.path.join(pipeline_directory, PIPELINE_FINISHED_FILENAME)
        rsync_started = os.path.join(pipeline_directory, RSYNC_STARTED_FILENAME)
        rsync_finished = os.path.join(pipeline_directory, RSYNC_FINISHED_FILENAME)
        # pipeline not finished or started
        if not os.path.exists(pipeline_finished) or not os.path.exists(pipeline_started):
            return False
        # rsync not finished or started
        if not os.path.exists(rsync_finished) or not os.path.exists(rsync_started):
            return False
    return True
    
def set_analysis_status(solexa_soap, run, status):
    if not run.analysisStatus == status:
        solexa_soap.service.setAnalysisStatus(run.process_id, status)
        log.info('analysis status in lims set to %s for process id %s' % (status, run.process_id))
    else:
        log.info('analysis status in lims already set to %s for process id %s' % (status, run.process_id))
    
def get_smallest_volume(archive_glob):
    volumes = glob.glob(archive_glob)
    if volumes:
        volume_sizes = {}
        for volume in volumes:
            device, size, used, available, percent, mountpoint = run_process(['df', '%s' % volume], False).split("\n")[1].split()
            volume_sizes[volume]=used
        min_volume = min(volume_sizes, key=lambda x: volume_sizes.get(x))
        return min_volume
    
def locate_archive_run_folder(run_folder_name, archive_glob):
    run_folders = glob.glob("%s/%s" % (archive_glob,run_folder_name))
    if run_folders:
        if len(run_folders) == 1:
            log.debug("archive run folder %s already exists" % run_folders)
            return run_folders[0]
        else:
            log.error("more than one archive run folders %s found %s" % (run_folder_name, run_folders))
    else:
        volume_name = get_smallest_volume(archive_glob)
        if volume_name:
            run_folder = os.path.join(volume_name, run_folder_name)
            os.makedirs(run_folder)
            log.debug("archive run folder %s created" % run_folder)
            return run_folder
        else:
            log.error('no archive run folder %s found' % archive_glob)

################################################################################
# CLASS DEFINITION
################################################################################

class Runs:
    def __init__(self, _db_url, _run_number=None):
        # CRI lims database connection
        self.solexa_db = SqlSoup(_db_url)
        self.runs = []
        self.populateRuns(_run_number)

    def populateRuns(self, _run_number=None):
        # get one run
        if _run_number:
            run = self.solexa_db.solexarun.filter_by(runNumber=_run_number).one()
            if run.status == 'COMPLETE':
                self.runs.append(run)
            else:
                log.warning('Run %s has not been completed, its current status is %s.' % (run.runNumber, run.status))
        # get all runs
        else:
            runs = self.solexa_db.solexarun.all()
            for run in runs:
                # select completed runs that have not been analysed
                if run.status == 'COMPLETE' and not (run.analysisStatus == 'COMPLETE' or run.analysisStatus == 'SECONDARY COMPLETE'):
                    self.runs.append(run)
            
################################################################################
# MAIN
################################################################################
def main(argv=None):
    
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'")
    parser.add_option("--archivedir", dest="archivedir", action="store", help="archive base directories e.g. '/solexa0[1-8]/data/Runs'")
    parser.add_option("--softdir", dest="softdir", action="store", default=SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % SOFT_PIPELINE_PATH)
    parser.add_option("--dburl", dest="dburl", action="store", default=DB_URL, help="database url [read only access] - default set to '%s'" % DB_URL)
    parser.add_option("--soapurl", dest="soapurl", action="store", default=SOAP_URL, help="soap url [for updating status only] - default set to '%s'" % SOAP_URL)
    parser.add_option("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % CLUSTER_HOST)
    parser.add_option("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_option("--step", dest="step", action="store", choices=list(MULTIPLEX_PIPELINES.viewkeys()), help="pipeline step to choose from %s" % list(MULTIPLEX_PIPELINES.viewkeys()))
    parser.add_option("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_option("--update-status", dest="update_status", action="store_true", default=False, help="use this option to update the status of a run in lims when process completed")
    parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_option("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    (options, args) = parser.parse_args()

    # consol logging configuration
    consol_handler = logging.StreamHandler()
    consol_handler.setFormatter(formatter)
    log.addHandler(consol_handler)
    consol_handler.setLevel(logging.INFO)
    if options.debug:
        consol_handler.setLevel(logging.DEBUG)

    # rotating file logging configuration - 10 files of up to 5MB
    if options.logfile:
        file_handler = logging.handlers.RotatingFileHandler(options.logfile, maxBytes=1024*1024*5, backupCount=10)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        log.addHandler(file_handler)
                  
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
        
    # get all completed runs that have not been analysed or just one run
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
    
    # TODO: publish external data - rsync to ldmz01
    # (1) create external directory with symlink to fastq files
    # (2) rsync to solexadmin@uk-cri-ldmz01:/dmz01/solexa/${institute}/current/SLX_????_CRIRUN_???.${fastq_filename}
    # TODO: remove data from lustre when process finished (currently done with solexa_cleanlustre.pl)
    # - when process completed - all pipelines finished and all rsync finished
    # - when lims status complete
    # - when no dont.delete file
    # remove Data/* ${pipeline_name}/* on lustre 
    

if __name__ == "__main__":
	sys.exit(main())


        

