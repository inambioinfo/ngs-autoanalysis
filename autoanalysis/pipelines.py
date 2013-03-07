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

# logging definition
log = logging.getLogger('root.pipelines')

# autoanalysis modules
import utils

################################################################################
# CONSTANTS
################################################################################
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

# ftp server
FTP_URL = "solexadmin@uk-cri-ldmz01:/dmz01/solexa"

# Default filenames
SETUP_SCRIPT_FILENAME = "setup-pipeline.sh"
RUN_SCRIPT_FILENAME = "run-pipeline.sh"
RSYNC_SCRIPT_FILENAME = "rsync.sh"
RSYNC_DEMUX_SCRIPT_FILENAME = "rsync_demux.sh"

CREATE_METAFILE_FILENAME = "create-metafile"
RUN_META_FILENAME = "run-meta.xml"
RUN_PIPELINE_FILENAME = "run-pipeline"

PIPELINE_STARTED_FILENAME = "pipeline.started"
PIPELINE_FINISHED_FILENAME = "pipeline.ended"
PIPELINE_FAILED_FILENAME = "pipeline.failed"

RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_FINISHED_FILENAME = "rsync.ended"
RSYNC_LOG_FILENAME = "rsync.log"
RSYNC_LOCK_FILENAME = "rsync.lock"
RSYNC_DEMUX_STARTED_FILENAME = "rsync_demux.started"
RSYNC_DEMUX_FINISHED_FILENAME = "rsync_demux.ended"

DEMUX_STATS_LOCK_FILENAME = "demux-stats.lock"
DEMUX_STATS_COPY_SCRIPT_FILENAME = 'copy.sh'
DEMUX_STATS_COPY_STARTED_FILENAME = 'copy.started'
DEMUX_STATS_COPY_FINISHED_FILENAME = 'copy.ended'
DEMUX_STATS_CLEAN_SCRIPT_FILENAME = 'clean.sh'
DEMUX_STATS_CLEAN_STARTED_FILENAME = 'clean.started'
DEMUX_STATS_CLEAN_FINISHED_FILENAME = 'clean.ended'

SEQUENCING_COMPLETED_FILENAME = "Run.completed"
PRIMARY_COMPLETED_FILENAME = "Run.primary.completed"
PROCESS_COMPLETED_FILENAME = "Run.all.completed"
ANALYSIS_IGNORE_FILENAME = "analysis.ignore"

# Default lims status
PRIMARY_ANALYSIS_COMPLETE_STATUS = 'PRIMARY COMPLETE'
ANALYSIS_COMPLETE_STATUS = 'COMPLETE'

# rsync exclude list
RSYNC_EXCLUDE = { 
    "primary" : "--exclude=Data/Intensities/*_pos.txt --exclude=Data/Intensities/L00? --exclude=Data/Intensities/BaseCalls --exclude=*/temp/* --exclude=fastqc --exclude=mga --exclude=demultiplex --exclude=secondary",
    "mga" : "",
    "demultiplex" : "",
    "fastqc" : "",
    "secondary" : "",                   
}

################################################################################
# CLASS SystemDefinition
################################################################################
class SystemDefinition(object):
    
    def __init__(self, _base_dir, _archive_dir):
        self.base_dir = _base_dir
        self.archive_dir = _archive_dir

################################################################################
# CLASS RunDefinition
################################################################################
class RunDefinition(object):
    
    def __init__(self, _base_dir, _archive_dir, _run):
        self.system = SystemDefinition(_base_dir, _archive_dir)
        self.run = _run
        self.run_folder = os.path.join(self.system.base_dir, self.run.pipelinePath)
        self.dest_run_folder = utils.locate_run_folder(os.path.basename(self.run_folder), self.system.archive_dir)
        if self.run.multiplexed == 1:
            self.multiplexed_run = True
        else:
            self.multiplexed_run = False
        self.run_number = self.run.runNumber
        self.analysis_ignore = os.path.join(self.run_folder, ANALYSIS_IGNORE_FILENAME)
        self.sequencing_completed = os.path.join(self.run_folder, SEQUENCING_COMPLETED_FILENAME)
        log.info('================================================================================')
        log.info('=== RUN: %s' % self.run_folder)
        log.info('================================================================================')
        
    def ready_to_process(self):
        if os.path.exists(self.run_folder):
            # check sequencing process has finished - do not just rely on lims status
            # and check analysis.ignore is not present - stop running analysis if present
            if os.path.exists(self.sequencing_completed) and not os.path.exists(self.analysis_ignore):
                return True
            else:
                if not os.path.exists(sequencing_completed):
                    log.warn('%s does not exists' % sequencing_completed)
                    return False
                if os.path.exists(analysis_ignore):
                    log.info('%s is present' % analysis_ignore)
                    return False
        return False
        
    def ready_to_analyse(self):
        if os.path.exists(self.run_folder):
            # check analysis.ignore is not present - stop running analysis if present
            if not os.path.exists(self.analysis_ignore):
                return True
            else:
                log.info('%s is present' % self.analysis_ignore)
                return False
        return False
            
