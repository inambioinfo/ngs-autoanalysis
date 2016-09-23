#!/usr/bin/env python
# encoding: utf-8
"""
lims.py

$Id$

Created by Anne Pajon on 2012-11-08.
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
from sqlalchemy.ext.sqlsoup import SqlSoup
from suds.client import Client

# logging definition
log = logging.getLogger('auto.lims')

################################################################################
# CONSTANTS
################################################################################
# Default database url
DB_URL = "mysql://readonly@uk-cri-lbio04/cri_solexa"

# Default SOAP url
SOAP_URL = "http://uk-cri-ldmz02.crnet.org/solexa-ws/SolexaExportBeanWS"

# Default lims status
SEQUENCING_STARTED_STATUS = 'STARTED'
SEQUENCING_COMPLETE_STATUS = 'COMPLETE'

################################################################################
# CLASS Lims
################################################################################
class Lims(object):
    
    db_url_pattern = 'mysql://(.*)/(.*)'
    db_url_string = 'mysql://%(host)s/%(db_name)s'
    
    lims_db_name = 'cri_lims'
    request_db_name = 'cri_request'
    general_db_name = 'cri_general'
    
    def __init__(self, _db_url=DB_URL):
        self.db_url = _db_url
        # main solexa database
        self.solexa = SqlSoup(_db_url)
        (self.db_host, self.solexa_db_name) = re.compile(Lims.db_url_pattern).findall(_db_url)[0]
        # other lims databases
        self.lims = SqlSoup(Lims.db_url_string % {'host':self.db_host, 'db_name':Lims.lims_db_name})
        self.request = SqlSoup(Lims.db_url_string % {'host':self.db_host, 'db_name':Lims.request_db_name})
        self.general = SqlSoup(Lims.db_url_string % {'host':self.db_host, 'db_name':Lims.general_db_name})

################################################################################
# CLASS SoapLims
################################################################################
class SoapLims(object):
    
    def __init__(self, _soap_url=SOAP_URL):
        self.soap_url = _soap_url
        # create soap client
        self.client = Client("%s?wsdl" % _soap_url)
        
    def getRun(self, _run_number):
        return self.client.service.getSolexaRunForRunNumber(_run_number, 'true')
        
    def setAnalysisStatus(self, run, status):
        if not run.analysisStatus == status:
            try:
                self.client.service.setAnalysisStatus(run.process_id, status)
                log.info('analysis status in lims set to %s for process id %s' % (status, run.process_id))
            except:
                log.exception('status not update to %s for process id %s' % (status, run.process_id))
                raise
        else:
            log.info('analysis status in lims already set to %s for process id %s' % (status, run.process_id))
    
    def setRunComplete(self, run, status):
        if not run.status == status:
            try:
                self.client.service.setRunComplete(run.process_id)
                log.info('run status in lims set to %s for process id %s' % (status, run.process_id))
            except:
                log.exception('status not update to %s for process id %s' % (status, run.process_id))
                raise
        else:
            log.info('run status in lims already set to %s for process id %s' % (status, run.process_id))
        
################################################################################
# CLASS Runs
################################################################################
class Runs(object):
    def __init__(self, _db_url=DB_URL):
        # CRI lims database connection
        self.lims = Lims(_db_url)

    def findRun(self, _run_number):
        run = self.lims.solexa.solexarun.filter_by(runNumber=_run_number).one()
        log.info('Run %s: status %s and %s; multiplexed %s' % (run.runNumber, run.status, run.analysisStatus, run.multiplexed))
        return run

    def findAllRuns(self, _run_number=None):
        if _run_number:
            return [self.findRun(_run_number)]
        return self.lims.solexa.solexarun.all()
        
    def findAllStartedRuns(self, _run_number=None):
        if _run_number:
            return [self.findRun(_run_number)]
        return self.lims.solexa.solexarun.filter_by(status=SEQUENCING_STARTED_STATUS).all()
        
    def findAllCompletedRuns(self, _run_number=None):
        if _run_number:
            return [self.findRun(_run_number)]
        return self.lims.solexa.solexarun.filter(self.lims.solexa.solexarun.status==SEQUENCING_COMPLETE_STATUS).filter(~self.lims.solexa.solexarun.analysisStatus.in_(['COMPLETE', 'SECONDARY COMPLETE', 'ABANDONED'])).all()
        
    def findExternalSampleIds(self, _run):
        samples = {}
        lanes = self.lims.solexa.lane.filter_by(run_id=_run.id)
        for lane in lanes:
            # select external lane
            if lane.isControl == 0 and lane.isExternal == 1:
                is_multiplexed = False
                if lane.multiplexing_id != None:
                    is_multiplexed = True
                samples[lane.genomicsSampleId] = {'institute' : lane.institute.lower().replace(' ', ''), 'run_number' : _run.runNumber, 'lane_number' : lane.lane, 'is_multiplexed': is_multiplexed}
        return samples

    def findSlxSeqFiles(self, _run, _slx_id):
        sequence_files = []
        lane = self.lims.solexa.lane.filter_by(run_id=_run.id, genomicsSampleId=_slx_id).one()
        if lane.isControl ==0:
            # select all file locations
            file_locations = self.lims.lims.analysisfileuri.filter_by(owner_id=lane.sampleProcess_id)
            for file_location in file_locations:
                file_type = self.lims.lims.analysisfiletype.filter_by(id=file_location.type_id).one()
                # select only FastQ files 
                if file_type.name == 'FastQ':
                    sequence_files.append(file_location)
        return sequence_files


################################################################################
# Unit tests
################################################################################
class limsTests(unittest.TestCase):
    
    def setUp(self):
        self.lims = Lims()
        self.run_number = '1016'
        self.runs = Runs()
        
    def test_database_names(self):
        solexa_db_name = self.lims.solexa.engine.url.database
        lims_db_name = self.lims.lims.engine.url.database
        request_db_name = self.lims.request.engine.url.database
        general_db_name = self.lims.general.engine.url.database
        self.assertEqual(solexa_db_name, self.lims.solexa_db_name)
        self.assertEqual(lims_db_name, self.lims.lims_db_name)
        self.assertEqual(request_db_name, self.lims.request_db_name)
        self.assertEqual(general_db_name, self.lims.general_db_name)
        
    def test_find_run(self):
        run = self.runs.findRun(self.run_number)
        self.assertEqual(str(run.runNumber), self.run_number)
        
    def test_find_all_complete_runs(self):
        for run in self.runs.findAllCompletedRuns():
            self.assertEqual(run.status, 'COMPLETE')
            self.assertNotEqual(run.analysisStatus, 'COMPLETE')
            self.assertNotEqual(run.analysisStatus, 'SECONDARY COMPLETE')
            self.assertNotEqual(run.analysisStatus, 'ABANDONED')
            
    def test_find_external_samples(self):
        run = self.runs.findRun(self.run_number)
        samples = self.runs.findExternalSampleIds(run)
        for sample_id in list(samples.viewkeys()):
            self.assertNotIn(' ', samples[sample_id]['institute'])
            self.assertEqual(str(samples[sample_id]['run_number']), self.run_number)
            
    def test_find_slx_files(self):
        run = self.runs.findRun('1003')
        slx_id = 'SLX-6023'
        seqfiles = self.runs.findSlxSeqFiles(run, slx_id)
        for seqfile in seqfiles:
            self.assertEqual('SLX-6023.1003.s_3.r_1.fq.gz', seqfile.filename)


if __name__ == '__main__':
	unittest.main()
