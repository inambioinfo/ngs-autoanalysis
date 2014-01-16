#!/usr/bin/env python
# encoding: utf-8
"""
glsextapi.py

Created by Anne Pajon on 2013-05-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import logging
import datetime

import glsclient
import glssql

"""
Important:
----------
1) Get all samples that have become available in the last N hours:
  a) email address,
  b) user sample ID,
  c) unique ID of lane for use in query 2.
2) Get Fastq location for sample from query 1.

Useful:
-------
3) Retrieve location of other sorts of files/data for a sample.
4) Get all samples with status "complete" (for auditing DB).

Would be nice:
--------------
5) Submit sample sheet.
6) Get demultiplexed files.
7) Retrieve all metadata about a flow cell, sample or lane.
8) Retrieve all lanes for a given LIMS sample ID, or user sample ID.
"""

"""
Data Types
----------
flowcellid - human-readable (more or less) string of characters, as in the outgoing LIMS, e.g. "D214AACXX" (unique, at least for status="complete")
laneid - number of flow cell lane (1-8, at least so far)
sampleid - internal LIMS id for a sample (unique)
runid - internal LIMS id for a run (unique)
samplename - user-provided text name of a sample (e.g. "jc1010") (not unique)
slxid - human-readable name of a tube containing sample(s) (unique)
groupname - human-readable name of a group (e.g. "JCLAB") (unique)
status - human-readable text name for a process status
time - date and time, in some suitable format
barcode - name of a particular index sequence

"""

class GlsExtApi(object):
    
    def __init__(self):
        self.log = logging.getLogger(__name__)    
        self.glsutil = glsclient.GlsUtil('lims')
    
    ### PRIORITY BEGIN
    
    def getRunsByStatus(self, modifiedafter, modifiedbefore=datetime.date.today()):
        """Provides runs changed since some date (and optionally before some date)
        [remove status from the method's signature]
        Returns a list of Runs including flowcellid, lastmodified        
        """
        query = glssql.RUNPROCESS_BY_MODIFIEDDATE_QUERY % {'begin_date':modifiedafter, 'end_date':modifiedbefore}
        self.log.debug(query)
        results = self.glsutil.db.execute(query).fetchall()
        processes = []
        for process in results:
            dprocess = {'luid': process.luid, 'name': process.displayname, 'createddate': str(process.createddate), 'daterun': str(process.daterun), 
            'finishdate':str(process.finishdate), 'lastmodifieddate':str(process.lastmodifieddate), 'flowcellid': process.flowcellid, 'status': process.status,
            'runfolder':process.runfolder, 'read1':process.read1, 'indexread1':process.indexread1, 'indexread2':process.indexread2, 'read2':process.read2}
            processes.append(dprocess)
        self.log.debug(processes)
        return {'runs_lastmodifieddate_begin': str(modifiedafter), 'runs_lastmodifieddate_end': str(modifiedbefore), 'runs': processes}
    
    def getLanesByFlowcell(self, flowcellid, status='COMPLETE'):
        """Provides information about a flow cell.
        Assumption: there is only one run for any given flow cell with status="complete" (or "published").
        This has been true historically (aside from errors).  Can we still assume it?
        Returns:
            For each run: status, lastmodified
              For each lane (by run): laneid, slxid, status
                For each sample (by lane): sampleid, samplename, barcode, owner email
        """
        pass
    
    def getFileLocations(self, filetype, flowcellid, laneid, sampleid):
        """Returns location of unique files for this sample and flowcell.
        Possible types are RAW-FASTQ, RAW-FASTQ-MD5, MGA, FASTQC, BARCODE-SUMMARY, FASTQ, FASTQ-MD5, BAM, BIGWIG, BAM-MD5
        May provide 2 FASTQ files, for PE lanes.
        """
        pass
    
    def getSampleIdsByGroup(self, groupname, modifiedafter, status='GOOD'):
        """Provides samples for the named group, that have been updated (i.e. sample
        status changed for some run associated with this sample) since the
        time given.  If necessary, we could do without the "groupname", and just
        ask by status and lastChangedAfter.  Or do without the lastChangedAfter
        but keep the group (not preferable).
        Returns just a list of sampleids.
        """
        pass
    
    def getAllLanes(self, sampleid, modifiedafter):
        """Returns list of lanes for a sample, including:
        flowcellid; laneid; slxid; status; runid
        """
        pass
    
    ### PRIORITY END
    
    def getSamplesBySlxId(self, slxid):
        """Return list of samples for a slx-id
        Pooled multiplexed library will return a list of its sub-samples
        """
        pass
    
    def getNumberOfLanes(self, sampleid):
        """Return number of lanes a sample is going to be sequenced on
        """


class GlsExtApiTest(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.extapi = GlsExtApi()
    
    def test_getRunsByStatus(self):
        afterdate = '2013-07-01'
        enddate = '2013-07-17'
        self.log.debug(datetime.date.today())
        self.log.debug(afterdate)
        self.log.debug(enddate)
        results = self.extapi.getRunsByStatus(afterdate, enddate)
        self.log.debug(results)
        self.assertEqual(30, len(results))
        results = self.extapi.getRunsByStatus(afterdate)
        self.log.debug(results)
        self.assertIsNotNone(results)


if __name__ == '__main__':
    unittest.main()
