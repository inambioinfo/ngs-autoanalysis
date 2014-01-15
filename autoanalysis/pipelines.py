#!/usr/bin/env python
# encoding: utf-8
"""
pipelines.py

$Id$

Created by Anne Pajon on 2012-11-22.
"""
################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import unittest
from collections import OrderedDict

# autoanalysis modules
import runfolders
import utils

################################################################################
# CONSTANTS
################################################################################
# Pipeline definitions and dependencies
PIPELINES = OrderedDict ([
    ("primary", []),
    ("mga", ["primary"]),
    ("fastqc", ["primary"]),
    ("fastq", ["primary"]),
    ("secondary", ["primary","fastq"])])
    
# External pipeline name
EXTERNAL_PIPELINE = 'external'
EXTERNAL_DEMUX_PIPELINE = 'external_demux'

# Pipeline commands
PIPELINE_SETUP_COMMAND = "%(bin_meta)s --basedir=%(basedir)s --queue=solexa --notifications --credentials=apiuser:apipassword %(options)s %(flowcell_id)s %(run_meta)s"

PIPELINE_RUN_COMMAND = "%(bin_run)s --mode=%(mode)s --clean %(run_meta)s"
PIPELINE_LOCAL_RUN_COMMAND = "cd %(work_dir)s; touch %(started)s; %(bin_run)s --mode=%(mode)s --clean %(run_meta)s"

# Template for rsync pipeline command
PIPELINE_RSYNC_COMMAND = '''
touch %(rsync_started)s
touch %(rsync_lock)s

if ( rsync %(rsync_options)s ) 
then
   touch %(rsync_ended)s
   cp %(rsync_ended)s %(archive_pipedir)s/.
else
    touch %(rsync_fail)s
fi

rm %(rsync_lock)s
'''

# Pipeline rsync exclude list
PIPELINE_RSYNC_EXCLUDE = { 
    "primary" : "--exclude=Data/Intensities/*_pos.txt --exclude=Data/Intensities/L00? --exclude=Data/Intensities/BaseCalls --exclude=fastqc --exclude=mga --exclude=fastq --exclude=secondary",
    "mga" : "",
    "fastqc" : "",
    "fastq" : "",
    "secondary" : "",                   
}

PIPELINE_RSYNC_ALL_EXCLUDE = "--exclude=temp --exclude=JobOutputs"

# Template for rsync runfolder command
RUNFOLDER_RSYNC_COMMAND = '''
touch %(rsync_started)s
touch %(rsync_lock)s

if ( rsync %(rsync_options)s )
then 
    touch %(rsync_ended)s
    cp %(rsync_ended)s %(archive_pipedir)s/.
    cp %(seq_completed)s %(archive_pipedir)s/../.
else 
    touch %(rsync_fail)s 
fi

rm %(rsync_lock)s
'''

# rsync exclude list
RUNFOLDER_RSYNC_EXCLUDE = [
    "--exclude=Data/Intensities/L00?/C*/*.tif", # images - not generated anymore by sequencers
    "--exclude=Data/RTALogs", 
    "--exclude=InterOp",
    "--exclude=Logs",
    "--exclude=Thumbnail_Images", # thumbnail images
    "--exclude=Data/Intensities/L00?/C*/*.cif", # intensitites
    "--exclude=Old*", # Anything that has been moved out of the way
    "--exclude=%s" % runfolders.SEQUENCING_COMPLETED
]

# Pipeline create-metafile extra options
PIPELINES_SETUP_OPTIONS = {
    "primary": "--index-files",
    "mga": "--create-sample-sheet --phix",
    "fastqc": "",
    "fastq": "--index-files",
    "secondary": ""}
        
# Software pipeline path
SOFT_PIPELINE_PATH = "/home/mib-cri/software/pipelines"

# ftp server
FTP_URL = "solexadmin@uk-cri-ldmz01:/dmz01/solexa"

# Default filenames
SETUP_SCRIPT_FILENAME = "setup-pipeline.sh"
RUN_SCRIPT_FILENAME = "run-pipeline.sh"

CREATE_METAFILE_FILENAME = "create-metafile"
RUN_META_FILENAME = "run-meta.xml"
RUN_PIPELINE_FILENAME = "run-pipeline"

PIPELINE_STARTED_FILENAME = "pipeline.started"
PIPELINE_ENDED_FILENAME = "pipeline.ended"
PIPELINE_FAILED_FILENAME = "pipeline.failed"

RSYNC_SCRIPT_FILENAME = "rsync.sh"
RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_ENDED_FILENAME = "rsync.ended"
RSYNC_FAIL_FILENAME = "rsync.failed"
RSYNC_LOG_FILENAME = "rsync.log"
RSYNC_LOCK_FILENAME = "rsync.lock"

PRIMARY_COMPLETED_FILENAME = "Analysis.primary.completed"

