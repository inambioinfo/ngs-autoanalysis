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
log = logging.getLogger('auto.utils')

################################################################################
# CONSTANTS
################################################################################
# Cluster host
CLUSTER_HOST = "uk-cri-lcst01"

# Template for shell script
SCRIPT_TEMPLATE = '''
#!/bin/bash
#
# Autoanalysis generated shell script for running command(s) locally
#

set -v

%(cmd)s

'''

# Template for lsf command
LSF_CMD_TEMPLATE = '''
export MEM_VALUE=%(mem_value)s
export MEM_LIMIT=$[${MEM_VALUE}*1024]
export JAVA_OPTS="-Xmx$[${MEM_VALUE}-512]M -Xms$[${MEM_VALUE}-512]M"

ssh %(cluster)s "cd %(work_dir)s; touch pipeline.started; bsub -M ${MEM_LIMIT} -R 'select[mem>=${MEM_VALUE}] rusage[mem=${MEM_VALUE}]' -J %(job_name)s -o %(job_name)s_%%J.out -q solexa %(cmd)s"

'''

################################################################################
# METHODS
################################################################################
def create_script(script_path, command):
    if not os.path.exists(script_path):    
        script_file = open(script_path, 'w')
        script_file.write(SCRIPT_TEMPLATE % {'cmd':command})
        script_file.close()
        os.chmod(script_path, 0755)
        log.info('%s created' % script_path)
    else:
        log.debug('%s already exists' % script_path)
    
def run_process(cmd, dry_run=True):
    if not dry_run:
        process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = process.communicate()[0]
        retcode = process.returncode
        log.info("command '%s' executed" % " ".join(cmd))
        log.debug(retcode)
        if retcode == 0:
            log.debug(out)
        else:
            log.error(out)
        return out
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def run_bg_process(cmd, dry_run=True, logfilename=None):
    if not dry_run:
        if logfilename:
            with open(logfilename, "wb") as logfile:
                subprocess.Popen(cmd, shell=False, stdout=logfile, stderr=subprocess.STDOUT)
        else:
            subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log.info("command '%s' executed" % " ".join(cmd))
    else:
        log.info("[dry-run] command '%s' to run" % " ".join(cmd))

def touch(fname, dry_run=False, times=None):
    try:
        if not dry_run:
            with file(fname, 'wa'):
                os.utime(fname, times)
        else:
            log.info("[dry-run] touch %s" % fname)
    except:
        log.exception('cannot touch %s' % fname)
        raise

def output_job_success(output_files):
    try:
        for output_file in output_files:
            with open(output_file) as output:
                i = 0
                for line in output:
                    i += 1
                    if i >= 50:
                        break
                    if 'Successfully completed' in line:
                        return True
    except IOError:
        log.exception('')
        raise
    else:
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
    try:
        os.makedirs(directory)
        log.info('%s created' % directory)
    except OSError:
        if os.path.exists(directory):
            log.debug('%s already exists' % directory)
        else:
            log.exception('cannot create directory %s' % directory)
            raise

def get_smallest_volume(archive_glob):
    try:
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
            except:
                log.exception('cannot get smallest volume from %s' % archive_glob)
                raise
        else:
            log.error('no volume %s found' % archive_glob)
            return None
    except:
        log.exception('cannot get smallest volume from %s' % archive_glob)
        raise

################################################################################
# UNIT TESTS
################################################################################
class utilsTests(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()