#!/usr/bin/env python
# encoding: utf-8
"""
autoassignsamples.py

Created by Anne Pajon on 2013-05-14.

"""

import sys
import os
import logging
import argparse
# email modules
import smtplib
from email.mime.text import MIMEText
# time module
import datetime

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient
import glsclient.glssql as glssql

WORKFLOW_MAPPING = {
'HiSeq': 'SLX: Sequencing for HiSeq v1',
'HiSeq 2000':'SLX: Sequencing for HiSeq 2000 v1',
'HiSeq 2-lane': 'SLX: Sequencing for HiSeq Rapid Run v1',
'HiSeq Express': 'SLX: Sequencing for HiSeq Express v1',
'Resubmit for HiSeq': 'SLX: Resubmit for HiSeq v1',
'MiSeq': 'SLX: Sequencing for MiSeq v1',
'MiSeq Express': 'SLX: Sequencing for MiSeq Express v1',
'GAIIx': 'SLX: Sequencing for GAIIx v1',
'Resubmit for MiSeq': 'SLX: Resubmit for MiSeq v1',

# New LPP submission form v16
'Truseq stranded mRNA': 'LPS: TruSeq RNA v3',
'Nextera': 'LPS: Nextera v2',
'Access Array': 'LPS: Access Array v3',
'ChIP Seq': 'LPS: TruSeq ChIP v3',
'Nextera Rapid Exome': 'LPS: Rapid Exome',
'Other - please contact genomics': 'LPS: Generic Library Prep with MiSeq',

# Old LPP submission - to be deleted later
'Truseq DNA with MiSeq': 'LPS: TruSeq DNA v3',
'Truseq RNA with MiSeq': 'LPS: TruSeq RNA v3',
'Truseq ChIPseq with MiSeq': 'LPS: TruSeq ChIP v3',
'Nextera with MiSeq': 'LPS: Nextera v2',
'Access Array with MiSeq': 'LPS: Access Array v3',

}

def send_email(txt_msg):
    msg = MIMEText("""
Samples assigned to MiSeq Express workflow:

%s
--
Anne Pajon, CRI Bioinformatics Core
anne.pajon@cruk.cam.ac.uk | +44 (0)1223 769 631
""" % txt_msg)
    
    me = 'anne.pajon@cruk.cam.ac.uk'
    you = 'genomics@cruk.cam.ac.uk'
    msg['Subject'] = 'Automatic MiSeq Express Notification'
    msg['From'] = me
    msg['To'] = you
    msg['Cc'] = me
    
    #s = smtplib.SMTP('uk-lif-lexb02.crwin.crnet.org')
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [me, you], msg.as_string())
    s.quit()


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to preform the update and not only report action")
    parser.add_argument("--updatesamples", dest="updatesamples", action="store_true", default=False, help="use this option to set the date received on sample and not only report action")
    parser.add_argument("--limsdev", dest="limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--email", dest="email", action="store_true", default=False, help="Send email to genomics on MiSeq Express samples")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    try:
        # connect to lims
        if options.limsdev:
            lims_server = 'limsdev'
        else:
            lims_server = 'lims'
        glsutil = glsclient.GlsUtil(server=lims_server)
        results = glsutil.db.execute(glssql.UNASSIGNED_SAMPLES_QUERY).fetchall()
        
        count = 0
        count_miseqexpress = 0
        report_assignedsamples = ''
        report_unassignedsamples = ''
        # MiSeq Express report to include: SLXID | username | workflow | entype | seqtype
        report_miseqexpresssamples = 'SLX-ID\t| project\t| researcher\t| read length\t| seq. type\n'
        for row in results:
            # projectname,researchername,artifactid,samplename,slxid,workflow,readlength,seqtype,seqinfo,submissiondate,email
            try:                
                # update sample date received if empty
                if row.submissiondate is None or row.submissiondate == '':
                    log.info('No date received on sample %s' % row.samplename)
                    if options.updatesamples:
                        artifact = glsutil.api.load('artifact', row.artifactid)
                        sample = glsutil.api.load('sample', artifact.sample[0].limsid)
                        sample.date_received = str(datetime.date.today())
                        log.debug(sample.toxml('utf-8'))
                        updated_sample = glsutil.api.update(sample)
                        log.info('Date set to %s on sample %s' % (updated_sample.date_received, updated_sample.name))
                        log.debug(updated_sample.toxml('utf-8'))

                # assign samples to workflow
                if row.workflow in WORKFLOW_MAPPING.keys():
                    details = "[%s,%s,%s,%s,%s] to be assigned to workflow '%s'" % (row.artifactid, row.projectname, row.samplename, row.slxid, row.workflow, WORKFLOW_MAPPING[row.workflow])
                    miseqexpress_details = "%s\t| %s\t| %s\t| %s\t| %s" % (row.slxid, row.projectname, row.researcher, row.readlength, row.seqtype)
                    report_assignedsamples += details + "\n"
                    log.info(details)
                    if options.update:
                        workflows = glsutil.api.list_filter_by_name('workflow', WORKFLOW_MAPPING[row.workflow])
                        workflow = workflows.workflow[0]
                        log.debug(workflow)
                        artifact = glsutil.api.load('artifact', row.artifactid)
                        glsutil.route_each_artifact_to_workflow([artifact.uri], WORKFLOW_MAPPING[row.workflow])
                        count += 1
                        if row.workflow == 'MiSeq Express':
                            log.debug(miseqexpress_details)
                            report_miseqexpresssamples += miseqexpress_details + "\n"
                            count_miseqexpress += 1
                else:
                    details = "[%s,%s,%s,%s,%s] not assigned" % (row.artifactid, row.projectname, row.samplename, row.slxid, row.workflow)
                    report_unassignedsamples += details + "\n"
                    log.warn(details)
            except:
                log.exception("Unexpected error")
                continue

        # email sent to genomics for MiSeq Express
        report_miseqexpresssamples = "%s samples assigned to MiSeq Express workflow\n" % (count_miseqexpress) + report_miseqexpresssamples
        if options.email and count_miseqexpress > 0:
            send_email(report_miseqexpresssamples)
        log.debug('MISEQ EXPRESS REPORT')
        log.debug(report_miseqexpresssamples)
        log.info("%s samples assigned to workflows over %s" % (count, len(results)))
        log.info("%s samples assigned to MiSeq Express workflow" % (count_miseqexpress))
        if not options.update:
            log.info('use --update to perform the operation in the lims')
            
        print report_assignedsamples
        print report_unassignedsamples

    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()
