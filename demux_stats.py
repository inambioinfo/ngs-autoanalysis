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
import argparse
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
import pipelines

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
# UTILITY METHODS
################################################################################
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
                        template[sample_name] = "%s\t%s" % (barcodes_sequence[barcode_id1], barcodes_sequence[barcode_id2])
                    else:
                        log.error('number of columns in %s not equal to 2 or 3.' % samplesheet_url)
        multiplex_templates[multiplex_name] = template
    return multiplex_templates

def create_html_report(report, html_filename):
    html_file = open(html_filename, 'w')
    report_table_lanes = ''
    for barcode_summary in report:
        report_table_lanes += "<tr><td><a href='http://uk-cri-lsol03.crnet.org:8080/solexa/%s'>%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (barcode_summary['summary_file'], os.path.basename(barcode_summary['summary_file'])[15:-4], barcode_summary['zero_error_match'], barcode_summary['zero_or_one_error_match'], barcode_summary['no_match'], barcode_summary['most_frequent'], barcode_summary['least_frequent'], barcode_summary['barcode_found'])
    html_file.write(HTML_TEMPLATE % report_table_lanes)
    html_file.close()
    
################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/DemuxStats'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--dburl", dest="dburl", action="store", default=lims.DB_URL, help="database url [read only access] - default set to '%s'" % lims.DB_URL)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--run", dest="run_number", action="store", help="run number e.g. '948'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_argument("--logfile", dest="logfile", action="store", help="File to print logging information")
    parser.add_argument("--htmlfile", dest="htmlfile", action="store", help="HTML file to write the report")
    parser.add_argument("--sample-list", dest="sample_list", action="store_true", default=False, help="Print list of multiplexed samples with extra information")

    options = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
                      
    if not os.path.exists(options.basedir):
        sys.exit("%s does not exists - check your '--basedir' option" % options.basedir)
    
    # create soap client
    soap_client = lims.SoapLims()
    # create lims client
    runs = lims.Runs(options.dburl)
    # create multiplexing templates
    multiplex_templates = get_multiplex_templates()
    summary_report = []
    # loop over all multiplexed runs that have been analysed or just one run
    for run in runs.findAllAnalysedMultiplexedRuns(options.run_number):
        log.info('--------------------------------------------------------------------------------')
        log.info('--- RUN: %s' % run.runNumber)
        log.info('--------------------------------------------------------------------------------')
        # create run folder in basedir for analysis
        run_folder = os.path.join(options.basedir, run.pipelinePath)
        utils.create_directory(run_folder)
        # create run definition
        run_definition = pipelines.RunDefinition(options.basedir, options.basedir, run)
        
        if run_definition.ready_to_analyse():
            # create pipeline
            demux_stat = pipelines.DemuxStatsPipelines(run_definition, multiplex_templates, runs, soap_client, options.softdir, options.cluster, options.dry_run)
            # execute pipeline
            demux_stat.execute_demux()
            # parse barcode summary files
            summary_report.extend(demux_stat.parse_summary_files())
        else:
            log.warn('run folder %s does not exists - demux-stats will not run' % run_folder)
        
        if options.htmlfile:
            create_html_report(summary_report, options.htmlfile)
        if options.sample_list:
            runs.printSampleDetails(run)    

if __name__ == "__main__":
	main()

                    
      