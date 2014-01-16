#!/usr/bin/env python
# encoding: utf-8
"""
sample_query.py

Created by Anne Pajon on 2013-01-29.
"""

import sys
import os
import requests

PROJECT_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.pardir)
sys.path.append(PROJECT_ROOT)

import glsapi.sample

HOSTNAME = 'http://limsdev.cri.camres.org:8080'
USERNAME = 'pajon01'
PASSWORD = 'lims'

SAMPLE_URI = HOSTNAME + "/api/v2/samples/"

def main():	
    """
    (1) Renaming a sample
    (2) Updating user-defined information for a sample
    """
    ### create a session for Requests, an HTTP library written in Python
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    session.headers.update({'content-type': 'application/xml', 'Accept': 'application/xml'})
    
    ### retrieve sample information
    sLUID = 'ACC401A3' # Sample id needs to be present in system
    xmldata = session.get(SAMPLE_URI + sLUID)
    xmldata.raise_for_status()
    sample = glsapi.sample.CreateFromDocument(xmldata.text)
	
    ### print sample details
    print "----------"
    print sample.name
    print sample.date_received
    print sample.project.limsid
    print sample.project.uri
    print sample.submitter.first_name
    print sample.submitter.last_name
    for field in sample.field:
        print field.name, field.type, field.value()

    print sample.toxml("utf-8")

    ### modify sample name
    sample.name = 'Isolate xC.32 updated via API'

    ### update sample name
    print "----------"
    s = session.put(SAMPLE_URI + sLUID, data=sample.toxml("utf-8"))
    print s.status_code
    updated_sample = glsapi.sample.CreateFromDocument(s.text)
    print updated_sample.name
    
    ### modify udf 'User Comments'
    print "----------"
    for field in updated_sample.field:
        if field.name == 'User Comments':
            updated_field = glsapi.userdefined.field('updated comment via API')
            updated_field.name = field.name
            updated_field.type = field.type
            updated_sample.field.remove(field)
            updated_sample.field.append(updated_field)

    print updated_sample.toxml("utf-8")
    
    ### update sample udf
    print "----------"
    s = session.put(SAMPLE_URI + sLUID, data=updated_sample.toxml("utf-8"))
    print s.status_code
    updated_sample = glsapi.sample.CreateFromDocument(s.text)
    print updated_sample.name
    for field in updated_sample.field:
        print field.name, field.type, field.value()
    
	
if __name__ == '__main__':
	main()