################################################################################
# CLASS PipelineDefinition
################################################################################        
class PipelineDefinition(object):

    def __init__(self, run, pipeline_name, software_path=SOFT_PIPELINE_PATH, cluster_host=None, use_limsdev=True):
        self.log = logging.getLogger(__name__)
        self.run = run
        self.pipeline_name = pipeline_name

        # create pipeline directory
        self.pipeline_directory = os.path.join(self.run.run_folder, self.pipeline_name)
        utils.create_directory(self.pipeline_directory)

        # create archive pipeline directory
        self.log.debug(self.run.dest_run_folder)
        self.log.debug(self.pipeline_name)
        self.archive_pipeline_directory = os.path.join(self.run.dest_run_folder, self.pipeline_name)
        #utils.create_directory(self.archive_pipeline_directory)
        self.rsync_lock = os.path.join(os.path.dirname(self.run.run_folder), RSYNC_LOCK_FILENAME)
        
        # shell script paths
        self.setup_script_path = os.path.join(self.pipeline_directory, SETUP_SCRIPT_FILENAME)
        self.run_script_path = os.path.join(self.pipeline_directory, RUN_SCRIPT_FILENAME)
        self.rsync_script_path = os.path.join(self.pipeline_directory, RSYNC_SCRIPT_FILENAME)

        self.pipeline_started = os.path.join(self.pipeline_directory, PIPELINE_STARTED_FILENAME)
        self.pipeline_ended = os.path.join(self.pipeline_directory, PIPELINE_ENDED_FILENAME)

        self.rsync_started = os.path.join(self.pipeline_directory, RSYNC_STARTED_FILENAME)
        self.rsync_ended = os.path.join(self.pipeline_directory, RSYNC_ENDED_FILENAME)
        self.rsync_fail = os.path.join(self.pipeline_directory, RSYNC_FAIL_FILENAME)
        self.rsync_log = os.path.join(self.pipeline_directory, RSYNC_LOG_FILENAME)

        # enviroment variables for setting up and running each pipeline
        self.env = {}
        self.setEnv(software_path, cluster_host, use_limsdev)
        
    def getHeader(self):
        return '--- %s' % self.pipeline_name.upper()
        
    def printHeader(self):
        self.log.info(self.getHeader())
        
    def setEnv(self, _software_path, _cluster_host, _use_limsdev):
        """set environment variables for generating shell scripts from their templates
        """
        self.env['bin_meta'] = '%s/%s/bin/%s' % (_software_path, self.pipeline_name, CREATE_METAFILE_FILENAME)
        self.env['bin_run'] = '%s/%s/bin/%s' % (_software_path, self.pipeline_name, RUN_PIPELINE_FILENAME)
        self.env['basedir'] = os.path.dirname(self.run.run_folder)
        if self.pipeline_name in PIPELINES_SETUP_OPTIONS.keys():
            if _use_limsdev:
                self.env['options'] = "%s --dev" % PIPELINES_SETUP_OPTIONS[self.pipeline_name]
            else:
                self.env['options'] = PIPELINES_SETUP_OPTIONS[self.pipeline_name]
        else:
            if _use_limsdev:
                self.env['options'] = '--dev'
            else:
                self.env['options'] = ''
        self.env['run_uid'] = self.run.run_uid
        self.env['flowcell_id'] = self.run.flowcell_id
        self.env['run_meta'] = os.path.join(self.pipeline_directory, RUN_META_FILENAME)
        if _cluster_host:
            self.env['mode'] = 'lsf' 
        else:
            self.env['mode'] = 'local'
        self.env['started'] = PIPELINE_STARTED_FILENAME
        self.env['mem_value'] = '2048'
        self.env['cluster'] = _cluster_host
        self.env['work_dir'] = self.pipeline_directory
        self.env['job_name'] = "%s_%s_pipeline" % (self.run.flowcell_id, self.pipeline_name)
        self.env['cmd'] = PIPELINE_RUN_COMMAND % self.env
        self.env['rsync_started'] = self.rsync_started
        self.env['rsync_lock'] = self.rsync_lock
        self.env['rsync_ended'] = self.rsync_ended
        self.env['rsync_fail'] = self.rsync_fail
        self.env['seq_completed'] = self.run.sequencing_completed
        if self.pipeline_name == 'primary':
            self.env['rsync_options'] = "-av %s %s %s %s > %s 2>&1" % (PIPELINE_RSYNC_ALL_EXCLUDE, PIPELINE_RSYNC_EXCLUDE[self.pipeline_name], self.run.run_folder, os.path.dirname(self.run.dest_run_folder), self.rsync_log)
        elif self.pipeline_name in PIPELINE_RSYNC_EXCLUDE.keys():
            self.env['rsync_options'] = "-av %s %s %s %s > %s 2>&1" % (PIPELINE_RSYNC_ALL_EXCLUDE, PIPELINE_RSYNC_EXCLUDE[self.pipeline_name], self.pipeline_directory, self.run.dest_run_folder, self.rsync_log)
        elif self.pipeline_name == 'rsync':
            self.env['rsync_options'] = "-av %s %s %s > %s 2>&1" % (" ".join(RUNFOLDER_RSYNC_EXCLUDE), self.run.run_folder, os.path.dirname(self.run.dest_run_folder), self.rsync_log)
        else:
            self.env['rsync_options'] = "-av %s %s %s > %s 2>&1" % (PIPELINE_RSYNC_ALL_EXCLUDE, self.pipeline_directory, self.run.dest_run_folder, self.rsync_log)                
        self.env['pipedir'] = self.pipeline_directory
        self.env['archive_pipedir'] = self.archive_pipeline_directory
        
    def createSetupPipelineScript(self):
        self.log.info('... create setup pipeline script ...............................................')
        try:
            if not os.path.exists(self.setup_script_path):
                utils.create_script(self.setup_script_path, PIPELINE_SETUP_COMMAND % self.env)
            else:
                self.log.debug('%s already exists' % self.setup_script_path)
        except:
            self.log.exception('unexpected error when creating setup pipeline script')
            raise
        
    def runSetupPipelineScript(self, _dependencies_satisfied=True, _dry_run=True):
        self.log.info('... run setup pipeline script ..................................................')
        try:
            if not os.path.exists(self.env['run_meta']):
                if _dependencies_satisfied:
                    utils.run_process(['sh', '%s' % self.setup_script_path], _dry_run)
                else:
                    self.log.info('%s pipeline dependencies not satisfied' % self.pipeline_name)
            else:
                self.log.debug('%s already exists' % self.env['run_meta'])
        except:
            self.log.exception('unexpected error when running setup pipeline script')
            raise
            
    def createRunPipelineScript(self):
        self.log.info('... create run pipeline script .................................................')
        try:
            if self.env['mode'] == 'lsf':
                utils.create_script(self.run_script_path, utils.LSF_CMD_TEMPLATE % self.env)
            else:
                utils.create_script(self.run_script_path, PIPELINE_LOCAL_RUN_COMMAND % self.env)
        except:
            self.log.exception('unexpected error when creating run pipeline script')
            raise
            
    def runRunPipelineScript(self, _dependencies_satisfied=True, _dry_run=True):
        self.log.info('... run run pipeline script ....................................................')
        if os.path.exists(self.env['run_meta']):
            # pipeline not started
            if not os.path.exists(self.pipeline_started):
                # no pipeline.finished file, then run-pipeline
                if not os.path.exists(self.pipeline_ended):
                    if _dependencies_satisfied:
                        utils.run_process(['sh', '%s' % self.run_script_path], _dry_run)
                    else:
                        self.log.info('%s pipeline dependencies not satisfied' % self.pipeline_name)
                else:
                    self.log.warn("%s presents with no %s" % (self.pipeline_ended, PIPELINE_STARTED_FILENAME))
            # pipeline started
            else:
                # pipeline not finished
                if not os.path.exists(self.pipeline_ended):
                    job_output = glob.glob(os.path.join(self.pipeline_directory, '%s_*.out' % self.env['job_name']))
                    # output file presents - check for errors
                    if job_output:
                        if utils.output_job_success(job_output):
                            self.log.info("%s pipeline finished successfully. %s do not exist yet." % (self.pipeline_name, self.pipeline_ended))
                        else:
                            self.log.error("[***FAIL***] %s pipeline in %s has failed." % (self.pipeline_name, self.run.run_folder))
                            self.log.error("please investigate %s." % job_output)
                    else:
                        self.log.info("%s pipeline in %s has not finished." % (self.pipeline_name, self.run.run_folder))
                # pipeline finished
                else:
                    self.log.info("[***OK***] %s pipeline finished successfully." % self.pipeline_name)
        else:
            self.log.warn("%s is missing" % self.env['run_meta'])
            
    def createRsyncPipelineScript(self):
        self.log.info('... create rsync pipeline script ...............................................')
        try:
            if not os.path.exists(self.rsync_script_path):
                utils.create_script(self.rsync_script_path, PIPELINE_RSYNC_COMMAND % self.env)
            else:
                self.log.debug('%s already exists' % self.rsync_script_path)
        except:
            self.log.exception('unexpected error when creating rsync pipeline script')
            raise
            
    def runRsyncPipelineScript(self, _dependencies_satisfied=True, _dry_run=True):
        """Run rsync script to synchronise data from lustre to lbio03
        Synchronise primary directory first, and then all the other pipeline folders
        """
        self.log.info('... run rsync pipeline script ..................................................')
        # rsync primary first
        if os.path.exists(self.rsync_script_path):            
            if os.path.exists(self.pipeline_started) and os.path.exists(self.pipeline_ended):
                if not os.path.exists(self.rsync_started):
                    if not os.path.exists(self.rsync_lock):
                        if not self.pipeline_name == 'primary':
                            if _dependencies_satisfied:
                                #utils.touch(self.rsync_lock, _dry_run)
                                utils.run_bg_process(['sh', '%s' % self.rsync_script_path], _dry_run)
                            else:
                                self.log.debug("nothing to rsync yet - primary pipeline not complete")
                        else:
                            #utils.touch(self.rsync_lock, _dry_run)
                            utils.run_bg_process(['sh', '%s' % self.rsync_script_path], _dry_run)
                    else:
                        self.log.info('%s presents - another rsync process is running' % self.rsync_lock)
                else:
                    if not os.path.exists(self.rsync_ended):
                        if os.path.exists(self.rsync_fail):
                            self.log.error("[***FAIL***] rsync for %s has failed." % self.run.run_folder)
                            self.log.error("please investigate %s." % self.rsync_log)
                        else:
                            self.log.info('%s pipeline is currently being synchronised' % self.pipeline_name)
                    else:
                        self.log.info('[***OK***] %s pipeline has been synchronised successfully' % self.pipeline_name)
            else:
                self.log.debug("nothing to rsync yet - %s and/or %s missing" % (PIPELINE_STARTED_FILENAME, PIPELINE_ENDED_FILENAME))
        else:
            self.log.warn('%s is missing' % self.rsync_script_path)
            
    def createRsyncRunFolderScript(self):
        self.log.info('... create rsync runfolder script ..............................................')
        try:
            if not os.path.exists(self.rsync_script_path):
                utils.create_script(self.rsync_script_path, RUNFOLDER_RSYNC_COMMAND % self.env)
            else:
                self.log.debug('%s already exists' % self.rsync_script_path)
        except:
            self.log.exception('unexpected error when creating rsync runfolder script')
            raise

    def runRsyncRunFolderScript(self, _dry_run=True):
        """Run rsync script to synchronise runfolder data from sequencing servers to lustre
        """
        self.log.info('... run rsync runfolder script .................................................')
        if os.path.exists(self.rsync_script_path):
            if not os.path.exists(self.rsync_started):
                if not os.path.exists(self.rsync_lock):
                    if self.run.isCompleted():
                        utils.touch(self.rsync_lock, _dry_run)
                        utils.run_bg_process(['sh', '%s' % self.rsync_script_path], _dry_run)
                    else:
                        self.log.debug("nothing to rsync yet - sequencing not completed")
                else:
                    self.log.info('%s presents - another rsync process is running' % self.rsync_lock)
            else:
                if not os.path.exists(self.rsync_ended):
                    if os.path.exists(self.rsync_fail):
                        self.log.error("[***FAIL***] rsync for %s has failed." % self.run.run_folder)
                        self.log.error("please investigate %s." % self.rsync_log)
                    else:
                        self.log.info('runfolder is currently being synchronised')
                else:
                    self.log.info('runfolder has been synchronised')
        else:
            self.log.warn('%s is missing' % self.rsync_script_path)
        
