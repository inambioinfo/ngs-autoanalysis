#!/usr/bin/env python
# encoding: utf-8
"""
runfolders.py

$Id$

Created by Anne Pajon on 2013-03-19.
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

################################################################################
# CONSTANTS
################################################################################

RUNFOLDER_GLOB = "%s/??????_*_*_*"
ONERUNFOLDER_GLOB = "%s/%s"
SEQUENCING_COMPLETED = 'Sequencing.completed'
SEQUENCING_FAILED = 'Sequencing.failed'
SYNC_COMPLETED = 'Sync.completed'
SYNC_FAILED = 'Sync.failed'
ANALYSIS_COMPLETED = "Analysis.completed"
ANALYSIS_IGNORE = 'analysis.ignore'
DONT_DELETE = 'dont.delete'
PUBLISHING_ASSIGNED = 'Publishing.assigned'
PUBLISHING_COMPLETED = 'Publishing.completed'

RSYNC_FOLDER = "rsync"
RSYNC_STARTED = "rsync.started"
RSYNC_ENDED = "rsync.ended"
RSYNC_FAILED = "rsync.failed"


RUN_HEADER = """
================================================================================
=== RUN: %(run_folder)s
================================================================================"""

################################################################################
# CLASSES
################################################################################
        
class RunFolders(object):
    def __init__(self, basedir, destdir, one_run_folder=None, do_create_destdirs=True): # destdir
        self.log = logging.getLogger(__name__) 
        self.do_create_destdirs = do_create_destdirs
        self.basedir = basedir
        self.destdir = destdir
        self.one_run_folder = one_run_folder
        if self.one_run_folder:
            self.run_folders = glob.glob(ONERUNFOLDER_GLOB % (self.basedir, self.one_run_folder))
        else:
            self.run_folders =  glob.glob(RUNFOLDER_GLOB % self.basedir)
        self.completed_runs = self.getCompletedRuns()
        self.analysed_runs = self.getAnalysedRuns()
        self.published_runs = self.getPublishedRuns()
        self.dest_run_folders = self.getDestinationRunFolders()
        
    def getAllRuns(self):
        runs = []
        for run_folder in self.run_folders:
            self.log.debug(run_folder)
            run = RunDefinition(run_folder, self.destdir, self.do_create_destdirs)
            runs.append(run)
        return runs
        
    def getCompletedRuns(self):
        completed_runs = []
        for run_folder in self.run_folders:
            run = RunDefinition(run_folder, self.destdir, self.do_create_destdirs)
            if run.isCompleted():
                completed_runs.append(run)
        return completed_runs
    
    #completed_runs = property(getCompletedRuns)
    
    def getAnalysedRuns(self):
        analysed_runs = []
        for run in self.completed_runs:
            if run.isAnalysisCompletedPresent():
                analysed_runs.append(run)
        return analysed_runs
        
    def getPublishedRuns(self):
        published_runs = []
        for run in self.completed_runs:
            if run.isAnalysisCompletedPresent() and run.isPublished():
                published_runs.append(run)
        return published_runs

    def getDestinationRunFolders(self):
        if self.one_run_folder:
            return glob.glob(ONERUNFOLDER_GLOB % (self.destdir, self.one_run_folder))
        return glob.glob(RUNFOLDER_GLOB % self.destdir)
        
class RunDefinition(object):
    def __init__(self, run_folder, destdir=None, do_create_destdir=True):
        self.log = logging.getLogger(__name__) 
        self.do_create_destdir = do_create_destdir
        self.run_folder = run_folder
        self.destdir = destdir
        self.run_folder_name = os.path.basename(self.run_folder)
        self.start_date = self.run_folder_name.split('_')[0]
        self.instrument = self.run_folder_name.split('_')[1]
        self.run_number = self.run_folder_name.split('_')[2]
        self.flowcell_id = self.run_folder_name.split('_')[-1]
        # TODO add reagent cartridge ID from runParameter.xml
        self.run_uid = '%s_%s' % (self.start_date, self.flowcell_id)
        self.sequencing_completed = os.path.join(self.run_folder, SEQUENCING_COMPLETED)
        self.sequencing_failed = os.path.join(self.run_folder, SEQUENCING_FAILED)
        self.sync_completed = os.path.join(self.run_folder, SYNC_COMPLETED)
        self.sync_failed = os.path.join(self.run_folder, SYNC_FAILED)
        self.analysis_completed = os.path.join(self.run_folder, ANALYSIS_COMPLETED)
        self.analysis_ignore = os.path.join(self.run_folder, ANALYSIS_IGNORE)
        self.publishing_assigned = os.path.join(self.run_folder, PUBLISHING_ASSIGNED)
        self.publishing_completed = os.path.join(self.run_folder, PUBLISHING_COMPLETED)
        self.dont_delete = os.path.join(self.run_folder, DONT_DELETE)
        self.dest_run_folder = self.createDestinationRunFolder()
        
    def getHeader(self):
        return RUN_HEADER % {'run_folder': self.run_folder_name}
        
    def createDestinationRunFolder(self):
        if self.isCompleted() and self.destdir and self.do_create_destdir:
            return utils.locate_run_folder(self.run_folder_name, self.destdir)
        elif self.isCompleted() and self.destdir:
            return os.path.join(self.destdir, self.run_folder_name)
        return None
        
    def updateSequencingStatus(self, _is_sequencing_complete, _dry_run=True):
        if _is_sequencing_complete is True: 
            if not os.path.exists(self.sequencing_completed):
                utils.touch(self.sequencing_completed, _dry_run)
                self.log.info('create %s' % self.sequencing_completed)
            else:
                self.log.debug('%s already exists' % self.sequencing_completed)
        elif _is_sequencing_complete is False:
            if not os.path.exists(self.sequencing_failed):
                utils.touch(self.sequencing_failed, _dry_run)
                self.log.info('create %s' % self.sequencing_failed)
            else:
                self.log.debug('%s already exists' % self.sequencing_failed)
        else:
            self.log.info('sequencing underway - unknown status')

                    
    def isSequencingStatusPresent(self):
        # check if Sequencing.completed or Sequencing.failed is present
        if os.path.exists(self.sequencing_completed):
            self.log.debug('%s found' % self.sequencing_completed)
            return True
        if os.path.exists(self.sequencing_failed):
            self.log.debug('%s found' % self.sequencing_failed)
            return True
        return False
        
    def updateSyncStatus(self, _dry_run=True):
        rsync_folder = os.path.join(self.run_folder, RSYNC_FOLDER)
        if os.path.exists(rsync_folder):
            if os.path.exists(os.path.join(rsync_folder, RSYNC_STARTED)):
                if os.path.exists(os.path.join(rsync_folder, RSYNC_ENDED)):
                    if not os.path.exists(self.sync_completed):
                        utils.touch(self.sync_completed, _dry_run)
                        self.log.info('create %s' % self.sync_completed)
                    else:
                        self.log.debug('%s already exists' % self.sync_completed)
                elif os.path.exists(os.path.join(rsync_folder, RSYNC_FAILED)):
                    if not os.path.exists(self.sync_failed):
                        utils.touch(self.sync_failed)
                        self.log.info('create %s' % self.sync_failed)
                    else:
                        self.log.debug('%s already exists' % self.sync_failed)
                else:
                    self.log.info('Sync not finished.')
                    
        else:
            self.log.info('Not sync yet. %s does not exist.' % rsync_folder)
            
    def isSyncStatusPresent(self):
        # check if Sync.completed or Sync.failed is present
        if os.path.exists(self.sync_completed):
            self.log.debug('%s found' % self.sync_completed)
            return True
        if os.path.exists(self.sync_failed):
            self.log.debug('%s found' % self.sync_failed)
            return True
        return False

    def updateAnalysisStatus(self, _all_fastq_found=False, _dry_run=True):
        if _all_fastq_found:
            if not os.path.exists(self.analysis_completed):
                utils.touch(self.analysis_completed, _dry_run)
                self.log.info('create %s' % self.analysis_completed)
            else:
                self.log.debug('%s already exists' % self.analysis_completed)
        else:
            if os.path.exists(self.sequencing_completed):
                self.log.info('All fastq files not found - analysis running')
            else:
                self.log.info('%s does not exist - sequencing running' % self.sequencing_completed)
                
    def isAnalysisCompletedPresent(self):
        # check if Analysed.completed is present
        if os.path.exists(self.analysis_completed):
            return True
        return False
            
    def isCompleted(self):
        # check Sequencing.completed is present and analysis.ignore is not present - ready for analysis
        if os.path.exists(self.run_folder):
            if os.path.exists(self.sequencing_completed) and not os.path.exists(self.analysis_ignore):
                self.log.debug('%s is present' % self.sequencing_completed)
                return True
            else:
                if not os.path.exists(self.sequencing_completed):
                    self.log.debug('%s does not exists' % self.sequencing_completed)
                    return False
                if os.path.exists(self.analysis_ignore):
                    self.log.debug('%s is present' % self.analysis_ignore)
                    return False
        return False
        
    def isPublishingAssignedPresent(self):
         # check Publishing.assigned is present
         if os.path.exists(self.run_folder):
             if os.path.exists(self.publishing_assigned):
                 return True
         return False
    
    def isPublished(self):
        # check Publishing.completed is present and dont_delete is not present - ready for cleaning
        if os.path.exists(self.run_folder):
            if os.path.exists(self.publishing_completed) and not os.path.exists(self.dont_delete):
                return True
            else:
                if not os.path.exists(self.publishing_completed):
                    self.log.debug('%s does not exists' % self.publishing_completed)
                    return False
                if os.path.exists(self.dont_delete):
                    self.log.debug('%s is present' % self.dont_delete)
                    return False
        return False

################################################################################
# UNIT TESTS
################################################################################
class SyncRunFoldersTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/seqdir/vol0[1-2]/data/Runs/')
        self.destdir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.runs = RunFolders(basedir=self.basedir, destdir=self.destdir)
        
    def tearDown(self):
        import shutil
        folder = os.path.join(self.destdir, '130417_HWI-ST230_1122_C1YH9ACXX')
        if os.path.exists(folder):
            shutil.rmtree(folder)
        
    def test_run_folders(self):
        self.assertEqual(self.basedir, self.runs.basedir)
        self.assertEqual(self.destdir, self.runs.destdir)
        self.assertEqual(3, len(self.runs.run_folders))
        
    def test_runs_to_process(self):
        self.assertEqual(1, len(self.runs.completed_runs))
        
    def test_destination_run_folders(self):
        self.assertEqual(4, len(self.runs.dest_run_folders))
        
class AnalysisRunFoldersTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.destdir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = RunFolders(basedir=self.basedir, destdir=self.destdir)
        
    def tearDown(self):
        import shutil
        for folder in self.runs.dest_run_folders:
            shutil.rmtree(folder)

    def testRunFolders(self):
        self.assertEqual(self.basedir, self.runs.basedir)
        self.assertEqual(self.destdir, self.runs.destdir)
        self.assertEqual(3, len(self.runs.run_folders))
        
    def testCompletedRuns(self):
        self.assertEqual(2, len(self.runs.completed_runs))
        
    def testAnalysedRuns(self):
        self.assertEqual(1, len(self.runs.analysed_runs))
        
    def testDestinationRunFolders(self):
        self.assertEqual(2, len(self.runs.dest_run_folders))
        
class OneRunFolderTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.destdir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = RunFolders(self.basedir, self.destdir, '130114_HWI-ST230_1016_D18MAACXX')

    def tearDown(self):
        import shutil
        for folder in self.runs.dest_run_folders:
            shutil.rmtree(folder)

    def testRunFolders(self):
        self.assertEqual(self.basedir, self.runs.basedir)
        self.assertEqual(self.destdir, self.runs.destdir)
        self.assertEqual(1, len(self.runs.run_folders))

    def testCompletedRuns(self):
        self.assertEqual(1, len(self.runs.completed_runs))
        
    def testDestinationRunFolders(self):
        self.assertEqual(1, len(self.runs.dest_run_folders))


class RunDefinitionTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/analysisdir/data/Runs/')
        self.destdir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = RunFolders(basedir=self.basedir, destdir=self.destdir)
        self.runs_run = self.runs.completed_runs[0]
        self.run_folder = self.runs_run.run_folder
        self.run_folder_name = os.path.basename(self.run_folder)
        self.run_def = RunDefinition(self.run_folder, self.destdir)
        
    def tearDown(self):
        import shutil
        for folder in self.runs.dest_run_folders:
            shutil.rmtree(folder)

    def testRun(self):
        self.assertEqual(self.run_folder, self.run_def.run_folder)
        self.assertEqual(self.run_folder_name, self.run_def.run_folder_name)
        self.assertEqual('130114', self.run_def.start_date)
        self.assertEqual('HWI-ST230', self.run_def.instrument)
        self.assertEqual('D18MAACXX', self.run_def.flowcell_id)
        self.assertEqual('130114_D18MAACXX', self.run_def.run_uid)
        #self.assertTrue(os.path.exists(self.run_def.archive_run_folder))
        
    def testRunHeader(self):
        self.assertEqual(RUN_HEADER % {'run_folder': self.run_folder_name}, self.run_def.getHeader())
        
    def testCompletedRun(self):
        self.assertTrue(self.run_def.isCompleted())
        
    def testAnalysedRun(self):
        self.assertFalse(self.run_def.isAnalysedPresent())
        
    def testDestinationRunFolders(self):
        folder = glob.glob("%s/%s" % (self.destdir, '130114_HWI-ST230_1016_D18MAACXX'))
        self.assertIsNotNone(folder)
        

if __name__ == '__main__':
    unittest.main()