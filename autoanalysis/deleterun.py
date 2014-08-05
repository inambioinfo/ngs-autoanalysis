#!/usr/bin/env python
# encoding: utf-8
"""
deleterun.py

$Id$

Created by Anne Pajon on 2013-03-08.

--------------------------------------------------------------------------------

Sequencing server script that deletes old runs and moves them to OldRuns

Usage:
> python deleterun.py --basedir=/solexa0[1-3]/data/Runs/ --debug
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import glob
import logging
import argparse
import time
import datetime

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders
import autoanalysis.glslims as auto_glslims

################################################################################
# CONSTANTS
################################################################################
# Default filenames
CLEAN_FOLDERNAME = 'clean'

################################################################################
# METHODS
################################################################################
def convert_day(day):
    return 60*60*24*day
    
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
        """ % {'started': clean_started, 'find': find_cmd, 'log': clean_log,'ended': clean_ended, 'fail': clean_fail}
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
    
def is_completed(run_folder, clean_task):
    clean_directory = os.path.join(run_folder, CLEAN_FOLDERNAME)
    clean_started = os.path.join(clean_directory, '%s.started' % clean_task)
    clean_ended = os.path.join(clean_directory, '%s.ended' % clean_task)
    if not os.path.exists(clean_started) or not os.path.exists(clean_ended):
        return False
    return True
        
    
################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="run folder directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--thumbnails", dest="thumbnails", action="store", help="number of days to keep thumbnails - default set to 90", default=90, type=int)
    parser.add_argument("--intensities", dest="intensities", action="store", help="number of days to keep intensities - default set to 21", default=21, type=int)
    parser.add_argument("--images", dest="images", action="store", help="number of days to keep images - default set to 14", default=14, type=int)
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()
                  
    try:
        # connect to lims
        glslims = auto_glslims.GlsLims(options.use_limsdev)
        
        # setting-up time
        present = time.time()
        delete_thumbnails_older_than = convert_day(options.thumbnails)
        delete_images_older_than = convert_day(options.images)
        delete_intensities_older_than = convert_day(options.intensities)
        move_folder_older_than = convert_day(options.thumbnails+options.images+options.intensities)

        # loop over all runs in options.basedir
        runs = auto_runfolders.RunFolders(options.basedir, None)
        all_runs = runs.get_all_runs()
        for run in all_runs:
            try:
                log.info(run.get_header())
                # check dont.delete is not present - stop cleaning if present
                if not os.path.exists(run.dont_delete):
                    
                    # check Sequencing.completed and Sync.completed and Primary Fastq Files Found in lims OR Sequencing.failed present
                    if ( ( os.path.exists(run.sequencing_completed) and os.path.exists(run.sync_completed) and glslims.is_fastq_files_found(run.run_folder_name) ) or os.path.exists(run.sequencing_failed) ):
                        if os.path.exists(run.sequencing_completed):
                            runfolder_age = present - os.path.getmtime(os.path.join(run.run_folder, 'Data'))
                            log.info('[IMG:%s|INT:%s|PIC:%s] run completed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))
                        else:
                            runfolder_age = present - os.path.getmtime(run.sequencing_failed)
                            log.info('[IMG:%s|INT:%s|PIC:%s] run failed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))
                            
                        # check deleting file has been done already
                        if is_completed(run.run_folder, 'delete_images') and is_completed(run.run_folder, 'delete_intensities') and is_completed(run.run_folder, 'delete_thumbnails'):
                            log.info('All images/intensities/thumbnails deleted')
                            # moving run folders to OldRuns after thumbnails+images+intensities days
                            if runfolder_age > move_folder_older_than:
                                oldruns_path = os.path.join(os.path.dirname(run.run_folder), 'OldRuns')
                                move_runfolder_cmd = ['mv', run.run_folder, oldruns_path]
                                utils.create_directory(oldruns_path)
                                log.info('moving run folder...')
                                utils.run_bg_process(move_runfolder_cmd, options.dry_run)
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
                    else:
                        log.info('run folder %s not ready to be deleted' % run.run_folder)
                        
                else:
                    log.debug('%s is present' % run.dont_delete)
            except:
                log.exception("Unexpected error")
                continue
                
    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == '__main__':
    main()

