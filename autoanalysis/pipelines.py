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
import os
import glob
import logging
import unittest
from collections import OrderedDict

# autoanalysis modules
import data
import utils

################################################################################
# CONSTANTS
################################################################################

# Pipeline setup command to generate metadata file
PIPELINE_SETUP_COMMAND = "%(bin_meta)s --basedir=%(basedir)s --notifications %(options)s %(flowcell_id)s %(run_meta)s"

PIPELINES_SETUP_OPTIONS = {
    "fastq": "",
    "primaryqc": "--create-sample-sheet --phix",
    "alignment": "--queue=solexa"}

# Pipeline run command to run pipeline
PIPELINE_RUN_COMMAND = "%(bin_run)s --mode=%(mode)s --clean %(run_meta)s"
PIPELINE_RUN_COMMAND_WITH_IGNOREWALLTIME = "%(bin_run)s --mode=%(mode)s --clean --ignore-walltime %(run_meta)s"

# Software pipeline path
SOFT_PIPELINE_PATH = "/home/mib-cri/software/pipelines"

# ftp server
FTP_SERVER = "solexadmin@uk-cri-ldmz01"
FTP_PATH = "/dmz01/solexa/external"
FTP_URL = "%s:%s" % (FTP_SERVER, FTP_PATH)

# Default filenames
SETUP_SCRIPT_FILENAME = "setup-pipeline.sh"
RUN_SCRIPT_FILENAME = "run-pipeline.sh"
PIPELINE_STARTED_FILENAME = "pipeline.started"
PIPELINE_ENDED_FILENAME = "pipeline.ended"
PIPELINE_FAILED_FILENAME = "pipeline.failed"
PIPELINE_LOG_FILENAME = "pipeline.log"
PIPELINE_LOCK_FILENAME = "pipeline.lock"

CREATE_METAFILE_FILENAME = "create-metafile"
RUN_META_FILENAME = "run-meta.xml"
RUN_PIPELINE_FILENAME = "run-pipeline"

