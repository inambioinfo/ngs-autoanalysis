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
import socket

# autoanalysis modules
import data
import utils

# constants and configurations
from config import cfg


################################################################################
# CLASS PipelineDefinition
################################################################################
class PipelineDefinition(object):

    def __init__(self, run, pipeline_name, software_path=cfg['SOFT_PIPELINE_PATH'], cluster_host=None, use_limsdev=True, mode='local'):
        self.log = logging.getLogger(__name__)
        self.run = run
        self.pipeline_name = pipeline_name
        self.software_path = software_path
        self.cluster_host = cluster_host
        self.use_limsdev = use_limsdev
        self.mode = mode
        if self.pipeline_name == 'alignment':
            self.pipeline_setup_options = cfg['PIPELINES_SETUP_OPTIONS'][pipeline_name] % (socket.gethostname(), str(self.run.run_folder)[1:])
        else:
            self.pipeline_setup_options = cfg['PIPELINES_SETUP_OPTIONS'].get(pipeline_name, '')

        # create pipeline directory
        if self.cluster_host and mode == 'lsf':
            self.pipeline_directory = os.path.join(self.run.lustre_run_folder, self.pipeline_name)
            utils.create_directory(self.pipeline_directory)
        else:
            self.pipeline_directory = os.path.join(self.run.run_folder, self.pipeline_name)
            utils.create_directory(self.pipeline_directory)

        # set path to pipeline directory in staging area
        self.archive_pipeline_directory = os.path.join(self.run.staging_run_folder, self.pipeline_name)

        # set environment
        self.setup_script_path = ""
        self.run_script_path = ""
        self.pipeline_started = ""
        self.pipeline_ended = ""
        self.pipeline_failed = ""
        self.pipeline_lock = ""
        self.pipeline_log = ""
        self.env = {}
        self.set_env()

    def get_header(self):
        return '--- %s' % self.pipeline_name.upper()

    def print_header(self):
        self.log.info(self.get_header())

    def set_env(self):
        """ set environment : set path to pipeline files
        and create an env dictionary containing variables for generating shell scripts from their templates
        """
        # set paths to pipeline files
        self.setup_script_path = os.path.join(self.pipeline_directory, cfg['SETUP_SCRIPT_FILENAME'])
        self.run_script_path = os.path.join(self.pipeline_directory, cfg['RUN_SCRIPT_FILENAME'])
        self.pipeline_started = os.path.join(self.pipeline_directory, cfg['PIPELINE_STARTED_FILENAME'])
        self.pipeline_ended = os.path.join(self.pipeline_directory, cfg['PIPELINE_ENDED_FILENAME'])
        self.pipeline_failed = os.path.join(self.pipeline_directory, cfg['PIPELINE_FAILED_FILENAME'])
        self.pipeline_lock = os.path.join(os.path.dirname(self.pipeline_directory), cfg['PIPELINE_LOCK_FILENAME'])
        self.pipeline_log = os.path.join(self.pipeline_directory, cfg['PIPELINE_LOG_FILENAME'])
        # environment variables for setting up and running each pipeline
        self.env['bin_meta'] = '%s/%s/bin/%s' % (self.software_path, self.pipeline_name, cfg['CREATE_METAFILE_FILENAME'])
        self.env['bin_run'] = '%s/%s/bin/%s' % (self.software_path, self.pipeline_name, cfg['RUN_PIPELINE_FILENAME'])
        self.env['basedir'] = os.path.dirname(os.path.dirname(self.pipeline_directory))

        if self.pipeline_name in cfg['PIPELINES_SETUP_OPTIONS'].keys():
            if self.use_limsdev:
                self.env['options'] = "%s --dev" % self.pipeline_setup_options
            else:
                self.env['options'] = self.pipeline_setup_options
        else:
            if self.use_limsdev:
                self.env['options'] = '--dev'
            else:
                self.env['options'] = ''
        self.env['flowcell_id'] = self.run.flowcell_id
        self.env['run_meta'] = os.path.join(self.pipeline_directory, cfg['RUN_META_FILENAME'])
        if self.cluster_host and self.mode == 'lsf':
            self.env['mode'] = 'lsf'
        else:
            self.env['mode'] = 'local'
        self.env['lsf_queue'] = 'solexa'
        self.env['mem_value'] = '2048'
        self.env['cluster'] = self.cluster_host
        self.env['work_dir'] = self.pipeline_directory
        self.env['job_name'] = "%s_%s_pipeline" % (self.run.flowcell_id, self.pipeline_name)
        self.env['cmd'] = cfg['PIPELINE_RUN_COMMAND'] % self.env
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
                utils.create_script(self.setup_script_path, cfg['PIPELINE_SETUP_COMMAND'] % self.env)
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
                            if self.pipeline_name == 'alignment' and not os.path.isfile(cfg['ALIGNMENT_DAEMON_PID']):
                                pid = str(os.getpid())
                                file(cfg['ALIGNMENT_DAEMON_PID'], 'w').write(pid)
                                utils.run_bg_process(['sh', '%s' % self.run_script_path], _dry_run)
                            else:
                                utils.run_bg_process(['sh', '%s' % self.run_script_path], _dry_run)
                        else:
                            utils.run_process(['sh', '%s' % self.run_script_path], _dry_run)
                    else:
                        self.log.info('%s pipeline dependencies not satisfied' % self.pipeline_name)
                else:
                    self.log.warn("%s presents with no %s" % (self.pipeline_ended, cfg['PIPELINE_STARTED_FILENAME']))
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
                        if os.path.exists(self.env['log']):
                            if utils.log_with_error(self.env['log']):
                                self.log.error("[***FAIL***] %s pipeline in %s has errors." % (self.pipeline_name, self.run.run_folder))
                                self.log.error("please investigate %s." % self.env['log'])
                            else:
                                self.log.info("%s pipeline in %s has not finished." % (self.pipeline_name, self.run.run_folder))
                        else:
                            self.log.info("%s pipeline in %s has not finished." % (self.pipeline_name, self.run.run_folder))
                # pipeline finished
                else:
                    if self.env['mode'] == 'local' and self.pipeline_name == 'alignment' and os.path.isfile(cfg['ALIGNMENT_DAEMON_PID']):
                        os.unlink(cfg['ALIGNMENT_DAEMON_PID'])
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

    def __init__(self, run, pipeline_step=None, software_path=cfg['SOFT_PIPELINE_PATH'], cluster_host=None, dry_run=True, use_limsdev=True, is_alignment_active=True, local_mode=False):
        self.log = logging.getLogger(__name__)
        self.run = run
        self.pipeline_step = pipeline_step
        self.software_path = software_path
        self.cluster_host = cluster_host
        self.dry_run = dry_run
        self.use_limsdev = use_limsdev
        self.is_alignment_active = is_alignment_active
        self.local_mode = local_mode

        self.pipelines = Pipelines.PIPELINES
        if self.pipeline_step:
            self.pipelines = {self.pipeline_step: ""}

        self.pipeline_definitions = {}

        self.all_completed = self.run.analysis_completed

    def execute(self):
        """execute all pipelines or just one by creating a shell script and running it for
        each of these three steps: setup_pipeline, run_pipeline, and rsync_pipeline
        """
        if self.run.is_ready_for_processing():
            for pipeline_name in self.pipelines.keys():
                if pipeline_name == 'alignment':
                    if self.is_alignment_active:
                        # special case for running alignment pipeline locally - just one pipeline at a time
                        if self.local_mode:
                            self._execute_steps(pipeline_name)
                        else:
                            self._execute_steps(pipeline_name)
                else:
                    self._execute_steps(pipeline_name)
            self.register_completion()

    def _execute_steps(self, pipeline_name):
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
        """ Create AnalysisComplete.txt when all pipelines have been successfully ran
        """
        # create AnalysisComplete.txt flag when all pipelines completed and when not
        # running only one step
        if self.are_pipelines_completed(self.pipeline_definitions):
            if not self.pipeline_step and not os.path.exists(self.all_completed):
                utils.touch(self.all_completed)
            self.log.info('*** ANALYSIS COMPLETED *********************************************************')
        else:
            # remove AnalysisComplete.txt when analysis not completed and file exists
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
    "--exclude=Data/Intensities/L00?",
    "--exclude=Data/Intensities/BaseCalls/L00?",
    "--exclude=Data/RTALogs",
    "--exclude=RTALogs",
    "--exclude=Logs",
    "--exclude=Thumbnail_Images",  # thumbnail images
    "--exclude=Images",  # *.tif images from MiSeq
    "--exclude=Old*",  # Anything that has been moved out of the way
    "--exclude=temp",
    "--exclude=JobOutputs",
    "--exclude=BCLtoFASTQ",
    "--exclude=primaryqc",
    "--exclude=%s" % cfg['PIPELINE_LOCK_FILENAME']
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

        self.sync_completed = self.run.sync_completed
        self.staging_sync_completed = os.path.join(self.run.staging_run_folder, cfg['SYNC_COMPLETED'])

    def execute(self):
        """execute synchronisation of run folder into staging by creating a shell script and running it
        """
        if self.run.is_ready_for_processing() and self.run.is_analysis_completed_present():
            # create rsync-pipeline script
            self.create_rsync_runfolder_script()
            # run rsync-pipeline script
            self.run_rsync_runfolder_script(self.dry_run)
            # register completion
            self.register_completion()

    def create_rsync_runfolder_script(self):
        self.log.info('... create staging sync script .................................................')
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
        self.log.info('... run staging sync script ....................................................')
        if os.path.exists(self.pipeline_definition.run_script_path):
            if not os.path.exists(self.pipeline_definition.pipeline_started):
                if not os.path.exists(self.pipeline_definition.pipeline_lock):
                    if self.run.is_analysis_completed_present():
                        utils.touch(self.pipeline_definition.pipeline_lock, _dry_run)
                        utils.run_bg_process(['sh', '%s' % self.pipeline_definition.run_script_path], _dry_run)
                    else:
                        self.log.debug("nothing to sync yet - analysis not completed")
                else:
                    self.log.info('%s presents - another sync process is running' % self.pipeline_definition.pipeline_lock)
            else:
                if not os.path.exists(self.pipeline_definition.pipeline_ended):
                    if os.path.exists(self.pipeline_definition.pipeline_failed):
                        self.log.error("[***FAIL***] sync for %s has failed." % self.run.run_folder)
                        self.log.error("please investigate %s." % self.pipeline_definition.pipeline_log)
                    else:
                        self.log.info('runfolder is currently being synchronised')
                else:
                    self.log.info('runfolder has been synchronised')
        else:
            self.log.warn('%s is missing' % self.pipeline_definition.run_script_path)

    def register_completion(self):
        """ Create SyncComplete.txt when data has been successfully synced to staging
        """
        if os.path.exists(self.pipeline_definition.pipeline_ended) and os.path.exists(self.pipeline_definition.pipeline_started):
            self.run.touch_event(cfg['SYNC_COMPLETED'])
            self.run.copy_event_to_staging(cfg['SYNC_COMPLETED'])
            self.log.info('*** SYNC COMPLETED *************************************************************')
        else:
            # remove SyncComplete.txt when pipeline not completed and file exists
            self.run.remove_event(cfg['SYNC_COMPLETED'])
            self.run.remove_event_from_staging(cfg['SYNC_COMPLETED'])


