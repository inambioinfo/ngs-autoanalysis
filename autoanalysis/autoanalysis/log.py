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
log = logging.getLogger("auto")
formatter = logging.Formatter('%(asctime)s %(name)-14s %(levelname)-8s: %(message)s')

def set_custom_logger(debug=None):
    # consol logging configuration
    consol_handler = logging.StreamHandler()
    consol_handler.setFormatter(formatter)
    if not len(log.handlers):
        log.addHandler(consol_handler)
    return log
                  
def set_file_handler(logfile):
    # rotating file logging configuration - 10 files of up to 5MB
    file_handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=1024*1024*5, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    return file_handler
    
def set_smtp_handler(subject):
    log.setLevel(logging.DEBUG)
    smtp_handler = logging.handlers.SMTPHandler(mailhost='smtp.cruk.cam.ac.uk', fromaddr='anne.pajon@cruk.cam.ac.uk', toaddrs=['anne.pajon@cruk.cam.ac.uk'], subject=subject)
    smtp_handler.setFormatter(formatter)
    smtp_handler.setLevel(logging.WARN)
    return smtp_handler


    