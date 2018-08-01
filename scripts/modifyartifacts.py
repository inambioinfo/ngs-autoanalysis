"""
Python script modifyartifacts

Created by Anne Pajon under user 'pajon01' on 01/03/2016
"""
import argparse

# import custom modules
import glsclient.log as logger
import glsclient.glsclient as glsclient
import glsclient.glssql as glssql

import glsapi.userdefined


QUERY = """
-- SELECT -------------------------------------------------------------------------
SELECT distinct
artifact.luid as luid,
case when artifact.name like 'SLX-%' then substring(artifact.name, '^(SLX-\d+).*')
     else 'SLX-Unknown'
end as slxid,
audf1.udfvalue as lpsbillable,
outaudf1.udfvalue as outlpsbillable
-- FROM ---------------------------------------------------------------------------
FROM process,
processtype,
processiotracker,
outputmapping,
artifact as outputartifact
LEFT OUTER JOIN artifact_udf_view as outaudf1 on (outaudf1.artifactid=outputartifact.artifactid AND outaudf1.udfname = 'LPS Billable')
LEFT OUTER JOIN artifact_udf_view as outaudf2 on (outaudf2.artifactid=outputartifact.artifactid AND outaudf2.udfname = 'Billing Information')
LEFT OUTER JOIN artifact_udf_view as outaudf3 on (outaudf3.artifactid=outputartifact.artifactid AND outaudf3.udfname = 'SLX Identifier'),
artifact
LEFT OUTER JOIN artifact_udf_view as audf1 on (audf1.artifactid=artifact.artifactid AND audf1.udfname = 'LPS Billable')
LEFT OUTER JOIN artifact_udf_view as audf2 on (audf2.artifactid=artifact.artifactid AND audf2.udfname = 'Billing Information')
LEFT OUTER JOIN artifact_udf_view as audf3 on (audf3.artifactid=artifact.artifactid AND audf3.udfname = 'SLX Identifier'),
artifact_sample_map,
sample
LEFT OUTER JOIN sample_udf_view as sudf1 on (sudf1.sampleid=sample.sampleid AND sudf1.udfname = 'Billing Information'),
process as sampleprocess,
project,
researcher,
lab
LEFT OUTER JOIN address on (lab.billingaddressid=address.addressid)
-- WHERE --------------------------------------------------------------------------
WHERE process.typeid = processtype.typeid
AND processtype.displayname='LPS Complete'
AND process.workstatus='COMPLETE'
AND process.daterun >= '2015-04-01' AND process.daterun <= '2016-03-31'
AND process.processid=processiotracker.processid
AND processiotracker.inputartifactid=artifact.artifactid
AND outputmapping.trackerid=processiotracker.trackerid
AND outputmapping.outputartifactid=outputartifact.artifactid
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample.processid=sampleprocess.processid
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND researcher.labid=lab.labid
AND sample.name NOT LIKE 'Genomics Control%'
AND project.name != 'Controls'
--AND sudf1.udfvalue <> audf2.udfvalue
-- ORDER BY -----------------------------------------------------------------------
ORDER BY slxid"""


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

        # count number of artifacts to modify
        count = 0

        # get all artifacts to modify in results
        #glsutil.db.execute(QUERY)
        #results = glsutil.db.fetchall()
        results = []
        with open('artifacts.txt') as data:
            for luid in data:
                results.append(luid.strip())

        for value in results:
            count += 1
            artifact = glsutil.api.load('artifact', value)
            #field_name = 'LPS Billable'
            field_name = 'PPMS Order ID'
            field_value = None
            for field in artifact.field:
                if field.name == field_name:
                    field_value = field.value()
            #field_new_value = row['outlpsbillable']
            #field_new_value = 'Bill - 10X Single Cell 3GEX'
            field_new_value = ''  # for removing UDF
            log.info("[%s] Retrieved artifact %s, field '%s' value '%s' will be set to '%s'" % (count, artifact.uri, field_name, field_value, field_new_value))
            if options.update:
                new_field = glsapi.userdefined.field(field_new_value)
                new_field.name = field_name
                artifact.field.append(new_field)
                log.debug(artifact.toxml('utf-8'))
                updated_artifact = glsutil.api.update(artifact)
                log.info("[%s] '%s' changed from '%s' to '%s' on artifact %s" % (count, field_name, field_value, field_new_value, updated_artifact.uri))

    except:
        log.exception("Unexpected error")
        raise

if __name__ == "__main__":
    main()
