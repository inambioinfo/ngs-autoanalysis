#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

$Id$

Created by Anne Pajon on 2012-10-26.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import subprocess 
import unittest

# logging definition
log = logging.getLogger('root.utils')

################################################################################
# CONSTANTS
################################################################################
# Template for local shell script
LOCAL_SCRIPT_TEMPLATE = '''
#!/bin/bash
#
# Shell script for running command(s) locally
#

set -v

%(cmd)s

'''

# Template for lsf shell script
LSF_SCRIPT_TEMPLATE = '''
#!/bin/bash
# 
# Shell script for executing run-pipeline on the cluster
#

set -v

export MEM_VALUE=%(mem_value)s
export MEM_LIMIT=$[${MEM_VALUE}*1024]
export JAVA_OPTS="-Xmx$[${MEM_VALUE}-512]M -Xms$[${MEM_VALUE}-512]M"

ssh %(cluster)s "cd %(work_dir)s; touch pipeline.started; bsub -M ${MEM_LIMIT} -R 'select[mem>=${MEM_VALUE}] rusage[mem=${MEM_VALUE}]' -J %(job_name)s -o %(job_name)s_%%J.out -q solexa %(cmd)s"

'''

################################################################################
# METHODS
################################################################################
def run_process(cmd, dry_run=True):
    if not dry_run:
        process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = process.communicate()
        log.info("command '%s' executed" % " ".join(cmd))
        if stdout:
            log.debug(stdout)
        if stderr:
            log.error(stderr)
        return stdout
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def run_bg_process(cmd, dry_run=True):
    if not dry_run:
        subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log.info("command '%s' executed" % " ".join(cmd))
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def touch(fname, times=None):
    with file(fname, 'wa'):
        os.utime(fname, times)

def output_job_success(output_files):
    for output_file in output_files:
        with open(output_file) as output:
            i = 0
            for line in output:
                i += 1
                if i >= 50:
                    break
                if 'Successfully completed' in line:
                    return True
    return False

def locate_run_folder(run_folder_name, archive_glob, create=True):
    run_folders = glob.glob("%s/%s" % (archive_glob,run_folder_name))
    if run_folders:
        if len(run_folders) == 1:
            log.debug("run folder %s already exists" % run_folders)
            return run_folders[0]
        else:
            log.error("more than one run folders %s found in %s" % (run_folder_name, run_folders))
    else:
        if create:
                volume_name = get_smallest_volume(archive_glob)
                if volume_name:
                    run_folder = os.path.join(volume_name, run_folder_name)
                    os.makedirs(run_folder)
                    log.debug("run folder %s created" % run_folder)
                    return run_folder
                else:
                    log.error('no volume %s found' % archive_glob)
        else:
            log.info('no run folder %s found in %s' % (run_folder_name, archive_glob))
    return None
    
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info('%s created' % directory)
    else:
        log.debug('%s already exists' % directory)

def get_smallest_volume(archive_glob):
    volumes = glob.glob(archive_glob)
    if volumes:
        try:
            volume_sizes = {}
            for volume in volumes:
                device, size, used, available, percent, mountpoint = run_process(['df', '%s' % volume], False).split("\n")[1].split()
                volume_sizes[volume]=used
            min_volume = min(volume_sizes, key=lambda x: volume_sizes.get(x))
            return min_volume
        except ValueError:
            return volumes[0]

def set_analysis_status(solexa_soap, run, status):
    if not run.analysisStatus == status:
        solexa_soap.service.setAnalysisStatus(run.process_id, status)
        log.info('analysis status in lims set to %s for process id %s' % (status, run.process_id))
    else:
        log.info('analysis status in lims already set to %s for process id %s' % (status, run.process_id))

def set_run_complete(solexa_soap, run, status):
    if not run.status == status:
        solexa_soap.service.setRunComplete(run.process_id)
        log.info('run status in lims set to %s for process id %s' % (status, run.process_id))
    else:
        log.info('run status in lims already set to %s for process id %s' % (status, run.process_id))

################################################################################
# UNIT TESTS
################################################################################
class utilsTests(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()