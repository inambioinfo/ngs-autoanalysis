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
    
    def __init__(self, use_dev_lims=True):
        self.log = logging.getLogger(__name__)
        if use_dev_lims:
            self.lims_server = LIMS_SERVERS['dev']
        else:
            self.lims_server = LIMS_SERVERS['pro']
        self.glsutil = glsclient.GlsUtil(server=self.lims_server)
        self.log.info('*** CONNECT TO GLS LIMS ********************************************************')
        
    def isSequencingRunComplete(self, run_id):
        # return False if all lanes marked FAILED; True if some lanes PASSED; None otherwise
        self.log.info('... check sequencing status ....................................................')
        return self.glsutil.isSequencingCompleted(run_id)
        
    def isAllFastqFilesFound(self, run_id):
        # return True if all Read 1 FASTQ files from fastq and demux processes are presents; False otherwise
        self.log.info('... check fastq files ..........................................................')
        return self.glsutil.isFastqPipelineComplete(run_id) and self.glsutil.isDemuxPipelineComplete(run_id)

    def isPrimaryFastqFilesFound(self, run_id):
        # return True if all Read 1 FASTQ files from fastq and demux processes are presents; False otherwise
        self.log.info('... check primary fastq files ..................................................')
        return self.glsutil.isFastqPipelineComplete(run_id)

    def createAnalysisProcesses(self, flowcell_id):
        """ Create analysis processes in lims only if sequencing run process exists
        and fastq/demux/align do not exist - just single analysis processes per flow-cell
        """
        self.log.info('... create analysis processes ..................................................')
        run = self.glsutil.getLatestCompleteRunProcessByFlowcellId(flowcell_id)
        if run is not None:
            fastq = self.glsutil.getSingleAnalysisProcessByFlowcellId('fastq', flowcell_id)
            if fastq is None:
                self.glsutil.createBclToFastqPipelineProcess(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['fastq'], flowcell_id))
            demux = self.glsutil.getSingleAnalysisProcessByFlowcellId('demux', flowcell_id)
            if demux is None:
                self.glsutil.createDemuxPipelineProcess(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['demux'], flowcell_id))
            align = self.glsutil.getSingleAnalysisProcessByFlowcellId('align', flowcell_id)
            if align is None:
                self.glsutil.createAlignmentPipelineProcess(flowcell_id)
                self.log.info("'%s' process created for flow-cell id %s" % (glsclient.ANALYSIS_PROCESS_NAMES['align'], flowcell_id))

    def publishFlowCell(self, run, dry_run=True):
        self.log.info('... publish flow-cell ..........................................................')
        if self.isPrimaryFastqFilesFound(run.run_folder_name):
            self.glsutil.assignFlowcellToPublishingWorkflow(run.flowcell_id)
            self.updateSampleProgressStatusToPublishingUnderway(run.flowcell_id)
            utils.touch(self.sync_completed, dry_run)
        else:
            self.log.info('No primary fastq files found for run %s' % run_id)
        
    def updateSampleProgressStatusToAnalysisUnderway(self, flowcell_id):
        """ Notify lims by updating Progress status UDF on samples to 'Analysis Underway'
        """
        self.log.info('... update sample progress status ..............................................')
        self.glsutil.updateFlowcellSamplesProgressStatus(flowcell_id, glsclient.ANALYSIS_UNDERWAY)
        
    def updateSampleProgressStatusToPublishingUnderway(self, flowcell_id):
        """ Notify lims by updating Progress status UDF on samples to 'Publishing Underway'
        """
        self.log.info('... update sample progress status ..............................................')
        self.glsutil.updateFlowcellSamplesProgressStatus(flowcell_id, glsclient.PUBLISHING_UNDERWAY)
        
    def findExternalData(self, run_id):
        self.log.info('... look for external data .....................................................')
        data = {}
        fastq_files = self.glsutil.getRawFastqFiles(run_id)
        for raw in fastq_files:
            ftpdirs = self.glsutil.getFtpDirFromArtifactId(raw.artifactid)
            if ftpdirs:
                data[raw.artifactid] = {'from_contenturi': raw.contenturi, 'to_ftpdirs': []}
                for ftpdir in ftpdirs:
                    data[raw.artifactid]['to_ftpdirs'].append(ftpdir.ftpdir)
        if data:
            self.log.info('External data found')
        else:
            self.log.info('No external data')
        return data

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
    
    
    