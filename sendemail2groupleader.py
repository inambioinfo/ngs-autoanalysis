"""
Python script sendemail2groupleader

Created by Anne Pajon @pajanne on Thu 19 Jan 2017
"""

import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient


def send_email(log, group_name, send_to, account_list, do_send_email=False):
    send_from = 'genomics-helpdesk@cruk.cam.ac.uk'
    institute_send_to = 'Anne.Pajon@cruk.cam.ac.uk,James.Hadfield@cruk.cam.ac.uk,Hannah.Haydon@cruk.cam.ac.uk'
    msg = MIMEMultipart()
    msg['Subject'] = 'CRUK-CIGC Update of user accounts'
    msg['From'] = send_from
    msg['To'] = ','.join(send_to)
    msg.attach(MIMEText("""Dear %(group_name)s's group leader,

The CRUK Cambridge Institute Genomics Core (CIGC) NGS service is updating the information we hold for each account in our LIMS.
Please see below for a list of user accounts which are active under your group account.

%(account_list)s

Please email our helpdesk at genomics-helpdesk@cruk.cam.ac.uk if any of these accounts will no-longer be used so we can update our records accordingly.
Many thanks.

Best wishes,
The Genomics Core
--
CRUK Cambridge Institute Genomics Core (CIGC)
genomics-helpdesk@cruk.cam.ac.uk
    """ % {'group_name': group_name, 'account_list': account_list}))

    if not do_send_email:
        log.info(msg.as_string())
        log.info('Email will be sent to ' + ','.join(send_to + institute_send_to.split(',')) + ', use --send-email flag to send them')
    else:
        mail = smtplib.SMTP('mailrelay.cruk.cam.ac.uk')
        out = mail.sendmail(send_from, send_to + institute_send_to.split(','), msg.as_string())
        log.info('Email sent to ' + ','.join(send_to + institute_send_to.split(',')))
        if out:
            log.error(out)
        mail.quit()


def get_group_accounts(gls):
    query = """
SELECT researcher.firstname || ' ' || researcher.lastname as researcher,
principals.username,
researcher.email,
lab.name as group_name, ludf1.udfvalue as leader_emails, ludf2.udfvalue as approver_emails
FROM researcher, principals, lab
LEFT OUTER JOIN entity_udf_view as ludf1 on (ludf1.attachtoid=lab.labid and ludf1.udfname='Group Leader Email')
LEFT OUTER JOIN entity_udf_view as ludf2 on (ludf2.attachtoid=lab.labid and ludf2.udfname='Approvers')
WHERE researcher.labid = lab.labid
AND researcher.researcherid = principals.principalid
AND principals.accountlocked = 'f'
ORDER BY lab.name
"""
    gls.db.execute(query)
    return gls.db.fetchall()


def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--send-email", dest="send_email", action="store_true", default=False, help="Send email")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    log.setLevel('INFO')

    try:
        # connect to lims
        lims_server = glsclient.SERVER
        log.info('Connected to ' + lims_server)
        glsutil = glsclient.GlsUtil(server=lims_server)

        current_group_name = ''
        account_list = ''
        account_members = ''
        report = ''
        fail_report = ''
        for account in get_group_accounts(glsutil):
            if current_group_name != account['group_name']:
                if current_group_name and account_list:
                    log.info('----------')
                    log.info(current_group_name)
                    log.info(account['leader_emails'])
                    log.info(account['approver_emails'])
                    log.info(account_list)
                    if account['leader_emails']:
                        report += 'OK\t%s\t%s\t%s\n' % (current_group_name, account['leader_emails'], account_members)
                        send_email(log, current_group_name, account['leader_emails'].split(','), account_list, options.send_email)
                    else:
                        log.error('Account without leader')
                        fail_report += 'FAIL\t%s\t%s\t%s\n' % (current_group_name, account['leader_emails'], account_members)
                current_group_name = account['group_name']
                account_list = ''
                account_members = ''

            account_list += '- %s <%s>\n' % (account['researcher'], account['email'])
            account_members += '%s <%s>,' % (account['researcher'], account['email'])
        log.info(report)
        log.info(fail_report)
    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
