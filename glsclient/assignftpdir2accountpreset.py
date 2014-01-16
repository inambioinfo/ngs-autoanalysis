#!/usr/bin/env python
# encoding: utf-8
"""
assignftpdir2accountpreset.py

Created by Anne Pajon on 2013-11-26.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import logging
import argparse

# import custom modules
import log as logger
import glsclient

ftpdir_newpresets = [
"gurdon_institute",
"haem_catgo",
"haem_cvejic",
"haem_ghevaert",
"haem_ouwehand",
"haem_warren",
"hutch_fitzgerald",
"ims_yeo",
"lmb_betz",
"lmb_chin",
"lmb_dear",
"lmb_debono",
"lmb_fersht",
"lmb_kay",
"lmb_mckenzie",
"lmb_radaneuberger",
"lmb_stewart",
"lmb_teichmann",
"lmb_ule",
"med_dolken",
"medgen_nejentsev",
"medgen_tischkowitz",
"obs_charnockjones",
"pdn_white",
"plant_baulcombe",
"plant_hibberd",
"plant_sciences",
"stem_frye",
"stem_gottgens",
"stem_vallier"
]

################################################################################
# MAIN
################################################################################
def main():
    # get the options
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", dest="update", action="store_true", default=False, help="use this option to preform the update and not only report action")
    parser.add_argument("--limsdev", dest="use_limsdev", action="store_true", default=False, help="Use the development LIMS url")
    parser.add_argument("--logfile", dest="logfile", action="store", default=False, help="File to print logging information")

    options = parser.parse_args()

    # logging configuration
    if options.logfile:
        log = logger.get_custom_logger(options.logfile)
    else:
        log = logger.get_custom_logger()

    try:
        # connect to lims
        if options.use_limsdev:
            lims_server = 'limsdev'
        else:
            #lims_server = 'lims'
            lims_server = 'lims'
        glsutil = glsclient.GlsUtil(server=lims_server)
        
        udf_ftpdir = glsutil.getFtpDirUdf()
        log.info(udf_ftpdir)
        existing_presets = []
        for preset_value in udf_ftpdir.preset:
            existing_presets.append(preset_value)
            log.info(preset_value)
        
        if options.update:
            for preset_value in ftpdir_newpresets:
                if not preset_value in udf_ftpdir.preset:
                    udf_ftpdir.preset.append(preset_value)
            glsutil.api.update(udf_ftpdir)
        else:
            log.info('To update use --update option')

    except:
        log.exception("Unexpected error")
        raise
    
if __name__ == "__main__":
	main()
