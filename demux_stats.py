#!/usr/bin/env python
# encoding: utf-8
"""
demux_stats.py

Created by Anne Pajon on 2012-10-01.

Usage:
    fab -f demux_stats.py local install
"""

import sys, os, glob
import optparse
import logging
import urllib2

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

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import autoanalysis


# database urls
HOST = "mysql://readonly@uk-cri-lbio04"
SOLEXA = "%s/cri_solexa" % HOST
LIMS = "%s/cri_lims" % HOST
REQUEST = "%s/cri_request" % HOST
GENERAL = "%s/cri_general" % HOST

# index file names
MULTIPLEX_KIT={
    'TruSeq RNA High Throughput' : 'truseq_rna_ht.csv',
    'Nextera Dual Index' : 'nextera.csv',
    'Fluidigm' : 'fluidigm.csv',
    'TruSeq Small RNA' : 'truseq_smallrna.csv',
    'TruSeq RNA Low Throughput' : 'truseq_rna_lt.csv',
    'TruSeq DNA Low Throughput' : 'truseq_dna_lt.csv',
    'TruSeq DNA High Throughput' : 'truseq_dna_ht.csv'
}

# logging configuration
log.setLevel(logging.DEBUG)        

# -- Host specific setup

def remote():
    """Setup environment for demultiplex statistic analysis on lustre
    """
    env.user = 'solexa'
    env.hosts = ['uk-cri-lsol03.crnet.org', 'uk-cri-lsol01.crnet.org']
    env.root_path = '/lustre/mib-cri/solexa/DemuxStats'
    env.soft_pipeline_path = autoanalysis.SOFT_PIPELINE_PATH
    
def local():    
    """Setup environment for demultiplex statistic analysis locally
    """
    env.user = 'pajon01'
    env.hosts = ['localhost']
    env.root_path = '/lustre/mib-cri/solexa/DemuxStats'
    env.soft_pipeline_path = '/Users/pajon01/software/pipelines'

# -- Fabric instructions

def install():
    """Setup demultiplex statistic analysis on all multiplexed run
    """
    install_data()
    setup_pipeline()
    
def run():
    """Run demultiplex statistic analysis on all multiplexed run
    """
    run_pipeline()
    
def list_samples():
    """Print list of multiplexed samples with extra information
    """
    runs = MultiplexedRuns()
    for run in runs.runs:
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
        # get all fastq files associated to demultiplexed lanes for this run
        fastq_files = runs.getKnownMultiplexSeqFiles(run)
        for fastq_file in fastq_files:
            # checking which host to copy the data from sol01 or sol03
            if env.host == fastq_file.host or env.host == 'localhost':
                log.info("%s\t%s\t%s\t%s" % (run.runNumber, fastq_file.host, fastq_file.path, fastq_file.filename))
                orig = os.path.join(fastq_file.path, fastq_file.filename)
                dest = os.path.join(run_analysis_folder, fastq_file.filename)
                _copy_file(orig, dest)
                                        
def setup_pipeline():
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")

    ### load index templates for all multiplex kits
    multiplex_templates={}
    for multiplex_name in list(MULTIPLEX_KIT.viewkeys()):
        barcodes_url = "http://uk-cri-ldmz02.crnet.org/shared/multiplexing/%s" % MULTIPLEX_KIT[multiplex_name]
        barcodes = urllib2.urlopen(barcodes_url)
        template = {}
        for barcode in barcodes:
            barcode_name, barcode_num, barcode_sequence = barcode.rstrip().split(',')
            template[barcode_sequence] = barcode_name
        multiplex_templates[multiplex_name] = template
    
    runs = MultiplexedRuns()
    for run in runs.runs:
        run_folder = os.path.join(env.root_path, run.pipelinePath)
        fastq_files = runs.getKnownMultiplexSeqFiles(run)

        ### configure fastq files
        # create primary folder
        primary_folder = os.path.join(run_folder, 'primary')
        _create_dir(primary_folder)
        # create symlink for fastq files in primary directory
        for fastq_file in fastq_files:
            new_fastq_filename = runs.getNewSeqFileName(fastq_file)
            link_name = "%s/%s" % (primary_folder, new_fastq_filename)
            fastq_path = os.path.join(run_folder, fastq_file.filename)
            log.debug(fastq_path)
            if os.path.lexists(link_name):
                os.remove(link_name)
            os.symlink(fastq_path, link_name)

        ### setup demux pipeline
        pipeline_directory = os.path.join(run_folder, 'demultiplex')
        setup_script_path = os.path.join(pipeline_directory, autoanalysis.SETUP_SCRIPT_FILENAME)
        run_scrip_path = os.path.join(pipeline_directory, autoanalysis.RUN_SCRIPT_FILENAME)
        # remove setup script if already exists
        if os.path.exists(setup_script_path):
            os.remove(setup_script_path)
        # set specific demux-stats pipeline options
        autoanalysis.PIPELINES_SETUP_OPTIONS['demultiplex'] = '' # do not generate index-files
        autoanalysis.CREATE_METAFILE_FILENAME = 'create-metafile'
        # call setup_pipelines to create setup script and run-meta.xml (dry-run=False)
        autoanalysis.setup_pipelines(run_folder, run.runNumber, {'demultiplex' : ''}, env.soft_pipeline_path, autoanalysis.SOAP_URL, False)
        # remove run script if already exists
        if os.path.exists(run_scrip_path):
            os.remove(run_scrip_path)
        # call run_pipelines to create run script
        autoanalysis.run_pipelines(run_folder, run.runNumber, {'demultiplex' : ''}, env.soft_pipeline_path, autoanalysis.CLUSTER_HOST)
            
        ### create index files
        for fastq_file in fastq_files:
            index_filename = runs.getIndexFileName(fastq_file)
            multiplex_type = runs.getMultiplexTypeFromSeqFile(fastq_file)
            barcodes = multiplex_templates[multiplex_type.name]
            log.debug(multiplex_type.name)
            index_path = os.path.join(pipeline_directory, index_filename)
            index_file = open(index_path, 'w')
            for barcode_seq in list(barcodes.viewkeys()):
                index_file.write("%s\t%s.%s.%s.fq.gz\n" % (barcode_seq, runs.getSlxSampleId(fastq_file), barcodes[barcode_seq], runs.getRunLaneRead(fastq_file)))
            index_file.close()
            log.info('%s created' % index_path)
            
