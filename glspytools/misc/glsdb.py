#!/usr/bin/env python
# encoding: utf-8
"""
db_query.py

Created by Anne Pajon on 2013-01-31.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import logging
from sqlalchemy.ext.sqlsoup import SqlSoup

# logging definition
import log as logger
log = logging.getLogger('root.glsdb')

# Database url
DB_URL = "postgres://readonly:readonly@lims/clarityDB"

### run notifier
get_new_query = """
select solexarun.id,flowcellId,runNumber,status,analysisStatus,lastUpdate
  from solexarun,flowcell
 where solexarun.flowcell_id = flowcell.id
   and lastUpdate > now() - INTERVAL 6 HOUR
   and analysisStatus in ('COMPLETE','PRIMARY COMPLETE','SECONDARY COMPLETE')
"""

get_lane_query = """
select id,lane,institute,userSampleId,genomicsSampleId,userEmail,experimentType,isControl,sampleProcess_id
  from lane
 where run_id = %s
"""

check_files_query = """
select count(*) as cnt
  from analysisfileuri
 where owner_id = %s
   and type_id = %s
"""

"""
mysql> desc solexarun;
+----------------+--------------+------+-----+-------------------+-------+
| Field          | Type         | Null | Key | Default           | Extra |
+----------------+--------------+------+-----+-------------------+-------+
| id             | bigint(20)   | NO   | PRI | NULL              |       | 
| optLockVersion | int(11)      | NO   |     | NULL              |       | 
| lastUpdate     | timestamp    | NO   |     | CURRENT_TIMESTAMP |       | 
| process_id     | bigint(20)   | YES  |     | NULL              |       | 
| flowcell_id    | bigint(20)   | NO   | MUL | NULL              |       | 
| instrument     | varchar(64)  | NO   |     | NULL              |       | 
| startDate      | datetime     | NO   |     | NULL              |       | 
| status         | varchar(16)  | NO   |     | NULL              |       | 
| cycles         | int(3)       | NO   |     | NULL              |       | 
| multiplexed    | tinyint(1)   | NO   |     | 0                 |       | 
| currentCycle   | int(3)       | YES  |     | NULL              |       | 
| currentLane    | int(1)       | YES  |     | NULL              |       | 
| pipelinePath   | varchar(255) | YES  |     | NULL              |       | 
| endType        | varchar(32)  | NO   |     | NULL              |       | 
| comments       | varchar(255) | YES  |     | NULL              |       | 
| runNumber      | int(6)       | NO   |     | 0                 |       | 
| endDate        | datetime     | YES  |     | NULL              |       | 
| analysisStatus | varchar(32)  | YES  |     | NULL              |       | 
| deviceType     | varchar(16)  | NO   |     | GAIIx             |       | 
| indexCycles    | int(3)       | YES  |     | 0                 |       | 
+----------------+--------------+------+-----+-------------------+-------+

mysql> desc lane;
+--------------------+--------------+------+-----+-------------------+-------+
| Field              | Type         | Null | Key | Default           | Extra |
+--------------------+--------------+------+-----+-------------------+-------+
| id                 | bigint(20)   | NO   | PRI | NULL              |       | 
| optLockVersion     | int(11)      | NO   |     | NULL              |       | 
| lastUpdate         | timestamp    | NO   |     | CURRENT_TIMESTAMP |       | 
| run_id             | bigint(20)   | NO   | MUL | NULL              |       | 
| userSampleId       | varchar(255) | YES  |     | NULL              |       | 
| genomicsSampleId   | varchar(64)  | NO   |     | NULL              |       | 
| userEmail          | varchar(64)  | NO   |     | NULL              |       | 
| project            | varchar(255) | YES  |     | NULL              |       | 
| genome             | varchar(64)  | NO   |     | NULL              |       | 
| endType            | varchar(32)  | NO   |     | NULL              |       | 
| sequenceType       | varchar(16)  | NO   |     | NULL              |       | 
| cycles             | int(3)       | NO   |     | NULL              |       | 
| lane               | int(2)       | NO   |     | NULL              |       | 
| institute          | varchar(64)  | NO   |     | NULL              |       | 
| isCRUK             | tinyint(1)   | NO   |     | 1                 |       | 
| request_id         | bigint(20)   | YES  |     | NULL              |       | 
| experimentType     | varchar(32)  | NO   |     | NULL              |       | 
| isControl          | tinyint(1)   | NO   |     | 0                 |       | 
| comments           | varchar(255) | YES  |     | NULL              |       | 
| dateSent           | datetime     | YES  |     | NULL              |       | 
| sampleProcess_id   | bigint(20)   | NO   |     | NULL              |       | 
| sample_id          | bigint(20)   | YES  |     | NULL              |       | 
| isExternal         | tinyint(1)   | NO   |     | 0                 |       | 
| indexReads         | smallint(6)  | NO   |     | 0                 |       | 
| multiplexing_id    | bigint(20)   | YES  | MUL | NULL              |       | 
| referenceGenome_id | bigint(20)   | YES  | MUL | NULL              |       | 
+--------------------+--------------+------+-----+-------------------+-------+