################################################################################
# CLASS Pipelines
################################################################################
class Pipelines(object):

    def __init__(self, run, pipeline_step=None, software_path=SOFT_PIPELINE_PATH, cluster_host=None, dry_run=True, use_limsdev=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.pipeline_step = pipeline_step
        self.software_path = software_path
        self.cluster_host = cluster_host
        self.dry_run = dry_run
        self.use_limsdev = use_limsdev 

        self.pipelines = PIPELINES
        if self.pipeline_step:
            self.pipelines = {self.pipeline_step : ""}
            
        self.primary_completed = os.path.join(self.run.run_folder, PRIMARY_COMPLETED_FILENAME)
        self.archive_primary_completed = os.path.join(self.run.dest_run_folder, PRIMARY_COMPLETED_FILENAME)
        self.all_completed = os.path.join(self.run.run_folder, runfolders.ANALYSIS_COMPLETED)
        self.archive_all_completed = os.path.join(self.run.dest_run_folder, runfolders.ANALYSIS_COMPLETED)
        
    def execute(self):
        """execute all pipelines or just one by creating a shell script and running it for
        each of these three steps: setup_pipeline, run_pipeline, and rsync_pipeline
        """
        if self.run.isCompleted():
            for pipeline_name in self.pipelines.keys():
                # create pipeline definition
                pipeline_definition = PipelineDefinition(self.run, pipeline_name, self.software_path, self.cluster_host, self.use_limsdev)
                pipeline_definition.printHeader()
                # - step 1 - create setup-pipeline script 
                pipeline_definition.createSetupPipelineScript()
                # run setup-pipeline script to create meta data 
                pipeline_definition.runSetupPipelineScript(self.areDependenciesSatisfied(pipeline_name), self.dry_run)
                # - step 2 - create run-pipeline script
                pipeline_definition.createRunPipelineScript()
                # run run-pipeline script to run the pipeline
                pipeline_definition.runRunPipelineScript(self.areDependenciesSatisfied(pipeline_name), self.dry_run)
                # - setp 3 - create rsync-pipeline script
                pipeline_definition.createRsyncPipelineScript()
                # run rsync-pipeline script
                pipeline_definition.runRsyncPipelineScript(self.areDependenciesSatisfied('primary'), self.dry_run)
            
    def registerCompletion(self, external_data=False):
        """ Create Analysis.primary.completed and Analysis.completed when pipelines
        have been successfully ran and synchronised and that external data has been published
        """
        # create Analysis.primary.completed when primary pipeline completed
        if self.arePipelinesCompleted(['primary']):
            if not os.path.exists(self.primary_completed):
                utils.touch (self.primary_completed)
            if not os.path.exists(self.archive_primary_completed):
                utils.touch (self.archive_primary_completed)
            self.log.info('*** PRIMARY COMPLETED **********************************************************')
        else:
            # remove Analysis.primary.completed when primary not completed and file exists
            if os.path.exists(self.primary_completed):
                os.remove(self.primary_completed)
            if os.path.exists(self.archive_primary_completed):
                os.remove(self.archive_primary_completed)

        # create Analysis.completed when all pipelines completed and rsynced and external data published
        if self.arePipelinesCompleted(self.pipelines.keys()) and self.isExternalDataPublished(external_data):
            if not os.path.exists(self.all_completed):
                utils.touch(self.all_completed)
            if not os.path.exists(self.archive_all_completed):
                utils.touch(self.archive_all_completed)
            self.log.info('*** ALL COMPLETED **************************************************************')
        else:
            # remove Analysis.completed when analysis not completed and file exists
            if os.path.exists(self.all_completed):
                os.remove(self.all_completed)
            if os.path.exists(self.archive_all_completed):
                os.remove(self.archive_all_completed)   
                
    ### Utility methods -------------------------------------------------------

    def areDependenciesSatisfied(self, pipeline_name):
        """For a given pipeline, checks that all dependent pipelines have finished
        Both pipeline.started and pipeline.ended need to be present
        """
        pipeline_dependencies = PIPELINES[pipeline_name]
        self.log.debug('%s pipeline dependencies: [%s]' % (pipeline_name, ",".join(pipeline_dependencies)))
        for dep_pipeline_name in pipeline_dependencies:
            pipeline_directory = os.path.join(self.run.run_folder, dep_pipeline_name)
            pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
            pipeline_ended = os.path.join(pipeline_directory, PIPELINE_ENDED_FILENAME)
            # pipeline not finished or started
            if not os.path.exists(pipeline_ended) or not os.path.exists(pipeline_started):
                return False
        return True

    def arePipelinesCompleted(self, list_pipelines, check_rsync=True):
        """Checks for a list of pipelines that each of them has finished and has
        been synchronised.
        pipeline.started and pipeline.ended need to be present as well as 
        rsync.started and rsync.ended 
        """
        for pipeline_name in list_pipelines:
            pipeline_directory = os.path.join(self.run.run_folder, pipeline_name)
            pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
            pipeline_ended = os.path.join(pipeline_directory, PIPELINE_ENDED_FILENAME)
            rsync_started = os.path.join(pipeline_directory, RSYNC_STARTED_FILENAME)
            rsync_ended = os.path.join(pipeline_directory, RSYNC_ENDED_FILENAME)
            # pipeline not finished or started
            if not os.path.exists(pipeline_ended) or not os.path.exists(pipeline_started):
                return False
            # rsync not finished or started
            if check_rsync:
                if not os.path.exists(rsync_ended) or not os.path.exists(rsync_started):
                    return False
        return True
        
    def isExternalDataPublished(self, external_data=False):
        """Checks that external data has been published
        """
        external_directory = os.path.join(self.run.dest_run_folder, EXTERNAL_PIPELINE)
        rsync_started = os.path.join(external_directory, RSYNC_STARTED_FILENAME)
        rsync_finished = os.path.join(external_directory, RSYNC_ENDED_FILENAME)
        if external_data:
            # rsync external data not finished or started
            if not os.path.exists(rsync_started) or not os.path.exists(rsync_finished):
                return False

        external_demux_directory = os.path.join(self.run.dest_run_folder, EXTERNAL_DEMUX_PIPELINE)
        demux_rsync_started = os.path.join(external_demux_directory, RSYNC_STARTED_FILENAME)
        demux_rsync_finished = os.path.join(external_demux_directory, RSYNC_ENDED_FILENAME)
        if external_data:
            # rsync demux external data not finished or started
            if not os.path.exists(demux_rsync_started) or not os.path.exists(demux_rsync_finished):
                return False

        return True

################################################################################
# CLASS External
################################################################################
class External(object):
    
    def __init__(self, run, external_data, dry_run=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.external_data = external_data
        self.pipeline_name = EXTERNAL_PIPELINE
        self.dry_run = dry_run
        
        self.pipelines_completed = self.arePipelinesCompleted(['primary'])

    def publish(self):
        """publish external data to ftp server - rsync to ldmz01
        create external directory with symlink to fastq files on archivedir (sol03) - not basedir (lustre) -
        synchronise external data to solexadmin@uk-cri-ldmz01:/dmz01/solexa/${institute}/current/
        """
        if self.run.isCompleted():
            if self.external_data:
                if self.run.dest_run_folder:
                    # create pipeline definition
                    pipeline_definition = PipelineDefinition(run=self.run, pipeline_name=self.pipeline_name)
                    pipeline_definition.printHeader()
                    # rsync fastq files when sync to archive finished
                    if self.pipelines_completed:
                        # create symlinks for external users
                        self.createSymlinks(pipeline_definition.archive_pipeline_directory)
                        # create rsync-pipeline script
                        self.createFtpRsyncScript(pipeline_definition.rsync_script_path, pipeline_definition.env)
                        # run rsync-pipeline script
                        self.runFtpRsyncScript(pipeline_definition.rsync_script_path, pipeline_definition.env)
                    else:
                        self.log.info('Rsync from lustre to archive not completed')
                else:
                    self.log.warn('%s does not exist' % self.run.dest_run_folder)
            else:
                self.log.info('No external data to publish')
            
    def arePipelinesCompleted(self, list_pipelines):
        """Checks for a list of pipelines that each of them has finished and has
        been synchronised.
        pipeline.started and pipeline.ended need to be present as well as 
        rsync.started and rsync.ended 
        """
        for pipeline_name in list_pipelines:
            pipeline_directory = os.path.join(self.run.dest_run_folder, pipeline_name)
            pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
            pipeline_ended = os.path.join(pipeline_directory, PIPELINE_ENDED_FILENAME)
            rsync_started = os.path.join(pipeline_directory, RSYNC_STARTED_FILENAME)
            rsync_ended = os.path.join(pipeline_directory, RSYNC_ENDED_FILENAME)
            # pipeline not finished or started
            if not os.path.exists(pipeline_ended) or not os.path.exists(pipeline_started):
                return False
            # rsync not finished or started
            if not os.path.exists(rsync_ended) or not os.path.exists(rsync_started):
                return False
        return True
    
    def createSymlinks(self, external_directory):
        """ Create symlink to external primary data into external folder
        3 files to symlink per lane per read:
            primary/SLX-7639.000000000-A4WMJ.s_1.r_1.fq.gz
            primary/SLX-7639.000000000-A4WMJ.s_1.r_1.failed.fq.gz
            primary/SLX-7639.000000000-A4WMJ.s_1.md5sums.txt
        """
        self.log.info('... create symlinks to external data ...........................................')
        for sample_id in list(self.external_data.viewkeys()):
            for ftpdir in self.external_data[sample_id]['to_ftpdirs']:
                # create ftpdir in external directory in run folder
                runfolder_ext_ftpdir = os.path.join(external_directory, ftpdir)
                utils.create_directory(runfolder_ext_ftpdir)
                filename = self.external_data[sample_id]['from_contenturi']
                splitted_filename = filename.split('.')
                splitted_filename_failed = splitted_filename
                splitted_filename_failed.insert(4, 'failed')
                filename_failed = ".".join(splitted_filename_failed)
                splitted_filename_md5sums = splitted_filename[:3]
                splitted_filename_md5sums.append('md5sums.txt')
                filename_md5sums = ".".join(splitted_filename_md5sums)
                splitted_index_filename = splitted_filename[:3]
                splitted_index_filename.append('index.csv')
                filename_index = ".".join(splitted_index_filename)
                try:
                    # create symlink
                    linkname = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename))
                    linkname_failed = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename_failed))
                    linkname_md5sums = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename_md5sums))
                    linkname_index = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename_index))
                    utils.create_symlink(filename, linkname)
                    utils.create_symlink(filename_failed, linkname_failed)
                    utils.create_symlink(filename_md5sums, linkname_md5sums)
                    utils.create_symlink(filename_index, linkname_index)
                except:
                    self.log.exception('unexpected error when creating symlink')
                    continue

    def createFtpRsyncScript(self, rsync_script, env):
        """Create rsync script for external data
        """
        self.log.info('... create ftp rsync pipeline script ...........................................')
        FTP_RSYNC_COMMAND = '''
        touch %(rsync_started)s
        touch %(rsync_lock)s

        if ( %(rsync_cmd)s ) 
        then
           touch %(rsync_ended)s
        else
            touch %(rsync_fail)s
        fi
        
        rsync -av %(pipedir)s/ %(archive_pipedir)s/
        
        rm %(rsync_lock)s
        '''
        
        rsync_cmd = ""
        # set of institutes
        ftpdirs = set()
        for sample_id in list(self.external_data.viewkeys()):
            for ftpdir in self.external_data[sample_id]['to_ftpdirs']:
                ftpdirs.add(ftpdir)
        for ftpdir in ftpdirs:
            src = os.path.join(env['archive_pipedir'], ftpdir)
            dest = "%s/%s/current/" % (FTP_URL, ftpdir)
            rsync_log = "%s/rsync_%s.log" % (env['archive_pipedir'], ftpdir)
            cmd = "rsync -rpgovD --copy-links %s/ %s > %s 2>&1; " % (src, dest, rsync_log)
            rsync_cmd = rsync_cmd + cmd
        env['rsync_cmd'] = rsync_cmd
        utils.create_script(rsync_script, FTP_RSYNC_COMMAND % env)

    def runFtpRsyncScript(self, rsync_script, env):
        """Run rsync script for external data
        """
        self.log.info('... run ftp rsync pipeline script ..............................................')
        if os.path.exists(rsync_script):
            if not os.path.exists(env['rsync_started']):
                if not os.path.exists(env['rsync_lock']):
                    utils.run_bg_process(['sh', '%s' % rsync_script], self.dry_run)
                else:
                    self.log.info('%s presents - another rsync process is running' % env['rsync_lock'])
            else:
                if not os.path.exists(env['rsync_ended']):
                    self.log.info('external data is currently being synchronised')
                else:
                    self.log.info('external data has been synchronised')
        else:
            self.log.warn('%s is missing' % sync_script)
            
            
