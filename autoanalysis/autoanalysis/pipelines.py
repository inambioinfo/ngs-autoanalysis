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

# logging definition
log = logging.getLogger('auto.pipelines')

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
    ("demultiplex", ["primary"]),
    ("fastqc", ["primary"]),
    ("secondary", ["primary","demultiplex"])])

# Pipeline commands
PIPELINE_SETUP_COMMAND = "%(bin_meta)s --basedir=%(basedir)s --queue=solexa --notifications %(options)s %(run_uid)s %(run_meta)s"

PIPELINE_RUN_COMMAND = "%(bin_run)s --mode=%(mode)s --clean %(run_meta)s"
PIPELINE_LOCAL_RUN_COMMAND = "cd %(work_dir)s; touch %(started)s; %(bin_run)s --mode=%(mode)s --clean %(run_meta)s"

PIPELINE_RSYNC_COMMAND = '''
touch %(rsync_started)s
touch %(rsync_lock)s

if ( rsync %(rsync_options)s ) 
then
   touch %(rsync_ended)s
   cp %(rsync_ended)s %(archive_pipedir)s/.
fi

rm %(rsync_lock)s
'''

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
RSYNC_SCRIPT_FILENAME = "rsync-pipeline.sh"
RSYNC_DEMUX_SCRIPT_FILENAME = "rsync-demux.sh"

CREATE_METAFILE_FILENAME = "create-metafile"
RUN_META_FILENAME = "run-meta.xml"
RUN_PIPELINE_FILENAME = "run-pipeline"

PIPELINE_STARTED_FILENAME = "pipeline.started"
PIPELINE_ENDED_FILENAME = "pipeline.ended"
PIPELINE_FAILED_FILENAME = "pipeline.failed"

RSYNC_STARTED_FILENAME = "rsync.started"
RSYNC_ENDED_FILENAME = "rsync.ended"
RSYNC_LOG_FILENAME = "rsync.log"
RSYNC_LOCK_FILENAME = "rsync.lock"

