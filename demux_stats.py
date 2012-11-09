#!/usr/bin/env python
# encoding: utf-8
"""
demux_stats.py

Created by Anne Pajon on 2012-10-01.

Usage:
    fab -f demux_stats.py local install
or  fab -f demux_stats.py remote install
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
import lims
import autoanalysis

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
def cluster():
    """Setup environment for demultiplex statistic analysis on lustre
    """
    env.user = 'solexa'
    env.hosts = ['localhost']
    env.root_path = '/lustre/mib-cri/solexa/DemuxStats'
    env.soft_pipeline_path = autoanalysis.SOFT_PIPELINE_PATH
    
def remote():
    """Setup environment for installing data on lustre
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

def list_samples():
    """Print list of multiplexed samples with extra information
    """
    runs = lims.MultiplexedRuns()
    for run in runs.filtered_runs:
        runs.printSampleDetails(run)
        
def install_data():
    """Install fastq file on lustre
    """
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")
    
    # create root_path if not exists
    if not exists(env.root_path):
        run("mkdir %s" % env.root_path)
    
    # get all multiplexed runs
    runs = lims.MultiplexedRuns()
    for run in runs.filtered_runs:
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
                                        
def setup_demux():
    """Setup demultiplex statistic analysis on all multiplexed run
    """
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")

    ### load index templates for all multiplex kits
    multiplex_templates={}
    for multiplex_name in list(MULTIPLEX_KIT.viewkeys()):
        # barcode id to sequence mapping: barcode_id,barcode_num,barcode_sequence
        barcodes_url = "http://uk-cri-ldmz02.crnet.org/shared/multiplexing/%s" % MULTIPLEX_KIT[multiplex_name]
        barcodes = urllib2.urlopen(barcodes_url)
        barcodes_sequence = {}
        for barcode in barcodes:
            barcode_id, barcode_num, barcode_sequence = barcode.rstrip().split(',')
            barcodes_sequence[barcode_id] = barcode_sequence

        # barcode templates: barcode_id1,barcode_id2,sample_name with header
        samplesheet_url = "http://uk-cri-ldmz02.crnet.org/shared/multiplexing/defaults/%s" % MULTIPLEX_KIT[multiplex_name]
        samplesheet = urllib2.urlopen(samplesheet_url)
        template = {}
        header = True
        for sample in samplesheet:
            if header:
                header = False
            else:
                columns = sample.rstrip().split(',')
                if len(columns) == 2:
                    barcode_id=columns[0]
                    sample_name=columns[1]
                    template[sample_name] = barcodes_sequence[barcode_id]
                else: 
                    if len(columns) == 3:
                        barcode_id1=columns[0]
                        barcode_id2=columns[1]
                        sample_name=columns[2]
                        template[sample_name] = "%s\t%s" % (barcodes_sequence[barcode_id1], barcodes_sequence[barcode_id1])
                    else:
                        log.error('number of columns in %s not equal to 2 or 3.' % samplesheet_url)
        multiplex_templates[multiplex_name] = template
    
    runs = lims.MultiplexedRuns()
    for run in runs.filtered_runs:
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
        autoanalysis.setup_pipelines(run_folder, run.runNumber, {'demultiplex' : ''}, env.soft_pipeline_path, lims.SOAP_URL, False)
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
            for barcode_name in list(barcodes.viewkeys()):
                index_file.write("%s\t%s.%s.%s.fq.gz\n" % (barcodes[barcode_name], runs.getSlxSampleId(fastq_file), barcode_name, runs.getRunLaneRead(fastq_file)))
            index_file.close()
            log.info('%s created' % index_path)
            
def run_demux():
    """Run demultiplex statistic analysis on all multiplexed run
    """
    # current host
    log.debug("################################################################################")
    log.debug(env.host)
    log.debug("################################################################################")
    runs = lims.MultiplexedRuns()
    for run in runs.filtered_runs:
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
                    
      