#!/usr/bin/env python
# encoding: utf-8
"""
log.py

$Id$

Created by Anne Pajon on 2012-10-26.
"""

import logging
import logging.config
import socket

# constants and configurations
from config import cfg


# logging definition
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': socket.gethostname() + ' %(asctime)s %(name)-24s %(levelname)-8s: %(message)s'
        },
        'simple': {
            'format': '%(name)-24s %(levelname)-8s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'info_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'info.log',
            'maxBytes': 1000000,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'errors.log',
            'maxBytes': 1000000,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'email': {
            'level': 'ERROR',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': cfg['HOST'],
            'fromaddr': cfg['SEND_FROM'],
            'toaddrs': cfg['SEND_TO'],
            'subject': cfg['SUBJECT'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'autoanalysis': {
            'handlers': ['console', 'info_file', 'error_file'],
            'propagate': True,
            'level': 'INFO',
        },
        'glsclient': {
            'handlers': ['console', 'info_file', 'error_file'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}


def get_custom_logger(logfile=None, noemail=False):
    if logfile:
        LOGGING['handlers']['info_file']['filename'] = logfile
        LOGGING['handlers']['error_file']['filename'] = logfile + ".errors"
    if not noemail:
        LOGGING['loggers']['autoanalysis']['handlers'].append('email')
        LOGGING['loggers']['glsclient']['handlers'].append('email')
    logging.config.dictConfig(LOGGING)
    return logging.getLogger('autoanalysis')
