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
import re
import glob
import logging
import unittest

# autoanalysis modules
import utils

# genologics client
import glsclient

################################################################################
# CONSTANTS
################################################################################
# genologics lims servers
LIMS_SERVERS = {
    "dev": "limsdev",
    "pro": "lims"
}

class GlsLims:
    
    def __init__(self, lims_server=LIMS_SERVERS['dev']):
        self.log = logging.getLogger(__name__)
        self.lims_server = lims_server
        self.glsutil = glsclient.GlsUtil(server=self.lims_server)

    def createAnalysisProcesses(self, flowcell_id):
        """ Create analysis processes in lims only if sequencing run process exists
        and fastq/demux/align do not exist - just single analysis processes per flow-cell
        """
        run = self.glsutil.getLatestRunProcessByFlowcellId(flowcell_id)
        if run is not None:
            fastq = self.glsutil.getSingleAnalysisProcessByFlowcellId('fastq', flowcell_id)
            if fastq is None:
                self.glsutil.createBclToFastqPipelineProcess(flowcell_id)
                self.log.debug("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['fastq'], flowcell_id))
            demux = self.glsutil.getSingleAnalysisProcessByFlowcellId('demux', flowcell_id)
            if demux is None:
                self.glsutil.createDemuxPipelineProcess(flowcell_id)
                self.log.debug("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['demux'], flowcell_id))
            align = self.glsutil.getSingleAnalysisProcessByFlowcellId('align', flowcell_id)
            if align is None:
                self.glsutil.createAlignmentPipelineProcess(flowcell_id)
                self.log.debug("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['align'], flowcell_id))

    def publishFlowCell(self, flowcell_id):
        self.glsutil.assignFlowcellToBioAnalysesWorkflow(flowcell_id)
        
    def updateSampleProgressStatus(self):
        # notify lims by updating progress status UDF on samples to 'Analysis Underway'
        pass

class GlsLimsTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.flowcell_id = '000000000-A474L'
        self.glslims = GlsLims()

    def test_getSamplesByUser(self):
        self.log.debug('Testing logging')
        self.assertIsNotNone(self.glslims.glsutil.getSamplesByUser('sarah.moffatt@cruk.cam.ac.uk'))
        
    def test_createAnalysisProcesses(self):
        self.glslims.createAnalysisProcesses(self.flowcell_id)
        process = self.glslims.glsutil.getSingleAnalysisProcessByFlowcellId('fastq', self.flowcell_id)
        self.assertNotEqual(None, process)
        process = self.glslims.glsutil.getSingleAnalysisProcessByFlowcellId('demux', self.flowcell_id)
        self.assertNotEqual(None, process)
        process = self.glslims.glsutil.getSingleAnalysisProcessByFlowcellId('align', self.flowcell_id)
        self.assertNotEqual(None, process)
        
    def test_publishFlowCell(self):
        self.glslims.publishFlowCell(self.flowcell_id)



if __name__ == '__main__':
    unittest.main()
    
    
    