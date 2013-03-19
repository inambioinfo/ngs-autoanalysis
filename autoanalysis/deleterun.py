#!/usr/bin/env python
# encoding: utf-8
"""
deleterun.py

$Id$

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
import autoanalysis.log as logger
log = logger.set_custom_logger()
# then import other custom modules
import autoanalysis.utils as utils
import autoanalysis.lims as lims

################################################################################
# CONSTANTS
################################################################################
# Default filenames
DONT_DELETE_FILENAME = 'dont.delete'
SEQUENCING_COMPLETED_FILENAME = "Run.completed"
THUMBNAILS_DELETED = 'Thumbnails.deleted'
INTENSITIES_DELETED = 'Intensities.deleted'
IMAGES_DELETED = 'Images.deleted'

################################################################################
# METHODS
################################################################################
def convert_day(day):
    return 60*60*24*day
    
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
                        thumbnails_deleted = os.path.join(run_folder, THUMBNAILS_DELETED)
                        intensities_deleted = os.path.join(run_folder, INTENSITIES_DELETED)
                        images_deleted = os.path.join(run_folder, IMAGES_DELETED)
                        runfolder_age = present - os.path.getmtime(os.path.join(run_folder, 'Data'))
                        log.info('[IMG:%s|INT:%s|PIC:%s] run completed %s ago' % (options.images, options.intensities, options.thumbnails, datetime.timedelta(seconds=runfolder_age)))
                        # check deleting file has been done already
                        if os.path.exists(images_deleted) and os.path.exists(intensities_deleted) and os.path.exists(thumbnails_deleted):
                            log.info('All images/intensities/thumbnails deleted')
                            # moving run folders to OldRuns after 10 days of cleaning thumbnails
                            thumbnails_deleted_age = present - os.path.getmtime(thumbnails_deleted)
                            if thumbnails_deleted_age > convert_day(10):
                                oldruns_path = os.path.join(os.path.dirname(run_folder), 'OldRuns')
                                move_runfolder_cmd = ['mv', run_folder, old_runs_path]
                                utils.create_directory(oldruns_path)
                                log.info('moving run folder...')
                                utils.run_bg_process(move_runfolder_cmd, options.dry_run)
                        else:
                            # deleting images
                            if os.path.exists(images_deleted):
                                log.info('All images deleted')
                            else:
                                if runfolder_age > delete_images_older_than:
                                    delete_images_cmd = ['find', run_folder, '-name', '*.tif', '-delete']
                                    log.info('deleting images...')
                                    if not options.dry_run:
                                        utils.touch(images_deleted)
                                    utils.run_bg_process(delete_images_cmd, options.dry_run)
                            # deleting intensities
                            if os.path.exists(intensities_deleted):
                                log.info('All intensities deleted')
                            else:
                                if runfolder_age > delete_intensities_older_than:
                                    delete_intensities_cmd = ['find', '%s/Data/Intensities/' % run_folder, '-name', '*_pos.txt', 
                                    '-o', '-name', '*.cif', '-o', '-name', '*.filter', '-o', '-name', '*.bcl', '-o', '-name', '*.stats', '-delete']
                                    log.info('deleting intensities...')
                                    if not options.dry_run:
                                        utils.touch(intensities_deleted)
                                    utils.run_bg_process(delete_intensities_cmd, options.dry_run)
                            # deleting thumbnails
                            if os.path.exists(thumbnails_deleted):
                                log.info('All thumbnails deleted')
                            else:
                                if runfolder_age > delete_thumbnails_older_than:
                                    delete_thumbnails_cmd = ['find', '%s/Thumbnail_Images/' % run_folder, '-name', '*.jpg', '-delete']
                                    log.info('deleting thumbnails...')
                                    if not options.dry_run:
                                        utils.touch(thumbnails_deleted)
                                    utils.run_bg_process(delete_thumbnails_cmd, options.dry_run)
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

