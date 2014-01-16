#!/usr/bin/env python
# encoding: utf-8
"""
artifact_query.py

Created by Anne Pajon on 2013-02-01.
"""

import sys
import os
import requests

PROJECT_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.pardir)
sys.path.append(PROJECT_ROOT)

import glsapi.artifact
import glsapi.sample

HOSTNAME = 'http://lims.cri.camres.org:8080'
USERNAME = 'pajon01'
PASSWORD = 'lims'

ARTIFACT_URI = HOSTNAME + "/api/v2/artifacts/"

def main():
    """
    Showing the relationship between samples and analyte artifacts
    (1) Retrieve an arbitrary artifact representation
    (2) Retrieve its corresponding samples
    (3) Retrieve that sample's original analyte artifact
    """
    
    ### create a session
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    session.headers.update({'content-type': 'application/xml', 'Accept': 'application/xml'})
    
    ### retrieve artifact information
    limsid = 'SCI148A8HS2'
    xml_artifact = session.get(ARTIFACT_URI + limsid)
    xml_artifact.raise_for_status()
    artifact = glsapi.artifact.CreateFromDocument(xml_artifact.text)
    print artifact.toxml()
	
    ### retrive all corresponding samples
    print "----------"
    print artifact.name
    for sample in artifact.sample:
        print sample.limsid, sample.uri
        xml_sample = session.get(sample.uri)
        xml_sample.raise_for_status()
        detailed_sample = glsapi.sample.CreateFromDocument(xml_sample.text)
        print detailed_sample.name
        print detailed_sample.toxml()
        
    ### retrive sample's original analyte artifact
    print "----------"
    sample = artifact.sample[0]
    xml_sample = session.get(sample.uri)
    xml_sample.raise_for_status()
    detailed_sample = glsapi.sample.CreateFromDocument(xml_sample.text)
    print detailed_sample.artifact.limsid
    print detailed_sample.artifact.uri
    xml_associated_artifact = session.get(detailed_sample.artifact.uri)
    xml_associated_artifact.raise_for_status()
    associated_artifact = glsapi.artifact.CreateFromDocument(xml_associated_artifact.text)
    print associated_artifact.toxml()
    
    
    
    
    


if __name__ == '__main__':
    main()