PRIMARY_COMPLETED_FILENAME = "Analysis.primary.completed"
ALL_COMPLETED_FILENAME = "Analysis.all.completed"
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

    def __init__(self, _run_definition, _pipeline_name, _software_path=SOFT_PIPELINE_PATH, _cluster_host=None):
        self.run_definition = _run_definition
        self.pipeline_name = _pipeline_name

        # create pipeline directory
        self.pipeline_directory = os.path.join(self.run_definition.run_folder, self.pipeline_name)
        utils.create_directory(self.pipeline_directory)

        # create archive pipeline directory
        self.archive_pipeline_directory = os.path.join(self.run_definition.archive_run_folder, self.pipeline_name)
        utils.create_directory(self.archive_pipeline_directory)
        self.rsync_lock = os.path.join(os.path.dirname(self.run_definition.run_folder), RSYNC_LOCK_FILENAME)
        
        # shell script paths
        self.setup_script_path = os.path.join(self.pipeline_directory, SETUP_SCRIPT_FILENAME)
        self.run_script_path = os.path.join(self.pipeline_directory, RUN_SCRIPT_FILENAME)
        self.rsync_script_path = os.path.join(self.pipeline_directory, RSYNC_SCRIPT_FILENAME)

        self.pipeline_started = os.path.join(self.pipeline_directory, PIPELINE_STARTED_FILENAME)
        self.pipeline_ended = os.path.join(self.pipeline_directory, PIPELINE_ENDED_FILENAME)

        self.rsync_started = os.path.join(self.pipeline_directory, RSYNC_STARTED_FILENAME)
        self.rsync_ended = os.path.join(self.pipeline_directory, RSYNC_ENDED_FILENAME)
        self.rsync_log = os.path.join(self.pipeline_directory, RSYNC_LOG_FILENAME)

        # enviroment variables for setting up and running each pipeline
        self.env = {}
        self.set_env(_software_path, _cluster_host)
        
    def get_header(self):
        return '--- %s' % self.pipeline_name.upper()
        
    def print_header(self):
        log.info(self.get_header())
        
    def set_env(self, _software_path, _cluster_host):
        """set environment variables for generating shell scripts from their templates
        """
        self.env['bin_meta'] = '%s/%s/bin/%s' % (_software_path, self.pipeline_name, CREATE_METAFILE_FILENAME)
        self.env['bin_run'] = '%s/%s/bin/%s' % (_software_path, self.pipeline_name, RUN_PIPELINE_FILENAME)
        self.env['basedir'] = os.path.dirname(self.run_definition.run_folder)
        if self.pipeline_name in PIPELINES_SETUP_OPTIONS.keys():
            self.env['options'] = PIPELINES_SETUP_OPTIONS[self.pipeline_name]
        else:
            self.env['options'] = ''
        self.env['run_uid'] = self.run_definition.run_uid
        self.env['run_meta'] = os.path.join(self.pipeline_directory, RUN_META_FILENAME)
        if _cluster_host:
            self.env['mode'] = 'lsf' 
        else:
            self.env['mode'] = 'local'
        self.env['started'] = PIPELINE_STARTED_FILENAME
        self.env['mem_value'] = '2048'
        self.env['cluster'] = _cluster_host
        self.env['work_dir'] = self.pipeline_directory
        self.env['job_name'] = "%s_%s_pipeline" % (self.run_definition.flowcell_id, self.pipeline_name)
        self.env['cmd'] = PIPELINE_RUN_COMMAND % self.env
        self.env['rsync_started'] = self.rsync_started
        self.env['rsync_lock'] = self.rsync_lock
        self.env['rsync_ended'] = self.rsync_ended
        if self.pipeline_name is 'primary':
            self.env['rsync_options'] = "-av %s %s %s %s > %s 2>&1" % (RSYNC_ALL_EXCLUDE, RSYNC_EXCLUDE[self.pipeline_name], self.run_definition.run_folder, self.run_definition.archive_run_folder, self.rsync_log)
        else:
            if self.pipeline_name in RSYNC_EXCLUDE.keys():
                self.env['rsync_options'] = "-av %s %s %s %s > %s 2>&1" % (RSYNC_ALL_EXCLUDE, RSYNC_EXCLUDE[self.pipeline_name], self.pipeline_directory, self.run_definition.archive_run_folder, self.rsync_log)
            else:
                self.env['rsync_options'] = "-av %s %s %s > %s 2>&1" % (RSYNC_ALL_EXCLUDE, self.pipeline_directory, self.run_definition.archive_run_folder, self.rsync_log)                
        self.env['archive_pipedir'] = self.archive_pipeline_directory
        
    def create_setup_pipeline_script(self):
        log.info('... create setup pipeline script ...............................................')
        try:
            if not os.path.exists(self.setup_script_path):
                utils.create_script(self.setup_script_path, PIPELINE_SETUP_COMMAND % self.env)
            else:
                log.debug('%s already exists' % self.setup_script_path)
        except:
            log.exception('unexpected error when creating setup pipeline script')
            raise
        
    def run_setup_pipeline_script(self, _dependencies_satisfied=True, _dry_run=True):
        log.info('... run setup pipeline script ..................................................')
        try:
            if not os.path.exists(self.env['run_meta']):
                if _dependencies_satisfied:
                    utils.run_process(['sh', '%s' % self.setup_script_path], _dry_run)
                else:
                    log.info('%s pipeline dependencies not satisfied' % self.pipeline_name)
            else:
                log.debug('%s already exists' % self.run_meta)
        except:
            log.exception('unexpected error when running setup pipeline script')
            raise
            
    def create_run_pipeline_script(self):
        log.info('... create run pipeline script .................................................')
        try:
            if self.env['cluster']:
                utils.create_script(self.run_script_path, utils.LSF_CMD_TEMPLATE % self.env)
            else:
                utils.create_script(self.run_script_path, PIPELINE_LOCAL_RUN_COMMAND % self.env)
        except:
            log.exception('unexpected error when creating run pipeline script')
            raise
            
    def run_run_pipeline_script(self, _dependencies_satisfied=True, _dry_run=True):
        log.info('... run run pipeline script ....................................................')
        if os.path.exists(self.env['run_meta']):
            # pipeline not started
            if not os.path.exists(self.pipeline_started):
                # no pipeline.finished file, then run-pipeline
                if not os.path.exists(self.pipeline_ended):
                    if _dependencies_satisfied:
                        utils.run_process(['sh', '%s' % pipeline_definition.run_script_path], _dry_run)
                    else:
                        log.info('%s pipeline dependencies not satisfied' % pipeline_name)
                else:
                    log.warn("%s presents with no %s" % (self.pipeline_ended, PIPELINE_STARTED_FILENAME))
            # pipeline started
            else:
                # pipeline not finished
                if not os.path.exists(self.pipeline_ended):
                    job_output = glob.glob(os.path.join(self.pipeline_directory, '%s_*.out' % self.env['job_name']))
                    # output file presents - check for errors
                    if job_output:
                        if utils.output_job_success(job_output):
                            log.info("%s pipeline finished successfully. %s do not exist yet." % (self.pipeline_name, self.pipeline_ended))
                        else:
                            log.error("[***FAIL***] %s pipeline in %s has failed." % (self.pipeline_name, self.run_definition.run_folder))
                            log.error("please investigate %s." % job_output)
                    else:
                        log.info("%s pipeline in %s has not finished." % (self.pipeline_name, self.run_definition.run_folder))
                # pipeline finished
                else:
                    log.info("%s pipeline finished successfully." % self.pipeline_name)
        else:
            log.warn("%s is missing" % self.env['run_meta'])
            
    def create_rsync_pipeline_script(self):
        log.info('... create rsync pipeline script ...............................................')
        try:
            if not os.path.exists(self.rsync_script_path):
                utils.create_script(self.rsync_script_path, PIPELINE_RSYNC_COMMAND % self.env)
            else:
                log.debug('%s already exists' % self.rsync_script_path)
        except:
            log.exception('unexpected error when creating setup pipeline script')
            raise
            
    def run_rsync_pipeline_script(self, _dependencies_satisfied=True, _dry_run=True):
        """Run rsync script to synchronise data from lustre to lbio03
        Synchronise primary directory first, and then all the other pipeline folders
        """
        log.info('... run rsync pipeline script ..................................................')
        # rsync primary first
        if os.path.exists(self.rsync_script_path):            
            if os.path.exists(self.pipeline_started) and os.path.exists(self.pipeline_ended):
                if not os.path.exists(self.rsync_started):
                    if not os.path.exists(self.rsync_lock):
                        if not self.pipeline_name is 'primary':
                            if _dependencies_satisfied:
                                utils.touch(self.rsync_lock)
                                utils.run_bg_process(['sh', '%s' % self.rsync_script_path], _dry_run)
                            else:
                                log.debug("nothing to rsync yet - primary pipeline not complete")
                        else:
                            utils.touch(self.rsync_lock)
                            utils.run_bg_process(['sh', '%s' % self.rsync_script_path], _dry_run)
                    else:
                        log.info('%s presents - another rsync process is running' % self.rsync_lock)
                else:
                    if not os.path.exists(self.rsync_ended):
                        log.info('%s pipeline is currently being synchronised' % self.pipeline_name)
                    else:
                        log.info('%s pipeline has been synchronised' % self.pipeline_name)
            else:
                log.debug("nothing to rsync yet - %s and/or %s missing" % (PIPELINE_STARTED_FILENAME, PIPELINE_ENDED_FILENAME))
        else:
            log.warn('%s is missing' % self.rsync_script_path)

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
            
        self.primary_completed = os.path.join(self.run_definition.run_folder, PRIMARY_COMPLETED_FILENAME)
        self.archive_primary_completed = os.path.join(self.run_definition.archive_run_folder, PRIMARY_COMPLETED_FILENAME)
        self.all_completed = os.path.join(self.run_definition.run_folder, ALL_COMPLETED_FILENAME)
        self.archive_all_completed = os.path.join(self.run_definition.archive_run_folder, ALL_COMPLETED_FILENAME)
        

    def execute_pipelines(self):
        """execute all pipelines or just one by creating a shell script and running it for
        each of these three steps: setup_pipeline, run_pipeline, and rsync_pipeline
        """
        if self.run_definition.is_ready_for_analysis:
            for pipeline_name in self.pipelines.keys():
                # create pipeline definition
                pipeline_definition = PipelineDefinition(self.run_definition, pipeline_name, self.software_path)
                pipeline_definition.print_header()
                # create setup-pipeline script 
                pipeline_definition.create_setup_pipeline_script()
                # run setup-pipeline script to create meta data 
                pipeline_definition.run_setup_pipeline_script(self.dependencies_satisfied(pipeline_name), self.dry_run)
                # create run-pipeline script
                pipeline_definition.create_run_pipeline_script()
                # run run-pipeline script to run the pipeline
                pipeline_definition.run_run_pipeline_script(self.dependencies_satisfied(pipeline_name), self.dry_run)
                # create rsync-pipeline script
                pipeline_definition.create_rsync_pipeline_script()
                # run rsync-pipeline script
                pipeline_definition.run_rsync_pipeline_script(self.dependencies_satisfied('primary'), self.dry_run)
            
    """ TODO
    - publish_external_data: publish external data to ftp server - rsync to ldmz01
    Create external directory with symlink to fastq files on archivedir (sol03) - not basedir (lustre) -
    Synchronise external data to solexadmin@uk-cri-ldmz01:/dmz01/solexa/${institute}/current/
    --> need list of external samples and to which institute they belong
    """

    def register_completion(self):
        """ Create Analysis.primary.completed and Analysis.all.completed when pipelines
        have been successfully ran and synchronised
        TODO: Update lims status if --update-status is on
        Update lims analysis status to PRIMARY COMPLETE when just primary completed and rsynced
        Update lims analysis status to COMPLETE when all processes completed and rsynced, even external data publication
        TODO: check that external data has been published
        """
        # create Analysis.primary.completed when primary pipeline completed
        if self.pipelines_completed(['primary']):
            if not os.path.exists(self.primary_completed):
                utils.touch (self.primary_completed)
            if not os.path.exists(self.archive_primary_completed):
                utils.touch (self.archive_primary_completed)
            log.info('*** PRIMARY COMPLETED **********************************************************')
        else:
            # remove Analysis.primary.complete when primary not complete and file exists
            if os.path.exists(self.primary_completed):
                os.remove(self.primary_completed)
            if os.path.exists(self.archive_primary_completed):
                os.remove(self.archive_primary_completed)

        # create Analysis.all.completed when all pipelines completed and rsynced
        if self.pipelines_completed(self.pipelines.keys()):
            if not os.path.exists(self.all_completed):
                utils.touch(self.all_completed)
            if not os.path.exists(self.archive_all_completed):
                utils.touch(self.archive_all_completed)
            log.info('*** PROCESS COMPLETED **********************************************************')
        else:
            # remove Analysis.all.completed when analysis not completed and file exists
            if os.path.exists(self.all_completed):
                os.remove(self.all_completed)
            if os.path.exists(self.archive_all_completed):
                os.remove(self.archive_all_completed)    

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
            pipeline_ended = os.path.join(pipeline_directory, PIPELINE_ENDED_FILENAME)
            # pipeline not finished or started
            if not os.path.exists(pipeline_ended) or not os.path.exists(pipeline_started):
                return False
        return True

    def pipelines_completed(self, list_pipelines, check_rsync=True):
        """Checks for a list of pipelines that each of them has finished and has
        been synchronised.
        pipeline.started and pipeline.ended need to be present as well as 
        rsync.started and rsync.ended 
        """
        for pipeline_name in list_pipelines:
            pipeline_directory = os.path.join(self.run_definition.run_folder, pipeline_name)
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

