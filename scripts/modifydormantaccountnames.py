"""
Python script modifyaccounts

Created by Anne Pajon under user 'pajon01' on 01/03/2016
"""

import argparse

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

        # count number of accounts to modify
        count = 0

        # get all accounts
        all_accounts = glsutil.api.list('lab')

        account_active_field_name = 'Account Active'

        for account in all_accounts.lab:
            lab = glsutil.api.load_by_uri('lab', account.uri)
            try:
                account_active_field_value = None
                for field in lab.field:
                    if field.name == account_active_field_name:
                        account_active_field_value = field.value()
                if account_active_field_value == 'false':
                    count += 1
                    lab_old_name = lab.name
                    lab_new_name = 'ZZZ %s' % lab.name
                    lab.name = lab_new_name
                    log.info("[%s] dormant account name will be changed from '%s' to '%s' on account %s" % (count, lab_old_name, lab.name, lab.uri))
                    if options.update:
                        new_field = glsapi.userdefined.field('Dormant Account')
                        new_field.name = 'Pricing'
                        lab.field.append(new_field)
                        updated_lab = glsutil.api.update(lab)
                        log.info("[%s] dormant account name changed from '%s' to '%s' on account %s" % (count, lab_old_name, updated_lab.name, updated_lab.uri))

            except AttributeError:
                log.error(account.name)
                continue

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
