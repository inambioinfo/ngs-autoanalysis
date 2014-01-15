#!/usr/bin/env python
# encoding: utf-8
"""
process_query.py

Created by Anne Pajon on 2013-02-01.
"""

import sys
import os
import requests
from collections import defaultdict

PROJECT_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.pardir)
sys.path.append(PROJECT_ROOT)

import glsapi.process

HOSTNAME = 'http://limsdev.cri.camres.org:8080'
USERNAME = 'pajon01'
PASSWORD = 'lims'

URI = HOSTNAME + "/api/v2/processes/"


def main():
    """
    Viewing the inputs and outputs of a process
    """
    ### create a session
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    session.headers.update({'content-type': 'application/xml', 'Accept': 'application/xml'})

    ### retrieve process information
    limsid = '1PL-UTA-130510-24-46027'
    response = session.get(URI + limsid)
    response.raise_for_status()
    process = glsapi.process.CreateFromDocument(response.text)
    print process.toxml()
    
    ### grouping all inputs for each output
    output_dict = defaultdict(list)
    print "----------"
    for io in process.input_output_map:
        print io.input.limsid
        print io.output.limsid, io.output.output_type
        output_dict['%s_%s' % (io.output.limsid, io.output.output_type)].append(io.input.limsid)
        
    print "----------"
    for key, values in output_dict.items():
        print key
        for value in values:
            print '   input: %s' % value
            
    ### retrieve all sequencing run processes
    print "----------"
    uri = 'http://lims.cri.camres.org:8080/api/v2/processes?type=Illumina Sequencing Run (Illumina SBS) 4.0&type=MiSeq Run (MiSeq) 4.0'
    response = session.get(uri)
    response.raise_for_status()
    processes = glsapi.process.CreateFromDocument(response.text)
    print processes.toxml()
    for process in processes.process:
        print process.limsid, process.uri
        
    ### retrieve all sequencing run processes with a sequencing status set to complete
    print "----------"
    uri = 'http://lims.cri.camres.org:8080/api/v2/processes?type=Illumina Sequencing Run&udf.Sequencing Status=Started'
    response = session.get(uri)
    response.raise_for_status()
    processes = glsapi.process.CreateFromDocument(response.text)
    print processes.toxml()
    for process in processes.process:
        print process.limsid, process.uri
    print "----------"
    uri = 'http://lims.cri.camres.org:8080/api/v2/processes?type=MiSeq Run&udf.SeqStatus=Testing'
    response = session.get(uri)
    response.raise_for_status()
    processes = glsapi.process.CreateFromDocument(response.text)
    print processes.toxml()
    for process in processes.process:
        print process.limsid, process.uri
   

    ### retrive all files associated with a run process for a certain sample name
    # http://lims.cri.camres.org:8080/api/v2/artifacts?type=ResultFile&process-type=Illumina%20Sequencing%20Run%20%28Illumina%20SBS%29%204.0&process-type=MiSeq%20Run%20%28MiSeq%29%204.0&sample-name=meerkatCF

if __name__ == '__main__':
    main()