################################################################################
# CLASS PipelineDefinition
################################################################################        
class PipelineDefinition(object):
    
    def __init__(self, _run_definition, _pipeline_name):
        self.run_definition = _run_definition
        self.pipeline_name = _pipeline_name
        self.pipeline_directory = os.path.join(self.run_definition.run_folder, self.pipeline_name)
        self.job_name = "%s_%s_pipeline" % (self.run_definition.run_number, self.pipeline_name)
        self.rsync_lock = os.path.join(os.path.dirname(self.run_definition.run_folder), RSYNC_LOCK_FILENAME)

        self.setup_script_path = os.path.join(self.pipeline_directory, SETUP_SCRIPT_FILENAME)
        self.run_meta = os.path.join(self.pipeline_directory, RUN_META_FILENAME)

        self.run_script_path = os.path.join(self.pipeline_directory, RUN_SCRIPT_FILENAME)
        self.pipeline_started = os.path.join(self.pipeline_directory, PIPELINE_STARTED_FILENAME)
        self.pipeline_finished = os.path.join(self.pipeline_directory, PIPELINE_FINISHED_FILENAME)

        self.rsync_script_path = os.path.join(self.pipeline_directory, RSYNC_SCRIPT_FILENAME)
        self.rsync_started = os.path.join(self.pipeline_directory, RSYNC_STARTED_FILENAME)
        self.rsync_finished = os.path.join(self.pipeline_directory, RSYNC_FINISHED_FILENAME)
        self.rsync_log = os.path.join(self.pipeline_directory, RSYNC_LOG_FILENAME)

        self.ext_rsync_demux_script_path = os.path.join(self.pipeline_directory, RSYNC_DEMUX_SCRIPT_FILENAME)
        self.ext_rsync_demux_started = os.path.join(self.pipeline_directory, RSYNC_DEMUX_STARTED_FILENAME)
        self.ext_rsync_demux_finished = os.path.join(self.pipeline_directory, RSYNC_DEMUX_FINISHED_FILENAME)

        self.primary_completed = os.path.join(self.run_definition.run_folder, PRIMARY_COMPLETED_FILENAME)
        self.dest_primary_completed = os.path.join(self.run_definition.dest_run_folder, PRIMARY_COMPLETED_FILENAME)
        self.process_completed = os.path.join(self.run_definition.run_folder, PROCESS_COMPLETED_FILENAME)
        self.dest_process_completed = os.path.join(self.run_definition.dest_run_folder, PROCESS_COMPLETED_FILENAME)

    def print_log(self):
        log.info('--- %s' % self.pipeline_name.upper())

