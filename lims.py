#!/usr/bin/env python
# encoding: utf-8
"""
lims.py

Created by Anne Pajon on 2012-11-08.
"""

import sys, os, glob
import logging
import unittest
from sqlalchemy.ext.sqlsoup import SqlSoup

# logging definition
log = logging.getLogger('root.lims')

################################################################################
# CONSTANTS
################################################################################
# Database url
DB_URL = "mysql://readonly@uk-cri-lbio04/cri_solexa"
# database urls
DB_HOST = "mysql://readonly@uk-cri-lbio04"
DB_SOLEXA = "%s/cri_solexa" % DB_HOST
DB_LIMS = "%s/cri_lims" % DB_HOST
DB_REQUEST = "%s/cri_request" % DB_HOST
DB_GENERAL = "%s/cri_general" % DB_HOST

# Soap url
SOAP_URL = "http://uk-cri-ldmz02.crnet.org/solexa-ws/SolexaExportBeanWS"

# Default lims status
SEQUENCING_STARTED_STATUS = 'STARTED'
SEQUENCING_COMPLETE_STATUS = 'COMPLETE'
ANALYSIS_READY_STATUS = 'READY'
PRIMARY_ANALYSIS_COMPLETE_STATUS = 'PRIMARY COMPLETE'
ANALYSIS_COMPLETE_STATUS = 'COMPLETE'

################################################################################
# CLASS DEFINITION
################################################################################
class AllRuns(object):
    def __init__(self, _db_url, _run_number=None):
        # CRI lims database connection
        self.solexa_db = SqlSoup(_db_url)
        self.runs = []
        self.filtered_runs = []
        self.__populateRuns(_run_number)

    def __populateRuns(self, _run_number=None):
        # get one run
        if _run_number:
            run = self.findRun(_run_number)
            self.runs.append(run)
        # get all runs
        else:
            runs = self.findAllRuns()
            for run in runs:
                self.runs.append(run)
    
    def filterRuns(self, _run_number, _sequencing_status):
        for run in self.runs:
            # check one run
            if _run_number:
                run = self.findRun(_run_number)
                self.filterCondition(run, _run_number, _sequencing_status)
            # check all runs
            else:
                self.filterCondition(run, _run_number, _sequencing_status)
                        
    def filterCondition(self, _run, _run_number, _sequencing_status):
        pass

    def findRun(self, _run_number=None):
        return self.solexa_db.solexarun.filter_by(runNumber=_run_number).one()
        
    def findAllRuns(self):
        return self.solexa_db.solexarun.all()
        
class StartedRuns(AllRuns):
    def __init__(self, _db_url, _run_number=None):
        super(StartedRuns, self).__init__(_db_url, _run_number)
        self.filterRuns(_run_number, SEQUENCING_STARTED_STATUS)

    def filterCondition(self, _run, _run_number, _status):
        # status could be STARTED or RE-STARTED
        if _status in _run.status:
            self.filtered_runs.append(_run)
            if _run_number:
                log.warning('Run %s is not set to %s, its current status is %s.' % (_run.runNumber, _status, _run.status))
        
class CompleteRuns(AllRuns):
    def __init__(self, _db_url, _run_number=None):
        super(CompleteRuns, self).__init__(_db_url, _run_number)
        self.filterRuns(_run_number, SEQUENCING_COMPLETE_STATUS)

    def filterCondition(self, _run, _run_number, _status):
        if _run.status == _status:
            if _run_number:
                self.filtered_runs.append(_run)
                log.warning('Run %s is not set to %s, its current status is %s.' % (_run.runNumber, _status, _run.status))
            else:
                # select completed runs that have not been analysed
                if not (_run.analysisStatus == 'COMPLETE' or _run.analysisStatus == 'SECONDARY COMPLETE' or _run.analysisStatus == 'ABANDONED'):
                    self.filtered_runs.append(_run)
                    
    def getExternalSampleIds(self, _run):
        samples = {}
        lanes = self.solexa_db.lane.filter_by(run_id=_run.id)
        for lane in lanes:
            # select external lane
            if lane.isControl == 0 and lane.isExternal == 1:
                samples[lane.genomicsSampleId] = lane.institute.lower()
        return samples

