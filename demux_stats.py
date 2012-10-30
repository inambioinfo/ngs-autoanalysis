#!/usr/bin/env python
# encoding: utf-8
"""
demux_stats.py

Created by Anne Pajon on 2012-10-01.

Usage:
    fab -f demux_stats.py local install
"""

import sys, os
import logging as log

try:
    from fabric.api import *
    from fabric.contrib.files import *
    from sqlalchemy.ext.sqlsoup import SqlSoup
except ImportError:
    print '''
 Please (a) install python modules { fabric | mysql-python | sqlalchemy } first 
 or (b) activate your python virtual environment.
 (a) ----------    
 wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py --no-check-certificate
 python virtualenv.py `pwd`
 source bin/activate
 pip install fabric mysql-python sqlalchemy
 (b) ----------
 source bin/activate
 '''
    sys.exit()

HOST = "mysql://readonly@uk-cri-lbio04"
SOLEXA = "%s/cri_solexa" % HOST
LIMS = "%s/cri_lims" % HOST
REQUEST = "%s/cri_request" % HOST
GENERAL = "%s/cri_general" % HOST

# logging configuration
log.basicConfig(format='%(levelname)s: %(message)s', level=log.DEBUG)

# -- Host specific setup

def remote():
    """Setup environment for demultiplex statistic analysis on lustre
    """
    env.user = 'solexa'
    env.hosts = ['uk-cri-lsol03.crnet.org', 'uk-cri-lsol01.crnet.org']
    env.root_path = '/lustre/mib-cri/solexa/DemuxStats'
    env.demux_path = '/home/mib-cri/software/pipelines/demultiplex/'
    
def local():    
    """Setup environment for demultiplex statistic analysis locally
    """
    env.user = 'pajon01'
    env.hosts = ['localhost']
    env.root_path = '/lustre/mib-cri/solexa/DemuxStats'
    env.demux_path = ''

# -- Fabric instructions

def install():
    """Setup demultiplex statistic analysis
    """
    install_data()
    setup_pipeline()
    #run_pipeline()
    
def list_samples():
    runs = MultiplexedRuns()
    for run in runs.runs:
        print("========== %s\t%s" % (run.runNumber, run.pipelinePath))
        runs.printSampleDetails(run)
        
def install_data():
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")
    
    # create root_path if not exists
    if not exists(env.root_path):
        run("mkdir %s" % env.root_path)
    
    # get all multiplexed runs
    runs = MultiplexedRuns()
    for run in runs.runs:
        # create folder in ROOT_PATH for analysis
        run_analysis_folder = os.path.join(env.root_path, run.pipelinePath)
        _create_dir(run_analysis_folder)
        # get all file locations associated to demultiplexed lanes for this run
        file_locations = runs.getSeqFileLocations(run)
        for file_location in file_locations:
            # checking which host to copy the data from sol01 or sol03
            if env.host == file_location.host or env.host == 'localhost':
                log.info("%s\t%s\t%s\t%s" % (run.runNumber, file_location.host, file_location.path, file_location.filename))
                orig = os.path.join(file_location.path, file_location.filename)
                dest = os.path.join(run_analysis_folder, file_location.filename)
                _copy_file(orig, dest)
                                        
def setup_pipeline(annotated_sample_file):
    runs = MultiplexedRuns()
    for run in runs.runs:
        _create_meta(run)

def _create_dir(dir):
    if not exists(dir):
        run("mkdir %s" % dir)
        log.debug("Directory %s created" % dir)
    else:
        log.debug("Directory %s already exists" % dir)

def _copy_file(orig, dest):
    if not exists(dest):
        if env.host == 'localhost':
            run("touch %s" % (dest))
        else:
            run("cp %s %s" % (orig, dest))
        log.debug("File %s copied to %s" % (orig, dest))
    else:
        log.debug('File %s already exists' % dest)
        
def _create_meta():
    run("/home/mib-cri/software/pipelines/demultiplex/bin/create-metafile -l 3 939 > run-meta.xml")
            
class MultiplexedRuns():
    
    def __init__(self):
        # CRI lims database connection
        self.solexa_db = SqlSoup(SOLEXA)
        self.lims_db = SqlSoup(LIMS)
        self.request_db = SqlSoup(REQUEST)
        self.general_db = SqlSoup(GENERAL)
        self.runs = []
        self.populateRuns()
        
    def populateRuns(self):
        # get All runs
        runs = self.solexa_db.solexarun.all()
        for run in runs:
            # select runs that have been successful
            if run.status == 'COMPLETE' and (run.analysisStatus == 'COMPLETE' or run.analysisStatus == 'SECONDARY COMPLETE'):
                # select multiplex runs
                if run.multiplexed == 1:
                    # create folder in ROOT_PATH for analysis
                    self.runs.append(run)
                    
    def getSeqFileLocations(self, run):
        sequence_files = []
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            if lane.multiplex == 'Other':
                # select all files for demultiplexed lanes
                file_locations = self.lims_db.analysisfileuri.filter_by(owner_id=lane.sampleProcess_id)
                for file_location in file_locations:
                    file_type = self.lims_db.analysisfiletype.filter_by(id=file_location.type_id).one()
                    # select only FastQ files 
                    if file_location.scheme == 'FILE' and file_location.role == 'ARCHIVE' and file_type.name == 'FastQ':
                        sequence_files.append(file_location)
        return sequence_files

    def printSampleDetails(self, run):
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            if lane.isControl == 0 and lane.multiplex != 'None':
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

                print ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (lane.genomicsSampleId, run.deviceType, lane.sequenceType, lane.endType, lane.cycles, lane.userSampleId, username, str_comment ))
                
      