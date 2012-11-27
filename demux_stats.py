#!/usr/bin/env python
# encoding: utf-8
"""
demux_stats.py

$Id$

Created by Anne Pajon on 2012-10-01.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import optparse
import urllib2

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from suds.client import Client
except ImportError:
    sys.exit('''
--------------------------------------------------------------------------------
>>> modules { mysql-python | sqlalchemy | suds } not installed.
--------------------------------------------------------------------------------
[on sols] use /home/mib-cri/software/python2.7/bin/python
[locally] install virtualenv; source bin/activate and pip install modules
--------------------------------------------------------------------------------
''')

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import lims
import autoanalysis

################################################################################
# CONSTANTS
################################################################################
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

# Default filenames
LOCK_FILENAME = "demux-stats.lock"
IGNORE_FILENAME = "demux-stats.ignore"

COPY_SCRIPT_FILENAME = 'copy.sh'
COPY_STARTED_FILENAME = 'copy.started'
COPY_FINISHED_FILENAME = 'copy.ended'

CLEAN_SCRIPT_FILENAME = 'clean.sh'
CLEAN_STARTED_FILENAME = 'clean.started'
CLEAN_FINISHED_FILENAME = 'clean.ended'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
   <body>
      <table border="1">
         <tr><th>Summary file</th><th>0 error</th><th>0 or 1 error</th><th>no match</th><th>most frequent index</th><th>least frequent index</th><th>most frequent barcodes found in pool</th></tr>
         %s
      </table>
   </body>
</html>
"""

################################################################################
# DEMUX STATS PIPELINE METHODS
################################################################################
def manage_data(run_folder, fastq_files, dry_run):
    """Create and run scripts to copy and clean fastq file on lustre
    """
    copy_script_path = os.path.join(run_folder, COPY_SCRIPT_FILENAME)
    copy_started = os.path.join(run_folder, COPY_STARTED_FILENAME)
    copy_finished = os.path.join(run_folder, COPY_FINISHED_FILENAME)
    lock = os.path.join(os.path.dirname(run_folder), LOCK_FILENAME)
    clean_script_path = os.path.join(run_folder, CLEAN_SCRIPT_FILENAME)
    clean_started = os.path.join(run_folder, CLEAN_STARTED_FILENAME)
    clean_finished = os.path.join(run_folder, CLEAN_FINISHED_FILENAME)
    
    copy = ""
    clean = ""
    for fastq_file in fastq_files:
        log.debug("%s\t%s\t%s" % (fastq_file.host, fastq_file.path, fastq_file.filename))
        orig = os.path.join(fastq_file.path, fastq_file.filename)
        dest = os.path.join(run_folder, fastq_file.filename)
        copy = copy + "scp %s:%s %s; " % (fastq_file.host, orig, dest)
        clean = clean + "rm -f %s; " % dest
        
    create_script(copy_script_path, copy, copy_started, copy_finished, lock)
    run_script(copy_script_path, copy_started, copy_finished, lock, dry_run)
    create_script(clean_script_path, clean, clean_started, clean_finished) 
    if process_completed(run_folder):
        run_script(clean_script_path, clean_started, clean_finished, dry_run)   

def get_multiplex_templates():
    """Load index templates for all multiplex kits
    """
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
    return multiplex_templates
                     
