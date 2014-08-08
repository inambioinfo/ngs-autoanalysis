#!/usr/bin/env python
# encoding: utf-8
"""
data.py

$Id$

Created by Anne Pajon on 2013-03-19.
"""

################################################################################
# IMPORTS
################################################################################
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

RTA_COMPLETED = 'RTAComplete.txt'

SEQUENCING_COMPLETED = 'SequencingComplete.txt'
SEQUENCING_FAILED = 'SequencingFail.txt'

SYNC_COMPLETED = 'Sync.completed'
SYNC_FAILED = 'Sync.failed'

ANALYSIS_COMPLETED = "AnalysisComplete.txt"
ANALYSIS_IGNORE = 'analysis.ignore'
DONT_DELETE = 'dont.delete'

PUBLISHING_ASSIGNED = 'PublishingAssign.txt'
PUBLISHING_COMPLETED = 'PublishingComplete.txt'

RSYNC_FOLDER = "rsync"
RSYNC_STARTED = "rsync.started"
RSYNC_ENDED = "rsync.ended"
RSYNC_FAILED = "rsync.failed"


class Folder(object):

    def __init__(self, path_to_folder, folder_name):
        self.path_to_folder = path_to_folder
        self.folder_name = folder_name
        self.full_path = os.path.join(self.path_to_folder, self.folder_name)
        self.log = logging.getLogger(__name__)

    def exists(self):
        return os.path.exists(self.full_path)

    def touch(self, file_name, dry_run=False):
        f = os.path.join(self.full_path, file_name)
        if not dry_run:
            if not os.path.isfile(f):
                open(f, 'wa').close()
                self.log.info('%s created' % f)
            else:
                self.log.info('%s already exists' % f)
        else:
            self.log.info('[dry-run] touch %s' % f)
        return f


class RunFolder(Folder):
    """
    Run folder class
    """

    PATTERN = "(\d{6})_([\w\-]+)_(\d{4})_([\w\-]+)"

    RUN_HEADER = """
================================================================================
=== RUN: %(run_folder)s
================================================================================"""

    def __init__(self, run_folder, staging_dir=None, lustre_dir=None, do_create_dir=True):
        self.log = logging.getLogger(__name__)
        self.run_folder = run_folder
        self.path_to_run_folder = os.path.dirname(self.run_folder)
        self.run_folder_name = os.path.basename(self.run_folder)

        super(RunFolder, self).__init__(self.path_to_run_folder, self.run_folder_name)
        self.date, self.instrument, self.run_number, self.flowcell_id = re.match(RunFolder.PATTERN, self.folder_name).groups()
        self.run_uid = '%s_%s' % (self.date, self.flowcell_id)

        self.do_create_dir = do_create_dir

        self.staging_dir = staging_dir
        self.lustre_dir = lustre_dir

        # event files
        self.rta_completed = os.path.join(self.run_folder, RTA_COMPLETED)
        self.sequencing_completed = os.path.join(self.run_folder, SEQUENCING_COMPLETED)
        self.sequencing_failed = os.path.join(self.run_folder, SEQUENCING_FAILED)
        self.sync_completed = os.path.join(self.run_folder, SYNC_COMPLETED)
        self.sync_failed = os.path.join(self.run_folder, SYNC_FAILED)
        self.analysis_completed = os.path.join(self.run_folder, ANALYSIS_COMPLETED)
        self.analysis_ignore = os.path.join(self.run_folder, ANALYSIS_IGNORE)
        self.publishing_assigned = os.path.join(self.run_folder, PUBLISHING_ASSIGNED)
        self.publishing_completed = os.path.join(self.run_folder, PUBLISHING_COMPLETED)
        self.dont_delete = os.path.join(self.run_folder, DONT_DELETE)

        self.staging_run_folder = self.create_runfolder(self.staging_dir)
        self.lustre_run_folder = self.create_runfolder(self.lustre_dir)

    def get_header(self):
        return RunFolder.RUN_HEADER % {'run_folder': self.run_folder_name}

    def create_runfolder(self, dir):
        if self.is_sequencing_completed() and dir:
            if self.do_create_dir:
                return utils.locate_run_folder(self.run_folder_name, dir)
            else:
                return os.path.join(dir, self.run_folder_name)

    def update_sequencing_status(self, is_sequencing_complete, dry_run=True):
        if os.path.exists(self.rta_completed) and is_sequencing_complete:
            self.touch(self.sequencing_completed, dry_run)
        else:
            self.log.info('sequencing underway or sequencing failed')

    def is_sequencing_status_present(self):
        # check if Sequencing.completed or Sequencing.failed is present
        if os.path.exists(self.sequencing_completed):
            self.log.debug('%s found' % self.sequencing_completed)
            return True
        if os.path.exists(self.sequencing_failed):
            self.log.debug('%s found' % self.sequencing_failed)
            return True
        return False

    def is_sequencing_completed(self):
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

    def update_sync_status(self, _dry_run=True):
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

    def is_sync_status_present(self):
        # check if Sync.completed or Sync.failed is present
        if os.path.exists(self.sync_completed):
            self.log.debug('%s found' % self.sync_completed)
            return True
        if os.path.exists(self.sync_failed):
            self.log.debug('%s found' % self.sync_failed)
            return True
        return False

    def update_analysis_status(self, _all_fastq_found=False, _dry_run=True):
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

    def is_analysis_completed_present(self):
        # check if Analysed.completed is present
        return os.path.exists(self.analysis_completed)

    def is_publishing_assigned_present(self):
        # check Publishing.assigned is present and dont_delete is not present - ready for cleaning
        if os.path.exists(self.run_folder):
            if os.path.exists(self.publishing_assigned) and not os.path.exists(self.dont_delete):
                return True
        return False


