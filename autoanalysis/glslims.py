#!/usr/bin/env python
# encoding: utf-8
"""
glslims.py

Created by Anne Pajon on 2013-06-05.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import inspect
import logging
import unittest
# import genologics client library
import glsclient.glsclient as glsclient
# import utils module
import utils

# Append root project to PYTHONPATH
ROOT_PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
sys.path.append(ROOT_PROJECT)


class GlsLims:

    def __init__(self, use_dev_lims=True):
        self.log = logging.getLogger(__name__)
        self.lims_server = glsclient.SERVER
        if use_dev_lims:
            self.lims_server = glsclient.TEST_SERVER
        self.glsutil = glsclient.GlsUtil(server=self.lims_server)
        self.log.info('*** CONNECT TO GLS LIMS ********************************************************')

    def is_sequencing_run_complete(self, run_id):
        # return True if sequencing process at the end of cycle; False if all lanes qc failed; None otherwise
        self.log.info('... check sequencing status ....................................................')
        return self.glsutil.is_sequencing_completed(run_id)

    def are_fastq_files_attached(self, run_id):
        # return True if all Read 1 FASTQ files are presents; False otherwise
        self.log.info('... check sample fastq files ...................................................')
        return self.glsutil.are_sample_fastq_files_attached(run_id)

    def create_auto_pipeline_reports_process(self, run_id):
        """ Create auto analysis process in lims only if sequencing run process exists
        and only if it does not exist yet - Only one single auto analysis process per flow-cell
        """
        self.log.info('... create auto-analysis process ...............................................')
        run = self.glsutil.get_completed_run_process_by_run_id(run_id)
        if run:
            auto_analysis_process = self.glsutil.get_process_by_run_id('reports', run_id)
            if not auto_analysis_process:
                self.glsutil.create_reports_process(run_id)
                self.log.info("'%s' process created for run id %s" % (glsclient.PROCESS_NAMES['reports'], run_id))

    def publish_flowcell(self, run, are_files_attached):
        """ Assign flow-cell to publishing queue, if no publishing process found
        and auto analysis process exists - just one single publishing process per flow-cell
        """
        self.log.info('... publish flow-cell ..........................................................')
        if are_files_attached and run.is_analysis_completed_present() and run.is_external_completed_present() and not run.is_publishing_assigned_present():
            try:
                self.glsutil.assign_flowcell_to_publishing_workflow(run.run_folder_name)
                run.touch_publishing_assign()
                run.copy_publishing_assign_to_staging()
                self.log.info('*** PUBLISHING ASSIGNED ********************************************************')
            except Exception, e:
                self.log.error("[***FAIL***] publish flow-cell %s has failed for run %s." % (run.flowcell_id, run.run_folder_name))
                self.log.exception(e)
                raise
        else:
            self.log.info('No fastq files attached or no external data synced yet for run %s' % run.run_folder_name)

    def find_external_data(self, run_id):
        self.log.info('... find external data files ...................................................')
        data = {}
        labftpdirs = self.glsutil.get_all_external_ftp_dirs()
        files = self.glsutil.get_fastq_files(run_id)
        if files:
            for i, f in enumerate(files):
                if f['labid'] in labftpdirs.keys():
                    data[i] = {'runfolder': f['runfolder'], 'ftpdir': labftpdirs[f['labid']]['ftpdir'], 'project': f['projectname'], 'nonpfdata': labftpdirs[f['labid']]['nonpfdata']}
        if data:
            self.log.info('External data found')
        else:
            self.log.info('No external data found')
        return data


class GlsLimsTests(unittest.TestCase):

    def setUp(self):
        import data
        import log as logger
        from autoanalysis.config import cfg
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing4publishing/')
        self.stagingdir = os.path.join(self.current_path, '../testdata/staging4publishing/')
        self.runs = data.RunFolderList(self.basedir, self.stagingdir)
        self.PUBLISHING_ASSIGNED = cfg['PUBLISHING_ASSIGNED']
        self.are_fastq_files_attached = True

        self.glslims = GlsLims(use_dev_lims=True)

    def tearDown(self):
        import shutil
        for run in self.runs.synced_runs:
            completed = os.path.join(run.run_folder, self.PUBLISHING_ASSIGNED)
            if os.path.exists(completed):
                os.remove(completed)
            staging_completed = os.path.join(run.staging_run_folder, self.PUBLISHING_ASSIGNED)
            if os.path.exists(staging_completed):
                os.remove(staging_completed)

    def test_create_auto_pipeline_reports_process(self):
        run_id = '140815_D00408_0163_C4EYLANXX'
        self.glslims.create_auto_pipeline_reports_process(run_id)
        process = self.glslims.glsutil.get_process_by_run_id('reports', run_id)
        self.assertIsNotNone(process)

    def test_publish_flowcell(self):
        for run in self.runs.synced_runs:
            self.log.info(run.flowcell_id)
            self.glslims.publish_flowcell(run, self.are_fastq_files_attached)
            self.assertTrue(os.path.isfile(run.publishing_assigned))
            self.assertTrue(os.path.isfile(os.path.join(run.staging_run_folder, self.PUBLISHING_ASSIGNED)))

    def test_no_publish_flowcell(self):
        for run in self.runs.synced_runs:
            self.log.info(run.flowcell_id)
            self.glslims.publish_flowcell(run, False)
            self.assertFalse(os.path.isfile(run.publishing_assigned))
            self.assertFalse(os.path.isfile(os.path.join(run.staging_run_folder, self.PUBLISHING_ASSIGNED)))

    def test_find_external_data(self):
        # run with external data; fastq files will be removed when archived
        # please test with a run in /staging/ area
        are_fastq_files_attached = self.glslims.are_fastq_files_attached('180530_K00252_0322_HW5TJBBXX')
        self.log.info(are_fastq_files_attached)
        self.assertTrue(are_fastq_files_attached)
        data = self.glslims.find_external_data('180530_K00252_0322_HW5TJBBXX')
        self.log.info(data)
        self.assertIsNotNone(data)

    def test_is_sequencing_run_complete(self):
        self.assertTrue(self.glslims.is_sequencing_run_complete('141022_D00491_0113_C5LTUANXX'))
        self.assertTrue(self.glslims.is_sequencing_run_complete('141022_M01686_0146_000000000-AAYM1'))

    def test_are_fastq_files_attached(self):
        self.assertTrue(self.glslims.are_fastq_files_attached('161123_M01712_0338_000000000-AWR96'))

if __name__ == '__main__':
    unittest.main()