def setup_demux(runs, run_folder, run_number, multiplex_templates, fastq_files, cluster, software_path):
    """Setup demultiplex statistic analysis
    """
    ### configure fastq files
    # create primary folder
    primary_folder = os.path.join(run_folder, 'primary')
    utils.create_directory(primary_folder)
    # create symlink for fastq files in primary directory
    if data_copied(run_folder):
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
    # set specific demux-stats pipeline options
    autoanalysis.PIPELINES_SETUP_OPTIONS['demultiplex'] = '--pipeline=/home/mib-cri/software/pipelines/demultiplex/demuxstatspipeline.xml' # do not generate index-files
    autoanalysis.CREATE_METAFILE_FILENAME = 'create-metafile'
    # call setup_pipelines to create setup script and run-meta.xml (dry-run=False)
    autoanalysis.setup_pipelines(run_folder, run_number, {'demultiplex' : ''}, software_path, lims.SOAP_URL, False)
    # call run_pipelines to create run script
    autoanalysis.run_pipelines(run_folder, run_number, {'demultiplex' : ''}, software_path, cluster)
        
    ### create index files
    for fastq_file in fastq_files:
        index_filename = runs.getIndexFileName(fastq_file)
        index_path = os.path.join(pipeline_directory, index_filename)
        if not os.path.exists(index_path):
            multiplex_type = runs.getMultiplexTypeFromSeqFile(fastq_file)
            barcodes = multiplex_templates[multiplex_type.name]
            log.debug(multiplex_type.name)
            index_file = open(index_path, 'w')
            for barcode_name in list(barcodes.viewkeys()):
                index_file.write("%s\t%s.%s.%s.fq.gz\n" % (barcodes[barcode_name], runs.getSlxSampleId(fastq_file), barcode_name, runs.getRunLaneRead(fastq_file)))
            index_file.close()
            log.info('%s created' % index_path)
        else:
            log.debug('%s already exists' % index_path)
            
def run_demux(run_folder, run_number, cluster, software_path):
    """Run demultiplex statistic analysis
    """
    lock = os.path.join(os.path.dirname(run_folder), LOCK_FILENAME)
    if process_completed(run_folder):
        if os.path.exists(lock):
            os.remove(lock)
    else:
        if not os.path.exists(lock) and data_copied(run_folder):
            utils.touch(lock)
            # call run_pipelines to run the demultiplex pipeline (dry-run=False)
            autoanalysis.run_pipelines(run_folder, run_number, {'demultiplex' : ''}, software_path, cluster, False)
        else:
            log.info('%s presents - another script is running' % lock)
            
def parse_summary_files(run_folder):
    """Parse barcode summary files and print demultiplex report
    Read each BarcodeSummary.SLX-4783.787.s_8.txt file and print report
    """
    report = []
    if process_completed(run_folder):
        pipeline_directory = os.path.join(run_folder, 'demultiplex')
        summary_files = glob.glob(os.path.join(pipeline_directory, 'BarcodeSummary.*.txt'))
        for summary_file in summary_files:
            with open(summary_file, 'r') as summary:
                barcode_summary = {}
                barcode_match = {}
                barcode_found = []
                distinct_barcodes = False
                for line in summary:
                    columns = line.strip().split()
                    if len(columns) == 7:
                        barcode_match[columns[0]] = [columns[1], columns[3], columns[5]]
                    elif columns[-1] == 'reads':
                        barcode_summary['total_reads'] = int(columns[0])
                    elif columns[-1] == 'lost':
                        barcode_summary['no_match'] = int(columns[0])
                    elif columns[-1] == 'codes':
                        distinct_barcodes = True
                        barcode_summary['distinct_barcodes'] = int(columns[0])
                    elif distinct_barcodes and len(columns) == 2:
                        barcode_found.append(columns[-1])

            zero_error_reads = 0
            one_error_reads = 0 
            most_frequent = 0
            least_frequent = barcode_summary['total_reads']
            for barcode in list(barcode_match.viewkeys()):
                total_reads = int(barcode_match[barcode][0])
                if total_reads > most_frequent:
                    most_frequent = total_reads
                if not total_reads == 0:
                    if total_reads < least_frequent :
                        least_frequent = total_reads
                zero_error_reads += int(barcode_match[barcode][1])
                one_error_reads += int(barcode_match[barcode][2])

            barcode_summary['most_frequent'] = float((most_frequent * 100 ) / barcode_summary['total_reads'])
            barcode_summary['least_frequent'] = float((least_frequent * 100 ) / barcode_summary['total_reads'])
            barcode_summary['zero_error_match'] = float((zero_error_reads * 100 ) / barcode_summary['total_reads'])
            barcode_summary['zero_or_one_error_match'] = float(((zero_error_reads + one_error_reads) * 100 ) / barcode_summary['total_reads'])
            barcode_summary['no_match'] = float((barcode_summary['no_match'] * 100) / barcode_summary['total_reads'])
            if len(barcode_found) > 0:
                barcode_summary['barcode_found'] = ':'.join(barcode_found)
            else:
                barcode_summary['barcode_found'] = 'none'
            barcode_summary['summary_file'] = summary_file
            
            report.append(barcode_summary)
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (os.path.basename(summary_file), barcode_summary['zero_error_match'], barcode_summary['zero_or_one_error_match'], barcode_summary['no_match'], barcode_summary['most_frequent'], barcode_summary['least_frequent'], barcode_summary['barcode_found'])
    return report

