#!/usr/bin/env python
# encoding: utf-8
"""
log.py

$Id$

Created by Anne Pajon on 2012-10-26.
"""

import logging
import logging.handlers

# logging definition
log = logging.getLogger("root")
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s: %(message)s')

def set_custom_logger(debug=None):
    # consol logging configuration
    consol_handler = logging.StreamHandler()
    consol_handler.setFormatter(formatter)
    log.addHandler(consol_handler)
    return log
                  
def set_file_handler(logfile):
    # rotating file logging configuration - 10 files of up to 5MB
    file_handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=1024*1024*5, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    return file_handler