def run_pipeline():
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")
    runs = MultiplexedRuns()
    for run in runs.runs:
        run_folder = os.path.join(env.root_path, run.pipelinePath)
        # call run_pipelines to run the demultiplex pipeline (dry-run=False)
        autoanalysis.run_pipelines(run_folder, run.runNumber, {'demultiplex' : ''}, env.soft_pipeline_path, autoanalysis.CLUSTER_HOST, False)
    
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
                # select multiplexed runs
                if run.multiplexed == 1:
                    self.runs.append(run)
                    
    def getKnownMultiplexSeqFiles(self, run):
        sequence_files = []
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            # select multiplexed lane
            if lane.isControl == 0 and lane.multiplexing_id != None:
                multiplex_type = self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()
                if multiplex_type.name != 'Other':
                    # select all files for multiplexed lanes of known type
                    file_locations = self.lims_db.analysisfileuri.filter_by(owner_id=lane.sampleProcess_id)
                    for file_location in file_locations:
                        file_type = self.lims_db.analysisfiletype.filter_by(id=file_location.type_id).one()
                        # select only FastQ files 
                        if file_location.scheme == 'FILE' and file_location.role == 'ARCHIVE' and file_type.name == 'FastQ':
                            # select only non-demultiplexed fastQ files
                            if 'Data/Intensities/' in file_location.path or 'primary' in file_location.path:
                                sequence_files.append(file_location)
        return sequence_files
    
    def getMultiplexTypeFromSeqFile(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        return self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()
    
    def getLaneFromSeqFile(self, analysisfileuri):
        return self.solexa_db.lane.filter_by(sampleProcess_id=analysisfileuri.owner_id).one()
        
    def getNewSeqFileName(self, analysisfileuri):
        return "%s.%s.fq.gz" % (self.getSlxSampleId(analysisfileuri), self.getRunLaneRead(analysisfileuri))
        
    def getIndexFileName(self, analysisfileuri):
        return "index.%s.txt" % self.getRunLaneRead(analysisfileuri)
    
    def getSlxSampleId(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        return lane.genomicsSampleId
        
    def getRunLaneRead(self, analysisfileuri):
        lane = self.getLaneFromSeqFile(analysisfileuri)
        run = self.solexa_db.solexarun.filter_by(id=lane.run_id).one()
        read_number = self.getReadNumber(analysisfileuri.filename)
        return "%s.s_%s.r_%s" % (run.runNumber, lane.lane, read_number)

    def getReadNumber(self, file_name):
        if 'sequence.txt.gz' in file_name:
            read_number = file_name[file_name.find('s_')+4:file_name.find('_sequence.txt.gz')]
            if read_number == '':
                read_number = '1'
            return read_number
        else:
            log.warning('sequence.txt.gz not found in %s' % file_name)
            return 1

    def printSampleDetails(self, run):
        lanes = self.solexa_db.lane.filter_by(run_id=run.id)
        for lane in lanes:
            # select multiplexed lanes
            if lane.isControl == 0 and lane.multiplexing_id != None:
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
                # multiplex type
                multiplex_type = self.solexa_db.multiplexing.filter_by(id=lane.multiplexing_id).one()
                if multiplex_type.name == 'Other':
                    multiplex_type_name = "*** %s ***" % multiplex_type.shortName
                else:
                    multiplex_type_name = multiplex_type.shortName

                print ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (multiplex_type_name, run.runNumber, lane.genomicsSampleId, run.deviceType, lane.sequenceType, lane.endType, lane.cycles, lane.userSampleId, username, str_comment ))
                
      