################################################################################
# CLASS PipelineDefinition
################################################################################        
class PipelineDefinition(object):

    def __init__(self, run, pipeline_name, software_path=SOFT_PIPELINE_PATH, cluster_host=None, use_limsdev=True, mode='local'):
        self.log = logging.getLogger(__name__)
        self.run = run
        self.pipeline_name = pipeline_name

        # create pipeline directory
        if cluster_host and mode == 'lsf':
            self.pipeline_directory = os.path.join(self.run.lustre_run_folder, self.pipeline_name)
            utils.create_directory(self.pipeline_directory)
        else:
            self.pipeline_directory = os.path.join(self.run.run_folder, self.pipeline_name)
            utils.create_directory(self.pipeline_directory)

        # create archive pipeline directory in staging area
        self.log.debug(self.run.staging_run_folder)
        self.log.debug(self.pipeline_name)
        self.archive_pipeline_directory = os.path.join(self.run.staging_run_folder, self.pipeline_name)
        
        # shell script paths
        self.setup_script_path = os.path.join(self.pipeline_directory, SETUP_SCRIPT_FILENAME)
        self.run_script_path = os.path.join(self.pipeline_directory, RUN_SCRIPT_FILENAME)

        self.pipeline_started = os.path.join(self.pipeline_directory, PIPELINE_STARTED_FILENAME)
        self.pipeline_ended = os.path.join(self.pipeline_directory, PIPELINE_ENDED_FILENAME)
        self.pipeline_failed = os.path.join(self.pipeline_directory, PIPELINE_FAILED_FILENAME)
        self.pipeline_lock = os.path.join(self.run.run_folder, PIPELINE_LOCK_FILENAME)
        self.pipeline_log = os.path.join(self.pipeline_directory, PIPELINE_LOG_FILENAME)

        # environment variables for setting up and running each pipeline
        self.env = {}
        self.set_env(software_path, cluster_host, use_limsdev, mode)
        
    def get_header(self):
        return '--- %s' % self.pipeline_name.upper()
        
    def print_header(self):
        self.log.info(self.get_header())
        
    def set_env(self, _software_path, _cluster_host, _use_limsdev, _mode):
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
        self.env['flowcell_id'] = self.run.flowcell_id
        self.env['run_meta'] = os.path.join(self.pipeline_directory, RUN_META_FILENAME)
        if _cluster_host and _mode == 'lsf':
            self.env['mode'] = 'lsf' 
        else:
            self.env['mode'] = 'local'
        self.env['lsf_queue'] = 'solexa'
        self.env['mem_value'] = '2048'
        self.env['cluster'] = _cluster_host
        self.env['work_dir'] = self.pipeline_directory
        self.env['job_name'] = "%s_%s_pipeline" % (self.run.flowcell_id, self.pipeline_name)
        self.env['cmd'] = PIPELINE_RUN_COMMAND % self.env
        self.env['pipedir'] = self.pipeline_directory
        self.env['archive_pipedir'] = self.archive_pipeline_directory
        self.env['started'] = self.pipeline_started
        self.env['ended'] = self.pipeline_ended
        self.env['failed'] = self.pipeline_failed
        self.env['log'] = self.pipeline_log
        self.env['lock'] = self.pipeline_lock

    def create_setup_pipeline_script(self):
        self.log.info('... create setup pipeline script ...............................................')
        try:
            if not os.path.exists(self.setup_script_path):
                utils.create_script(self.setup_script_path, PIPELINE_SETUP_COMMAND % self.env)
            else:
                self.log.debug('%s already exists' % self.setup_script_path)
        except:
            self.log.exception('unexpected error when creating setup pipeline script')
            raise
        
    def run_setup_pipeline_script(self, _dependencies_satisfied=True, _dry_run=True):
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
            
    def create_run_pipeline_script(self):
        self.log.info('... create run pipeline script .................................................')
        try:
            if self.env['mode'] == 'lsf':
                utils.create_script(self.run_script_path, utils.LSF_CMD_TEMPLATE % self.env)
            else:
                utils.create_script(self.run_script_path, utils.LOCAL_CMD_TEMPLATE % self.env)
        except:
            self.log.exception('unexpected error when creating run pipeline script')
            raise
            
    def run_run_pipeline_script(self, _dependencies_satisfied=True, _dry_run=True):
        self.log.info('... run run pipeline script ....................................................')
        if os.path.exists(self.env['run_meta']):
            # pipeline not started
            if not os.path.exists(self.pipeline_started):
                # no pipeline.finished file, then run-pipeline
                if not os.path.exists(self.pipeline_ended):
                    if _dependencies_satisfied:
                        if self.env['mode'] == 'local':
                            utils.run_bg_process(['sh', '%s' % self.run_script_path], _dry_run)
                        else:
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