################################################################################
# Unit tests
################################################################################

class PipelineDefinitionTests(unittest.TestCase):
	
    def setUp(self):
        import log as logger
        log = logger.set_custom_logger()
        log.setLevel(logging.DEBUG)  
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/basedir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        self.run_definition = self.runs.findRunsToAnalyse()[0]
        self.pipeline_definition = PipelineDefinition(self.run_definition, 'test')
        self.pipeline_definition_cluster = PipelineDefinition(self.run_definition, 'test', SOFT_PIPELINE_PATH, 'uk-cri-test')
        self.pipeline_definition.print_header()
        
    def tearDown(self):
        import shutil
        shutil.rmtree(self.pipeline_definition.pipeline_directory)
        shutil.rmtree(self.pipeline_definition.archive_pipeline_directory)
        
    def test_pipeline_definition_create_setup_script(self):
        self.assertEqual('test', self.pipeline_definition.pipeline_name)
        self.pipeline_definition.create_setup_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.pipeline_directory))
        self.assertTrue(os.path.exists(self.pipeline_definition.setup_script_path))

    def test_pipeline_definition_create_run_script(self):
        self.pipeline_definition.create_run_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.run_script_path))

    def test_pipeline_definition_create_run_script_cluster(self):
        self.pipeline_definition_cluster.create_run_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition_cluster.run_script_path))
        
    def test_pipeline_definition_create_rsync_script(self):
        self.pipeline_definition.create_rsync_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))
        
    def test_pipeline_definition_run_rsync_script(self):
        import time
        utils.touch(self.pipeline_definition.pipeline_started)
        utils.touch(self.pipeline_definition.pipeline_ended)
        self.pipeline_definition.create_rsync_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.rsync_script_path))
        self.pipeline_definition.run_rsync_pipeline_script(True, False)
        time.sleep(5) # wait for rsync to synchronise files
        self.assertTrue(os.path.exists(self.pipeline_definition.archive_pipeline_directory))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, PIPELINE_STARTED_FILENAME)))
        self.assertTrue(os.path.isfile(os.path.join(self.pipeline_definition.archive_pipeline_directory, PIPELINE_ENDED_FILENAME)))
        
class PipelinesTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        log = logger.set_custom_logger()
        log.setLevel(logging.DEBUG)  
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/basedir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = runfolders.RunFolders(self.basedir, self.archivedir)
        
    def tearDown(self):
        import shutil
        for run_definition in self.runs.findRunsToAnalyse():
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                if os.path.exists(pipeline_folder):
                    shutil.rmtree(pipeline_folder)
                archive_run_folder = utils.locate_run_folder(os.path.basename(run_definition.run_folder), self.archivedir)
                archive_pipeline_folder = os.path.join(archive_run_folder, pipeline_name)
                if os.path.exists(archive_pipeline_folder):
                    shutil.rmtree(archive_pipeline_folder)
            filelist = []
            filelist.extend(glob.glob("%s/Analysis.*.completed" % run_definition.run_folder))
            filelist.extend(glob.glob("%s/Analysis.*.completed" % archive_run_folder))
            for f in filelist:
                os.remove(f)

    def test_pipelines_execute(self):
        for run_definition in self.runs.findRunsToAnalyse():
            pipelines = Pipelines(run_definition)
            self.assertEqual(run_definition.run_folder_name, pipelines.run_definition.run_folder_name)
            pipelines.execute_pipelines()
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                self.assertTrue(os.path.exists(pipeline_folder))
                self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                
    def test_pipelines_register_completion(self):
        for run_definition in self.runs.findRunsToAnalyse():
            pipelines = Pipelines(run_definition)
            self.assertEqual(run_definition.run_folder_name, pipelines.run_definition.run_folder_name)
            pipelines.execute_pipelines()
            for pipeline_name in PIPELINES.keys():
                pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                utils.touch(os.path.join(pipeline_folder, PIPELINE_STARTED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, PIPELINE_ENDED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, RSYNC_STARTED_FILENAME))
                utils.touch(os.path.join(pipeline_folder, RSYNC_ENDED_FILENAME))
                archive_pipeline_folder = os.path.join(utils.locate_run_folder(os.path.basename(run_definition.run_folder), self.archivedir), pipeline_name)
                utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_STARTED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, PIPELINE_ENDED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, RSYNC_STARTED_FILENAME))
                utils.touch(os.path.join(archive_pipeline_folder, RSYNC_ENDED_FILENAME))
            pipelines.register_completion()
            self.assertTrue(os.path.isfile(pipelines.primary_completed))
            self.assertTrue(os.path.isfile(pipelines.all_completed))
            self.assertTrue(os.path.isfile(pipelines.archive_primary_completed))
            self.assertTrue(os.path.isfile(pipelines.archive_all_completed))
            
    def test_pipelines_execute_only_primary(self):
        for run_definition in self.runs.findRunsToAnalyse():
            pipelines = Pipelines(run_definition, 'primary')
            self.assertEqual(run_definition.run_folder_name, pipelines.run_definition.run_folder_name)
            pipelines.execute_pipelines()
            for pipeline_name in PIPELINES.keys():
                if pipeline_name is 'primary':
                    pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                    self.assertTrue(os.path.exists(pipeline_folder))
                    self.assertTrue(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                else:
                    pipeline_folder = os.path.join(run_definition.run_folder, pipeline_name)
                    self.assertFalse(os.path.exists(pipeline_folder))
                    self.assertFalse(os.path.exists(os.path.join(pipeline_folder, SETUP_SCRIPT_FILENAME)))
                    
        

if __name__ == '__main__':
	unittest.main()