"""
Python script modifyaccounts

Created by Anne Pajon under user 'pajon01' on 01/03/2016
"""

import argparse
from collections import defaultdict

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient
import glsclient.glssql as glssql

import glsapi.userdefined


def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to preform the update and not only report action")
    parser.add_argument("--limsprod", dest="limsprod", action="store_true", default=False, help="Use the production LIMS url, by default it runs against the dev server.")
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
        if options.limsprod:
            lims_server = glsclient.SERVER
        else:
            lims_server = glsclient.TEST_SERVER
        log.info('Connected to ' + lims_server)
        glsutil = glsclient.GlsUtil(server=lims_server)

        # get all accounts
        all_accounts = glsutil.api.list('lab')

        field_name = 'PPMS Pricing'
        collaboration_institutions = defaultdict(list)

        for account in all_accounts.lab:
            lab = glsutil.api.load_by_uri('lab', account.uri)
            is_collaboration_lab = False
            for field in lab.field:
                if field.name == field_name:
                    field_value = field.value()
                    if field_value == 'Collaboration':
                        is_collaboration_lab = True
            if is_collaboration_lab:
                collaboration_institutions[lab.billing_address.institution].append(lab.name)
                print lab.billing_address.institution, '\t', lab.name
        print '---'
        for i in collaboration_institutions:
            print '| ' + i + ' | ' + 'yes' + ' | ' + 'yes' + ' |'
        for i in collaboration_institutions:
            print '*', i
            for g in collaboration_institutions[i]:
                print '**', g

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
