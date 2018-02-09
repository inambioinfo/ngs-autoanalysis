#!/usr/bin/env python
# encoding: utf-8
"""
autoassignsamples.py

Created by Anne Pajon on 2013-05-14.

"""

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
    'HiSeq 2500': 'SLX: Sequencing for HiSeq v1',
    'HiSeq 2000': 'SLX: Sequencing for HiSeq 2000 v1',
    'HiSeq 4000': 'SLX: Sequencing for HiSeq 4000 v1',
    'HiSeq 2-lane': 'SLX: Sequencing for HiSeq Rapid Run v1',
    'HiSeq Express': 'SLX: Sequencing for HiSeq Express v1',

    'MiSeq': 'SLX: Sequencing for MiSeq v1',
    'MiSeq Express': 'SLX: Sequencing for MiSeq Express v1',
    'Resubmit for MiSeq': 'SLX: Resubmit for MiSeq v1',
    # New MiSeq Nano workflows
    'MiSeq Nano': 'SLX: Sequencing for MiSeq Nano v1',
    'MiSeq Express Nano': 'SLX: Sequencing for MiSeq Express Nano v1',

    'GAIIx': 'SLX: Sequencing for GAIIx v1',

    # Mapping old UDF values to new NextSeq workflows
    'NextSeq Direct Mid Output': 'SLX: NextSeq Express Mid Output v1',
    'NextSeq Direct High Output': 'SLX: NextSeq Express High Output v1',
    # New NextSeq workflows
    'NextSeq Mid Output': 'SLX: NextSeq Mid Output v1',
    'NextSeq High Output': 'SLX: NextSeq High Output v1',
    'NextSeq Express Mid Output': 'SLX: NextSeq Express Mid Output v1',
    'NextSeq Express High Output': 'SLX: NextSeq Express High Output v1',

    # New LPP submission form v17
    'Truseq stranded mRNA': 'LPS: TruSeq RNA v4',  # was 'LPS: TruSeq RNA v3',
    'TruSeq Rapid Exome': 'LPS: TruSeq Rapid Exome v2',
    'Nextera DNA/XT': 'LPS: Nextera v3',  # was 'LPS: Nextera v2',
    'Access Array': 'LPS: Access Array v4',  # was 'LPS: Access Array v3',
    'ThruPLEX ChIP Seq': 'LPS: Thruplex ChIP',  # was 'LPS: TruSeq ChIP v3',
    'Nextera Rapid Exome': 'LPS: Nextera Rapid Capture',  # was 'LPS: Rapid Exome',
    # 'Other - please contact genomics': 'LPS: Generic Library Prep with MiSeq',

    # New 10X work flows
    '10X Chromium Single Cell': 'LPS: 10X Single Cell v2',
    '10X Chromium Genome': 'LPS: 10X Phased Genome v1'
}