class ExternalDemux(External):
    
    def __init__(self, run, external_data, dry_run=True):
        External.__init__(self, run, external_data, dry_run)
        self.pipeline_name = EXTERNAL_DEMUX_PIPELINE

        self.pipelines_completed = self.arePipelinesCompleted(PIPELINES.keys())
        
    def createSymlinks(self, external_directory):
        """
        fastq/SLX-6658.A027.D29VHACXX.s_3.r_1.fq.gz
        fastq/SLX-6658.A027.D29VHACXX.s_3.md5sums.txt
        fastq/SLX-6658.A025.D29VHACXX.s_3.r_1.fq.gz
        fastq/SLX-6658.A025.D29VHACXX.s_3.md5sums.txt
        fastq/...
        fastq/SLX-6658.D29VHACXX.s_3.r_1.barcodesummary.txt
        """
        self.log.info('... create symlinks to  demux external data ....................................')
        for sample_id in list(self.external_data.viewkeys()):
            for ftpdir in self.external_data[sample_id]['to_ftpdirs']:
                # create ftpdir in external directory in run folder
                runfolder_ext_ftpdir = os.path.join(external_directory, ftpdir)
                utils.create_directory(runfolder_ext_ftpdir)
                filename = self.external_data[sample_id]['from_contenturi']
                try:
                    # create symlink
                    linkname = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename))
                    utils.create_symlink(filename, linkname)
                except:
                    self.log.exception('unexpected error when creating symlink')
                    continue
    
            
