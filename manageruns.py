#!/usr/bin/env python
# encoding: utf-8
"""
manageruns.py

$Id$

Created by Anne Pajon on 2013-06-11.

"""

################################################################################
# IMPORTS
################################################################################
import os
import argparse
import glob
import time
import datetime
import logging

# import custom modules
import autoanalysis.log as logger
import autoanalysis.data as auto_data
import autoanalysis.glslims as auto_glslims
import autoanalysis.utils as utils


CLEAN_FOLDERNAME = 'clean'


def convert_day(day):
    return 60 * 60 * 24 * day


def is_completed(run_folder, clean_task):
    clean_directory = os.path.join(run_folder, CLEAN_FOLDERNAME)
    clean_started = os.path.join(clean_directory, '%s.started' % clean_task)
    clean_ended = os.path.join(clean_directory, '%s.ended' % clean_task)
    if not os.path.exists(clean_started) or not os.path.exists(clean_ended):
        return False
    return True


def setup_clean(run_folder, clean_task, find_cmd):
    """Delete tasks are delete_thumbnails, delete_intensities and delete_images
    """
    log = logging.getLogger(__name__)
    clean_directory = os.path.join(run_folder, CLEAN_FOLDERNAME)
    clean_script_path = os.path.join(clean_directory, '%s.sh' % clean_task)
    clean_started = os.path.join(clean_directory, '%s.started' % clean_task)
    clean_ended = os.path.join(clean_directory, '%s.ended' % clean_task)
    clean_fail = os.path.join(clean_directory, '%s.fail' % clean_task)
    clean_log = os.path.join(clean_directory, '%s.log' % clean_task)

    # create clean folder
    if not os.path.exists(clean_directory):
        os.makedirs(clean_directory)
        log.info('%s created' % clean_directory)
    else:
        log.debug('%s already exists' % clean_directory)

    # create clean script
    if not os.path.exists(clean_script_path):
        command = """
touch %(started)s

if ( %(find)s > %(log)s 2>&1 )
then
    touch %(ended)s
else
    touch %(fail)s
fi
        """ % {'started': clean_started, 'find': find_cmd, 'log': clean_log, 'ended': clean_ended, 'fail': clean_fail}
        utils.create_script(clean_script_path, command)
    else:
        log.debug('%s already exists' % clean_script_path)


def clean(run_folder, clean_task, dry_run=True):
    log = logging.getLogger(__name__)
    clean_directory = os.path.join(run_folder, CLEAN_FOLDERNAME)
    clean_script_path = os.path.join(clean_directory, '%s.sh' % clean_task)
    clean_started = os.path.join(clean_directory, '%s.started' % clean_task)
    clean_ended = os.path.join(clean_directory, '%s.ended' % clean_task)
    clean_fail = os.path.join(clean_directory, '%s.fail' % clean_task)
    clean_log = os.path.join(clean_directory, '%s.log' % clean_task)

    # run clean script to clean data from sequencing servers
    if os.path.exists(clean_script_path):
        if not os.path.exists(clean_started):
            utils.run_bg_process(['sh', '%s' % clean_script_path], dry_run)
        else:
            if not os.path.exists(clean_ended):
                if os.path.exists(clean_fail):
                    log.error("[***FAIL***] %s for %s has failed." % (clean_task, run_folder))
                    log.error("please investigate %s." % clean_log)
                else:
                    log.info('%s in %s is currently being deleted' % (clean_task, run_folder))
            else:
                log.info('%s in %s has been deleted successfully' % (clean_task, run_folder))
    else:
        log.warn('%s is missing' % clean_script_path)


