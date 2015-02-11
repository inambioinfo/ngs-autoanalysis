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

IGNORE_ME = 'ignore.me'
DONT_DELETE = 'dont.delete'

ANALYSIS_COMPLETED = "AnalysisComplete.txt"
EXTERNAL_COMPLETED = 'ExternalComplete.txt'
SYNC_COMPLETED = 'SyncComplete.txt'
PUBLISHING_ASSIGNED = 'PublishingAssign.txt'


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
        self.analysis_completed = os.path.join(self.run_folder, ANALYSIS_COMPLETED)
        self.sync_completed = os.path.join(self.run_folder, SYNC_COMPLETED)
        self.external_completed = os.path.join(self.run_folder, EXTERNAL_COMPLETED)
        self.publishing_assigned = os.path.join(self.run_folder, PUBLISHING_ASSIGNED)
        self.ignore_me = os.path.join(self.run_folder, IGNORE_ME)
        self.dont_delete = os.path.join(self.run_folder, DONT_DELETE)

        # only create run folders when sequencing is complete
        self.staging_run_folder = self.create_runfolder(self.staging_dir)
        self.lustre_run_folder = self.create_runfolder(self.lustre_dir)

    def get_header(self):
        return RunFolder.RUN_HEADER % {'run_folder': self.run_folder_name}

    def create_runfolder(self, dir):
        if self.is_ready_for_processing() and dir:
            if self.do_create_dir:
                return utils.locate_run_folder(self.run_folder_name, dir)
            else:
                return os.path.join(dir, self.run_folder_name)

    def update_sequencing_status(self, is_sequencing_complete, dry_run=True):
        if os.path.exists(self.rta_completed) and is_sequencing_complete:
            self.touch(self.sequencing_completed, dry_run)
            self.log.info('sequencing completed')
        else:
            if is_sequencing_complete == False:
                self.touch(self.sequencing_failed, dry_run)
                self.log.info('sequencing failed')
            else:
                self.log.info('sequencing underway or with unknown status')

    def is_sequencing_status_present(self):
        # check if SequencingComplete.txt or SequencingFail.txt is present
        if os.path.exists(self.sequencing_completed):
            self.log.debug('%s found' % self.sequencing_completed)
            return True
        if os.path.exists(self.sequencing_failed):
            self.log.debug('%s found' % self.sequencing_failed)
            return True
        return False

    def is_sequencing_completed_present(self):
        # check if SequencingComplete.txt is present
        return os.path.exists(self.sequencing_completed)

    def is_sequencing_failed_present(self):
        # check if SequencingFail.txt is present
        return os.path.exists(self.sequencing_failed)

    def is_ready_for_processing(self):
        # check SequencingComplete.txt is present and ignore.me is not present
        if os.path.exists(self.run_folder):
            if os.path.exists(self.sequencing_completed) and not os.path.exists(self.ignore_me):
                self.log.debug('%s is present' % self.sequencing_completed)
                return True
            else:
                if not os.path.exists(self.sequencing_completed):
                    self.log.debug('%s does not exists' % self.sequencing_completed)
                if os.path.exists(self.ignore_me):
                    self.log.debug('%s is present' % self.ignore_me)
        return False

    def is_to_be_ignored(self):
        return os.path.exists(self.ignore_me)

    def is_analysis_completed_present(self):
        # check if AnalysisComplete.txt is present
        return os.path.exists(self.analysis_completed)

    def is_sync_completed_present(self):
        # check if SyncComplete.txt is present
        return os.path.exists(self.sync_completed)

    def is_external_completed_present(self):
        # check if ExternalComplete.txt is present
        return os.path.exists(self.external_completed)

    def is_publishing_assigned_present(self):
        # check PublishingAssigned.txt is present
        return os.path.exists(self.publishing_assigned)

    def copy_event_to_staging(self, event_filename):
        # copy event file to staging
        event_file = os.path.join(self.staging_run_folder, event_filename)
        if not os.path.exists(event_file):
            utils.touch(event_file)

    def copy_publishing_assign_to_staging(self):
        self.copy_event_to_staging(PUBLISHING_ASSIGNED)

    def touch_event(self, event_filename):
        # touch event file in run folder
        event_file = os.path.join(self.run_folder, event_filename)
        if not os.path.exists(event_file):
            utils.touch(event_file)

    def touch_publishing_assign(self):
        self.touch_event(PUBLISHING_ASSIGNED)

    def remove_event(self, event_filename):
        event_file = os.path.join(self.run_folder, event_filename)
        if os.path.exists(event_file):
            os.remove(event_file)

    def remove_event_from_staging(self, event_filename):
        event_file = os.path.join(self.staging_run_folder, event_filename)
        if os.path.exists(event_file):
            os.remove(event_file)


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

        self.run_folders = self.get_folders(self.processing_dir)
        self.all_runs, self.completed_runs, self.failed_runs, self.runs_to_analyse, self.analysed_runs, self.synced_runs, self.published_runs, self.unknown_runs = self.populate_runs()

    def populate_runs(self):
        all_runs = []
        completed_runs = []
        failed_runs = []
        unknown_runs = []
        runs_to_analyse = []
        analysed_runs = []
        synced_runs = []
        published_runs = []
        for run_folder in self.run_folders:
            self.log.debug(run_folder)
            run = RunFolder(run_folder, self.staging_dir, self.lustre_dir, do_create_dir=self.do_create_dir)
            all_runs.append(run)
            if run.is_sequencing_completed_present():
                completed_runs.append(run)
                if not run.is_publishing_assigned_present() and not run.is_to_be_ignored():
                    runs_to_analyse.append(run)
            if run.is_sequencing_failed_present():
                failed_runs.append(run)
            if not run.is_sequencing_completed_present() and not run.is_sequencing_failed_present():
                unknown_runs.append(run)
            if run.is_analysis_completed_present():
                analysed_runs.append(run)
            if run.is_sync_completed_present():
                synced_runs.append(run)
            if run.is_publishing_assigned_present():
                published_runs.append(run)
        return all_runs, completed_runs, failed_runs, runs_to_analyse, analysed_runs, synced_runs, published_runs, unknown_runs

    def get_destination_runfolders(self):
        return self.get_folders(self.staging_dir)

    def get_lustre_runfolders(self):
        return self.get_folders(self.lustre_dir)

    def get_folders(self, this_dir):
        if self.one_run_folder:
            return glob.glob(RunFolderList.ONERUNFOLDER_GLOB % (this_dir, self.one_run_folder))
        return glob.glob(RunFolderList.RUNFOLDER_GLOB % this_dir)


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
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')

        self.run_folder_name = '130417_HWI-ST230_1122_C1YH9ACXX'
        self.run_folder = os.path.join(self.basedir, self.run_folder_name)
        self.run = RunFolder(self.run_folder, self.destdir, self.lustredir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.run.staging_run_folder)
        shutil.rmtree(self.run.lustre_run_folder)

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
        self.assertTrue(self.run.is_ready_for_processing())

    def test_destination_runfolders(self):
        folder = glob.glob("%s/%s" % (self.destdir, '130417_HWI-ST230_1122_C1YH9ACXX'))
        self.assertIsNotNone(folder)
        folder = glob.glob("%s/%s" % (self.lustredir, '130417_HWI-ST230_1122_C1YH9ACXX'))
        self.assertIsNotNone(folder)