################################################################################
# CLASS Pipelines
################################################################################
class Pipelines(object):
    
    def __init__(self, _run_definition, _external_samples, _pipeline_step, _update_status, _soap_client, _software_path=SOFT_PIPELINE_PATH, _cluster_host=None, _dry_run=True):
        self.run_definition = _run_definition
        self.external_samples = _external_samples
        self.pipeline_step = _pipeline_step       
        self.update_status = _update_status
        self.software_path = _software_path
        self.soap_client = _soap_client
        self.soap_url = self.soap_client.soap_url
        self.cluster_host = _cluster_host
        self.dry_run = _dry_run
        
        # get list of pipeline names for processing and completion
        if self.run_definition.multiplexed_run:
            self.pipelines = MULTIPLEX_PIPELINES
            self.pipelines_for_completion = MULTIPLEX_PIPELINES
        else:
            self.pipelines = PIPELINES
            self.pipelines_for_completion = PIPELINES
        if self.pipeline_step:
            self.pipelines = {self.pipeline_step : ""}
                
    def execute(self):
        log.info('--- SETUP PIPELINES ------------------------------------------------------------')
        self.setup_pipelines()
        log.info('--- SETUP RSYNC ----------------------------------------------------------------')
        self.setup_rsync_pipelines()
        log.info('--- RUN PIPELINES --------------------------------------------------------------')
        self.run_pipelines()
        log.info('--- RUN RSYNC ------------------------------------------------------------------')
        self.rsync_pipelines()
        log.info('--- PUBLISH EXTERNAL DATA ------------------------------------------------------')
        self.publish_external_data()
        log.info('--- UPDATE STATUS --------------------------------------------------------------')
        self.register_process_completed()
                
    def setup_pipelines(self):
        """Setup pipelines by creating and running shell script to generate run-meta.xml for each pipeline
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
            pipeline_definition.print_log()

            # create pipeline folder
            utils.create_directory(pipeline_definition.pipeline_directory)

            # create setup-pipeline script 
            command = "%s/%s/bin/%s --basedir=%s --queue=solexa --url=%s --notifications %s %s %s" % (self.software_path, pipeline_name, CREATE_METAFILE_FILENAME, os.path.dirname(self.run_definition.run_folder), self.soap_url, PIPELINES_SETUP_OPTIONS[pipeline_name], self.run_definition.run_number, pipeline_definition.run_meta)
            utils.create_script(pipeline_definition.setup_script_path, command)

            # run setup-pipeline script to create meta data 
            if not os.path.exists(pipeline_definition.run_meta):
                if self.dependencies_satisfied(pipeline_name):
                    utils.run_process(['sh', '%s' % pipeline_definition.setup_script_path], self.dry_run)
                else:
                    log.info('%s pipeline dependencies not satisfied' % pipeline_name)
            else:
                # TODO: check output file for errors
                log.debug('%s already exists' % pipeline_definition.run_meta)
                
    def _create_run_pipeline_script(self, pipeline_definition):
        # create run-pipeline script
        if self.cluster_host:
            bsub_cmd = "%s/%s/bin/%s --mode=lsf --clean %s" % (self.software_path, pipeline_definition.pipeline_name, RUN_PIPELINE_FILENAME, RUN_META_FILENAME)
            command = utils.LSF_CMD_TEMPLATE % {'mem_value': '2048', 'cluster':self.cluster_host, 'work_dir':pipeline_definition.pipeline_directory, 'job_name':pipeline_definition.job_name, 'cmd':bsub_cmd}
            utils.create_script(pipeline_definition.run_script_path, command)
        else:
            command = "cd %s; touch %s; %s/%s/bin/%s --mode=local --clean %s" % (pipeline_definition.pipeline_directory, PIPELINE_STARTED_FILENAME, self.software_path, pipeline_definition.pipeline_name, RUN_PIPELINE_FILENAME, RUN_META_FILENAME)
            utils.create_script(pipeline_definition.run_script_path, command)
                
    def run_pipelines(self):
        """Run pipelines by creating and running a shell script to run run-pipeline for each pipeline
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
            pipeline_definition.print_log()

            # create run-pipeline script
            self._create_run_pipeline_script(pipeline_definition)
            
            # run run-pipeline script to run the pipeline
            if os.path.exists(pipeline_definition.run_meta):
                # pipeline not started
                if not os.path.exists(pipeline_definition.pipeline_started):
                    # no pipeline.finished file, then run-pipeline
                    if not os.path.exists(pipeline_definition.pipeline_finished):
                        if self.dependencies_satisfied(pipeline_name):
                            utils.run_process(['sh', '%s' % pipeline_definition.run_script_path], self.dry_run)
                        else:
                            log.info('%s pipeline dependencies not satisfied' % pipeline_name)
                    else:
                        log.warn("%s presents with no %s" % (pipeline_definition.pipeline_finished, PIPELINE_STARTED_FILENAME))
                # pipeline started
                else:
                    # pipeline not finished
                    if not os.path.exists(pipeline_definition.pipeline_finished):
                        job_output = glob.glob(os.path.join(pipeline_definition.pipeline_directory, '%s_*.out' % pipeline_definition.job_name))
                        # output file presents - check for errors
                        if job_output:
                            if utils.output_job_success(job_output):
                                log.info("%s pipeline finished successfully. %s do not exist yet." % (pipeline_name, pipeline_definition.pipeline_finished))
                            else:
                                log.warn("[***FAIL***] %s pipeline in %s has failed." % (pipeline_name, self.run_definition.run_folder))
                                log.warn("please investigate %s." % job_output)
                        else:
                            log.info("%s pipeline in %s has not finished." % (pipeline_name, self.run_definition.run_folder))
                    # pipeline finished
                    else:
                        log.info("%s pipeline finished successfully." % pipeline_name)
            else:
                log.warn("%s is missing" % pipeline_definition.run_meta)

    def setup_rsync_pipelines(self): 
        """ Create an rsync script for each pipeline to synchronise data from lustre
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
                   
            if self.run_definition.dest_run_folder:
                dest_basedir = os.path.dirname(self.run_definition.dest_run_folder)
                dest_pipeline_directory = os.path.join(self.run_definition.dest_run_folder, pipeline_name)

                # create rsync-pipeline script 
                if os.path.exists(pipeline_definition.pipeline_directory):
                    if pipeline_name is 'primary':
                        rsync_options = "-av %s %s %s > %s 2>&1" % (RSYNC_EXCLUDE[pipeline_name], self.run_definition.run_folder, dest_basedir, pipeline_definition.rsync_log)
                    else:
                        rsync_options = "-av %s %s %s > %s 2>&1" % (RSYNC_EXCLUDE[pipeline_name], pipeline_definition.pipeline_directory, self.run_definition.dest_run_folder, pipeline_definition.rsync_log)
                    copy_finished = "%s %s/." % (pipeline_definition.rsync_finished, dest_pipeline_directory)
                    command = "touch %s; touch %s; rsync %s; touch %s; cp %s; rm %s" % (pipeline_definition.rsync_started, pipeline_definition.rsync_lock, rsync_options, pipeline_definition.rsync_finished, copy_finished, pipeline_definition.rsync_lock)
                    utils.create_script(pipeline_definition.rsync_script_path, command)
                else:
                    log.warn('%s is missing' % pipeline_definition.pipeline_directory)
    
    def rsync_pipelines(self):
        """Run rsync script to synchronise data from lustre to lbio03
        Synchronise primary directory first, and then all the other pipeline folders
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
            pipeline_definition.print_log()
           
            # rsync primary first
            if os.path.exists(pipeline_definition.rsync_script_path):            
                if os.path.exists(pipeline_definition.pipeline_started) and os.path.exists(pipeline_definition.pipeline_finished):
                    if not os.path.exists(pipeline_definition.rsync_started):
                        if not os.path.exists(pipeline_definition.rsync_lock):
                            if not pipeline_name is 'primary':
                                if self.process_completed(['primary']):
                                    utils.touch(pipeline_definition.rsync_lock)
                                    utils.run_bg_process(['sh', '%s' % pipeline_definition.rsync_script_path], self.dry_run)
                                else:
                                    log.debug("nothing to rsync yet - primary pipeline not complete")
                            else:
                                utils.touch(pipeline_definition.rsync_lock)
                                utils.run_bg_process(['sh', '%s' % pipeline_definition.rsync_script_path], self.dry_run)
                        else:
                            log.info('%s presents - another rsync process is running' % pipeline_definition.rsync_lock)
                    else:
                        if not os.path.exists(pipeline_definition.rsync_finished):
                            log.info('%s pipeline is currently being synchronised' % pipeline_name)
                        else:
                            log.info('%s pipeline has been synchronised' % pipeline_name)
                else:
                    log.debug("nothing to rsync yet - %s and/or %s missing" % (PIPELINE_STARTED_FILENAME, PIPELINE_FINISHED_FILENAME))
            else:
                log.warn('%s is missing' % pipeline_definition.rsync_script_path)
                
    def publish_external_data(self):
        """publish external data - rsync to ldmz01
        Create external directory with symlink to fastq files on sol03 - not lustre -
        Synchronise external data to solexadmin@uk-cri-ldmz01:/dmz01/solexa/${institute}/current/
        """
        # create pipeline definition
        pipeline_definition = PipelineDefinition(self.run_definition, 'external')
        
        if self.external_samples:
            if self.run_definition.run_folder:
                # create external directory
                utils.create_directory(pipeline_definition.pipeline_directory)

                # rsync fastq files at the end of primary
                if os.path.exists(pipeline_definition.primary_completed):            
                    # symlink matching files from primary directory
                    for sample_id in list(self.external_samples.viewkeys()):
                        institute_directory = os.path.join(pipeline_definition.pipeline_directory, self.external_samples[sample_id]['institute'])
                        # create institute directory
                        utils.create_directory(institute_directory)
                        file_names = glob.glob("%s/%s.*" % (os.path.join(self.run_definition.run_folder, 'primary'), sample_id))
                        for file_name in file_names:
                            # create symlink
                            link_name = os.path.join(institute_directory, os.path.basename(file_name))                
                            if os.path.lexists(link_name):
                                os.remove(link_name)
                            os.symlink(file_name, link_name)
                            log.debug("%s symlink created" % link_name)
                    # create rsync script
                    self.create_external_rsync_script(pipeline_definition.pipeline_directory, pipeline_definition.rsync_script_path, pipeline_definition.rsync_started, pipeline_definition.rsync_finished, 'rsync', pipeline_definition.rsync_lock)
                    # run rsync
                    self.run_external_rsync_script(pipeline_definition.rsync_script_path, pipeline_definition.rsync_started, pipeline_definition.rsync_finished, pipeline_definition.rsync_lock)
                else:
                    log.info('Primary not completed')

                # rsync demux fastq files at the end of demultiplex
                if self.run_definition.multiplexed_run:
                    if self.process_completed(['demultiplex']):
                        # symlink matching files from demultiplex directory
                        for sample_id in list(self.external_samples.viewkeys()):
                            if self.external_samples[sample_id]['is_multiplexed']:
                                institute_directory = os.path.join(pipeline_definition.pipeline_directory, self.external_samples[sample_id]['institute'])
                                demux_directory = os.path.join(institute_directory, '%s.%s.s_%s.demux' % (sample_id, self.external_samples[sample_id]['run_number'], self.external_samples[sample_id]['lane_number']))
                                # create sample demux directory
                                utils.create_directory(demux_directory)
                                file_names = glob.glob("%s/*%s*" % (os.path.join(self.run_definition.run_folder, 'demultiplex'), sample_id))
                                for file_name in file_names:
                                    # create symlink
                                    link_name = os.path.join(demux_directory, os.path.basename(file_name))                
                                    if os.path.lexists(link_name):
                                        os.remove(link_name)
                                    os.symlink(file_name, link_name)
                                    log.debug("%s symlink created" % link_name)

                        # create rsync_demux script
                        self.create_external_rsync_script(pipeline_definition.pipeline_directory, pipeline_definition.ext_rsync_demux_script_path, pipeline_definition.ext_rsync_demux_started, pipeline_definition.ext_rsync_demux_finished, 'rsync_demux', pipeline_definition.rsync_lock)

                        # run rsync_demux
                        self.run_external_rsync_script(pipeline_definition.ext_rsync_demux_script_path, pipeline_definition.ext_rsync_demux_started, pipeline_definition.ext_rsync_demux_finished, pipeline_definition.rsync_lock)
                    else:
                        log.info('Demultiplex not completed')
                else:
                    log.info('Not a demultiplexed run')

            else:
                log.warn('%s does not exist' % run_folder)
        else:
            log.info('No external samples to publish')

    def register_process_completed(self):
        """Update lims status if --update-status is on
        Update lims analysis status to PRIMARY COMPLETE when just primary completed and rsynced
        Update lims analysis status to COMPLETE when all processes completed and rsynced, even external data publication
        """
        # create pipeline definition
        pipeline_definition = PipelineDefinition(self.run_definition, 'complete')

        # touch Run.primary.complete when process completed
        if self.process_completed(['primary']):
            if not os.path.exists(pipeline_definition.primary_completed):
                utils.touch (pipeline_definition.primary_completed)
            if not os.path.exists(pipeline_definition.dest_primary_completed):
                utils.touch (pipeline_definition.dest_primary_completed)
            log.info('*** PRIMARY COMPLETED **********************************************************')
        else:
            # remove Run.primary.complete when primary not complete and file exists
            if os.path.exists(pipeline_definition.primary_completed):
                os.remove(pipeline_definition.primary_completed)
            if os.path.exists(pipeline_definition.dest_primary_completed):
                os.remove(pipeline_definition.dest_primary_completed)

        # update lims analysis status when all processes completed and rsynced
        if self.process_completed(list(self.pipelines_for_completion.viewkeys())) and self.external_data_published():
            if not os.path.exists(pipeline_definition.process_completed):
                utils.touch(pipeline_definition.process_completed)
            if not os.path.exists(pipeline_definition.dest_process_completed):
                utils.touch(pipeline_definition.dest_process_completed)
            log.info('*** PROCESS COMPLETED **********************************************************')
            # update analysis status in lims
            if self.update_status:
                self.soap_client.setAnalysisStatus(self.run_definition.run, ANALYSIS_COMPLETE_STATUS)
            else:
                log.debug('lims not updated - use --update-status option to turn it on')
        else:
            # update lims analysis status when just primary completed and rsynced
            if self.process_completed(['primary']):
                # update analysis status in lims
                if self.update_status:
                    self.soap_client.setAnalysisStatus(self.run_definition.run, PRIMARY_ANALYSIS_COMPLETE_STATUS)
                else:
                    log.debug('lims not updated - use --update-status option to turn it on')
            # remove Run.all.complete when process not completed and file exists
            if os.path.exists(pipeline_definition.process_completed):
                os.remove(pipeline_definition.process_completed)
            if os.path.exists(pipeline_definition.dest_process_completed):
                os.remove(pipeline_definition.dest_process_completed)    
    
    ### Utility methods -------------------------------------------------------
        
    def dependencies_satisfied(self, pipeline_name):
        """For a given pipeline, checks that all dependent pipelines have finished
        Both pipeline.started and pipeline.ended need to be present
        """
        pipeline_dependencies = self.pipelines[pipeline_name]
        log.debug('%s pipeline dependencies: [%s]' % (pipeline_name, ",".join(pipeline_dependencies)))
        for dep_pipeline_name in pipeline_dependencies:
            pipeline_directory = os.path.join(self.run_definition.run_folder, dep_pipeline_name)
            pipeline_started = os.path.join(pipeline_directory, PIPELINE_STARTED_FILENAME)
            pipeline_finished = os.path.join(pipeline_directory, PIPELINE_FINISHED_FILENAME)
            # pipeline not finished or started
            if not os.path.exists(pipeline_finished) or not os.path.exists(pipeline_started):
                return False
        return True
    
    def process_completed(self, list_pipelines):
        """Checks for all pipeline in the list that each of them has finished and has
        been synchronised.
        pipeline.started and pipeline.ended need to be present as well as 
        rsync.started and rsync.ended need to be present
        """
        for pipeline_name in list_pipelines:
            pipeline_directory = os.path.join(self.run_definition.run_folder, pipeline_name)
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
        
    ### External rsync utility methods ----------------------------------------

    def create_external_rsync_script(self, external_directory, rsync_script_path, rsync_started, rsync_finished, log_prefix, rsync_lock):
        """Create rsync script for external data
        """
        rsync = ""
        # set of institutes
        institutes = set()
        for sample_id in list(self.external_samples.viewkeys()):
            institutes.add(self.external_samples[sample_id]['institute'])
        for institute in institutes:
            src = os.path.join(external_directory, institute)
            dest = "%s/%s/current/" % (FTP_URL, institute)
            rsync_log = "%s/%s_%s.log" % (external_directory, log_prefix, institute)
            rsync = rsync + "rsync -av --copy-links %s/ %s > %s 2>&1; " % (src, dest, rsync_log)
        command = "touch %s; touch %s; %s touch %s; rm %s" % (rsync_started, rsync_lock, rsync, rsync_finished, rsync_lock)
        utils.create_script(rsync_script_path, command)
        
    def run_external_rsync_script(self, rsync_script_path, rsync_started, rsync_finished, rsync_lock):
        """Run rsync script for external data
        """
        if os.path.exists(rsync_script_path):
            if not os.path.exists(rsync_started):
                if not os.path.exists(rsync_lock):
                    utils.touch(rsync_lock)
                    utils.run_bg_process(['sh', '%s' % rsync_script_path], self.dry_run)
                else:
                    log.info('%s presents - another rsync process is running' % rsync_lock)
            else:
                if not os.path.exists(rsync_finished):
                    log.info('external data is currently being synchronised')
                else:
                    log.info('external data has been synchronised')
        else:
            log.warn('%s is missing' % rsync_script_path)
   
    def external_data_published(self):
        """Checks that external data has been published
        """
        external_directory = os.path.join(self.run_definition.run_folder, 'external')
        rsync_started = os.path.join(external_directory, RSYNC_STARTED_FILENAME)
        rsync_finished = os.path.join(external_directory, RSYNC_FINISHED_FILENAME)
        rsync_demux_started = os.path.join(external_directory, RSYNC_DEMUX_STARTED_FILENAME)
        rsync_demux_finished = os.path.join(external_directory, RSYNC_DEMUX_FINISHED_FILENAME)
        if self.external_samples:
            # rsync external data not finished or started
            if not os.path.exists(rsync_started) or not os.path.exists(rsync_finished):
                return False
            if self.run_definition.multiplexed_run:
                if not os.path.exists(rsync_demux_started) or not os.path.exists(rsync_demux_finished):
                    return False
        return True