"""

class GlsDb(object):
    
    def __init__(self, _db_url=DB_URL):
        self.db_url = _db_url
        self.db = SqlSoup(self.db_url)
        
    def getSamplesByUser(self, _email):
        query = """
        SELECT 
            sample.projectid, 
            sample.sampleid, 
            artifact.luid, 
            sample.name, 
            sample.datereceived, 
            sample.datecompleted, 
            sample.maximumanalyteid, 
            sample.bisourceid, 
            sample.processid
        FROM sample, project, researcher, artifact, artifact_sample_map
        WHERE sample.projectid = project.projectid
        AND project.researcherid = researcher.researcherid
        AND researcher.email = '%s' 
        AND artifact_sample_map.processid = sample.processid
        AND artifact_sample_map.artifactid = artifact.artifactid
        ORDER BY project.name
        """
        udf_query = """
        SELECT udfname as key, udfvalue as value
        FROM sample_udf_view
        WHERE sampleid = %s
        """
        results = self.db.execute(query % _email).fetchall()
        samples = []
        for sample in results:
            dsample = {'projectid': sample.projectid, 'sampleid': sample.sampleid, 'luid': sample.luid, 'name': sample.name, 'datereceived': sample.datereceived, 'datecompleted': sample.datecompleted}
            sample_udfs = self.db.execute(udf_query % sample.sampleid).fetchall()
            for udf in sample_udfs:
                dsample[udf.key] = udf.value
            samples.append(dsample)
        log.debug(samples)
        return samples
        
    def getSampleIdsBySlxId(self, _slxid):
        query = """
        SELECT sampleid
        FROM sample_udf_view
        WHERE udfname = 'SLX Identifier'
        AND udfvalue = '%s'
        """
        results = self.db.execute(query % _slxid).fetchall()
        sampleids = []
        for sample in results:
            sampleids.append(sample.sampleid)
        log.debug(sampleids)
        return sampleids
        
    def getSlxIdBySampleId(self, _sampleid):
        query = """
        SELECT DISTINCT(udfvalue) as slxid
        FROM sample_udf_view 
        WHERE udfname = 'SLX Identifier'
        AND sampleid = %s 
        """
        results = self.db.execute(query % _sampleid).fetchall()
        if len(results) > 1:
            raise Exception('More than one SLX-ID per sample id %s' % _sampleid)
        log.debug(results[0].slxid)
        return results[0].slxid
        
    def getRunProcessesBySampleId(self, _sampleid):
        query = """
        SELECT process.processid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate
        FROM process, processtype, processiotracker, artifact, artifact_sample_map, sample
        WHERE process.typeid = processtype.typeid
        AND processiotracker.processid = process.processid
        AND processiotracker.inputartifactid = artifact.artifactid
        AND artifact_sample_map.artifactid = artifact.artifactid
        AND artifact_sample_map.processid = sample.processid
        AND processtype.displayname LIKE '%%Run%%'
        AND sample.sampleid = %s
        """
        udf_query = """
        SELECT udfname as key, udfvalue as value
        FROM process_udf_view
        WHERE processid = %s
        """
        results = self.db.execute(query % _sampleid).fetchall()
        runs = []
        for run in results:
            drun = {'processid': run.processid, 'daterun': run.daterun, 'name': run.displayname, 'status': run.workstatus, 'datecreated': run.createddate, 'datemodified': run.lastmodifieddate}
            run_udfs = self.db.execute(udf_query % run.processid).fetchall()
            for udf in run_udfs:
                drun[udf.key] = udf.value
            runs.append(drun)
        log.debug(runs)
        return runs
        
    def getAllUdfNamesByProcessName(self, _process_name):
        query = """
        SELECT 
            processtype.displayname,
            udf.name, 
            udf.isvisible
        FROM processtype, classindex, udf
            WHERE classindex.classname = 'ConfiguredProcess'
            AND processtype.typename = 'ConfiguredProcess'
            AND udf.attachtoclassid = classindex.classindexid
            AND udf.attachtosubtypeid = processtype.typeid
            AND processtype.displayname like '%%s%'
        ORDER BY processtype.displayname
        """
        results = self.db.execute(query).fetchall()
        log.debug(results)
        return results
    

def old_main():
    
    print "----------"
    get_file_by_sampleid = """
    SELECT
        glsfile.fileid,
        glsfile.contenturi,
        glsfile.server,
        sample.sampleid
    FROM glsfile, sample, classindex
    WHERE glsfile.attachtoid = sample.sampleid
    AND glsfile.attachtoclassid = classindex.classindexid
    AND classindex.tablename='sample'
    AND sample.sampleid = %s
    """
    # http://lims.cri.camres.org:8080/lablink/secure/DownloadFile.do?id=46151
    files = DB.execute(get_file_by_sampleid % '35317').fetchall()
    for f in files:
        print f.fileid, f.contenturi, f.server, f.sampleid

                  
class GlsDbTest(unittest.TestCase):

	def setUp(self):
	    log = logger.set_custom_logger()
	    log.setLevel(logging.DEBUG)
	    self.glsdb = GlsDb()
	    
	def test_getSamplesByUser(self):
	    self.assertIsNotNone(self.glsdb.getSamplesByUser('sarah.moffatt@cruk.cam.ac.uk'))
	    
	def test_getSampleIdsBySlxId(self):
	    self.assertIsNotNone(self.glsdb.getSampleIdsBySlxId('SLX-1661'))
	    
	def test_getSlxIdBySampleId(self):
	    self.assertIsNotNone(self.glsdb.getSlxIdBySampleId('16903'))
	    
	def test_getRunProcessesBySampleId(self):
	    self.assertIsNotNone(self.glsdb.getRunProcessesBySampleId('16903'))
	    
	def test_getAllUdfNamesByProcessName(self):
	    self.assertIsNotNone(self.glsdb.getAllUdfNamesByProcessName('MiSeq Run'))


if __name__ == '__main__':
	unittest.main()

