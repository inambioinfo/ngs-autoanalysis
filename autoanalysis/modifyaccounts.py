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
            lims_server = 'lims'
        else:
            lims_server = 'limsdev'
        log.info('Connected to ' + lims_server)
        glsutil = glsclient.GlsUtil(server=lims_server)

        # count number of accounts to modify
        count = 0

        # get all accounts
        all_accounts = glsutil.api.list('lab')

        field_name = 'Email Address for Billing Notifications'

        for account in all_accounts.lab:
            lab = glsutil.api.load_by_uri('lab', account.uri)
            try:
                if lab.billing_address.institution == 'CRUK Cambridge Institute':
                    count += 1
                    log.info(lab.billing_address.institution)
                    field_value = None
                    for field in lab.field:
                        if field.name == field_name:
                            field_value = field.value()
                            log.info(field_value)
                    if options.update:
                        field_new_value = 'John.Wells@cruk.cam.ac.uk, James.Hadfield@cruk.cam.ac.uk, Hannah.Haydon@cruk.cam.ac.uk, Marta.Grzelak@cruk.cam.ac.uk'
                        new_field = glsapi.userdefined.field(field_new_value)
                        new_field.name = field_name
                        lab.field.append(new_field)
                        log.debug(lab.toxml('utf-8'))
                        updated_lab = glsutil.api.update(lab)
                        log.info("[%s] '%s' changed from '%s' to '%s' on account %s" % (count, field_name, field_value, field_new_value, updated_lab.uri))

            except AttributeError:
                log.error(account.name)
                continue

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()

