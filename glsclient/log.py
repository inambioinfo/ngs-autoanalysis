#!/usr/bin/env python
# encoding: utf-8
"""
log.py

Created by Anne Pajon on 2013-02-19.
"""

import logging
import logging.config

# logging definition
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)-24s %(levelname)-8s: %(message)s'
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
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'glsclient.log',
            'maxBytes': '1024*1024*5',
            'backupCount': '10',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'glsclient': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'glsextapi': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
} 


def get_custom_logger(logfile=None):
    if logfile:
        LOGGING['handlers']['file']['filename'] = logfile
    logging.config.dictConfig(LOGGING)
    return logging.getLogger('glsclient')


