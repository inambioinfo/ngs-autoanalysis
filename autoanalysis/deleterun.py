#!/usr/bin/env python
# encoding: utf-8
"""
deleterun.py

$Id: $

Created by Anne Pajon on 2013-03-08.
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

try:
    from sqlalchemy.ext.sqlsoup import SqlSoup
    from sqlalchemy.orm.exc import NoResultFound
except ImportError:
    sys.exit("""
--------------------------------------------------------------------------------
>>> modules { mysql-python | sqlalchemy } not installed.
--------------------------------------------------------------------------------
[on sols] use /home/mib-cri/software/python2.7/bin/python
[locally] install virtualenv; source bin/activate and pip install modules
--------------------------------------------------------------------------------
""")

# import logging module first
import log as logger
log = logger.set_custom_logger()
# then import other custom modules
import utils
import lims

################################################################################
# CONSTANTS
################################################################################
# Default filenames
DONT_DELETE_FILENAME = 'dont.delete'
SEQUENCING_COMPLETED_FILENAME = "Run.completed"
CLEAN_FOLDERNAME = 'clean'

################################################################################
# METHODS
################################################################################
def convert_day(day):
    return 60*60*24*day
    
def setup_clean(run_folder, clean_task, find_cmd):
    """Delete tasks are delete_thumbnails, delete_intensities and delete_images
    """
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
    
def is_ended(run_folder, clean_task):
    clean_directory = os.path.join(run_folder, CLEAN_FOLDERNAME)
    clean_started = os.path.join(clean_directory, '%s.started' % clean_task)
    clean_ended = os.path.join(clean_directory, '%s.ended' % clean_task)
    if not os.path.exists(clean_started) or not os.path.exists(clean_ended):
        return False
    return True
        
    
################################################################################
# MAIN
################################################################################

# delete_old_run_data.pl -thumbnails 90 -images 14 -intensities 21 -runfolderlocglob '/solexa0*/data/Runs/??????_*'
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--basedir", dest="basedir", action="store", help="run folder directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
    parser.add_argument("--thumbnails", dest="thumbnails", action="store", help="number of days to keep thumbnails - default set to 90", default=90, type=int)
    parser.add_argument("--intensities", dest="intensities", action="store", help="number of days to keep intensities - default set to 21", default=21, type=int)
    parser.add_argument("--images", dest="images", action="store", help="number of days to keep images - default set to 14", default=14, type=int)
    parser.add_argument("--dburl", dest="dburl", action="store", default=lims.DB_URL, help="database url [read only access] - default set to '%s'" % lims.DB_URL)
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
    parser.add_argument("--debug", dest="debug", action="store_true", default=False, help="Set logging level to DEBUG, by default INFO")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    log.setLevel(logging.INFO)
    if options.debug:
        log.setLevel(logging.DEBUG)        
    if options.logfile:
        log.addHandler(logger.set_file_handler(options.logfile))
        
    try:        
        # lims db
        solexa_db = SqlSoup(options.dburl)
    
        # setting-up time
        present = time.time()
        delete_thumbnails_older_than = convert_day(options.thumbnails)
        delete_images_older_than = convert_day(options.images)
        delete_intensities_older_than = convert_day(options.intensities)
        move_folder_older_than = convert_day(options.thumbnails+options.images+options.intensities)
    
        # removing data into completed run folders
        run_folders = glob.glob("%s/??????_*_*_*" % options.basedir)
        for run_folder in run_folders:
            log.info('--------------------------------------------------------------------------------')
            log.info('--- RUN: %s' % run_folder)
            log.info('--------------------------------------------------------------------------------')
            # check dont.delete is not present - stop cleaning if present
            dont_delete = os.path.join(run_folder, DONT_DELETE_FILENAME)
            if not os.path.exists(dont_delete):
                try:
                    run = solexa_db.solexarun.filter_by(pipelinePath=os.path.basename(run_folder)).one()
                    log.info('Sequencing status %s and analysis status %s' % (run.status, run.analysisStatus))
                    if (run.status == 'COMPLETE' and (run.analysisStatus == 'COMPLETE' or run.analysisStatus == 'SECONDARY COMPLETE')) or ('ABORTED' in run.status) or (run.status == 'FAILED'):
                        runfolder_age = present - os.path.getmtime(os.path.join(run_folder, 'Data'))
                        log.info('[IMG:%s|INT:%s|PIC:%s] run completed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))
                        # check deleting file has been done already
                        if is_ended(run_folder, 'delete_images') and is_ended(run_folder, 'delete_intensities') and is_ended(run_folder, 'delete_thumbnails'):
                            log.info('All images/intensities/thumbnails deleted')
                            # moving run folders to OldRuns after thumbnails+images+intensities days
                            if runfolder_age > move_folder_older_than:
                                oldruns_path = os.path.join(os.path.dirname(run_folder), 'OldRuns')
                                move_runfolder_cmd = ['mv', run_folder, oldruns_path]
                                utils.create_directory(oldruns_path)
                                log.info('moving run folder...')
                                utils.run_bg_process(move_runfolder_cmd, options.dry_run)
                        else:
                            # deleting images
                            if is_ended(run_folder, 'delete_images'):
                                log.info('All images deleted')
                            else:
                                if runfolder_age > delete_images_older_than:
                                    delete_images_cmd = "find %s -name *.tif -delete" % run_folder
                                    setup_clean(run_folder, 'delete_images', delete_images_cmd)
                                    clean(run_folder, 'delete_images', options.dry_run)
                            # deleting intensities
                            if is_ended(run_folder, 'delete_intensities'):
                                log.info('All intensities deleted')
                            else:
                                if runfolder_age > delete_intensities_older_than:
                                    delete_intensities_cmd = "find %s/Data/Intensities/ \( -name *_pos.txt -or -name *.cif -or -name *.filter -or -name *.bcl -or -name *.stats \) -delete" % run_folder
                                    setup_clean(run_folder, 'delete_intensities', delete_intensities_cmd)
                                    clean(run_folder, 'delete_intensities', options.dry_run)
                            # deleting thumbnails
                            if is_ended(run_folder, 'delete_thumbnails'):
                                log.info('All thumbnails deleted')
                            else:
                                if runfolder_age > delete_thumbnails_older_than:
                                    delete_thumbnails_cmd = "find %s/Thumbnail_Images/ -name *.jpg -delete" % run_folder
                                    setup_clean(run_folder, 'delete_thumbnails', delete_thumbnails_cmd)
                                    clean(run_folder, 'delete_thumbnails', options.dry_run)
                except (NoResultFound):
                    log.info('No result found in lims for pipelinePath %s' % os.path.basename(run_folder))
                except:
                    log.exception("Unexpected error")
                    continue
            else:
                log.debug('%s is present' % dont_delete)
    except:
        log.exception("Unexpected error")
        raise
        
if __name__ == '__main__':
    main()

