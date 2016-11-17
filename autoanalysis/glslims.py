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
# autoanalysis modules
import utils

# Append root project to PYTHONPATH
ROOT_PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
sys.path.append(ROOT_PROJECT)

# import genologics client
import glsclient.glsclient as glsclient

################################################################################
# CONSTANTS
################################################################################
# genologics lims servers
LIMS_SERVERS = {
    "dev": "limsdev",
    "pro": "lims"
}


class GlsLims:

    def __init__(self, use_dev_lims=True):
        self.log = logging.getLogger(__name__)
        if use_dev_lims:
            self.lims_server = glsclient.TEST_SERVER
        else:
            self.lims_server = glsclient.SERVER
        self.glsutil = glsclient.GlsUtil(server=self.lims_server)
        self.log.info('*** CONNECT TO GLS LIMS ********************************************************')

    def is_sequencing_run_complete(self, run_id):
        # return True if sequencing process at the end of cycle; False if all lanes qc failed; None otherwise
        self.log.info('... check sequencing status ....................................................')
        return self.glsutil.is_sequencing_completed(run_id)

    def are_fastq_files_attached(self, run_id):
        # return True if all Read 1 FASTQ files from FASTQ Sample Pipeline process are presents; False otherwise
        self.log.info('... check sample fastq files ...................................................')
        return self.glsutil.are_sample_fastq_files_attached(run_id)

    def is_alignment_active(self, run_id):
        # return True if passed QC, not external and project core supported or auto alignment lab
        self.log.info('... check alignment status .....................................................')
        return self.glsutil.is_alignment_active(run_id)

    def create_analysis_processes(self, flowcell_id, is_alignment_active):
        """ Create analysis processes in lims only if sequencing run process exists
        and lane & sample fastq & alignment do not exist - just one single analysis processes per flow-cell
        do only create alignment process when ii is active
        """
        self.log.info('... create analysis processes ..................................................')
        run = self.glsutil.get_latest_complete_run_process_by_flowcell_id(flowcell_id)
        if run is not None:
            lanfq = self.glsutil.get_single_analysis_process_by_flowcell_id('lanfq', flowcell_id)
            if lanfq is None:
                self.glsutil.create_fastq_lane_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['lanfq'], flowcell_id))
            samfq = self.glsutil.get_single_analysis_process_by_flowcell_id('samfq', flowcell_id)
            if samfq is None:
                self.glsutil.create_fastq_sample_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['samfq'], flowcell_id))
            align = self.glsutil.get_single_analysis_process_by_flowcell_id('align', flowcell_id)
            if align is None and is_alignment_active:
                self.glsutil.create_alignment_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['align'], flowcell_id))

    def publish_flowcell(self, run, are_files_attached):
        """ Assign flow-cell to publishing queue, if no publishing process found
        and lane & sample fastq & alignment processes exist - just one single publishing process per flow-cell
        """
        self.log.info('... publish flow-cell ..........................................................')
        if are_files_attached and run.is_analysis_completed_present() and run.is_external_completed_present() and not run.is_publishing_assigned_present():
            try:
                self.glsutil.assign_flowcell_to_publishing_workflow(run.flowcell_id)
                run.touch_publishing_assign()
                run.copy_publishing_assign_to_staging()
                self.log.info('*** PUBLISHING ASSIGNED ********************************************************')
            except Exception, e:
                self.log.error("[***FAIL***] publish flow-cell %s has failed." % run.flowcell_id)
                self.log.exception(e)
                raise
        else:
            self.log.info('No fastq files attached or no external data synced yet for run %s' % run.run_folder_name)

    def find_external_data(self, run_id):
        self.log.info('... find external data files ...................................................')
        data = {}
        labftpdirs = self.glsutil.get_all_external_ftp_dirs()
        files = self.glsutil.get_sample_fastq_files(run_id)
        if files:
            files.extend(self.glsutil.get_lane_fastq_files(run_id))
            for f in files:
                if f['labid'] in labftpdirs.keys():
                    data[f['artifactid']] = {'runfolder': f['runfolder'], 'ftpdir': labftpdirs[f['labid']]['ftpdir'], 'project': f['projectname'], 'nonpfdata': labftpdirs[f['labid']]['nonpfdata']}
        if data:
            self.log.info('External data found')
        else:
            self.log.info('No external data found')
        return data


class GlsLimsTests(unittest.TestCase):

    def setUp(self):
        import data
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing4publishing/')
        self.archivedir = os.path.join(self.current_path, '../testdata/staging4publishing/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = data.RunFolderList(self.basedir, self.archivedir, self.lustredir)
        self.PUBLISHING_ASSIGNED = data.PUBLISHING_ASSIGNED
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
            shutil.rmtree(run.lustre_run_folder)

    def test_create_analysis_processes(self):
        flowcell_id = 'H9VT6ADXX' # 140729_D00408_0159_H9VT6ADXX
        self.glslims.create_analysis_processes(flowcell_id, True)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('lanfq', flowcell_id)
        self.assertIsNotNone(process)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('samfq', flowcell_id)
        self.assertIsNotNone(process)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('align', flowcell_id)
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
        are_fastq_files_attached = self.glslims.are_fastq_files_attached('140813_M01712_0104_000000000-A9YBB')
        self.log.info(are_fastq_files_attached)
        #self.assertTrue(are_fastq_files_attached)  # no file attached in lims
        data = self.glslims.find_external_data('140813_M01712_0104_000000000-A9YBB')
        self.log.info(data)
        self.assertIsNotNone(data)

    def test_is_alignment_active(self):
        self.assertTrue(self.glslims.is_alignment_active('140815_D00408_0163_C4EYLANXX'))
        self.assertFalse(self.glslims.is_alignment_active('140813_M01712_0104_000000000-A9YBB'))

    def test_is_sequencing_run_complete(self):
        self.assertTrue(self.glslims.is_sequencing_run_complete('141022_D00491_0113_C5LTUANXX'))
        self.assertTrue(self.glslims.is_sequencing_run_complete('141022_M01686_0146_000000000-AAYM1'))



if __name__ == '__main__':
    unittest.main()
