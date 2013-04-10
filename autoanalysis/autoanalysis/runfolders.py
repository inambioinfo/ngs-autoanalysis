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

# logging definition
log = logging.getLogger('auto.runfolders')

# autoanalysis modules
import utils

################################################################################
# CONSTANTS
################################################################################

RUNFOLDER_GLOB = "%s/??????_*_*_*"
SEQUENCING_COMPLETED = 'Sequencing.completed'
ANALYSIS_IGNORE = 'analysis.ignore'

RUN_HEADER = """================================================================================
=== RUN: %(run_folder)s
================================================================================
"""

################################################################################
# CLASSES
################################################################################
        
class RunFolders(object):
    def __init__(self, _basedir, _archivedir):
        self.basedir = _basedir
        self.archivedir = _archivedir
        self.run_folders =  glob.glob(RUNFOLDER_GLOB % self.basedir)
        self.archived_run_folders = glob.glob(RUNFOLDER_GLOB % self.archivedir)
        
    def findRunsToAnalyse(self):
        completed_runs = []
        for run_folder in self.run_folders:
            run_definition = RunDefinition(run_folder, self.archivedir)
            if run_definition.is_ready_for_analysis():
                completed_runs.append(run_definition)
        return completed_runs
        
    
class RunDefinition(object):
    def __init__(self, _run_folder, _archivedir=None):
        self.run_folder = _run_folder
        self.archive_run_folder = utils.locate_run_folder(os.path.basename(self.run_folder), _archivedir)
        self.run_folder_name = os.path.basename(self.run_folder)
        self.start_date = self.run_folder_name.split('_')[0]
        self.instrument = self.run_folder_name.split('_')[1]
        self.flowcell_id = self.run_folder_name.split('_')[-1]
        self.run_uid = '%s_%s' % (self.start_date, self.flowcell_id)
        self.sequencing_completed = os.path.join(self.run_folder, SEQUENCING_COMPLETED)
        self.analysis_ignore = os.path.join(self.run_folder, ANALYSIS_IGNORE)
        
    def get_header(self):
        return RUN_HEADER % {'run_folder': self.run_folder_name}
        
    def is_ready_for_analysis(self):
        if os.path.exists(self.run_folder):
            # check sequencing process has finished and check analysis.ignore is not present
            if os.path.exists(self.sequencing_completed) and not os.path.exists(self.analysis_ignore):
                return True
            else:
                if not os.path.exists(self.sequencing_completed):
                    log.warn('%s does not exists' % self.sequencing_completed)
                    return False
                if os.path.exists(self.analysis_ignore):
                    log.info('%s is present' % self.analysis_ignore)
                    return False
        return False


################################################################################
# UNIT TESTS
################################################################################

class RunFoldersTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        log = logger.set_custom_logger()
        log.setLevel(logging.DEBUG)  
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/basedir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = RunFolders(self.basedir, self.archivedir)
        
    def test_run_folders_creation(self):
        self.assertEqual(self.basedir, self.runs.basedir)
        self.assertEqual(self.archivedir, self.runs.archivedir)
        self.assertEqual(2, len(self.runs.run_folders))
        self.assertEqual(2, len(self.runs.archived_run_folders))
        
    def test_find_runs_to_analyse(self):
        self.assertEqual(1, len(self.runs.findRunsToAnalyse()))
        
        
class RunDefinitionTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        log = logger.set_custom_logger()
        log.setLevel(logging.DEBUG)  
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/basedir/data/Runs/')
        self.archivedir = os.path.join(self.current_path, '../testdata/archivedir/vol0[1-2]/data/Runs/')
        self.runs = RunFolders(self.basedir, self.archivedir)
        self.runs_run_definition = self.runs.findRunsToAnalyse()[0]
        self.run_folder = self.runs_run_definition.run_folder
        self.run_folder_name = os.path.basename(self.run_folder)
        self.run_def = RunDefinition(self.run_folder, self.archivedir)
        
    def tearDown(self):
        import shutil
        shutil.rmtree(self.run_def.archive_run_folder)

    def test_run_definition(self):
        self.assertEqual(self.run_folder, self.run_def.run_folder)
        self.assertEqual(self.run_folder_name, self.run_def.run_folder_name)
        self.assertEqual('130114', self.run_def.start_date)
        self.assertEqual('HWI-ST230', self.run_def.instrument)
        self.assertEqual('D18MAACXX', self.run_def.flowcell_id)
        self.assertEqual('130114_D18MAACXX', self.run_def.run_uid)
        self.assertTrue(os.path.exists(self.run_def.archive_run_folder))
        
    def test_run_definition_header(self):
        self.assertEqual(RUN_HEADER % {'run_folder': self.run_folder_name}, self.run_def.get_header())
        
    def test_run_definition_ready_for_analysis(self):
        self.assertTrue(self.run_def.is_ready_for_analysis())


if __name__ == '__main__':
    unittest.main()