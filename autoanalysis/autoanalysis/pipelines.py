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
log = logging.getLogger('auto.pipelines')

# autoanalysis modules
import runfolders
import utils

################################################################################
# CONSTANTS
################################################################################
# Pipeline definitions and dependencies
PIPELINES = {
    "primary": [],
    "mga": ["primary"],
    "demultiplex": ["primary"],
    "fastqc": ["primary"],
    "secondary": ["primary","demultiplex"]}

# Pipeline setup command
PIPELINE_SETUP_COMMAND = "%(bin)s --basedir=%(basedir)s --queue=solexa --notifications %(options)s %(run_uid)s %(output)s"

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

PRIMARY_COMPLETED_FILENAME = "Analysis.primary.completed"
PROCESS_COMPLETED_FILENAME = "Analysis.all.completed"
ANALYSIS_IGNORE_FILENAME = "analysis.ignore"

# rsync exclude list
RSYNC_EXCLUDE = { 
    "primary" : "--exclude=Data/Intensities/*_pos.txt --exclude=Data/Intensities/L00? --exclude=Data/Intensities/BaseCalls --exclude=fastqc --exclude=mga --exclude=demultiplex --exclude=secondary",
    "mga" : "",
    "demultiplex" : "",
    "fastqc" : "",
    "secondary" : "",                   
}

RSYNC_ALL_EXCLUDE = "--exclude=temp --exclude=JobOutputs"


################################################################################
# CLASS PipelineDefinition
################################################################################        
class PipelineDefinition(object):

    def __init__(self, _run_definition, _pipeline_name):
        self.run_definition = _run_definition
        self.pipeline_name = _pipeline_name
        self.pipeline_directory = os.path.join(self.run_definition.run_folder, self.pipeline_name)
        self.dest_pipeline_directory = os.path.join(self.run_definition.archive_run_folder, self.pipeline_name)
        self.job_name = "%s_%s_pipeline" % (self.run_definition.flowcell_id, self.pipeline_name)
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

        self.ext_rsync_script_path = os.path.join(self.dest_pipeline_directory, RSYNC_SCRIPT_FILENAME)
        self.ext_rsync_started = os.path.join(self.dest_pipeline_directory, RSYNC_STARTED_FILENAME)
        self.ext_rsync_finished = os.path.join(self.dest_pipeline_directory, RSYNC_FINISHED_FILENAME)
        self.ext_rsync_log = os.path.join(self.dest_pipeline_directory, RSYNC_LOG_FILENAME)

        self.ext_rsync_demux_script_path = os.path.join(self.dest_pipeline_directory, RSYNC_DEMUX_SCRIPT_FILENAME)
        self.ext_rsync_demux_started = os.path.join(self.dest_pipeline_directory, RSYNC_DEMUX_STARTED_FILENAME)
        self.ext_rsync_demux_finished = os.path.join(self.dest_pipeline_directory, RSYNC_DEMUX_FINISHED_FILENAME)

        self.primary_completed = os.path.join(self.run_definition.run_folder, PRIMARY_COMPLETED_FILENAME)
        self.dest_primary_completed = os.path.join(self.run_definition.archive_run_folder, PRIMARY_COMPLETED_FILENAME)
        self.process_completed = os.path.join(self.run_definition.run_folder, PROCESS_COMPLETED_FILENAME)
        self.dest_process_completed = os.path.join(self.run_definition.archive_run_folder, PROCESS_COMPLETED_FILENAME)
        
    def get_header(self):
        return '--- %s' % self.pipeline_name.upper()
        
    def print_log(self):
        log.info(self.get_header())
        
    def create_pipeline_folder(self):
        utils.create_directory(self.pipeline_directory)
        
    def set_setup_command(self):
        pass
        

