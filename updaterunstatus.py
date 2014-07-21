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
import os
import argparse

# import custom modules
import autoanalysis.log as logger
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.glslims as auto_glslims


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/processing'", required=True)
    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--dev-lims", dest="use_dev_lims", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False,  help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # lims connection
        glslims = auto_glslims.GlsLims(options.use_dev_lims)
        # loop over all runs in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, None, options.run_folder)
        all_runs = runs.get_all_runs()
        completed_runs = []
        tosync_runs = []
        syncfail_runs = []
        seqfail_runs = []
        unknown_runs = []
        for run in all_runs:
            try:
                log.info(run.get_header())
                if not run.is_sequencing_status_present():
                    is_sequencing_complete = glslims.isSequencingRunComplete(run.run_folder_name)
                    run.update_sequencing_status(is_sequencing_complete, options.dry_run)
                if not run.is_sync_status_present():
                    run.update_sync_status(options.dry_run)
                    
                # reporting
                if os.path.exists(run.sequencing_completed):
                    if os.path.exists(run.sync_completed):
                        completed_runs.append(run)
                    elif os.path.exists(run.sync_failed):
                        syncfail_runs.append(run)
                    else:
                        tosync_runs.append(run)
                elif os.path.exists(run.sequencing_failed):
                    seqfail_runs.append(run)
                else:
                    unknown_runs.append(run)
            except:
                log.exception("Unexpected error")
                continue
        # print run reports
        log.info('*** RUN REPORTS ****************************************************************')
        for run in completed_runs:
            log.info('COMPLETE  %s' % run.run_folder)
        for run in seqfail_runs:
            log.info('SEQ FAIL  %s' % run.run_folder)
        for run in syncfail_runs:
            log.info('SYNC FAIL %s' % run.run_folder)
        for run in tosync_runs:
            log.info('TO SYNC   %s' % run.run_folder)
        for run in unknown_runs:
            log.info('UNKNOWN   %s' % run.run_folder)
        log.info('COMPLETE  RUNS: %s' % len(completed_runs))
        log.info('SEQ FAIL  RUNS: %s' % len(seqfail_runs))
        log.info('SYNC FAIL RUNS: %s' % len(syncfail_runs))
        log.info('TO SYNC   RUNS: %s' % len(tosync_runs))
        log.info('UNKNOWN   RUNS: %s' % len(unknown_runs))
    except:
        log.exception("Unexpected error")
        raise


if __name__ == '__main__':
    main()