################################################################################
# CLASS Sync
################################################################################
class Sync(object):

    def __init__(self, run, dry_run=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.pipeline_name = 'rsync'
        self.dry_run = dry_run

    def execute(self):
        """execute rsync_runfolder by creating a shell script and running it
        """
        if self.run.isCompleted():
            # create pipeline definition
            pipeline_definition = PipelineDefinition(run=self.run, pipeline_name=self.pipeline_name)
            pipeline_definition.printHeader()
            # create rsync-pipeline script
            pipeline_definition.createRsyncRunFolderScript()
            # run rsync-pipeline script
            pipeline_definition.runRsyncRunFolderScript(self.dry_run)

################################################################################
# Unit tests
################################################################################

class PipelineDefinitionTests(unittest.TestCase):
	
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        self.run = self.runs.completed_runs[0]
        self.log.debug('Testing logging')
        self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name='test') 
        self.pipeline_definition_cluster = PipelineDefinition(run=self.run, pipeline_name='test', cluster_host='uk-cri-test')
        self.pipeline_definition.printHeader()
        
    def tearDown(self):
        import shutil
        shutil.rmtree(self.pipeline_definition.pipeline_directory)
        for run in self.runs.completed_runs:
            shutil.rmtree(run.dest_run_folder)
        
    def testCreateSetupScript(self):
        self.assertEqual('test', self.pipeline_definition.pipeline_name)
        self.pipeline_definition.createSetupPipelineScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.pipeline_directory))
        self.assertTrue(os.path.exists(self.pipeline_definition.setup_script_path))

    def testCreateRunScript(self):
        self.pipeline_definition.createRunPipelineScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.run_script_path))

    def testCreateRunScriptCluster(self):
        self.pipeline_definition_cluster.createRunPipelineScript()
        self.assertTrue(os.path.exists(self.pipeline_definition_cluster.run_script_path))
        
    def testCreateRsyncScript(self):
        self.pipeline_definition.createRsyncPipelineScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))
        
    def testRunRsyncScript(self):
        import time
        utils.touch(self.pipeline_definition.pipeline_started)
        utils.touch(self.pipeline_definition.pipeline_ended)
        self.pipeline_definition.createRsyncPipelineScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))
        self.pipeline_definition.runRsyncPipelineScript(True, False)
        time.sleep(5) # wait for rsync to synchronise files
        self.assertTrue(os.path.exists(self.pipeline_definition.archive_pipeline_directory))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, PIPELINE_STARTED_FILENAME)))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, PIPELINE_ENDED_FILENAME)))
        
class SyncPipelineDefinitionTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/seqdir/vol0[1-2]/data/Runs/')
        self.destdir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.destdir)
        self.run = self.runs.completed_runs[0]
        self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name='rsync')
        self.pipeline_definition.printHeader()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.pipeline_definition.pipeline_directory)
        for run in self.runs.completed_runs:
            shutil.rmtree(self.run.dest_run_folder)

    def testCreateRsyncScript(self):
        self.pipeline_definition.createRsyncRunFolderScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))

    def testRunRsyncScript(self):
        import time
        self.pipeline_definition.createRsyncRunFolderScript()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))
        self.pipeline_definition.runRsyncRunFolderScript(False)
        time.sleep(5) # wait for rsync to synchronise files
        self.assertTrue(os.path.exists(self.pipeline_definition.archive_pipeline_directory))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, RSYNC_STARTED_FILENAME)))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, RSYNC_ENDED_FILENAME)))
        self.assertTrue(os.path.isfile(os.path.join(self.run.dest_run_folder, runfolders.SEQUENCING_COMPLETED)))

class AutonalaysisPipelinesTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        
    def tearDown(self):
        import shutil
        for run in self.runs.completed_runs:
            shutil.rmtree(run.dest_run_folder)
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                if os.path.exists(pipeline_folder):
                    shutil.rmtree(pipeline_folder)
            filelist = []
            if not run.run_folder_name == '130409_HWI-ST230_1109_C1AENACXX':
                filelist.extend(glob.glob("%s/Analysis*.completed" % run.run_folder))
            for f in filelist:
                os.remove(f)

    def testExecute(self):
        for run in self.runs.completed_runs:
            pipelines = Pipelines(run=run)
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                self.assertTrue(os.path.exists(pipeline_folder))
                self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                
    def testRegisterCompletion(self):
        for run in self.runs.completed_runs:
            pipelines = Pipelines(run=run)
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                utils.touch(os.path.join(pipeline_folder, PIPELINE_STARTED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, PIPELINE_ENDED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, RSYNC_STARTED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, RSYNC_ENDED_FILENAME))
                archive_pipeline_folder = os.path.join(utils.locate_run_folder(os.path.basename(run.run_folder), self.archivedir), pipeline_name)
                utils.create_directory(archive_pipeline_folder)
                utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_STARTED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_ENDED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, RSYNC_STARTED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, RSYNC_ENDED_FILENAME))
            pipelines.registerCompletion()
            self.assertTrue(os.path.isfile(pipelines.primary_completed))
            self.assertTrue(os.path.isfile(pipelines.all_completed))
            self.assertTrue(os.path.isfile(pipelines.archive_primary_completed))
            self.assertTrue(os.path.isfile(pipelines.archive_all_completed))
            
    def testExecuteOnlyPrimary(self):
        for run in self.runs.completed_runs:
            pipelines = Pipelines(run=run, pipeline_step='primary')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in PIPELINES.keys():
                if pipeline_name == 'primary':
                    pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                    self.assertTrue(os.path.exists(pipeline_folder))
                    self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                else:
                    pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                    self.assertFalse(os.path.exists(pipeline_folder))
                    self.assertFalse(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                    
class PipelinesOneRunFolderTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir, '130114_HWI-ST230_1016_D18MAACXX')

    def tearDown(self):
        import shutil
        run = self.runs.completed_runs[0]
        shutil.rmtree(run.dest_run_folder)
        for pipeline_name in PIPELINES.keys():
            pipeline_folder = os.path.join(run.run_folder, pipeline_name)
            if os.path.exists(pipeline_folder):
                shutil.rmtree(pipeline_folder)
        filelist = []
        filelist.extend(glob.glob("%s/Analysis*.completed" % run.run_folder))
        for f in filelist:
            os.remove(f)

    def testOneRunFolder(self):
        self.assertEqual(1, len(self.runs.run_folders))
        self.assertEqual(1, len(self.runs.completed_runs))
        self.assertEqual(0, len(self.runs.analysed_runs))

    def testExecute(self):
        run = self.runs.completed_runs[0]
        pipelines = Pipelines(run=run)
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in PIPELINES.keys():
            pipeline_folder = os.path.join(run.run_folder, pipeline_name)
            self.assertTrue(os.path.exists(pipeline_folder))
            self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))

    def testRegisterCompletion(self):
        run = self.runs.completed_runs[0]
        pipelines = Pipelines(run=run)
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in PIPELINES.keys():
            pipeline_folder = os.path.join(run.run_folder, pipeline_name)
            utils.touch(os.path.join(pipeline_folder, PIPELINE_STARTED_FILENAME))
            utils.touch(os.path.join(pipeline_folder, PIPELINE_ENDED_FILENAME))
            utils.touch(os.path.join(pipeline_folder, RSYNC_STARTED_FILENAME))
            utils.touch(os.path.join(pipeline_folder, RSYNC_ENDED_FILENAME))
            archive_pipeline_folder = os.path.join(utils.locate_run_folder(os.path.basename(run.run_folder), self.archivedir), pipeline_name)
            utils.create_directory(archive_pipeline_folder)
            utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_STARTED_FILENAME))
            utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_ENDED_FILENAME))
            utils.touch(os.path.join(archive_pipeline_folder, RSYNC_STARTED_FILENAME))
            utils.touch(os.path.join(archive_pipeline_folder, RSYNC_ENDED_FILENAME))
        pipelines.registerCompletion()
        self.assertTrue(os.path.isfile(pipelines.primary_completed))
        self.assertTrue(os.path.isfile(pipelines.all_completed))
        self.assertTrue(os.path.isfile(pipelines.archive_primary_completed))
        self.assertTrue(os.path.isfile(pipelines.archive_all_completed))

    def testExecuteOnlyPrimary(self):
        for run in self.runs.completed_runs:
            pipelines = Pipelines(run=run, pipeline_step='primary')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in PIPELINES.keys():
                if pipeline_name == 'primary':
                    pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                    self.assertTrue(os.path.exists(pipeline_folder))
                    self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                else:
                    pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                    self.assertFalse(os.path.exists(pipeline_folder))
                    self.assertFalse(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                    
class SyncTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/seqdir/vol0[1-2]/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        
    def tearDown(self):
        import shutil
        for run in self.runs.completed_runs:
            pipeline_folder = os.path.join(run.run_folder, 'rsync')
            shutil.rmtree(pipeline_folder)
            shutil.rmtree(run.dest_run_folder)

    def testExecute(self):
        import time
        for run in self.runs.completed_runs:
            sync = Sync(run=run, dry_run=False)
            self.assertEqual(run.run_folder_name, sync.run.run_folder_name)
            sync.execute()
            time.sleep(5) # wait for rsync to synchronise files
            pipeline_folder = os.path.join(run.run_folder, sync.pipeline_name)
            dest_pipeline_folder = os.path.join(run.dest_run_folder, sync.pipeline_name)
            self.assertTrue(os.path.exists(pipeline_folder))
            self.assertTrue(os.path.exists(os.path.join(pipeline_folder, RSYNC_SCRIPT_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, RSYNC_STARTED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, RSYNC_ENDED_FILENAME)))
            self.assertTrue(os.path.exists(dest_pipeline_folder))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, RSYNC_STARTED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, RSYNC_ENDED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(run.dest_run_folder, runfolders.SEQUENCING_COMPLETED)))
                                                    
if __name__ == '__main__':
	unittest.main()