################################################################################
# CLASS Pipelines
################################################################################
class Pipelines(object):

    def __init__(self, _run_definition, _pipeline_step=None, _software_path=SOFT_PIPELINE_PATH, _cluster_host=None, _dry_run=True):
        self.run_definition = _run_definition
        self.pipeline_step = _pipeline_step       
        self.software_path = _software_path
        self.cluster_host = _cluster_host
        self.dry_run = _dry_run

        self.pipelines = PIPELINES
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
        #log.info('--- PUBLISH EXTERNAL DATA ------------------------------------------------------')
        #self.publish_external_data()
        #log.info('--- UPDATE STATUS --------------------------------------------------------------')
        #self.register_process_completed()

    def setup_pipelines(self):
        """Setup pipelines by creating and running shell script to generate run-meta.xml for each pipeline
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
            pipeline_definition.print_log()

            # create pipeline folder
            pipeline_definition.create_pipeline_folder()

            # create setup-pipeline script 
            command = "%s/%s/bin/%s --basedir=%s --queue=solexa --notifications %s %s %s" % (self.software_path, pipeline_name, CREATE_METAFILE_FILENAME, os.path.dirname(self.run_definition.run_folder), PIPELINES_SETUP_OPTIONS[pipeline_name], self.run_definition.run_uid, pipeline_definition.run_meta)
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
                
    def clean_setup_pipelines(self):
        """Remove setup scripts
        """
        for pipeline_name in list(self.pipelines.viewkeys()):
            # create pipeline definition
            pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name)
            pipeline_definition.print_log()
            if os.path.exists(pipeline_definition.setup_script_path):
                os.remove(pipeline_definition.setup_script_path)
                log.info('%s has been removed' % pipeline_definition.setup_script_path)

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
                        rsync_options = "-av %s %s %s %s > %s 2>&1" % (RSYNC_ALL_EXCLUDE, RSYNC_EXCLUDE[pipeline_name], self.run_definition.run_folder, dest_basedir, pipeline_definition.rsync_log)
                    else:
                        rsync_options = "-av %s %s %s %s > %s 2>&1" % (RSYNC_ALL_EXCLUDE, RSYNC_EXCLUDE[pipeline_name], pipeline_definition.pipeline_directory, self.run_definition.dest_run_folder, pipeline_definition.rsync_log)
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
            if self.run_definition.dest_run_folder:
                # create external directory
                utils.create_directory(pipeline_definition.dest_pipeline_directory)

                # rsync fastq files at the end of primary
                if os.path.exists(pipeline_definition.primary_completed):            
                    # symlink matching files from primary directory
                    for sample_id in list(self.external_samples.viewkeys()):
                        institute_directory = os.path.join(pipeline_definition.dest_pipeline_directory, self.external_samples[sample_id]['institute'])
                        # create institute directory
                        utils.create_directory(institute_directory)
                        file_names = glob.glob("%s/%s.*" % (os.path.join(self.run_definition.dest_run_folder, 'primary'), sample_id))
                        for file_name in file_names:
                            # create symlink
                            link_name = os.path.join(institute_directory, os.path.basename(file_name))                
                            if os.path.lexists(link_name):
                                os.remove(link_name)
                            os.symlink(file_name, link_name)
                            log.debug("%s symlink created" % link_name)
                    # create rsync script
                    self.create_external_rsync_script(pipeline_definition.dest_pipeline_directory, pipeline_definition.ext_rsync_script_path, pipeline_definition.ext_rsync_started, pipeline_definition.ext_rsync_finished, 'rsync', pipeline_definition.rsync_lock)
                    # run rsync
                    self.run_external_rsync_script(pipeline_definition.ext_rsync_script_path, pipeline_definition.ext_rsync_started, pipeline_definition.ext_rsync_finished, pipeline_definition.rsync_lock)
                else:
                    log.info('Primary not completed')

                # rsync demux fastq files at the end of demultiplex
                if self.run_definition.multiplexed_run:
                    if self.process_completed(['demultiplex']):
                        # symlink matching files from demultiplex directory
                        for sample_id in list(self.external_samples.viewkeys()):
                            if self.external_samples[sample_id]['is_multiplexed']:
                                institute_directory = os.path.join(pipeline_definition.dest_pipeline_directory, self.external_samples[sample_id]['institute'])
                                demux_directory = os.path.join(institute_directory, '%s.%s.s_%s.demux' % (sample_id, self.external_samples[sample_id]['run_number'], self.external_samples[sample_id]['lane_number']))
                                # create sample demux directory
                                utils.create_directory(demux_directory)
                                file_names = glob.glob("%s/*%s*" % (os.path.join(self.run_definition.dest_run_folder, 'demultiplex'), sample_id))
                                for file_name in file_names:
                                    # create symlink
                                    link_name = os.path.join(demux_directory, os.path.basename(file_name))                
                                    if os.path.lexists(link_name):
                                        os.remove(link_name)
                                    os.symlink(file_name, link_name)
                                    log.debug("%s symlink created" % link_name)

                        # create rsync_demux script
                        self.create_external_rsync_script(pipeline_definition.dest_pipeline_directory, pipeline_definition.ext_rsync_demux_script_path, pipeline_definition.ext_rsync_demux_started, pipeline_definition.ext_rsync_demux_finished, 'rsync_demux', pipeline_definition.rsync_lock)

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
        if self.process_completed(list(self.pipelines.viewkeys())) and self.external_data_published():
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

    def process_completed(self, list_pipelines, check_rsync=True):
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
            if check_rsync:
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
        external_directory = os.path.join(self.run_definition.dest_run_folder, 'external')
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
# Unit tests
################################################################################

class PipelinesTests(unittest.TestCase):
	
    def setUp(self):
        import log as logger
        log = logger.set_custom_logger()
        log.setLevel(logging.DEBUG)  
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/basedir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        
    def test_nothing(self):
        pass
        
    def test_run_definition(self):
        for run_folder in self.runs.run_folders:
            run_definition = runfolders.RunDefinition(run_folder, self.archivedir)
            pipeline_definition = PipelineDefinition(run_definition, 'test')
            self.assertEqual('test', pipeline_definition.pipeline_name)
            pipeline_definition.create_pipeline_folder()
            self.assertTrue(os.path.exists(pipeline_definition.pipeline_directory))
            # clean-up after testing
            os.rmdir(pipeline_definition.pipeline_directory)
            self.assertFalse(os.path.exists(pipeline_definition.pipeline_directory))

    def test_pipelines_setup(self):
        for run_folder in self.runs.run_folders:
            run_definition = runfolders.RunDefinition(run_folder, self.archivedir)
            pipelines = Pipelines(run_definition)
            self.assertEqual(run_definition.run_folder_name, pipelines.run_definition.run_folder_name)
            pipelines.setup_pipelines()
            for pipeline_name in list(PIPELINES.viewkeys()):
                pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                self.assertTrue(os.path.exists(pipeline_folder))
                self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                


if __name__ == '__main__':
	unittest.main()