################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--lustredir", dest="lustredir", action="store", help="lustre base directory e.g. '/lustre/mib-cri/solexa/Runs'", required=True)
    parser.add_argument("--processingdir", dest="processingdir", action="store", help="processing base directories e.g. '/processing'", required=True)
    parser.add_argument("--stagingdir", dest="stagingdir", action="store", help="staging base directories e.g. '/staging'", required=True)

    parser.add_argument("--processeddir", dest="processeddir", action="store", default=os.path.join('processing', 'ProcessedRuns'), help="processed runs directory on processing", required=True)
    parser.add_argument("--trashdir", dest="trashdir", action="store", default=os.path.join('lustre', 'mib-cri', 'solexa', 'TrashRuns'), help="trash runs directory on lustre", required=True)

    parser.add_argument("--thumbnails", dest="thumbnails", action="store", help="number of days to keep thumbnails - default set to 90", default=90, type=int)
    parser.add_argument("--intensities", dest="intensities", action="store", help="number of days to keep intensities - default set to 21", default=21, type=int)
    parser.add_argument("--images", dest="images", action="store", help="number of days to keep images - default set to 14", default=14, type=int)

    parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--dev-lims", dest="use_dev_lims", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False,  help="File to print logging information")
    parser.add_argument("--nologemail", dest="nologemail", action="store_true", default=False, help="turn off sending log emails on error")

    options = parser.parse_args()

    # logging configuration
    log = logger.get_custom_logger(options.logfile, options.nologemail)

    # setting up directories
    utils.create_directory(options.processeddir)
    utils.create_directory(options.trashdir)

    # setting-up time
    present = time.time()
    delete_thumbnails_older_than = convert_day(options.thumbnails)
    delete_images_older_than = convert_day(options.images)
    delete_intensities_older_than = convert_day(options.intensities)

    try:
        # lims connection
        glslims = auto_glslims.GlsLims(options.use_dev_lims)
        # loop over all runs in options.processingdir
        runs = auto_data.RunFolderList(options.processingdir, options.stagingdir, options.lustredir, options.run_folder, False)

        ### print run reports ...........................................................
        log.info('********************************************************************************')
        log.info('*** RUN REPORTS ****************************************************************')
        log.info('********************************************************************************')
        for run in runs.runs_to_analyse:
            log.info('TO ANALYSE  %s' % run.run_folder)
        for run in runs.unknown_runs:
            log.info('UNKNOWN     %s' % run.run_folder)
        log.info('--------------------')
        log.info(' COMPLETED RUNS: %s' % len(runs.completed_runs))
        log.info('    FAILED RUNS: %s' % len(runs.failed_runs))
        log.info('   UNKNOWN RUNS: %s' % len(runs.unknown_runs))
        log.info('--------------------')
        log.info('RUNS TO ANALYSE: %s' % len(runs.runs_to_analyse))
        log.info('  ANALYSED RUNS: %s' % len(runs.analysed_runs))
        log.info('    SYNCED RUNS: %s' % len(runs.synced_runs))
        log.info(' PUBLISHED RUNS: %s' % len(runs.published_runs))
        log.info('--------------------')

        ### update run status ...........................................................
        log.info('********************************************************************************')
        log.info('*** UPDATE RUN STATUS **********************************************************')
        log.info('********************************************************************************')
        for run in runs.all_runs:
            try:
                # add SequencingComplete.txt or SequencingFail.txt by retrieving info from lims on run
                if not run.is_sequencing_status_present():
                    log.info('*** %s' % run.run_folder_name)
                    is_sequencing_complete = glslims.is_sequencing_run_complete(run.run_folder_name)
                    run.update_sequencing_status(is_sequencing_complete, options.dry_run)
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue

        ### manage runs .................................................................
        log.info('********************************************************************************')
        log.info('*** MANAGE PUBLISHED RUNS ******************************************************')
        log.info('********************************************************************************')
        # move published runs in lustre into options.trashdir and in processing into options.processeddir
        for run in runs.published_runs:
            try:
                if os.path.exists(run.ignore_me):
                    log.info('%s is present' % run.ignore_me)
                else:
                    cmd = ['mv', run.run_folder, options.processeddir]
                    utils.run_bg_process(cmd, options.dry_run)
                    log.info('*** run %s moved to %s' % (run.run_folder_name, options.processeddir))
                    if os.path.exists(run.lustre_run_folder):
                        cmd = ['mv', run.lustre_run_folder, options.trashdir]
                        utils.run_bg_process(cmd, options.dry_run)
                        log.info('*** run %s on lustre moved to %s' % (run.run_folder_name, options.trashdir))
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue
        log.info('********************************************************************************')
        log.info('*** MANAGE FAILED RUNS *********************************************************')
        log.info('********************************************************************************')
        # move failed runs in processing into options.processeddir
        for run in runs.failed_runs:
            try:
                if os.path.exists(run.ignore_me):
                    log.info('%s is present' % run.ignore_me)
                else:
                    cmd = ['mv', run.run_folder, options.faileddir]
                    utils.run_bg_process(cmd, options.dry_run)
                    log.info('*** failed run %s moved to %s' % (run.run_folder_name, options.processeddir))
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue

        ### delete runs .................................................................
        log.info('********************************************************************************')
        log.info('*** CLEAN PROCESSED RUNS *******************************************************')
        log.info('********************************************************************************')
        # delete all runs in options.trashdir older than 3 days
        trash_run_folders = glob.glob("%s/??????_*_*_*" % options.trashdir)
        for run_folder in trash_run_folders:
            try:
                if (present - os.path.getmtime(run_folder)) > convert_day(3):
                    cmd = ['rm', '-rf', run_folder]
                    utils.run_bg_process(cmd, options.dry_run)
                    log.info('*** run folder %s deleted' % run_folder)
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue
        # clean all runs in options.processeddir
        processed_run_folders = glob.glob("%s/??????_*_*_*" % options.processeddir)
        for run_folder in processed_run_folders:
            log.info('*** run folder %s' % run_folder)
            try:
                # calculate age of run folder
                if os.path.exists(os.path.join(run_folder, auto_data.SEQUENCING_COMPLETED)):
                    runfolder_age = present - os.path.getmtime(os.path.join(run_folder, auto_data.SEQUENCING_COMPLETED))
                    log.info('[IMG:%s|INT:%s|PIC:%s] run completed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))
                else:
                    runfolder_age = present - os.path.getmtime(os.path.join(run_folder, auto_data.SEQUENCING_FAILED))
                    log.info('[IMG:%s|INT:%s|PIC:%s] run failed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))

                # check deleting file has been done already
                if is_completed(run.run_folder, 'delete_images') and is_completed(run.run_folder, 'delete_intensities') and is_completed(run.run_folder, 'delete_thumbnails'):
                    log.info('All images/intensities/thumbnails deleted')
                    cmd = ['rm', '-rf', run_folder]
                    utils.run_bg_process(cmd, options.dry_run)
                    log.info('*** run folder %s deleted' % run_folder)
                else:
                    # deleting images
                    if is_completed(run.run_folder, 'delete_images'):
                        log.info('All images deleted')
                    else:
                        if runfolder_age > delete_images_older_than:
                            delete_images_cmd = "find %s -name *.tif -delete" % run.run_folder
                            setup_clean(run.run_folder, 'delete_images', delete_images_cmd)
                            clean(run.run_folder, 'delete_images', options.dry_run)
                    # deleting intensities
                    if is_completed(run.run_folder, 'delete_intensities'):
                        log.info('All intensities deleted')
                    else:
                        if runfolder_age > delete_intensities_older_than:
                            delete_intensities_cmd = "find %s/Data/Intensities/ \( -name *_pos.txt -or -name *.cif -or -name *.filter -or -name *.bcl -or -name *.stats \) -delete" % run.run_folder
                            setup_clean(run.run_folder, 'delete_intensities', delete_intensities_cmd)
                            clean(run.run_folder, 'delete_intensities', options.dry_run)
                    # deleting thumbnails
                    if is_completed(run.run_folder, 'delete_thumbnails'):
                        log.info('All thumbnails deleted')
                    else:
                        if runfolder_age > delete_thumbnails_older_than:
                            delete_thumbnails_cmd = "find %s/Thumbnail_Images/ -name *.jpg -delete" % run.run_folder
                            setup_clean(run.run_folder, 'delete_thumbnails', delete_thumbnails_cmd)
                            clean(run.run_folder, 'delete_thumbnails', options.dry_run)
            except Exception, e:
                log.exception("Unexpected error")
                log.exception(e)
                continue

    except:
        log.exception("Unexpected error")
        raise


if __name__ == '__main__':
    main()