def send_email(subject, txt_msg):
    msg = MIMEText("""
%s
--
Anne Pajon, CRUK-CI Bioinformatics Core
anne.pajon@cruk.cam.ac.uk | +44 (0)1223 769 631
""" % txt_msg)

    me = 'anne.pajon@cruk.cam.ac.uk'
    you = 'genomics@cruk.cam.ac.uk'
    msg['Subject'] = 'Automatic %s Notification' % subject
    msg['From'] = me
    msg['To'] = you
    msg['Cc'] = me

    s = smtplib.SMTP('smtp.cruk.cam.ac.uk')
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
        lims_server = glsclient.SERVER
        if options.limsdev:
            lims_server = glsclient.TEST_SERVER
        glsutil = glsclient.GlsUtil(server=lims_server)
        glsutil.db.execute(glssql.UNASSIGNED_SAMPLES_QUERY)
        results = glsutil.db.fetchall()

        count = 0
        count_miseqexpress = 0
        count_nextseqdirect = 0
        count_unknownworkflow = 0
        report_assignedsamples = ''
        report_unassignedsamples = ''
        # MiSeq Express report to include: SLXID | username | workflow | entype | seqtype
        report_miseqexpresssamples = 'SLX-ID\t| project\t| researcher\t| read length\t| seq. type\n'
        # NextSeq Direct report to include: SLXID | username | workflow | entype | seqtype
        report_nextseqdirectsamples = 'SLX-ID\t| project\t| researcher\t| read length\t| seq. type\n'
        # Unassigned samples report to include: SLXID | username | workflow | entype | seqtype
        report_unknownworkflowsamples = 'SLX-ID\t| project\t| researcher\t| read length\t| seq. type\n'
        for row in results:
            # projectname,researchername,artifactid,samplename,slxid,workflow,readlength,seqtype,seqinfo,submissiondate,email
            try:
                # update sample date received if empty
                if row['submissiondate'] is None or row['submissiondate'] == '':
                    log.info('No date received on sample %s' % row['samplename'])
                    if options.updatesamples:
                        artifact = glsutil.api.load('artifact', row['artifactid'])
                        sample = glsutil.api.load('sample', artifact.sample[0].limsid)
                        sample.date_received = str(datetime.date.today())
                        log.debug(sample.toxml('utf-8'))
                        updated_sample = glsutil.api.update(sample)
                        log.info('Date set to %s on sample %s' % (updated_sample.date_received, updated_sample.name))
                        log.debug(updated_sample.toxml('utf-8'))


                # assign samples to workflow
                if row['workflow'] in WORKFLOW_MAPPING.keys():
                    details = "[%s,%s,%s,%s,%s] to be assigned to workflow '%s'" % (row['artifactid'], row['projectname'], row['samplename'], row['slxid'], row['workflow'], WORKFLOW_MAPPING[row['workflow']])
                    detailed_info_for_report = "%s\t| %s\t| %s\t| %s\t| %s" % (row['slxid'], row['projectname'], row['researcher'], row['readlength'], row['seqtype'])
                    report_assignedsamples += details + "\n"
                    log.info(details)
                    if options.update:
                        workflows = glsutil.api.list_filter_by_name('workflow', WORKFLOW_MAPPING[row['workflow']])
                        workflow = workflows.workflow[0]
                        log.debug(workflow)
                        artifact = glsutil.api.load('artifact', row['artifactid'])
                        glsutil.route_each_artifact_to_workflow([artifact.uri], WORKFLOW_MAPPING[row['workflow']])
                        count += 1
                        if row['workflow'] == 'MiSeq Express':
                            log.debug(detailed_info_for_report)
                            report_miseqexpresssamples += detailed_info_for_report + "\n"
                            count_miseqexpress += 1
                        if row['workflow'].startswith('NextSeq Direct') or row['workflow'].startswith('NextSeq Express'):
                            log.debug(detailed_info_for_report)
                            report_nextseqdirectsamples += detailed_info_for_report + "\n"
                            count_nextseqdirect += 1
                else:
                    details = "[%s,%s,%s,%s,%s] not assigned" % (row['artifactid'], row['projectname'], row['samplename'], row['slxid'], row['workflow'])
                    detailed_info_for_report = "%s\t| %s\t| %s\t| %s\t| %s\t| %s" % (row['slxid'], row['projectname'], row['researcher'], row['readlength'], row['seqtype'], row['workflow'])
                    report_unassignedsamples += details + "\n"
                    log.warn(details)
                    report_unknownworkflowsamples += detailed_info_for_report + "\n"
                    count_unknownworkflow += 1
            except:
                log.exception("Unexpected error")
                continue

        # email sent to genomics for MiSeq Express
        report_miseqexpresssamples = "%s samples assigned to MiSeq Express workflow:\n\n" % count_miseqexpress + report_miseqexpresssamples
        if options.email and count_miseqexpress > 0:
            send_email('MiSeq Express', report_miseqexpresssamples)
        log.info('MISEQ EXPRESS REPORT')
        log.info(report_miseqexpresssamples)

        # email sent to genomics for NextSeq Direct
        report_nextseqdirectsamples = "%s samples assigned to NextSeq Express workflow:\n\n" % count_nextseqdirect + report_nextseqdirectsamples
        if options.email and count_nextseqdirect > 0:
            send_email('NextSeq Express', report_nextseqdirectsamples)
        log.info('NEXTSEQ EXPRESS REPORT')
        log.info(report_nextseqdirectsamples)

        # email sent to genomics for unknown workflow
        report_unknownworkflowsamples = "%s samples unassigned to workflow:\n\n" % count_unknownworkflow + report_unknownworkflowsamples
        if options.email and count_unknownworkflow > 0:
            send_email('Unknown Workflow', report_unknownworkflowsamples)
        log.info('UNKNOWN WORKFLOW REPORT')
        log.info(report_unknownworkflowsamples)

        log.info("%s samples assigned to workflows over %s" % (count, len(results)))
        log.info("%s samples assigned to MiSeq Express workflow" % count_miseqexpress)
        log.info("%s samples assigned to NextSeq Direct workflow" % count_nextseqdirect)
        log.info("%s samples unassigned to any workflow" % count_unknownworkflow)

        if not options.update:
            log.info('use --update to perform the operation in the lims')

        print report_assignedsamples
        print report_unassignedsamples

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
