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

# import custom modules
import log as logger
import glsclient
import glssql

WORKFLOW_MAPPING = {
'HiSeq': 'SLX: Sequencing for HiSeq v1',
'HiSeq Express': 'SLX: Sequencing for HiSeq Express v1',
'Resubmit for HiSeq': 'SLX: Resubmit for HiSeq v1',
'MiSeq': 'SLX: Sequencing for MiSeq v1',
'MiSeq Express': 'SLX: Sequencing for MiSeq Express v1',
'GAIIx': 'SLX: Sequencing for GAIIx v1',
'Resubmit for MiSeq': 'SLX: Resubmit for MiSeq v1',

'Truseq DNA with MiSeq': 'LPS: TruSeq DNA v3',
'Truseq RNA with MiSeq': 'LPS: TruSeq RNA v3',
'Truseq ChIPseq with MiSeq': 'LPS: TruSeq ChIP v3',
'Nextera with MiSeq': 'LPS: Nextera v2',
'Access Array with MiSeq': 'LPS: Access Array v3',
'Other - please contact genomics': 'LPS: Generic Library Prep with MiSeq',
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
            # projectname,artifactid,samplename,slxid,workflow
            try:                
                if row.workflow in WORKFLOW_MAPPING.keys():
                    details = "[%s,%s,%s,%s,%s] to be assigned to workflow '%s'" % (row.artifactid, row.projectname, row.samplename, row.slxid, row.workflow, WORKFLOW_MAPPING[row.workflow])
                    miseqexpress_details = "%s\t| %s\t| %s\t| %s\t| %s" % (row.slxid, row.projectname, row.researcher, row.readlength, row.seqtype)
                    report_assignedsamples += details + "\n"
                    log.info(details)
                    if options.update:
                        workflows = glsutil.api.listFilterByName('workflow', WORKFLOW_MAPPING[row.workflow])
                        workflow = workflows.workflow[0]
                        log.debug(workflow)
                        artifact = glsutil.api.load('artifact', row.artifactid)
                        glsutil.routeEachArtifactToWorkflow([artifact.uri], WORKFLOW_MAPPING[row.workflow])
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