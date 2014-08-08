#!/usr/bin/env python
# encoding: utf-8
"""
rerunmga.py

Created by Anne Pajon on 2013-07-30.
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import argparse
import logging

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.data as auto_data
import autoanalysis.pipelines as auto_pipelines

RSYNC = """
touch %(process_run_dir)s/rerunmga_primary_rsync.started
touch %(process_dir)s/rerunmga_primary_rsync.lock

if ( rsync -av %(base_run_dir)s/primary %(process_run_dir)s/ > %(process_run_dir)s/rerunmga_primary_rsync.log 2>&1 ) 
then
   touch %(process_run_dir)s/rerunmga_primary_rsync.ended
else
    touch %(process_run_dir)s/rerunmga_primary_rsync.failed
fi

rm %(process_dir)s/rerunmga_primary_rsync.lock
"""

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--processdir", dest="processdir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--runfolders", dest="runfolders", action="store", nargs='+', help="list of run folders e.g. '--runfolders 121019_HWI-ST230_957_D18DUACXX 121011_HWI-ST230_952_D19D3ACXX'", required=True)
    parser.add_argument("--softdir", dest="softdir", action="store", default=auto_pipelines.SOFT_PIPELINE_PATH, help="software base directory where pipelines are installed - default set to %s" % auto_pipelines.SOFT_PIPELINE_PATH)
    parser.add_argument("--cluster", dest="cluster", action="store", help="cluster hostname e.g. %s" % utils.CLUSTER_HOST)
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    # get list of run folders from command line
    log.debug("List of runfolders to process: " % options.runfolders)
    for runfolder in options.runfolders:
        log.info(auto_data.RUN_HEADER % {'run_folder': runfolder})
        # find runfolder in basedir
        runfolder_path = utils.locate_run_folder(runfolder, options.basedir, False)
        log.debug(runfolder_path)
        # create runfolder in processdir if it does not already exists
        process_runfolder_path = os.path.join(options.processdir, runfolder)
        if not os.path.exists(process_runfolder_path):
            utils.create_directory(process_runfolder_path)
        log.debug(process_runfolder_path)
        ### rsync primary directory from basedir to processdir
        # create rsync script
        rsync_script_path = os.path.join(process_runfolder_path, 'rerunmga_primary_rsync.sh')
        utils.create_script(rsync_script_path, RSYNC % {'process_dir':options.processdir, 'process_run_dir':process_runfolder_path, 'base_run_dir':runfolder_path})
        # run rsync script
        rsync_started = os.path.join(process_runfolder_path, 'rerunmga_primary_rsync.started')
        rsync_lock = os.path.join(options.processdir, 'rerunmga_primary_rsync.lock')
        rsync_ended = os.path.join(process_runfolder_path, 'rerunmga_primary_rsync.ended')
        rsync_failed = os.path.join(process_runfolder_path, 'rerunmga_primary_rsync.failed')
        if not os.path.exists(rsync_started):
            if not os.path.exists(rsync_lock):
                utils.run_bg_process(['sh', '%s' % rsync_script_path], options.dry_run)
            else:
                log.info('%s presents - another rsync process is running' % rsync_lock)
        else:
            if not os.path.exists(rsync_ended):
                if os.path.exists(rsync_failed):
                    log.error("[***FAIL***] rsync for %s has failed." % runfolder)
                else:
                    log.info('rsync is currently running...')
            else:
                log.info('[***OK***] rsync finished successfully')
        ### touch Sequencing.completed
        utils.touch(os.path.join(process_runfolder_path,'Sequencing.completed'), False)
        ### setup/run mga pipeline
        # create pipelines
        run = auto_data.RunFolder(process_runfolder_path, options.basedir)
        log.debug(run.staging_run_folder)
        pipelines = auto_pipelines.Pipelines(run, 'mga', options.softdir, options.cluster, options.dry_run, options.use_limsdev)
        # run pipelines
        pipelines.execute()
        
    


if __name__ == '__main__':
    main()

