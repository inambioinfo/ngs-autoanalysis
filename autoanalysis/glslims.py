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
import re
import glob
import logging
import unittest
# autoanalysis modules
import utils

# Append root project to PYTHONPATH
ROOT_PROJECT=os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
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
            self.lims_server = LIMS_SERVERS['dev']
        else:
            self.lims_server = LIMS_SERVERS['pro']
        self.glsutil = glsclient.GlsUtil(server=self.lims_server)
        self.log.info('*** CONNECT TO GLS LIMS ********************************************************')
        
    def isSequencingRunComplete(self, run_id):
        # return True if sequencing process at the end of cycle; False if all lanes qc failed; None otherwise
        self.log.info('... check sequencing status ....................................................')
        return self.glsutil.is_sequencing_completed(run_id)
        
    def isFastqFilesFound(self, run_id):
        # return True if all Read 1 FASTQ files from FASTQ Sample Pipeline process are presents; False otherwise
        self.log.info('... check sample fastq files ...................................................')
        return self.glsutil.is_sample_fastq_files_attached(run_id)

    def createAnalysisProcesses(self, flowcell_id):
        """ Create analysis processes in lims only if sequencing run process exists
        and fastq/demux/align do not exist - just single analysis processes per flow-cell
        """
        self.log.info('... create analysis processes ..................................................')
        run = self.glsutil.get_latest_complete_run_process_by_flowcell_id(flowcell_id)
        if run is not None:
            fastq = self.glsutil.get_single_analysis_process_by_flowcell_id('lanfq', flowcell_id)
            if fastq is None:
                self.glsutil.create_fastq_lane_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['lanfq'], flowcell_id))
            demux = self.glsutil.get_single_analysis_process_by_flowcell_id('samfq', flowcell_id)
            if demux is None:
                self.glsutil.create_fastq_sample_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['samfq'], flowcell_id))
            align = self.glsutil.get_single_analysis_process_by_flowcell_id('align', flowcell_id)
            if align is None:
                self.glsutil.create_alignment_pipeline_process(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['align'], flowcell_id))

    def publishFlowCell(self, run):
        self.log.info('... publish flow-cell ..........................................................')
        if self.isFastqFilesFound(run.run_folder_name):
            self.glsutil.assign_flowcell_to_publishing_workflow(run.flowcell_id)
            utils.touch(run.publishing_assigned)
        else:
            self.log.info('No sample fastq files found for run %s' % run.run_folder_name)

    def isExternalData(self, run_id):
        self.log.info('... look for external data .....................................................')
        is_external_data = self.glsutil.is_external_data(run_id)
        if is_external_data:
            self.log.info('external data found')
        else:
            self.log.info('no external data')
        return is_external_data
        
    def findExternalData(self, run_id, is_published=False):
        self.log.info('... find external data files ...................................................')
        data = {}
        labftpdirs = self.glsutil.get_all_external_ftp_dirs()
        files = self.glsutil.get_sample_fastq_files(run_id, is_published)
        if files:
            files.extend(self.glsutil.get_lane_fastq_files(run_id, is_published))
            for f in files:
                if f['labid'] in labftpdirs.keys():
                    data[f['artifactid']] = {'runfolder': f['runfolder'], 'ftpdir': labftpdirs[f['labid']]['ftpdir'], 'project': f['projectname'], 'nonpfdata': labftpdirs[f['labid']]['nonpfdata']}
        if data:
            self.log.info('External data found')
        else:
            self.log.info('No sample external data')
        return data

class GlsLimsTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.flowcell_id = '000000000-A474L'
        self.glslims = GlsLims('limsdev')

    def test_createAnalysisProcesses(self):
        self.glslims.createAnalysisProcesses(self.flowcell_id)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('lanfq', self.flowcell_id)
        self.assertNotEqual(None, process)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('samfq', self.flowcell_id)
        self.assertNotEqual(None, process)
        process = self.glslims.glsutil.get_single_analysis_process_by_flowcell_id('align', self.flowcell_id)
        self.assertNotEqual(None, process)
        
    def test_publishFlowCell(self):
        self.glslims.publishFlowCell(self.flowcell_id)
        
    def test_findExternalData(self):
        self.log.debug('Testing findExternalData')
        data = self.glslims.findExternalData('131231_7001449_0083_C3BW4ACXX')
        self.log.debug(data)


if __name__ == '__main__':
    unittest.main()
    
    
    