################################################################################
# CLASS Pipelines
################################################################################
class Pipelines(object):

    # Pipeline definitions and dependencies
    PIPELINES = OrderedDict([
        ("fastq", []),
        ("primaryqc", ["fastq"]),
        ("alignment", ["fastq"])
    ])

    PIPELINES_DEFAULT_MODE = {
        "fastq": "local",
        "primaryqc": "local",
        "alignment": "lsf"
    }

    def __init__(self, run, pipeline_step=None, software_path=SOFT_PIPELINE_PATH, cluster_host=None, dry_run=True, use_limsdev=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.pipeline_step = pipeline_step
        self.software_path = software_path
        self.cluster_host = cluster_host
        self.dry_run = dry_run
        self.use_limsdev = use_limsdev 

        self.pipelines = Pipelines.PIPELINES
        if self.pipeline_step:
            self.pipelines = {self.pipeline_step: ""}

        self.pipeline_definitions = {}
            
        self.all_completed = os.path.join(self.run.run_folder, data.ANALYSIS_COMPLETED)
        self.archive_all_completed = os.path.join(self.run.staging_run_folder, data.ANALYSIS_COMPLETED)
        
    def execute(self):
        """execute all pipelines or just one by creating a shell script and running it for
        each of these three steps: setup_pipeline, run_pipeline, and rsync_pipeline
        """
        if self.run.is_sequencing_completed():
            for pipeline_name in self.pipelines.keys():
                # create pipeline definition
                pipeline_definition = PipelineDefinition(self.run, pipeline_name, self.software_path, self.cluster_host, self.use_limsdev, Pipelines.PIPELINES_DEFAULT_MODE[pipeline_name])
                pipeline_definition.print_header()
                self.pipeline_definitions[pipeline_name] = pipeline_definition
                # - step 1 - create setup-pipeline script
                pipeline_definition.create_setup_pipeline_script()
                # run setup-pipeline script to create meta data 
                pipeline_definition.run_setup_pipeline_script(self.are_dependencies_satisfied(pipeline_name), self.dry_run)
                # - step 2 - create run-pipeline script
                pipeline_definition.create_run_pipeline_script()
                # run run-pipeline script to run the pipeline
                pipeline_definition.run_run_pipeline_script(self.are_dependencies_satisfied(pipeline_name), self.dry_run)

    def register_completion(self):
        """ Create Analysis.completed when pipelines have been successfully ran and synchronised
        """
        # create AnalysisComplete.txt flag when all pipelines completed
        if self.are_pipelines_completed(self.pipeline_definitions):
            if not os.path.exists(self.all_completed):
                utils.touch(self.all_completed)
            self.log.info('*** ANALYSIS COMPLETED *********************************************************')
        else:
            # remove Analysis.completed when analysis not completed and file exists
            if os.path.exists(self.all_completed):
                os.remove(self.all_completed)

    ### Utility methods -------------------------------------------------------
    def are_dependencies_satisfied(self, pipeline_name):
        """For a given pipeline, checks that all dependent pipelines have finished
        Both pipeline.started and pipeline.ended need to be present
        """
        pipeline_dependencies = Pipelines.PIPELINES[pipeline_name]
        self.log.debug('%s pipeline dependencies: [%s]' % (pipeline_name, ",".join(pipeline_dependencies)))
        for dep_pipeline_name in pipeline_dependencies:
            # pipeline not finished or started
            if not os.path.exists(self.pipeline_definitions[dep_pipeline_name].pipeline_ended) or not os.path.exists(self.pipeline_definitions[dep_pipeline_name].pipeline_started):
                return False
        return True

    def are_pipelines_completed(self, list_pipelines):
        """Checks for a list of pipelines that each of them has finished
        pipeline.started and pipeline.ended need to be present
        """
        for pipeline_name in list_pipelines.keys():
            # pipeline not finished or started
            if not os.path.exists(list_pipelines[pipeline_name].pipeline_ended) or not os.path.exists(list_pipelines[pipeline_name].pipeline_started):
                return False
        return True
        

################################################################################
# CLASS External
################################################################################
class External(object):

    # External pipeline name
    EXTERNAL_PIPELINE = 'external'

    def __init__(self, run, all_data, external_data, dry_run=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.all_data = all_data
        self.external_data = external_data
        self.pipeline_name = self.EXTERNAL_PIPELINE
        self.publishing_assigned = os.path.join(self.run.run_folder, data.PUBLISHING_ASSIGNED)
        self.publishing_completed = os.path.join(self.run.run_folder, data.PUBLISHING_COMPLETED)
        self.archive_publishing_completed = os.path.join(self.run.staging_run_folder, data.PUBLISHING_COMPLETED)
        self.dry_run = dry_run
        
    def sync(self):
        """synchronise external data to ftp server - rsync to ldmz01
        create external directory with symlink to fastq files on archivedir (sol03) - not basedir (lustre) -
        synchronise external data to temp on solexadmin@uk-cri-ldmz01:/dmz01/solexa/external/tmp/${ftp_group_dir}/
        """
        if self.run.is_analysis_completed_present():
            if self.external_data:
                if self.run.staging_run_folder:
                    # create pipeline definition
                    pipeline_definition = PipelineDefinition(run=self.run, pipeline_name=self.pipeline_name)
                    pipeline_definition.print_header()
                    # create symlinks for external users
                    self.create_symlinks(pipeline_definition.archive_pipeline_directory)
                    # create rsync-pipeline script
                    self.create_ftp_rsync_script(pipeline_definition.run_script_path, pipeline_definition.env)
                    # run rsync-pipeline script
                    self.run_ftp_rsync_script(pipeline_definition.run_script_path, pipeline_definition.env)
                else:
                    self.log.warn('%s does not exist' % self.run.staging_run_folder)
            else:
                self.log.info('No external data to publish')
                
    def create_symlinks(self, external_directory):
        """ Create symlink to external fastq data into external folder
        - files to symlink per lane:
            SLX-7957.C3BW4ACXX.s_8.contents.csv
            SLX-7957.C3BW4ACXX.s_8.r_1.lostreads.fq.gz
            SLX-7957.C3BW4ACXX.s_8.lostreads.md5sums.txt
        - files to symlink per sample:
            SLX-7957.A002.C3BW4ACXX.s_8.r_1.fq.gz
            SLX-7957.A002.C3BW4ACXX.s_8.md5sums.txt
        - if non PF data requested
            SLX-7957.C3BW4ACXX.s_8.r_1.failed.fq.gz
            SLX-7957.C3BW4ACXX.s_8.failed.md5sums.txt
        """
        self.log.info('... create symlinks to external data ...........................................')
        for file_id in list(self.external_data.viewkeys()):
            # create ftpdir in external directory in run folder
            runfolder_ext_ftpdir = os.path.join(external_directory, self.external_data[file_id]['ftpdir'])
            utils.create_directory(runfolder_ext_ftpdir)
            filename = self.external_data[file_id]['runfolder']
            try:
                # create symlink
                linkname = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename))
                utils.create_symlink(filename, linkname)
                # symlink non PF data
                if self.external_data[file_id]['nonpfdata'] == 'True' and filename.endswith('.contents.csv'):
                    for file_extension in ['.r_1.failed.fq.gz', '.r_2.failed.fq.gz', '.failed.md5sums.txt']:
                        filename_failed = filename.replace('.contents.csv', file_extension)
                        linkname_failed = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename_failed))
                        utils.create_symlink(filename_failed, linkname_failed)                
            except:
                continue

    def create_ftp_rsync_script(self, rsync_script, env):
        """Create rsync script for external data
        """
        self.log.info('... create ftp rsync pipeline script ...........................................')
        ftp_rsync_command = '''
        touch %(started)s
        touch %(lock)s

        if ( %(rsync_cmd)s ) 
        then
           touch %(ended)s
        else
            touch %(failed)s
        fi
        
        rsync -av %(pipedir)s/ %(archive_pipedir)s/
        
        rm %(lock)s
        '''
        
        rsync_cmd = ""
        # set of institutes
        ftpdirs = set()
        for file_id in list(self.external_data.viewkeys()):
            ftpdirs.add(self.external_data[file_id]['ftpdir'])
        for ftpdir in ftpdirs:
            src = os.path.join(env['archive_pipedir'], ftpdir)
            dest = "%s/tmp/%s/" % (FTP_URL, ftpdir)
            rsync_log = "%s/rsync_%s.log" % (env['archive_pipedir'], ftpdir)
            cmd = "rsync -rv --copy-links %s/ %s > %s 2>&1; " % (src, dest, rsync_log)
            rsync_cmd += cmd
        env['rsync_cmd'] = rsync_cmd
        utils.create_script(rsync_script, ftp_rsync_command % env)

    def run_ftp_rsync_script(self, rsync_script, env):
        """Run rsync script for external data
        """
        self.log.info('... run ftp rsync pipeline script ..............................................')
        if os.path.exists(rsync_script):
            if not os.path.exists(env['started']):
                if not os.path.exists(env['lock']):
                    utils.run_bg_process(['sh', '%s' % rsync_script], self.dry_run)
                else:
                    self.log.info('%s presents - another rsync process is running' % env['lock'])
            else:
                if not os.path.exists(env['ended']):
                    if not os.path.exists(env['failed']):
                        self.log.info('external data is currently being synchronised')
                    else:
                        self.log.info('[***FAIL***] rsync for external data onto ftp server has failed')
                else:
                    self.log.info('external data has been synchronised')
        else:
            self.log.warn('%s is missing' % rsync_script)

    def publish(self):
        """Publish external data to ftp server that have been published in lims and add Publishing.completed
        Move external data from tmp to public directory solexadmin@uk-cri-ldmz01:/dmz01/solexa/external/${ftp_group_dir}/
        THIS IS NOW DONE AS PART OF AN EPP SCRIPT ATTACHED TO THE PUBLISHING PROCESS
        """
        if self.run.is_analysis_completed_present():
            if self.all_data:
                if self.external_data:
                    if self.is_external_data_synchronised():
                        if not self.is_publishing_completed():
                            self.log.info('... move external data to public folders .......................................')
                            # build dictionnary of SLX-IDs to be moved
                            data = {}
                            for file_id in list(self.external_data.viewkeys()):
                                filename = os.path.basename(self.external_data[file_id]['runfolder'])
                                if filename.endswith('.contents.csv'):
                                    # "/solexa03/data/Runs/140228_SN1078_0260_C3JEHACXX/fastq/SLX-8180.C3JEHACXX.s_8.contents.csv"
                                    fparts = filename.split('.') 
                                    slxkey = '%s*%s*%s' % (fparts[0], fparts[1], fparts[2])  # key made of SLX-ID*FC-ID*LANE-ID
                                    data[slxkey] = self.external_data[file_id]['ftpdir']
                            # move data
                            for slxkey in data.viewkeys():
                                # ssh solexadmin@uk-cri-ldmz01 mv /dmz01/solexa/external/tmp/gurdon_institute/SLX-xxxx*FCID*s_x* /dmz01/solexa/external/gurdon_institute/
                                src = "%s/tmp/%s/%s*" % (FTP_PATH, data[slxkey], slxkey)
                                dest = "%s/%s/" % (FTP_PATH, data[slxkey])
                                cmd = ['ssh', FTP_SERVER, 'mv %s %s' % (src, dest)]
                                utils.run_process(cmd, self.dry_run)
                            # register completion
                            utils.touch(self.publishing_completed)
                            utils.touch(self.archive_publishing_completed)
                        else:
                            self.log.info('External data already move to public folders')
                        self.log.info('*** PUBLISH COMPLETED ******************************************************')
                    else:
                        self.log.info('External data not synchronised to ftp yet')
                else:
                    self.log.info('No external data')
                    if not self.is_publishing_completed():
                        # register completion
                        utils.touch(self.publishing_completed)
                        utils.touch(self.archive_publishing_completed)
                    self.log.info('*** PUBLISH COMPLETED ******************************************************')
            else:
                self.log.info('Sample FASTQ files not attached in lims yet')
               
    def is_publishing_completed(self):
        if os.path.exists(self.publishing_completed) and os.path.exists(self.archive_publishing_completed):
            return True
        return False
        
    def is_external_data_synchronised(self):
        """Checks that external data has been synchronised to the ftp tmp folder
        """
        # on current location
        external_directory = os.path.join(self.run.run_folder, self.pipeline_name)
        rsync_started = os.path.join(external_directory, PIPELINE_STARTED_FILENAME)
        rsync_finished = os.path.join(external_directory, PIPELINE_ENDED_FILENAME)
        # at destination
        dest_external_directory = os.path.join(self.run.staging_run_folder, self.pipeline_name)
        dest_rsync_started = os.path.join(dest_external_directory, PIPELINE_STARTED_FILENAME)
        dest_rsync_finished = os.path.join(dest_external_directory, PIPELINE_ENDED_FILENAME)
        # data files attached in lims 
        if self.all_data:
            # external data found
            if self.external_data:
                # rsync to ftp finished - data synchronised
                if os.path.exists(rsync_started) and os.path.exists(rsync_finished) and os.path.exists(dest_rsync_started) and os.path.exists(dest_rsync_finished):
                    return True
                return False
            # no external data found
            return True
        # no data files attached
        return False


