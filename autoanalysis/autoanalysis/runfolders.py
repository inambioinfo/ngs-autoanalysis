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
ANALYSIS_COMPLETED = "Analysis.completed"
ANALYSIS_IGNORE = 'analysis.ignore'
DONT_DELETE = 'dont.delete'

RUN_HEADER = """
================================================================================
=== RUN: %(run_folder)s
================================================================================"""

################################################################################
# CLASSES
################################################################################
        
class RunFolders(object):
    def __init__(self, basedir, destdir, one_run_folder=None): # destdir
        self.log = logging.getLogger(__name__) 
        self.basedir = basedir
        self.destdir = destdir
        self.one_run_folder = one_run_folder
        if self.one_run_folder:
            self.run_folders = glob.glob(ONERUNFOLDER_GLOB % (self.basedir, self.one_run_folder))
        else:
            self.run_folders =  glob.glob(RUNFOLDER_GLOB % self.basedir)
        self.completed_runs = self.getCompletedRuns()
        self.analysed_runs = self.getAnalysedRuns()
        self.dest_run_folders = self.getDestinationRunFolders()
        
    def getCompletedRuns(self):
        completed_runs = []
        for run_folder in self.run_folders:
            run = RunDefinition(run_folder, self.destdir)
            if run.isCompleted():
                completed_runs.append(run)
        return completed_runs
    
    #completed_runs = property(getCompletedRuns)
    
    def getAnalysedRuns(self):
        analysed_runs = []
        for run in self.completed_runs:
            if run.isAnalysed():
                analysed_runs.append(run)
        return analysed_runs
        
    def getDestinationRunFolders(self):
        if self.one_run_folder:
            return glob.glob(ONERUNFOLDER_GLOB % (self.destdir, self.one_run_folder))
        return glob.glob(RUNFOLDER_GLOB % self.destdir)
        
class RunDefinition(object):
    def __init__(self, run_folder, destdir=None):
        self.log = logging.getLogger(__name__) 
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
        self.analysis_completed = os.path.join(self.run_folder, ANALYSIS_COMPLETED)
        self.analysis_ignore = os.path.join(self.run_folder, ANALYSIS_IGNORE)
        self.dont_delete = os.path.join(self.run_folder, DONT_DELETE)
        self.dest_run_folder = self.createDestinationRunFolder()
        
    def getHeader(self):
        return RUN_HEADER % {'run_folder': self.run_folder_name}
        
    def createDestinationRunFolder(self):
        if self.isCompleted():
            return utils.locate_run_folder(os.path.basename(self.run_folder), self.destdir)
        return None
        
    def isCompleted(self):
        if os.path.exists(self.run_folder):
            # check Sequencing.completed is present and analysis.ignore is not present
            if os.path.exists(self.sequencing_completed) and not os.path.exists(self.analysis_ignore):
                return True
            else:
                if not os.path.exists(self.sequencing_completed):
                    self.log.debug('%s does not exists' % self.sequencing_completed)
                    return False
                if os.path.exists(self.analysis_ignore):
                    self.log.debug('%s is present' % self.analysis_ignore)
                    return False
        return False
        
    def isAnalysed(self):
        if os.path.exists(self.run_folder):
            # check Analysed.completed is present and dont_delete is not present
            if os.path.exists(self.analysis_completed) and not os.path.exists(self.dont_delete):
                return True
            else:
                if not os.path.exists(self.analysis_completed):
                    self.log.debug('%s does not exists' % self.analysis_completed)
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
        self.assertFalse(self.run_def.isAnalysed())
        
    def testDestinationRunFolders(self):
        folder = glob.glob("%s/%s" % (self.destdir, '130114_HWI-ST230_1016_D18MAACXX'))
        self.assertIsNotNone(folder)
        

if __name__ == '__main__':
    unittest.main()