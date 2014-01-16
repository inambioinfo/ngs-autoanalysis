#!/usr/bin/env python
# encoding: utf-8
"""
db_query.py

Created by Anne Pajon on 2013-04-23.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.

Ideas: https://github.com/deliciousrobots/sqlnap/blob/master/sqlnap.py
"""

import sys
import os
import bottle
from bottle import (response, request, route, run)
import json
import collections
import datetime

# import custom modules
import log as logger
import glsextapi

DEFAULT_LIMIT=1000
DEFAULT_ENCODING='utf-8'
IDENTITY_TYPES = (unicode, int, float, bool)

def to_data(obj):
    for thetype in IDENTITY_TYPES:
        if isinstance(obj, thetype):
            return obj
    if obj is None:
        return obj
    elif isinstance(obj, str):
        return obj.decode(DEFAULT_ENCODING)
    elif isinstance(obj, collections.Mapping):
        return dict([(unicode(key), to_data(obj[key])) for key in obj])
    elif isinstance(obj, collections.Sequence):
        return [to_data(val) for val in obj]
    else:
        return unicode(obj)

def row_to_data(obj):
    return dict([(key, to_data(obj.__dict__[key])) for key in obj.__dict__ if isinstance(key, unicode)])

def dump_json(obj):
    response.content_type = 'application/json'
    return json.dumps(obj, indent=4)

@route('/glsextapi', method='GET')
def info():
    info = """ 
    <h3>External genologics API</h3>
    <p>Available services:
    <ul>
        <li>/glsextapi/runs/2013-07-01:2013-07-18 : returns the list of runs modified between these two dates.</li>
    </ul>
    """
    return info
    
@route('/glsextapi/runs/<dates>', method='GET')
def runs(dates):
    extapi = glsextapi.GlsExtApi()
    splited_dates = dates.split(':')
    if len(splited_dates) == 2:
        results = extapi.getRunsByStatus(splited_dates[0], splited_dates[1])
    else:
        results = extapi.getRunsByStatus(splited_dates[0])
    return dump_json(results)
    
def main():
    bottle.debug(True) 
    run(host='0.0.0.0', port=8181, server='cherrypy', debug=True, reloader=True)

if __name__ == '__main__':
    main()