################################################################################
# UTILITY METHODS
################################################################################
def create_script(script_path, cmd, started, ended, lock=None):
    if not os.path.exists(script_path):
        script_file = open(script_path, 'w')
        if lock:
            command = "touch %s; touch %s; %s touch %s; rm %s" % (lock, started, cmd, ended, lock)
        else:
            command = "touch %s; %s touch %s" % (started, cmd, ended)
        script_file.write(utils.LOCAL_SCRIPT_TEMPLATE % {'cmd':command})
        script_file.close()
        os.chmod(script_path, 0755)
        log.info('%s created' % script_path)
    else:
        log.debug('%s already exists' % script_path)

def run_script(script_path, started, ended, lock=None, dry_run=False):
    """Run script
    """
    if os.path.exists(script_path):
        if not os.path.exists(started):
            if lock:
                if not os.path.exists(lock):
                    utils.touch(lock)
                    utils.run_bg_process(['sh', '%s' % script_path], dry_run)
                else:
                    log.info('%s presents - another script is running' % lock)
            else:
                utils.run_bg_process(['sh', '%s' % script_path], dry_run)
        else:
            if not os.path.exists(ended):
                log.info('script is currently running')
            else:
                log.info('script has finished')
    else:
        log.warn('%s is missing' % script_path)
    
def create_html_report(report, html_filename):
    html_file = open(html_filename, 'w')
    report_table_lanes = ''
    for barcode_summary in report:
        report_table_lanes += "<tr><td><a href='http://uk-cri-lsol03.crnet.org:8080/solexa/%s'>%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (barcode_summary['summary_file'], os.path.basename(barcode_summary['summary_file']), barcode_summary['zero_error_match'], barcode_summary['zero_or_one_error_match'], barcode_summary['no_match'], barcode_summary['most_frequent'], barcode_summary['least_frequent'], barcode_summary['barcode_found'])
    html_file.write(HTML_TEMPLATE % report_table_lanes)
    html_file.close()
    
def process_completed(run_folder):
    demux_directory = os.path.join(run_folder, 'demultiplex')
    demux_started = os.path.join(demux_directory, autoanalysis.PIPELINE_STARTED_FILENAME)
    demux_finished = os.path.join(demux_directory, autoanalysis.PIPELINE_FINISHED_FILENAME)
    # pipeline not finished or started
    if not os.path.exists(demux_started) or not os.path.exists(demux_finished):
        return False
    return True
    
def process_failed(run_folder):
    demux_directory = os.path.join(run_folder, 'demultiplex')
    demux_started = os.path.join(demux_directory, autoanalysis.PIPELINE_STARTED_FILENAME)
    demux_finished = os.path.join(demux_directory, autoanalysis.PIPELINE_FINISHED_FILENAME)
    if os.path.exists(demux_started) and not os.path.exists(demux_finished):
        job_output = glob.glob(os.path.join(demux_directory, '*.out'))
        if job_output:
            if not utils.output_job_success(job_output):
                return True
    return False

