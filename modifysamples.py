"""
Python script modifysamples

Created by Anne Pajon under user 'pajon01' on 16/10/15
"""

import argparse
import csv

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient
import glsclient.glssql as glssql

import glsapi.userdefined

SAMPLES_QUERY = """
SELECT
process.luid as luid,
sample.name as samplename,
sudf2.udfvalue as billingcode
FROM sample LEFT OUTER JOIN sample_udf_view as sudf2 on (sudf2.sampleid=sample.sampleid AND sudf2.udfname = '%s'),
process
WHERE sudf2.udfvalue='%s'
AND sample.processid = process.processid
"""


def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--mapping", dest="mapping", action="store", help="mapping file, tab separated columns with old/new header '/path/to/mapping/file/mapping.txt'", required=True)
    parser.add_argument("--field", dest="field", action="store", help="sample UDF name e.g. 'Billing Information'", required=True)
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
        # read mapping file
        mappings = []
        with open(options.mapping, "U") as f:
            reader = csv.DictReader(f, delimiter='\t')
            for line in reader:
                mappings.append(line)
        log.debug(mappings)

        # connect to lims
        if options.limsprod:
            lims_server = glsclient.SERVER
        else:
            lims_server = glsclient.TEST_SERVER
        log.debug('Connected to ' + lims_server)
        glsutil = glsclient.GlsUtil(server=lims_server)

        # count number of samples to modify
        count = 0

        # loop over all changes in mapping file
        for mapping in mappings:
            # get all samples to modify in results
            glsutil.db.execute(SAMPLES_QUERY % (options.field, mapping['old']))
            results = glsutil.db.fetchall()
            for row in results:
                count += 1
                sample = glsutil.api.load('sample', row['luid'])
                log.info("[%s] Retrieved sample %s, field '%s' has old value '%s', it will be changed to '%s'" % (count, sample.uri, options.field, mapping['old'], mapping['new']))
                if options.update:
                    new_field = glsapi.userdefined.field(mapping['new'])
                    new_field.name = options.field
                    sample.field.append(new_field)
                    log.debug(sample.toxml('utf-8'))
                    updated_sample = glsutil.api.update(sample)
                    log.info("[%s] '%s' changed from '%s' to '%s' on sample %s" % (count, options.field, mapping['old'], mapping['new'], updated_sample.uri))

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