class RunFolderListTests(unittest.TestCase):
    
    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.basedir = os.path.join(self.current_path, '../testdata/processing/')
        self.destdir = os.path.join(self.current_path, '../testdata/staging/')
        self.lustredir = os.path.join(self.current_path, '../testdata/lustre/')
        self.runs = RunFolderList(processing_dir=self.basedir, staging_dir=self.destdir, lustre_dir=self.lustredir)
        
    def tearDown(self):
        import shutil
        for folder in self.runs.get_destination_runfolders():
            shutil.rmtree(folder)
        for folder in self.runs.get_lustre_runfolders():
            shutil.rmtree(folder)

    def test_all_run_folders(self):
        self.assertEqual(self.basedir, self.runs.processing_dir)
        self.assertEqual(self.destdir, self.runs.staging_dir)
        self.assertEqual(self.lustredir, self.runs.lustre_dir)
        self.assertEqual(5, len(self.runs.run_folders))
        self.assertEqual(len(self.runs.run_folders), len(self.runs.all_runs))
        
    def test_completed_runs(self):
        self.assertEqual(4, len(self.runs.completed_runs))

    def test_to_analyse_runs(self):
        self.assertEqual(2, len(self.runs.runs_to_analyse))

    def test_analysed_runs(self):
        self.assertEqual(2, len(self.runs.analysed_runs))

    def test_published_runs(self):
        self.assertEqual(1, len(self.runs.published_runs))
        
    def test_destination_run_folders(self):
        self.assertEqual(3, len(self.runs.get_destination_runfolders()))
        self.assertEqual(3, len(self.runs.get_lustre_runfolders()))

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