################################################################################
# CLASS Sync
################################################################################
class Sync(object):

    # Template for syncing run folder command
    RUNFOLDER_RSYNC_COMMAND = '''
touch %(started)s
touch %(lock)s

if ( rsync %(rsync_options)s )
then
    touch %(ended)s
    cp %(ended)s %(archive_pipedir)s/.
else
    touch %(failed)s
fi

rm %(lock)s
'''

    # rsync exclude list
    RUNFOLDER_RSYNC_EXCLUDE = [
    "--exclude=Data/Intensities/*_pos.txt",
    "--exclude=Data/Intensities/L00?",
    "--exclude=Data/Intensities/BaseCalls",
    "--exclude=Data/RTALogs",
    "--exclude=Logs",
    "--exclude=Thumbnail_Images",  # thumbnail images
    "--exclude=Images",  # *.tif images from MiSeq
    "--exclude=Old*",  # Anything that has been moved out of the way
    "--exclude=temp",
    "--exclude=JobOutputs",
    "--exclude=primaryqc"
    ]


    def __init__(self, run, dry_run=True):
        self.log = logging.getLogger(__name__) 
        self.run = run
        self.pipeline_name = 'sync'
        self.dry_run = dry_run

        # create pipeline definition
        self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name=self.pipeline_name)
        self.pipeline_definition.print_header()

        self.env = self.pipeline_definition.env
        self.env['rsync_options'] = "-av %s %s %s > %s 2>&1" % (" ".join(self.RUNFOLDER_RSYNC_EXCLUDE), self.run.run_folder, os.path.dirname(self.run.staging_run_folder), self.pipeline_definition.pipeline_log)


    def execute(self):
        """execute synchronisation of run folder into staging by creating a shell script and running it
        """
        if self.run.is_sequencing_completed():
            # create rsync-pipeline script
            self.create_rsync_runfolder_script()
            # run rsync-pipeline script
            self.run_rsync_runfolder_script(self.dry_run)

    def create_rsync_runfolder_script(self):
        self.log.info('... create rsync runfolder script ..............................................')
        try:
            if not os.path.exists(self.pipeline_definition.run_script_path):
                utils.create_script(self.pipeline_definition.run_script_path, self.RUNFOLDER_RSYNC_COMMAND % self.env)
            else:
                self.log.debug('%s already exists' % self.pipeline_definition.run_script_path)
        except:
            self.log.exception('unexpected error when creating rsync run script')
            raise

    def run_rsync_runfolder_script(self, _dry_run=True):
        """Run rsync script to synchronise runfolder data from sequencing servers to lustre
        """
        self.log.info('... run rsync runfolder script .................................................')
        if os.path.exists(self.pipeline_definition.run_script_path):
            if not os.path.exists(self.pipeline_definition.pipeline_started):
                if not os.path.exists(self.pipeline_definition.pipeline_lock):
                    if self.run.is_analysis_completed_present():
                        utils.touch(self.pipeline_definition.pipeline_lock, _dry_run)
                        utils.run_bg_process(['sh', '%s' % self.pipeline_definition.run_script_path], _dry_run)
                    else:
                        self.log.debug("nothing to rsync yet - analysis not completed")
                else:
                    self.log.info('%s presents - another rsync process is running' % self.pipeline_definition.pipeline_lock)
            else:
                if not os.path.exists(self.pipeline_definition.pipeline_ended):
                    if os.path.exists(self.pipeline_definition.pipeline_failed):
                        self.log.error("[***FAIL***] rsync for %s has failed." % self.run.run_folder)
                        self.log.error("please investigate %s." % self.pipeline_definition.pipeline_log)
                    else:
                        self.log.info('runfolder is currently being synchronised')
                else:
                    self.log.info('runfolder has been synchronised')
        else:
            self.log.warn('%s is missing' % self.pipeline_definition.run_script_path)