class MultiplexedRuns(AllRuns):
    def __init__(self, _db_url=DB_SOLEXA):
        super(MultiplexedRuns, self).__init__(_db_url, None)
        self.filterRuns(None, SEQUENCING_COMPLETE_STATUS)
        # other lims databases
        self.lims_db = SqlSoup(DB_LIMS)
        self.request_db = SqlSoup(DB_REQUEST)
        self.general_db = SqlSoup(DB_GENERAL)
        
    def filterCondition(self, _run, _run_number, _status):
        # select completed runs that have been analysed and are multiplexed
        if _run.status == _status and (_run.analysisStatus == 'COMPLETE' or _run.analysisStatus == 'SECONDARY COMPLETE'):
            if _run.multiplexed == 1:
                self.filtered_runs.append(_run)
            
    def getKnownMultiplexSeqFiles(self, run):
        sequence_files = []
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            # select multiplexed lane
            if lane.isControl == 0 and lane.multiplexing_id != None:
                multiplex_type = self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()
                if multiplex_type.name != 'Other':
                    # select all files for multiplexed lanes of known type
                    file_locations = self.lims_db.analysisfileuri.filter_by(owner_id=lane.sampleProcess_id)
                    for file_location in file_locations:
                        file_type = self.lims_db.analysisfiletype.filter_by(id=file_location.type_id).one()
                        # select only FastQ files 
                        if file_location.scheme == 'FILE' and file_location.role == 'ARCHIVE' and file_type.name == 'FastQ':
                            # select only non-demultiplexed fastQ files
                            if 'Data/Intensities/' in file_location.path or 'primary' in file_location.path:
                                sequence_files.append(file_location)
        return sequence_files

    def getMultiplexTypeFromSeqFile(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        return self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()

    def getLaneFromSeqFile(self, analysisfileuri):
        return self.solexa_db.lane.filter_by(sampleProcess_id=analysisfileuri.owner_id).one()

    def getNewSeqFileName(self, analysisfileuri):
        return "%s.%s.fq.gz" % (self.getSlxSampleId(analysisfileuri), self.getRunLaneRead(analysisfileuri))

    def getIndexFileName(self, analysisfileuri):
        return "index.%s.txt" % self.getRunLaneRead(analysisfileuri)

    def getSlxSampleId(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        return lane.genomicsSampleId

    def getRunLaneRead(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        run = self.solexa_db.solexarun.filter_by(id=lane.run_id).one()
        read_number = self.getReadNumber(analysisfileuri.filename)
        return "%s.s_%s.r_%s" % (run.runNumber, lane.lane, read_number)

    def getReadNumber(self, file_name):
        if 'sequence.txt.gz' in file_name:
            read_number = file_name[file_name.find('s_')+4:file_name.find('_sequence.txt.gz')]
            if read_number == '':
                read_number = '1'
            return read_number
        else:
            log.warning('sequence.txt.gz not found in %s' % file_name)
            return 1

    def printSampleDetails(self, run):
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            # select multiplexed lanes
            if lane.isControl == 0 and lane.multiplexing_id != None:
                # user
                user = self.general_db.user.filter_by(email=lane.userEmail).one()
                username = "%s.%s" % (user.firstname, user.surname)
                # comments
                str_comment = ''
                request_requestfieldvalues = self.request_db.request_requestfieldvalue.filter_by(Request_id=lane.request_id)
                requestfieldtype_comments = self.request_db.requestfieldtype.filter_by(name='Comments').one()
                for request_requestfieldvalue in request_requestfieldvalues:
                    comments = self.request_db.requestfieldvalue.filter_by(id=request_requestfieldvalue.fieldValues_id,type_id=requestfieldtype_comments.id)
                    for comment in comments:
                        str_comment = comment.strValue
                # multiplex type
                multiplex_type = self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()
                if multiplex_type.name == 'Other':
                    multiplex_type_name = "*** %s ***" % multiplex_type.shortName
                else:
                    multiplex_type_name = multiplex_type.shortName

                print ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (multiplex_type_name, run.runNumber, lane.genomicsSampleId, run.deviceType, lane.sequenceType, lane.endType, lane.cycles, lane.userSampleId, username, str_comment ))



################################################################################
# UNIT TESTS
################################################################################
class limsTests(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()