def data_copied(run_folder):
    copy_started = os.path.join(run_folder, COPY_STARTED_FILENAME)
    copy_finished = os.path.join(run_folder, COPY_FINISHED_FILENAME)
    if not os.path.exists(copy_started) or not os.path.exists(copy_finished):
        return False
    return True
    
def all_process_completed(run_folder):
    clean_started = os.path.join(run_folder, CLEAN_STARTED_FILENAME)
    clean_finished = os.path.join(run_folder, CLEAN_FINISHED_FILENAME)
    if not data_copied(run_folder) or not process_completed(run_folder):
        return False
    if not os.path.exists(clean_started) or not os.path.exists(clean_finished):
        return False
    return True
    
################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = optparse.OptionParser()
    parser.add_option("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/DemuxStats'")
    parser.add_option("--softdir", dest="softdir", action="store", default=autoanalysis.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % autoanalysis.SOFT_PIPELINE_PATH)
    parser.add_option("--dburl", dest="dburl", action="store", default=lims.DB_SOLEXA, help="database url [read only access] - default set to '%s'" % lims.DB_SOLEXA)
    parser.add_option("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % autoanalysis.CLUSTER_HOST)
    parser.add_option("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_option("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_option("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_option("--logfile", dest="logfile", action="store", help="File to print logging information")
    parser.add_option("--htmlfile", dest="htmlfile", action="store", help="HTML file to write the report")
    parser.add_option("--sample-list", dest="sample_list", action="store_true", default=False, help="Print list of multiplexed samples with extra information")

    (options, args) = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
              
    for option in ['basedir']:
        if getattr(options, option) == None:
            print "Please supply a --%s parameter.\n" % (option)
            sys.exit(parser.print_help())
        
    if not os.path.exists(options.basedir):
        sys.exit("%s does not exists - check your '--basedir' option" % options.basedir)
        
    runs = lims.MultiplexedRuns(options.dburl, options.run_number)
    multiplex_templates = get_multiplex_templates()
    summary_report = []
    for run in runs.filtered_runs:
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run.runNumber)
        log.info('--------------------------------------------------------------------------------')
        # create run folder in basedir for analysis
        run_folder = os.path.join(options.basedir, run.pipelinePath)
        utils.create_directory(run_folder)
        # get all fastq files associated to demultiplexed lanes for this run
        fastq_files = runs.getKnownMultiplexSeqFiles(run)
        # lock file
        lock = os.path.join(os.path.dirname(run_folder), LOCK_FILENAME)
        ignore = os.path.join(run_folder, IGNORE_FILENAME)
        if os.path.exists(run_folder):
            # check demux-stats.ignore is not present - stop running analysis if present
            if not os.path.exists(ignore):
                if not all_process_completed(run_folder):
                    if process_failed(run_folder):
                        log.info('*** [***FAIL***] ***************************************************************')
                        utils.touch(ignore)
                        # remove lock file
                        if os.path.exists(lock):
                            os.remove(lock)
                    else:
                        log.info('--- MANAGE DATA ----------------------------------------------------------------')
                        manage_data(run_folder, fastq_files, options.dry_run)
                        log.info('--- SETUP DEMUX STATS ----------------------------------------------------------')
                        setup_demux(runs, run_folder, run.runNumber, multiplex_templates, fastq_files, options.cluster, options.softdir)
                        log.info('--- RUN DEMUX STATS ------------------------------------------------------------')
                        run_demux(run_folder, run.runNumber, options.cluster, options.softdir)
                else:
                    log.info('--- DEMUX STATS REPORT ---------------------------------------------------------')
                    summary_report.extend(parse_summary_files(run_folder))
                    log.info('*** DEMUX-STATS COMPLETED ******************************************************')
            else:
                log.info('%s is present' % ignore)
        else:
            log.warn('run folder %s does not exists - deumx-stats will not run' % run_folder)
        if options.htmlfile:
            create_html_report(summary_report, options.htmlfile)
        if options.sample_list:
            runs.printSampleDetails(run)    

if __name__ == "__main__":
	main()

                    
      