################################################################################
# Unit tests
################################################################################
class PipelineDefinitionTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir)
        self.run = self.runs.toanalyse_runs[0]
        self.log.debug('Testing logging')
        self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name='test_local')
        self.pipeline_definition.print_header()
        self.pipeline_definition_cluster = PipelineDefinition(run=self.run, pipeline_name='test_lsf', cluster_host='uk-cri-test', use_limsdev=False, mode='lsf')
        self.pipeline_definition_cluster.print_header()
        
    def tearDown(self):
        import shutil
        shutil.rmtree(self.pipeline_definition.pipeline_directory)
        for run in self.runs.completed_runs:
            shutil.rmtree(run.staging_run_folder)
            shutil.rmtree(run.lustre_run_folder)

    def test_create_setup_script(self):
        self.assertEqual('test_local', self.pipeline_definition.pipeline_name)
        self.pipeline_definition.create_setup_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.pipeline_directory))
        self.assertTrue(os.path.exists(self.pipeline_definition.setup_script_path))

    def test_create_run_script(self):
        self.pipeline_definition.create_run_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition.run_script_path))

    def test_create_setup_script_cluster(self):
        self.assertEqual('test_lsf', self.pipeline_definition_cluster.pipeline_name)
        self.pipeline_definition_cluster.create_setup_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition_cluster.pipeline_directory))
        self.assertTrue(os.path.exists(self.pipeline_definition_cluster.setup_script_path))

    def test_create_run_script_cluster(self):
        self.assertEqual('test_lsf', self.pipeline_definition_cluster.pipeline_name)
        self.pipeline_definition_cluster.create_run_pipeline_script()
        self.assertTrue(os.path.exists(self.pipeline_definition_cluster.run_script_path))


class PipelinesTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir)
        
    def tearDown(self):
        import shutil
        for run in self.runs.completed_runs:
            shutil.rmtree(run.staging_run_folder)
            shutil.rmtree(run.lustre_run_folder)
            for pipeline_name in Pipelines.PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                if os.path.exists(pipeline_folder):
                    shutil.rmtree(pipeline_folder)
            if run.run_folder_name == '130417_HWI-ST230_1122_C1YH9ACXX' and os.path.exists(run.analysis_completed):
                os.remove(run.analysis_completed)

    def test_execute(self):
        for run in self.runs.toanalyse_runs:
            pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in pipelines.pipeline_definitions.keys():
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))
                
    def test_register_completion(self):
        for run in self.runs.toanalyse_runs:
            pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in pipelines.pipeline_definitions.keys():
                utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_started)
                utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_ended)
            pipelines.register_completion()
            self.assertTrue(os.path.isfile(pipelines.all_completed))

    def test_execute_only_fastq(self):
        for run in self.runs.toanalyse_runs:
            pipelines = Pipelines(run=run, pipeline_step='fastq')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in pipelines.pipeline_definitions.keys():
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))


class PipelinesOneRunFolderTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir, '130417_HWI-ST230_1122_C1YH9ACXX')

    def tearDown(self):
        import shutil
        for run in self.runs.completed_runs:
            shutil.rmtree(run.staging_run_folder)
            shutil.rmtree(run.lustre_run_folder)
            for pipeline_name in Pipelines.PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                if os.path.exists(pipeline_folder):
                    shutil.rmtree(pipeline_folder)
            if run.run_folder_name == '130417_HWI-ST230_1122_C1YH9ACXX' and os.path.exists(run.analysis_completed):
                os.remove(run.analysis_completed)

    def test_one_runfolder(self):
        self.assertEqual(1, len(self.runs.run_folders))
        self.assertEqual(1, len(self.runs.completed_runs))
        self.assertEqual(1, len(self.runs.toanalyse_runs))
        self.assertEqual(0, len(self.runs.analysed_runs))

    def test_execute(self):
        run = self.runs.toanalyse_runs[0]
        pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in pipelines.pipeline_definitions.keys():
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))

    def test_register_completion(self):
        run = self.runs.toanalyse_runs[0]
        pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in pipelines.pipeline_definitions.keys():
            utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_started)
            utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_ended)
        pipelines.register_completion()
        self.assertTrue(os.path.isfile(pipelines.all_completed))

    def test_execute_only_fastq(self):
        run = self.runs.toanalyse_runs[0]
        pipelines = Pipelines(run=run, pipeline_step='fastq')
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in pipelines.pipeline_definitions.keys():
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))


class SyncTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir)
        
    def tearDown(self):
        import shutil
        for run in self.runs.completed_runs:
            pipeline_folder = os.path.join(run.run_folder, 'sync')
            if os.path.exists(pipeline_folder):
                shutil.rmtree(pipeline_folder)
            shutil.rmtree(run.staging_run_folder)
            shutil.rmtree(run.lustre_run_folder)

    def test_execute(self):
        import time
        for run in self.runs.analysed_runs:
            sync = Sync(run=run, dry_run=False)
            self.assertEqual(run.run_folder_name, sync.run.run_folder_name)
            sync.execute()
            time.sleep(5)  # wait for rsync to synchronise files
            pipeline_folder = os.path.join(run.run_folder, sync.pipeline_name)
            dest_pipeline_folder = os.path.join(run.staging_run_folder, sync.pipeline_name)
            self.assertTrue(os.path.exists(pipeline_folder))
            self.assertTrue(os.path.exists(os.path.join(pipeline_folder, RUN_SCRIPT_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, PIPELINE_STARTED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, PIPELINE_ENDED_FILENAME)))
            self.assertTrue(os.path.exists(dest_pipeline_folder))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, PIPELINE_STARTED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, PIPELINE_ENDED_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(run.staging_run_folder, data.SEQUENCING_COMPLETED)))
                                                    
if __name__ == '__main__':
    unittest.main()