class RunFolderList(object):
    """
    List of run folders of different status
    """

    RUNFOLDER_GLOB = "%s/??????_*_*_*"
    ONERUNFOLDER_GLOB = "%s/%s"

    def __init__(self, processing_dir, staging_dir, lustre_dir=None, one_run_folder=None, do_create_dir=True):
        self.log = logging.getLogger(__name__) 
        self.do_create_dir = do_create_dir
        self.processing_dir = processing_dir
        self.staging_dir = staging_dir
        self.lustre_dir = lustre_dir
        self.one_run_folder = one_run_folder

        if self.one_run_folder:
            self.run_folders = glob.glob(RunFolderList.ONERUNFOLDER_GLOB % (self.processing_dir, self.one_run_folder))
        else:
            self.run_folders = glob.glob(RunFolderList.RUNFOLDER_GLOB % self.processing_dir)

        self.all_runs, self.completed_runs, self.analysed_runs, self.published_runs = self.populate_runs()

    def populate_runs(self):
        all_runs = []
        completed_runs = []
        analysed_runs = []
        published_runs = []
        for run_folder in self.run_folders:
            self.log.debug(run_folder)
            run = RunFolder(run_folder, self.staging_dir, do_create_dir=self.do_create_dir)
            all_runs.append(run)
            if run.is_sequencing_completed():
                completed_runs.append(run)
            if run.is_analysis_completed_present():
                analysed_runs.append(run)
            if run.is_analysis_completed_present() and run.is_publishing_assigned_present():
                published_runs.append(run)
        return all_runs, completed_runs, analysed_runs, published_runs

    def get_destination_runfolders(self):
        if self.one_run_folder:
            return glob.glob(RunFolderList.ONERUNFOLDER_GLOB % (self.staging_dir, self.one_run_folder))
        return glob.glob(RunFolderList.RUNFOLDER_GLOB % self.staging_dir)


################################################################################
# UNIT TESTS
################################################################################

class RunFolderTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.destdir = os.path.join(self.current_path, '../testdata/staging/')

        self.run_folder_name = '130417_HWI-ST230_1122_C1YH9ACXX'
        self.run_folder = os.path.join(self.basedir, self.run_folder_name)
        self.run = RunFolder(self.run_folder, self.destdir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.run.staging_run_folder)
        pass

    def test_run(self):
        self.assertEqual(self.run_folder, self.run.run_folder)
        self.assertEqual(self.run_folder_name, self.run.run_folder_name)
        # 130417_HWI-ST230_1122_C1YH9ACXX
        self.assertEqual('130417', self.run.date)
        self.assertEqual('HWI-ST230', self.run.instrument)
        self.assertEqual('C1YH9ACXX', self.run.flowcell_id)
        self.assertEqual('130417_C1YH9ACXX', self.run.run_uid)
        self.assertTrue(os.path.exists(self.run.staging_run_folder))

    def test_run_header(self):
        self.assertEqual(RunFolder.RUN_HEADER % {'run_folder': self.run_folder_name}, self.run.get_header())

    def test_completed_run(self):
        self.assertTrue(self.run.is_sequencing_status_present())
        self.assertTrue(self.run.is_sequencing_completed())

    def test_destination_runfolders(self):
        folder = glob.glob("%s/%s" % (self.destdir, '130417_HWI-ST230_1122_C1YH9ACXX'))
        self.assertIsNotNone(folder)


class RunFolderListTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.destdir = os.path.join(self.current_path, '../testdata/staging/')
        self.runs = RunFolderList(processing_dir=self.basedir, staging_dir=self.destdir, lustre_dir=None)
        
    def tearDown(self):
        import shutil
        folder = os.path.join(self.destdir, '130417_HWI-ST230_1122_C1YH9ACXX')
        if os.path.exists(folder):
            shutil.rmtree(folder)
        
    def test_run_folders(self):
        self.assertEqual(self.basedir, self.runs.processing_dir)
        self.assertEqual(self.destdir, self.runs.staging_dir)
        self.assertEqual(3, len(self.runs.run_folders))
        self.assertEqual(len(self.runs.run_folders), len(self.runs.all_runs))
        
    def test_runs_to_process(self):
        self.assertEqual(1, len(self.runs.completed_runs))
        self.assertEqual(0, len(self.runs.analysed_runs))
        self.assertEqual(0, len(self.runs.published_runs))
        
    def test_destination_run_folders(self):
        self.assertEqual(1, len(self.runs.get_destination_runfolders()))
        

class AnalysisRunFoldersTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.destdir = os.path.join(self.current_path, '../testdata/staging/')
        self.runs = RunFolderList(processing_dir=self.basedir, staging_dir=self.destdir, lustre_dir=None)
        
    def tearDown(self):
        import shutil
        for folder in self.runs.get_destination_runfolders():
            shutil.rmtree(folder)

    def test_runfolders(self):
        self.assertEqual(self.basedir, self.runs.processing_dir)
        self.assertEqual(self.destdir, self.runs.staging_dir)
        self.assertEqual(3, len(self.runs.run_folders))
        
    def test_completed_runs(self):
        self.assertEqual(1, len(self.runs.completed_runs))
        self.assertEqual(1, len(self.runs.completed_runs))

    def test_analysed_runs(self):
        self.assertEqual(0, len(self.runs.analysed_runs))
        
    def test_destination_runfolders(self):
        self.assertEqual(1, len(self.runs.get_destination_runfolders()))
        

class OneRunFolderTests(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.destdir = os.path.join(self.current_path, '../testdata/staging/')
        self.runs = RunFolderList(self.basedir, self.destdir, None, '130417_HWI-ST230_1122_C1YH9ACXX')

    def tearDown(self):
        import shutil
        for folder in self.runs.get_destination_runfolders():
            shutil.rmtree(folder)

    def test_run_folders(self):
        self.assertEqual(self.basedir, self.runs.processing_dir)
        self.assertEqual(self.destdir, self.runs.staging_dir)
        self.assertEqual(1, len(self.runs.run_folders))

    def test_completed_runs(self):
        self.assertEqual(1, len(self.runs.completed_runs))
        
    def test_destination_runfolders(self):
        self.assertEqual(1, len(self.runs.get_destination_runfolders()))


if __name__ == '__main__':
    unittest.main()