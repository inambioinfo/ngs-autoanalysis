#!/usr/bin/env python
# encoding: utf-8
"""
updaterunstatus.py

$Id$

Created by Anne Pajon on 2013-06-11.

"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging

# to connect to old lims for checking status of old runs
from sqlalchemy.ext.sqlsoup import SqlSoup
from sqlalchemy.orm.exc import NoResultFound

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.pipelines as auto_pipelines
import autoanalysis.glslims as auto_glslims

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--lims", dest="lims", action="store", choices=list(auto_glslims.LIMS_SERVERS.viewkeys()), default='dev', help="lims servers to choose from %s - default set to 'dev'" % list(auto_glslims.LIMS_SERVERS.viewkeys()))
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # lims connection
        glslims = auto_glslims.GlsLims(auto_glslims.LIMS_SERVERS[options.lims])
        # loop over all runs in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, options.lustredir, options.run_folder)
        all_runs = runs.getAllRuns()
        passed_runs = []
        failed_runs = []
        unknown_runs = []
        known_runs = []
        for run in all_runs:
            try:
                log.info(run.getHeader())
                if not run.isSequencingStatusUpdated():
                    qc_flag = glslims.isSequencingRunComplete(run.run_folder_name)
                    run.updateSequencingStatus(qc_flag, options.dry_run)
                    run.updateAnalysisStatus(options.dry_run)
                    if qc_flag is not None:
                        if qc_flag:
                            passed_runs.append(run)
                        else:
                            failed_runs.append(run)
                    else:
                        unknown_runs.append(run)
                else:
                    known_runs.append(run)
            except:
                log.exception("Unexpected error")
                continue
                
        log.info('*** OLD LIMS CONNECTION ********************************************************')
        # looking for failed runs in old lims that have not been migrated
        solexa_db = SqlSoup('mysql://readonly@uk-cri-lbio04/cri_solexa')
        for run in list(unknown_runs):
            try:
                log.info('UNKNOWN %s' % run.run_folder)
                solexa_run = solexa_db.solexarun.filter_by(pipelinePath=os.path.basename(run.run_folder)).one()
                log.debug(solexa_run.status)
                if (solexa_run.status == 'ABORTED') or (solexa_run.status == 'FAILED'):
                    run.updateSequencingStatus(False, options.dry_run)
                    failed_runs.append(run)
                    unknown_runs.remove(run)
            except NoResultFound:
                log.info("No result found for %s in solexa db" % run.run_folder)
                continue
            except:
                log.exception("Unexpected error")
                continue

        # print run reports
        log.info('*** RUN REPORTS ****************************************************************')
        for run in known_runs:
            log.info('KNOWN   %s' % run.run_folder)
        for run in passed_runs:
            log.info('PASSED  %s' % run.run_folder)
        for run in failed_runs:
            log.info('FAILED  %s' % run.run_folder)
        for run in unknown_runs:
            log.info('UNKNOWN %s' % run.run_folder)
        log.info('ALL     RUNS: %s' % len(all_runs))
        log.info('KNOWN   RUNS: %s' % len(known_runs))
        log.info('PASSED  RUNS: %s' % len(passed_runs))
        log.info('FAILED  RUNS: %s' % len(failed_runs))
        log.info('UNKNOWN RUNS: %s' % len(unknown_runs))
    except:
        log.exception("Unexpected error")
        raise


if __name__ == '__main__':
	main()