################################################################################
# CLASS External
################################################################################
class External(object):

    # External pipeline name
    EXTERNAL_PIPELINE = 'external'

    def __init__(self, run, are_files_attached, external_data, dry_run=True, ftp_server=cfg['FTP_SERVER'], ftp_path=cfg['FTP_PATH']):
        self.log = logging.getLogger(__name__)
        self.run = run
        self.are_files_attached = are_files_attached
        self.external_data = external_data
        self.dry_run = dry_run
        self.ftp_server = ftp_server
        self.ftp_path = ftp_path
        self.pipeline_name = self.EXTERNAL_PIPELINE
        self.pipeline_definition = None
        self.external_completed = self.run.external_completed
        self.staging_external_completed = os.path.join(self.run.staging_run_folder, cfg['EXTERNAL_COMPLETED'])

    def execute(self):
        """synchronise external data to ftp server
        create external directory with symlink to fastq files
        synchronise external data to private folders on comp-ftpdmz001 for each research groups ${ftp_group_dir}/
        """
        if self.run.is_ready_for_processing() and self.run.is_analysis_completed_present() and self.run.is_sync_completed_present() and self.are_files_attached:
            if self.external_data:
                # create pipeline definition
                self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name=self.pipeline_name)
                # re-set pipeline directory to be in staging area
                self.pipeline_definition.pipeline_directory = self.pipeline_definition.archive_pipeline_directory
                self.pipeline_definition.set_env()
                self.pipeline_definition.print_header()
                # create symlinks for external users
                self.create_symlinks()
                # create rsync-pipeline script
                self.create_ftp_rsync_script()
                # run rsync-pipeline script
                self.run_ftp_rsync_script()
                # register completion
                self.register_completion()
            else:
                self.log.info('No external data to publish')
                if not os.path.exists(self.external_completed):
                    utils.touch(self.external_completed)
                if not os.path.exists(self.staging_external_completed):
                    utils.touch(self.staging_external_completed)
                self.log.info('*** EXTERNAL COMPLETED *********************************************************')

    def create_symlinks(self):
        """ Create symlink to external fastq data into external folder
        - files to symlink:
            fastq/SLX-12650.HGYGKBBXX.s_8.barcodesummary.txt
            fastq/SLX-12650.HGYGKBBXX.s_8.contents.csv
            fastq/SLX-12650.HGYGKBBXX.s_8.lostreads.md5sums.txt
            fastq/SLX-12650.HGYGKBBXX.s_8.r_1.lostreads.fq.gz
            fastq/SLX-12650.HGYGKBBXX.s_8.r_2.lostreads.fq.gz
            fastq/SLX-12650.NEBNext08.HGYGKBBXX.s_8.md5sums.txt
            fastq/SLX-12650.NEBNext08.HGYGKBBXX.s_8.r_1.fq.gz
            fastq/SLX-12650.NEBNext08.HGYGKBBXX.s_8.r_2.fq.gz
            fastqc/SLX-12650.HGYGKBBXX.s_8.r_1.fastqc.html
            fastqc/SLX-12650.HGYGKBBXX.s_8.r_2.fastqc.html
            mga/SLX-12650.HGYGKBBXX.s_8.mga.html
        - if non PF data requested
            SLX-7957.C3BW4ACXX.s_8.r_1.failed.fq.gz
            SLX-7957.C3BW4ACXX.s_8.failed.md5sums.txt
        """
        self.log.info('... create symlinks to external data ...........................................')
        for file_id in list(self.external_data.viewkeys()):
            # create ftpdir in external directory in run folder
            runfolder_ext_ftpdir = os.path.join(self.pipeline_definition.pipeline_directory, self.external_data[file_id]['ftpdir'])
            utils.create_directory(runfolder_ext_ftpdir)
            filename = self.external_data[file_id]['runfolder'].replace('/runs/', os.path.dirname(self.run.staging_dir) + '/')
            try:
                # get all files associated to *.contents.csv file from run folder on disk
                # /staging/161130_K00252_0085_HGYGKBBXX/fastq/SLX-12650.HGYGKBBXX.s_8.contents.csv
                if filename.endswith('.contents.csv'):
                    bname = os.path.basename(filename)
                    folder = os.path.dirname(os.path.dirname(filename))
                    slx = bname.split('.')[0]
                    fc = bname.split('.')[2]
                    files_in_folder = glob.glob('%s/fastq/%s*%s*' % (folder, slx, fc))
                    files_in_folder.extend(glob.glob('%s/fastqc/%s*%s*' % (folder, slx, fc)))
                    files_in_folder.extend(glob.glob('%s/mga/%s*%s*' % (folder, slx, fc)))
                    self.log.debug(files_in_folder)
                    for f in files_in_folder:
                        # create symlinks
                        linkname = os.path.join(runfolder_ext_ftpdir, os.path.basename(f))
                        utils.create_symlink(f, linkname)
                    # symlink non PF data
                    if self.external_data[file_id]['nonpfdata'] == 'True' and filename.endswith('.contents.csv'):
                        for file_extension in ['.r_1.failed.fq.gz', '.r_2.failed.fq.gz', '.failed.md5sums.txt']:
                            filename_failed = filename.replace('.contents.csv', file_extension)
                            linkname_failed = os.path.join(runfolder_ext_ftpdir, os.path.basename(filename_failed))
                            utils.create_symlink(filename_failed, linkname_failed)
            except:
                continue

    def create_ftp_rsync_script(self):
        """Create rsync script for external data to new ftp server comp-ftpdmz001
        """
        self.log.info('... create external sync pipeline script .......................................')
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
            src = os.path.join(self.pipeline_definition.env['archive_pipedir'], ftpdir)
            dest = "%s/private/%s/" % (self.ftp_path, ftpdir)
            rsync_log = "%s/rsync_%s.log" % (self.pipeline_definition.env['archive_pipedir'], ftpdir)
            if self.ftp_server:
                cmd = "rsync --verbose --recursive --copy-links --size-only --temp-dir=/processing/.rsync_tmp/ %s/ %s > %s 2>&1; " % (src, dest, rsync_log)
            else:
                # to allow testing without tmp directory
                cmd = "rsync --verbose --recursive --copy-links --size-only %s/ %s > %s 2>&1; " % (src, dest, rsync_log)
            rsync_cmd += cmd
        self.pipeline_definition.env['rsync_cmd'] = rsync_cmd
        utils.create_script(self.pipeline_definition.run_script_path, ftp_rsync_command % self.pipeline_definition.env)

    def run_ftp_rsync_script(self):
        """Run rsync script for external data to new ftp server comp-ftpdmz001
        """
        self.log.info('... run external sync pipeline script ..........................................')
        if os.path.exists(self.pipeline_definition.run_script_path):
            if not os.path.exists(self.pipeline_definition.env['started']):
                if not os.path.exists(self.pipeline_definition.env['lock']):
                    utils.run_bg_process(['sh', '%s' % self.pipeline_definition.run_script_path], self.dry_run)
                else:
                    self.log.info('%s presents - another rsync process is running' % self.pipeline_definition.env['lock'])
            else:
                if not os.path.exists(self.pipeline_definition.env['ended']):
                    if not os.path.exists(self.pipeline_definition.env['failed']):
                        self.log.info('external data is currently being synchronised onto server %s' % self.ftp_server)
                    else:
                        self.log.error('[***FAIL***] rsync for external data onto ftp server %s has failed' % self.ftp_server)
                else:
                    self.log.info('external data has been synchronised onto server %s' % self.ftp_server)
        else:
            self.log.warn('%s is missing' % self.pipeline_definition.run_script_path)

    def register_completion(self):
        """ Create ExternalComplete.txt when external data has been successfully synced
        """
        if os.path.exists(self.pipeline_definition.pipeline_ended) and os.path.exists(self.pipeline_definition.pipeline_started):
            self.run.touch_event(cfg['EXTERNAL_COMPLETED'])
            self.run.copy_event_to_staging(cfg['EXTERNAL_COMPLETED'])
            self.log.info('*** EXTERNAL COMPLETED *********************************************************')
        else:
            # remove ExternalComplete.txt when pipeline not completed and file exists
            self.run.remove_event(cfg['EXTERNAL_COMPLETED'])
            self.run.remove_event_from_staging(cfg['EXTERNAL_COMPLETED'])


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
        self.run = self.runs.runs_to_analyse[0]
        self.log.debug('Testing logging')
        self.pipeline_definition = PipelineDefinition(run=self.run, pipeline_name='test_local')
        self.pipeline_definition.print_header()
        self.pipeline_definition_cluster = PipelineDefinition(run=self.run, pipeline_name='test_lsf', cluster_host='uk-cri-test', use_limsdev=False, mode='lsf')
        self.pipeline_definition_cluster.print_header()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.pipeline_definition.pipeline_directory)
        for run in self.runs.runs_to_analyse:
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
        for run in self.runs.runs_to_analyse:
            shutil.rmtree(run.staging_run_folder)
            shutil.rmtree(run.lustre_run_folder)
            for pipeline_name in Pipelines.PIPELINES.keys():
                pipeline_folder = os.path.join(run.run_folder, pipeline_name)
                if os.path.exists(pipeline_folder):
                    shutil.rmtree(pipeline_folder)
            if run.run_folder_name == '130417_HWI-ST230_1122_C1YH9ACXX' and os.path.exists(run.analysis_completed):
                os.remove(run.analysis_completed)

    def test_execute(self):
        for run in self.runs.runs_to_analyse:
            pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in pipelines.pipeline_definitions.keys():
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))

    def test_execute_without_alignment(self):
        for run in self.runs.runs_to_analyse:
            pipelines = Pipelines(run=run, cluster_host='uk-cri-test', is_alignment_active=False)
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            self.assertFalse(os.path.exists(os.path.join(run.run_folder, 'alignment')))
            for pipeline_name in pipelines.pipeline_definitions.keys():
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
                self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))

    def test_register_completion(self):
        for run in self.runs.runs_to_analyse:
            pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
            self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
            pipelines.execute()
            for pipeline_name in pipelines.pipeline_definitions.keys():
                utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_started)
                utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_ended)
            pipelines.register_completion()
            self.assertTrue(os.path.isfile(pipelines.all_completed))

    def test_execute_only_fastq(self):
        for run in self.runs.runs_to_analyse:
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
        for run in self.runs.runs_to_analyse:
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
        self.assertEqual(1, len(self.runs.runs_to_analyse))
        self.assertEqual(0, len(self.runs.analysed_runs))

    def test_execute(self):
        run = self.runs.runs_to_analyse[0]
        pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in pipelines.pipeline_definitions.keys():
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].pipeline_directory))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].setup_script_path))
            self.assertTrue(os.path.exists(pipelines.pipeline_definitions[pipeline_name].run_script_path))

    def test_register_completion(self):
        run = self.runs.runs_to_analyse[0]
        pipelines = Pipelines(run=run, cluster_host='uk-cri-test')
        self.assertEqual(run.run_folder_name, pipelines.run.run_folder_name)
        pipelines.execute()
        for pipeline_name in pipelines.pipeline_definitions.keys():
            utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_started)
            utils.touch(pipelines.pipeline_definitions[pipeline_name].pipeline_ended)
        pipelines.register_completion()
        self.assertTrue(os.path.isfile(pipelines.all_completed))

    def test_execute_only_fastq(self):
        run = self.runs.runs_to_analyse[0]
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
        for run in self.runs.analysed_runs:
            pipeline_folder = os.path.join(run.run_folder, 'sync')
            if os.path.exists(pipeline_folder):
                shutil.rmtree(pipeline_folder)
            completed = os.path.join(run.run_folder, cfg['SYNC_COMPLETED'])
            if os.path.exists(completed):
                os.remove(completed)
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
            self.assertTrue(os.path.exists(os.path.join(pipeline_folder, cfg['RUN_SCRIPT_FILENAME'])))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, cfg['PIPELINE_STARTED_FILENAME'])))
            self.assertTrue(os.path.isfile(os.path.join(pipeline_folder, cfg['PIPELINE_ENDED_FILENAME'])))
            self.assertTrue(os.path.exists(dest_pipeline_folder))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, cfg['PIPELINE_STARTED_FILENAME'])))
            self.assertTrue(os.path.isfile(os.path.join(dest_pipeline_folder, cfg['PIPELINE_ENDED_FILENAME'])))
            self.assertTrue(os.path.isfile(os.path.join(run.staging_run_folder, cfg['SEQUENCING_COMPLETED'])))
            sync.register_completion()
            self.assertTrue(os.path.isfile(sync.sync_completed))
            self.assertTrue(os.path.isfile(sync.staging_sync_completed))


class ExternalTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing4external/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging4external/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.ftpdir = os.path.join(self.current_path, '../testdata/external')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir)
        self.are_fastq_files_attached = True

    def tearDown(self):
        import shutil
        for run in self.runs.synced_runs:
            pipeline_folder = os.path.join(run.run_folder, 'external')
            if os.path.exists(pipeline_folder):
                shutil.rmtree(pipeline_folder)
            staging_pipeline_folder = os.path.join(run.staging_run_folder, 'external')
            if os.path.exists(staging_pipeline_folder):
                shutil.rmtree(staging_pipeline_folder)
            completed = os.path.join(run.run_folder, cfg['EXTERNAL_COMPLETED'])
            if os.path.exists(completed):
                os.remove(completed)
            staging_completed = os.path.join(run.staging_run_folder, cfg['EXTERNAL_COMPLETED'])
            if os.path.exists(staging_completed):
                os.remove(staging_completed)
            shutil.rmtree(run.lustre_run_folder)
        if os.path.exists(os.path.join(self.ftpdir, 'tmp')):
            for folder in os.listdir(os.path.join(self.ftpdir, 'tmp')):
                shutil.rmtree(os.path.join(self.ftpdir, 'tmp', folder))
        if os.path.exists(os.path.join(self.ftpdir, 'private')):
            for folder in os.listdir(os.path.join(self.ftpdir, 'private')):
                shutil.rmtree(os.path.join(self.ftpdir, 'private', folder))

    def test_execute_non_external(self):
        external_data = {}
        for run in self.runs.synced_runs:
            external = External(run, self.are_fastq_files_attached, external_data, False, None, self.ftpdir)
            external.execute()
            self.assertTrue(os.path.isfile(external.external_completed))

    def test_execute_external(self):
        external_data = {
            2169090L: {'project': '#216', 'ftpdir': 'hutch_vanharanta', 'nonpfdata': 'False', 'runfolder': '/runs/161130_K00252_0085_HGYGKBBXX/fastq/SLX-12650.HGYGKBBXX.s_8.contents.csv'},
            2169091L: {'project': '#216', 'ftpdir': 'hutch_vanharanta', 'nonpfdata': 'False', 'runfolder': '/runs/161130_K00252_0085_HGYGKBBXX/fastq/SLX-12650.NEBNext08.HGYGKBBXX.s_8.r_1.fq.gz'},
            2169092L: {'project': '#216', 'ftpdir': 'hutch_vanharanta', 'nonpfdata': 'False', 'runfolder': '/runs/161130_K00252_0085_HGYGKBBXX/fastq/SLX-12650.NEBNext08.HGYGKBBXX.s_8.r_2.fq.gz'},
        }
        import time
        for run in self.runs.synced_runs:
            external = External(run, True, external_data, False, None, self.ftpdir)
            external.execute()
            time.sleep(10)  # wait for rsync to synchronise files
            external.register_completion()
            self.assertTrue(os.path.isfile(external.external_completed))

if __name__ == '__main__':
    unittest.main()