################################################################################
# CLASS DemuxPipelines
################################################################################
class DemuxStatsPipelines(Pipelines):
    
    def __init__(self, _run_definition, _multiplex_templates, _lims_client, _soap_client, _software_path=SOFT_PIPELINE_PATH, _cluster_host=None, _dry_run=True):
        
        Pipelines.__init__(self, _run_definition, None, 'demultiplex', None, _soap_client, _software_path=SOFT_PIPELINE_PATH, _cluster_host=None, _dry_run=True)
        self.lims_client = _lims_client
        # get all fastq files associated to demultiplexed lanes for this run
        self.fastq_files = self.lims_client.findKnownMultiplexSeqFiles(self.run_definition.run)
        self.multiplex_templates = _multiplex_templates
        # create pipeline definition
        self.pipeline_definition = PipelineDefinition(self.run_definition, self.pipeline_step)
        self.pipeline_definition.print_log()
        # specific files for running demux stats analysis
        self.lock = os.path.join(os.path.dirname(self.run_definition.run_folder), DEMUX_STATS_LOCK_FILENAME)
        self.copy_script_path = os.path.join(self.run_definition.run_folder, DEMUX_STATS_COPY_SCRIPT_FILENAME)
        self.copy_started = os.path.join(self.run_definition.run_folder, DEMUX_STATS_COPY_STARTED_FILENAME)
        self.copy_finished = os.path.join(self.run_definition.run_folder, DEMUX_STATS_COPY_FINISHED_FILENAME)
        self.clean_script_path = os.path.join(self.run_definition.run_folder, DEMUX_STATS_CLEAN_SCRIPT_FILENAME)
        self.clean_started = os.path.join(self.run_definition.run_folder, DEMUX_STATS_CLEAN_STARTED_FILENAME)
        self.clean_finished = os.path.join(self.run_definition.run_folder, DEMUX_STATS_CLEAN_FINISHED_FILENAME)        
        
    def execute_demux(self):
        if not self.all_process_completed():
            if self.process_failed():
                log.info('*** [***FAIL***] ***************************************************************')
                utils.touch(self.run_definition.analysis_ignore)
                # remove lock file
                if os.path.exists(self.lock):
                    os.remove(self.lock)
            else:
                log.info('--- MANAGE DATA ----------------------------------------------------------------')
                self.manage_data()
                log.info('--- SETUP DEMUX STATS ----------------------------------------------------------')
                self.setup_demux()
                log.info('--- CREATE INDEXES -------------------------------------------------------------')
                self.create_indexes()
                log.info('--- RUN DEMUX STATS ------------------------------------------------------------')
                self.run_demux()
        else:
            log.info('*** DEMUX-STATS COMPLETED ******************************************************')
        
    def manage_data(self):
        """Create and run scripts to copy and clean fastq file on lustre
        """
        copy = ""
        clean = ""
        for fastq_file in self.fastq_files:
            log.debug("%s\t%s\t%s" % (fastq_file.host, fastq_file.path, fastq_file.filename))
            orig = os.path.join(fastq_file.path, fastq_file.filename)
            dest = os.path.join(self.run_definition.run_folder, fastq_file.filename)
            copy = copy + "scp %s:%s %s; " % (fastq_file.host, orig, dest)
            clean = clean + "rm -f %s; " % dest
        # create/run copy script
        self._create_script(self.copy_script_path, copy, self.copy_started, self.copy_finished, self.lock)
        self._run_script(self.copy_script_path, self.copy_started, self.copy_finished, self.lock)
        # create/run clean script
        self._create_script(self.clean_script_path, clean, self.clean_started, self.clean_finished) 
        if self.process_completed(['demultiplex']):
            self._run_script(self.clean_script_path, self.clean_started, self.clean_finished)  
        # create symlink for fastq files in primary directory
        if self.data_copied():
            # create primary folder
            primary_folder = os.path.join(self.run_definition.run_folder, 'primary')
            utils.create_directory(primary_folder)
            for fastq_file in self.fastq_files:
                new_fastq_filename = self.lims_client.getNewSeqFileName(fastq_file)
                link_name = "%s/%s" % (primary_folder, new_fastq_filename)
                fastq_path = os.path.join(run_folder, fastq_file.filename)
                log.debug(fastq_path)
                if os.path.lexists(link_name):
                    os.remove(link_name)
                os.symlink(fastq_path, link_name)

    def setup_demux(self):
        """Setup demultiplex statistic analysis
        """        
        ### setup demux pipeline
        # set specific demux-stats pipeline options
        PIPELINES_SETUP_OPTIONS['demultiplex'] = '--pipeline=/home/mib-cri/software/pipelines/demultiplex/demuxstatspipeline.xml' # do not generate index-files
        # call setup_pipelines to create setup script and run-meta.xml
        self.setup_pipelines()
        # create run-pipeline script
        self._create_run_pipeline_script(self.pipeline_definition)
        
    def create_indexes(self):
        """Create index files
        """
        for fastq_file in self.fastq_files:
            index_filename = self.lims_client.getIndexFileName(fastq_file)
            index_path = os.path.join(self.pipeline_definition.pipeline_directory, index_filename)
            if not os.path.exists(index_path):
                multiplex_type = self.lims_client.getMultiplexTypeFromSeqFile(fastq_file)
                barcodes = self.multiplex_templates[multiplex_type.name]
                log.debug(multiplex_type.name)
                index_file = open(index_path, 'w')
                for barcode_name in list(barcodes.viewkeys()):
                    index_file.write("%s\t%s.%s.%s.fq.gz\n" % (barcodes[barcode_name], self.lims_client.getSlxSampleId(fastq_file), barcode_name, self.lims_client.findRunLaneRead(fastq_file)))
                index_file.close()
                log.info('%s created' % index_path)
            else:
                log.debug('%s already exists' % index_path)
        
    def run_demux(self):
        """Run demultiplex statistic analysis
        """
        if self.process_completed(['demultiplex']):
            if os.path.exists(self.lock):
                os.remove(self.lock)
        else:
            if not os.path.exists(self.lock) and self.data_copied():
                utils.touch(self.lock)
                # call run_pipelines to run the demultiplex pipeline only one at a time
                self.run_pipelines()
            else:
                log.info('%s presents - another script is running' % self.lock)
                
    def parse_summary_files(self):
        """Parse barcode summary files and return demultiplex report
        Read each BarcodeSummary.SLX-4783.787.s_8.txt file and print report
        """
        report = []
        if self.process_completed(['demultiplex']):
            log.info('--- DEMUX STATS REPORT ---------------------------------------------------------')
            summary_files = glob.glob(os.path.join(self.pipeline_definition.pipeline_directory, 'BarcodeSummary.*.txt'))
            for summary_file in summary_files:
                with open(summary_file, 'r') as summary:
                    barcode_summary = {}
                    barcode_match = {}
                    barcode_found = []
                    distinct_barcodes = False
                    for line in summary:
                        columns = line.strip().split()
                        if len(columns) == 7:
                            barcode_match[columns[0]] = [columns[1], columns[3], columns[5]]
                        elif columns[-1] == 'reads':
                            barcode_summary['total_reads'] = int(columns[0])
                        elif columns[-1] == 'lost':
                            barcode_summary['no_match'] = int(columns[0])
                        elif columns[-1] == 'codes':
                            distinct_barcodes = True
                            barcode_summary['distinct_barcodes'] = int(columns[0])
                        elif distinct_barcodes and len(columns) == 2:
                            barcode_found.append(columns[-1])

                zero_error_reads = 0
                one_error_reads = 0 
                most_frequent = 0
                least_frequent = barcode_summary['total_reads']
                for barcode in list(barcode_match.viewkeys()):
                    total_reads = int(barcode_match[barcode][0])
                    if total_reads > most_frequent:
                        most_frequent = total_reads
                    if not total_reads == 0:
                        if total_reads < least_frequent :
                            least_frequent = total_reads
                    zero_error_reads += int(barcode_match[barcode][1])
                    one_error_reads += int(barcode_match[barcode][2])

                barcode_summary['most_frequent'] = float((most_frequent * 100 ) / barcode_summary['total_reads'])
                barcode_summary['least_frequent'] = float((least_frequent * 100 ) / barcode_summary['total_reads'])
                barcode_summary['zero_error_match'] = float((zero_error_reads * 100 ) / barcode_summary['total_reads'])
                barcode_summary['zero_or_one_error_match'] = float(((zero_error_reads + one_error_reads) * 100 ) / barcode_summary['total_reads'])
                barcode_summary['no_match'] = float((barcode_summary['no_match'] * 100) / barcode_summary['total_reads'])
                if len(barcode_found) > 0:
                    barcode_summary['barcode_found'] = ':'.join(barcode_found)
                else:
                    barcode_summary['barcode_found'] = 'none'
                barcode_summary['summary_file'] = summary_file

                report.append(barcode_summary)
                log.info("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (os.path.basename(summary_file), barcode_summary['zero_error_match'], barcode_summary['zero_or_one_error_match'], barcode_summary['no_match'], barcode_summary['most_frequent'], barcode_summary['least_frequent'], barcode_summary['barcode_found']))
        return report
    
    
    def data_copied(self):
        if not os.path.exists(self.copy_started) or not os.path.exists(self.copy_finished):
            return False
        return True

    def all_process_completed(self):
        if not self.data_copied() or not self.process_completed(['demultiplex']):
            return False
        if not os.path.exists(self.clean_started) or not os.path.exists(self.clean_finished):
            return False
        return True

    def process_failed(self):
        if os.path.exists(self.pipeline_definition.pipeline_started) and not os.path.exists(self.pipeline_definition.pipeline_finished):
            job_output = glob.glob(os.path.join(self.pipeline_definition.pipeline_directory, '*.out'))
            if job_output:
                if not utils.output_job_success(job_output):
                    return True
        return False
        
    def _create_script(self, script_path, cmd, started, ended, lock=None):
        if lock:
            command = "touch %s; touch %s; %s touch %s; rm %s" % (lock, started, cmd, ended, lock)
        else:
            command = "touch %s; %s touch %s" % (started, cmd, ended)
        utils.create_script(script_path, command)

    def _run_script(self, script_path, started, ended, lock=None):
        """Run script
        """
        if os.path.exists(script_path):
            if not os.path.exists(started):
                if lock:
                    if not os.path.exists(lock):
                        utils.touch(lock)
                        utils.run_bg_process(['sh', '%s' % script_path], self.dry_run)
                    else:
                        log.info('%s presents - another script is running' % lock)
                else:
                    utils.run_bg_process(['sh', '%s' % script_path], self.dry_run)
            else:
                if not os.path.exists(ended):
                    log.info('script is currently running')
                else:
                    log.info('script has finished')
        else:
            log.warn('%s is missing' % script_path)
    
################################################################################
# Unit tests
################################################################################

class pipelinesTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()