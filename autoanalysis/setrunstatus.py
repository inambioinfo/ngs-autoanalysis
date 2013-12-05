#!/usr/bin/env python
# encoding: utf-8
"""
setrunstatus.py

$Id$

Created by Anne Pajon on 2013-04-25.

--------------------------------------------------------------------------------

Sequencing server script that creates Sequencing.completed

Usage:
> python setrunstatus.py --basedir=/solexa0[1-3]/data/Runs --debug
"""

################################################################################
# IMPORTS
################################################################################
import sys
import os
import argparse

# import custom modules
import autoanalysis.log as logger
import autoanalysis.utils as utils
import autoanalysis.runfolders as auto_runfolders

################################################################################
# CONSTANTS
################################################################################
# Instrument names with their run completed dependencies
INSTRUMENTS = {
	'HWI-ST230' : ['RTAComplete.txt'],
	'M01686' : ['RTAComplete.txt'],
	'M01642' : ['RTAComplete.txt'],
	'M01712' : ['RTAComplete.txt'],
	'HWI-EAS350' : ['Basecalling_Netcopy_complete.txt'],
	'HWI-EAS202' : ['Basecalling_Netcopy_complete.txt']
}

def create_sequencing_completed(run_folder, dry_run):
	sequencing_completed = os.path.join(run_folder, auto_runfolders.SEQUENCING_COMPLETED)
	if is_sequencing_completed(run_folder):
		if not os.path.exists(sequencing_completed):
			utils.touch(sequencing_completed, dry_run)
			log.info("%s created" % auto_runfolders.SEQUENCING_COMPLETED)
		else:
			log.info("Sequencing COMPLETED")
	else:
		log.info("Sequencing STARTED")

def is_sequencing_completed(run_folder):
	instrument_match = False
	files_found = True
	for instrument in list(INSTRUMENTS.viewkeys()):
		if instrument in run_folder:
			for filename in INSTRUMENTS[instrument]:
				if not os.path.exists(os.path.join(run_folder, filename)):
					files_found = False
			instrument_match = True
	return instrument_match and files_found

################################################################################
# MAIN
################################################################################
def main():

	# get the options
	parser = argparse.ArgumentParser()
	parser.add_argument("--basedir", dest="basedir", action="store", help="sequencing server base directories e.g. '/solexa0[1-8]/data/Runs'", required=True)
	parser.add_argument("--runfolder", dest="run_folder", action="store", help="run folder e.g. '130114_HWI-ST230_1016_D18MAACXX'")
	parser.add_argument("--dry-run", dest="dry_run", action="store_true", default=False, help="use this option to not do any shell command execution, only report actions")
	parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

	options = parser.parse_args()

	# logging configuration
	if options.logfile:
		log = logger.get_custom_logger(options.logfile)
	else:
		log = logger.get_custom_logger()

	try:
		runs = auto_runfolders.RunFolders(options.basedir, "", options.run_folder)
		# loop over all run folders in options.basedir
		for run_folder in runs.run_folders:
			try:
				# create Sequencing.completed
				log.info(auto_runfolders.RUN_HEADER % {'run_folder': run_folder})
				create_sequencing_completed(run_folder, options.dry_run)
			except:
				log.exception("Unexpected error")
				continue
	except:
		log.exception("Unexpected error")
		raise

if __name__ == "__main__":
	sys.exit(main())


