#!/usr/bin/env python
# encoding: utf-8
"""
createbillingreport.py

Created by Anne Pajon on 2013-07-29.
"""

import sys
import os
import logging
import argparse

# import custom modules
import log as logger
import glsclient
import glssql


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limsdev", dest="limsdev", action="store_true", default=False, help="Use the development LIMS url")
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
            #lims_server = 'lims'
            lims_server = 'lims'
        glsutil = glsclient.GlsUtil(server=lims_server)
        
        
        results = glsutil.db.execute(glssql.BILLING_QUERY).fetchall()
        
        report = "code,researcher,lab,runtype,month,submissiondate,completiondate,ishistorical,lane,slxid,mgalanereport,mgareport\n"

        for raw in results:
            log.info("%s\t%s" % (raw.runfolder, raw.lane))
            # runfolder: 130619_HWI-ST230_0602_C23YNACXX - split('_') date,instrument,runnumber,flowcellid
            # runtype: Hiseq_SE40
            # flowcellid: C23YNACXX
            # instrument: Luke-Leia [HWI-ST230]
            # 1184_B Leia_D214AACXX_SEM75 runnumber,instrument,flowcellid,runtype
            code = None
            if raw.runfolder and raw.runtype and raw.instrument:
                runfolder_elements = raw.runfolder.split('_')
                runtype_elements = raw.runtype.split('_')
                instrument_elements = raw.instrument.split()
                flowcellid = runfolder_elements[3]
                if '-' in runfolder_elements[3]:
                    flowcellid = runfolder_elements[3].split('-')[1]
                code = "%s_%s_%s_%s" % (runfolder_elements[2], instrument_elements[0], flowcellid, runtype_elements[1])
            
            mga_lanereport_files = glsutil.db.execute(glssql.MGA_LANE_FILES_QUERY % (raw.runfolder)).fetchall()
            mga_lanereport_url = None
            for mgafile in mga_lanereport_files:
                lane = mgafile.name.split()[0][0]
                lanename = 'Lane%s' % lane
                if raw.lane == lanename:
                    mga_lanereport_url = "%s://%s:%s%s%s" % (mgafile.scheme, mgafile.host, mgafile.port, mgafile.dir, mgafile.contenturi)
            
            mga_report_files = glsutil.db.execute(glssql.MGA_FILES_QUERY % (raw.runfolder)).fetchall()
            mga_report_url = None
            if mga_report_files:
                mga_report_url = "%s://%s:%s%s%s" % (mga_report_files[0].scheme, mga_report_files[0].host, mga_report_files[0].port, mga_report_files[0].dir, mga_report_files[0].contenturi)
            
            # format output report
            lane_report = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (code,raw.researcher,raw.lab,raw.runtype,raw.month,raw.submissiondate,raw.completiondate,raw.ishistorical,raw.lane,raw.slxid,mga_lanereport_url,mga_report_url)
            log.info(lane_report)
            report = report + lane_report
        
        print report
            

    except:
        log.exception("Unexpected error")
        raise

if __name__ == '__main__':
    main()

