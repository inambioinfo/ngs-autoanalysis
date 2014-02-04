#!/usr/bin/env python
# encoding: utf-8
"""
glsapi.py

Created by Anne Pajon on 2013-02-19.
"""

import sys
import os
import inspect
import unittest
import logging
import requests
from xml.dom import minidom
from collections import defaultdict

from sqlalchemy.ext.sqlsoup import SqlSoup

# Append root project to PYTHONPATH
ROOT_PROJECT=os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
sys.path.append(ROOT_PROJECT)

# import glsapi
import glsapi.artifact
import glsapi.container
import glsapi.configuration
import glsapi.containertype
import glsapi.instrument
import glsapi.lab
import glsapi.process
import glsapi.processexecution
import glsapi.processtype
import glsapi.project
import glsapi.researcher
import glsapi.ri
import glsapi.routing
import glsapi.sample
import glsapi.userdefined
import glsapi.wkfcnf

# import glssql for all database queries
import glssql

# Server names
#SERVER = 'limsdev.cri.camres.org'
#SERVER = 'genomicsequencing.cruk.cam.ac.uk'
SERVERS = {'lims': 'genomicsequencing.cruk.cam.ac.uk',
           'limsdev': 'limsdev.cri.camres.org'}

# Genologics REST API
HOSTNAME = 'http://%(server)s:8080' 
USERNAME = 'apiuser'
PASSWORD = 'apipassword'
API_VERSION = 'v2'

# REST uri template
REST_URI_TEMPLATE = "%(hostname)s/api/%(api_version)s/%(resource)s/%(luid)s"
REST_URI_FILTER_TEMPLATE = "%(hostname)s/api/%(api_version)s/%(resource)s?%(filters)s"

# Genologics Database url
DB_URL = "postgres://readonly:readonly@%(server)s/clarityDB"

# Specific fields used in lims
SLX_FIELD = "SLX Identifier"
RUN_ID_FIELD = "Run ID"
FLOW_CELL_ID_FIELD = "Flow Cell ID"
REAGENT_CARTRIDGE_ID_FIELD = "Reagent Cartridge ID"
PROGRESS_STATUS = 'Progress'

FLOW_CELL_CONTAINER_TYPE = "Illumina Flow Cell"
MISEQ_CONTAINER_TYPE = "MiSeq Reagent Cartridge"

RUN_PROCESS_NAMES = ["Illumina Sequencing Run", "MiSeq Run", "Historical Sequencing Run"]
ANALYSIS_PROCESS_NAMES = {'fastq': 'FASTQ Lane Pipeline',
                          'demux': 'FASTQ Sample Pipeline',
                          'align': 'Alignment Pipeline',
                          'publi': 'Publishing'}
                          
WORKFLOW_NAMES = {'publi': 'BIO: Publishing and Billing',
                  'bill': 'BIO: Billing Only'}
                          
ANALYSIS_UNDERWAY = 'Analysis Underway'
PUBLISHING_UNDERWAY = 'Publishing Underway'
DATA_PUBLISHED = 'Data Published'

################################################################################
# Class
################################################################################
class GlsClientApi(object):
    
    def __init__(self, hostname, username, password):
        self.log = logging.getLogger(__name__)    
        self.hostname = hostname
        self.username = username
        self.password = password
        ### create a request session
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({'content-type': 'application/xml', 'Accept': 'application/xml','Accept-Encoding': 'gzip, deflate, compress', 'charset': 'UTF-8'})
        
        ### set resources
        self.resources = {
        'artifact': {'uri':'artifacts', 'mod':'artifact'},
        'container': {'uri':'containers', 'mod':'container'},
        'container_type': {'uri':'containertypes', 'mod':'containertype'},
        'configuration': {'uri':'configuration/udfs', 'mod':'configuration'},
        'instrument': {'uri':'instruments', 'mod':'instrument'},
        'lab': {'uri':'labs', 'mod':'lab'},
        'process': {'uri':'processes', 'mod':'process'},
        'process_type': {'uri':'processtypes', 'mod':'processtype'},
        'project': {'uri':'projects', 'mod':'project'},
        'researcher': {'uri':'researchers', 'mod':'researcher'},
        'routing': {'uri':'route/artifacts', 'mod':'routing'},
        'sample': {'uri':'samples', 'mod':'sample'},
        'workflow': {'uri':'configuration/workflows', 'mod':'wkfcnf'},
        #'': {'uri':'', 'mod':''},
        }
        ### set filters
        self.sample_filter_by_projectname = 'projectname'
        self.artifact_filter_by_samplename = 'sample-name'
        
    def list(self, _resource_name):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': ''}
        response = self.session.get(uri)
        return self._createFromDoc(_resource_name, response)
        
    def listFilterByName(self, _resource_name, _name):
        return self.listFilter(_resource_name, 'name', _name)

    def listFilter(self, _resource_name, _filter_key, _filter_value):
        filters = {_filter_key:_filter_value}
        return self.listFilters(_resource_name, filters)

    def listFilters(self, _resource_name, _filters):
        filters_uri = ''
        for key,value in _filters.iteritems():
            filters_uri += '%(key)s=%(value)s&' % {'key': key, 'value': value}
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_FILTER_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'filters': filters_uri[:-1]}
        response = self.session.get(uri)
        return self._createFromDoc(_resource_name, response)

    def load(self, _resource_name, _limsid):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': _limsid}
        response = self.session.get(uri)
        return self._createFromDoc(_resource_name, response)
        
    def loadByUri(self, _resource_name, _uri):
        response = self.session.get(_uri)
        return self._createFromDoc(_resource_name, response)
        
    def update(self, _object):
        response = self.session.put(_object.uri, data=_object.toxml('utf-8'))
        resource = _object.__class__.__module__.split('.')[-1]
        return self._createFromDoc(resource, response)
    
    def create(self, _resource_name, _object):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': ''}
        self.log.debug(self.prettyXml(_object.toxml('utf-8')))
        response = self.session.post(uri, _object.toxml('utf-8'))
        return self._createFromDoc(_resource_name, response)
        
    def delete(self, _object):
        try:
            response = self.session.delete(_object.uri)
            response.raise_for_status()
            return response
        except:
            self.log.exception(_response.text)
            raise
            
    def _createFromDoc(self, _resource_name, _response):
        try:
            resource = self.resources[_resource_name]['mod']
            self.log.debug(_response.status_code)
            self.log.debug(self.prettyXml(_response.text))
            _response.raise_for_status()
            return getattr(glsapi, resource).CreateFromDocument(_response.text.encode('utf-8'))
        except:
            self.log.exception(_response.text)
            self.log.error(_response.raise_for_status())
            raise
            
    def prettyXml(self, _rough_xml):
        reparsed = minidom.parseString(_rough_xml.encode('utf-8'))
        return reparsed.toprettyxml(indent="    ")
        

################################################################################
# Class
################################################################################
class GlsUtil(object):

    def __init__(self, server, username=USERNAME, password=PASSWORD):
        self.log = logging.getLogger(__name__)
        self.server = server
        self.hostname = HOSTNAME % {'server':SERVERS[self.server]}
        self.username = username
        self.password = password
        self.api = GlsClientApi(self.hostname, self.username, self.password)
        self.db_url = DB_URL % {'server':self.server}
        self.db = SqlSoup(self.db_url)

    def getSamplesByUser(self, _email):
        results = self.db.execute(glssql.SAMPLE_BY_USER_QUERY % _email).fetchall()
        samples = []
        for sample in results:
            dsample = {'projectid': sample.projectid, 'sampleid': sample.sampleid, 'luid': sample.luid, 'name': sample.name, 'datereceived': sample.datereceived, 'datecompleted': sample.datecompleted}
            sample_udfs = self.db.execute(glssql.SAMPLEID_UDF_QUERY % sample.sampleid).fetchall()
            for udf in sample_udfs:
                dsample[udf.key] = udf.value
            samples.append(dsample)
        self.log.debug(samples)
        return samples

    def getSampleIdsBySlxId(self, _slxid):
        results = self.db.execute(glssql.SAMPLEID_BY_SLXID_QUERY % _slxid).fetchall()
        sampleids = []
        for sample in results:
            sampleids.append(sample.sampleid)
        self.log.debug(sampleids)
        return sampleids

    def getSlxIdBySampleId(self, _sampleid):
        results = self.db.execute(glssql.SLXID_BY_SAMPLEID_QUERY % _sampleid).fetchall()
        if len(results) > 1:
            raise Exception('More than one SLX-ID per sample id %s' % _sampleid)
        self.log.debug(results[0].slxid)
        return results[0].slxid

    def getProcessByFlowcellId(self, _process_name, _flowcell_id):
        results = self.db.execute(glssql.PROCESS_BY_UDF_QUERY % (_process_name, FLOW_CELL_ID_FIELD, _flowcell_id)).fetchall()
        processes = []
        for process in results:
            dprocess = {'id': process.luid, 'daterun': process.daterun, 'name': process.displayname, 'status': process.workstatus, 'createddate': process.createddate, 'lastmodifieddate': process.lastmodifieddate, 'flowcellid': process.udfvalue}
            processes.append(dprocess)
        self.log.debug(processes)
        return processes
    
    def getCompleteRunProcessByFlowcellId(self, _flowcell_id):
        results = self.db.execute(glssql.COMPLETERUNPROCESS_BY_UDF_QUERY % (FLOW_CELL_ID_FIELD, _flowcell_id)).fetchall()
        processes = []
        for process in results:
            dprocess = {'id': process.luid, 'daterun': process.daterun, 'name': process.displayname, 'status': process.workstatus, 'createddate': process.createddate, 'lastmodifieddate': process.lastmodifieddate, 'flowcellid': process.udfvalue}
            processes.append(dprocess)
        self.log.debug(processes)
        return processes

    def getCompleteRunProcessByRunId(self, _run_id):
        results = self.db.execute(glssql.COMPLETERUNPROCESS_BY_UDF_QUERY % (RUN_ID_FIELD, _run_id)).fetchall()
        processes = []
        for process in results:
            dprocess = {'id': process.luid, 'daterun': process.daterun, 'name': process.displayname, 'status': process.workstatus, 'createddate': process.createddate, 'lastmodifieddate': process.lastmodifieddate, 'flowcellid': process.udfvalue}
            processes.append(dprocess)
        self.log.debug(processes)
        return processes
        
    def getPublishingProcessByInputArtifact(self, _artifact_luid):
        results = self.db.execute(glssql.PUBLISHINGPROCESS_BY_INPUTARTIFACTLUID_QUERY % _artifact_luid).fetchall()
        processes = []
        for process in results: 
            dprocess = {'id': process.luid, 'daterun': process.daterun, 'name': process.displayname, 'status': process.workstatus, 'createddate': process.createddate, 'lastmodifieddate': process.lastmodifieddate}
            processes.append(dprocess)
        self.log.debug(processes)
        return processes
        
    def getBillingProcessByInputArtifact(self, _artifact_luid):
        results = self.db.execute(glssql.BILLINGPROCESS_BY_INPUTARTIFACTLUID_QUERY % _artifact_luid).fetchall()
        processes = []
        for process in results: 
            dprocess = {'id': process.luid, 'daterun': process.daterun, 'name': process.displayname, 'status': process.workstatus, 'createddate': process.createddate, 'lastmodifieddate': process.lastmodifieddate}
            processes.append(dprocess)
        self.log.debug(processes)
        return processes

    def getLatestCompleteRunProcessByRunId(self, _run_id):
        results = self.getCompleteRunProcessByRunId(_run_id)
        if not results:
            self.log.warning('no run process found for run id %s' % _run_id)
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one run processes found for run id %s' % _run_id)
            return self.api.load('process', results[0]['id'])
            
    def getLatestCompleteRunProcessByFlowcellId(self, _flowcell_id):
        results = self.getCompleteRunProcessByFlowcellId(_flowcell_id)
        if not results:
            self.log.warning('no run process found for flow-cell id %s' % _flowcell_id)
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one run processes found for flow-cell id %s' % _flowcell_id)
            return self.api.load('process',results[0]['id'])
            
    def areAllFailedLanesOnRunProcess(self, _run_id):
        if not self.db.execute(glssql.NONFAILEDLANE_RUNPROCESS_BY_RUNID_QUERY % _run_id).fetchall():
            return True
        return False

    def getUniqueInputUriListFromProcess(self, _process):
        input_uri_list = []
        for io_elem in _process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        return set(input_uri_list)
        
    def getUniqueOutputUriListFromProcess(self, _process):
        output_uri_list = []
        for io_elem in _process.input_output_map:
            output_uri_list.append(io_elem.output.uri)
        return set(output_uri_list)

    def getUniqueInputPostProcessUriListFromProcess(self, _process):
        input_uri_list = []
        for io_elem in _process.input_output_map:
            input_uri_list.append(io_elem.input.post_process_uri)
        return set(input_uri_list)

    def isSequencingCompleted(self, _run_id):
        # get latest complete sequencing process where x=y in cycle x of y and finish date exists
        run_process = self.getLatestCompleteRunProcessByRunId(_run_id)
        if run_process is None:
            return False
        else:
            return True
        """
        Do not check qc flags at lane level on sequencing run anymore (10/01/2014)
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputPostProcessUriListFromProcess(run_process)
        passed = False
        failed = False
        unknown = False
        for input_artifact_uri in input_uri_set:
            artifact = self.api.loadByUri('artifact', input_artifact_uri)
            if artifact.qc_flag == 'PASSED':
                passed = True
            if artifact.qc_flag == 'FAILED':
                failed = True
            if artifact.qc_flag == 'UNKNOWN':
                unknown = True
        if failed and not passed and not unknown:
            return False
        if passed and not unknown:
            return True
        return None
        """
        
    def isSequencingFailed(self, _run_id):
        complete_run_process_byrunid = self.getLatestCompleteRunProcessByRunId(_run_id)
        # no complete run process found for run folder
        if complete_run_process_byrunid is None:
            # no process found for run folder
            run_process_byrunid = self.db.execute(glssql.PROCESS_BY_UDF_QUERY % ('%%Run%%', RUN_ID, _run_id)).fetchall()
            if run_process_byrunid is None:
                # check if a complete run process exists for this FC
                fc_id = _run_id.split('_')[-1]
                run_process_byfcid = self.getLatestCompleteRunProcessByFlowcellId(fc_id)
                # complete run process found for FC - sequencing failed for this run folder
                if run_process_byfcid:
                    return True
            # process found for run folder
            else:
                # check if all lane qc flags are set to failed and run not at the end of cycle
                if self.areAllFailedLanesOnRunProcess(_run_id):
                    return True
        return False
        
    def createAnalysisProcess(self, _name, _run_process):
        technician_uri = self.api.listFilter('researcher', 'username', USERNAME).researcher[0].uri
        process = glsapi.processexecution.process()
        process.type = ANALYSIS_PROCESS_NAMES[_name]
        process.technician = glsapi.processexecution.technician()
        process.technician.uri = technician_uri
        # set udfs
        for run_field in _run_process.field:
            if run_field.name == RUN_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == FLOW_CELL_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == REAGENT_CARTRIDGE_ID_FIELD:
                process.field.append(run_field)
        return process
        
    def createBclToFastqPipelineProcess(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.getLatestCompleteRunProcessByFlowcellId(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputUriListFromProcess(run_process)
        # create bcl to fastq pipeline process
        process = self.createAnalysisProcess('fastq', run_process)
        # create input-output-maps
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            # 7 output result files per lane for fastq pipeline
            # Read 1 FASTQ,Read 2 FASTQ,FASTQ MD5 Checksums,Lane Index,MGA Lane Report,FASTQC Lane Report,Demultiplex Barcode Summary
            for i in range(7):
                io_map = glsapi.processexecution.input_output_map()
                io_map.input.append(input_artifact) 
                io_map.output = glsapi.processexecution.output()
                io_map.output.type = 'ResultFile'
                process.input_output_map.append(io_map)

        self.log.debug(self.api.prettyXml(process.toxml('utf-8')))
        return self.api.create('process', process)
        
    def createDemuxPipelineProcess(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.getLatestCompleteRunProcessByFlowcellId(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputUriListFromProcess(run_process)
        # create demultiplexing pipeline process
        process = self.createAnalysisProcess('demux', run_process)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the process is configured to exclusively produce outputs per reagent label
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(self.api.prettyXml(process.toxml('utf-8')))
        return self.api.create('process', process)
        
    def createAlignmentPipelineProcess(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.getLatestCompleteRunProcessByFlowcellId(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputUriListFromProcess(run_process)
        # create alignment pipeline process
        process = self.createAnalysisProcess('align', run_process)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the process is configured to exclusively produce outputs per reagent label
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(self.api.prettyXml(process.toxml('utf-8')))
        return self.api.create('process', process)
        
    def getSingleAnalysisProcessByFlowcellId(self, _name, _flowcell_id):
        results = self.getProcessByFlowcellId(ANALYSIS_PROCESS_NAMES[_name], _flowcell_id)
        if not results:
            self.log.debug('no %s process found for flow-cell id %s' % (_name, _flowcell_id))
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one %s processes found for flow-cell id %s' % (_name, _flowcell_id))
            return self.api.load('process',results[0]['id'])
            
    def routeEachArtifactToWorkflow(self, _artifact_uri_set, _workflow_name):
        # get workflow
        workflows = self.api.listFilterByName('workflow', _workflow_name)
        workflow = workflows.workflow[0]
        # assign each artifact to workflow queue
        for artifact_uri in _artifact_uri_set: 
            routing_artifact = glsapi.routing.artifact()
            routing_artifact.uri = artifact_uri
            routing_assignment = glsapi.routing.extArtifactAssignments()
            routing_assignment.workflow_uri = workflow.uri
            routing_assignment.artifact.append(routing_artifact)
            routing = glsapi.routing.routing()
            routing.assign.append(routing_assignment)
            self.log.debug(self.api.prettyXml(routing.toxml('utf-8')))
            created_route = self.api.create('routing', routing)

    def assignFlowcellToPublishingWorkflow(self, _flowcell_id):
        # check run process exists
        run = self.getLatestCompleteRunProcessByFlowcellId(_flowcell_id)
        # get one input artifact from run process
        input_artifact = self.api.loadByUri('artifact', run.input_output_map[0].input.uri)
        publi = self.getPublishingProcessByInputArtifact(input_artifact.limsid)
        # if publishing process do not already exist
        if not publi:
            # get fastq & demux & alignment processes
            fastq = self.getSingleAnalysisProcessByFlowcellId('fastq', _flowcell_id)
            demux = self.getSingleAnalysisProcessByFlowcellId('demux', _flowcell_id)
            align = self.getSingleAnalysisProcessByFlowcellId('align', _flowcell_id)
            # check fastq & demux & alignment processes exist
            if fastq and demux and align:
                # get workflow
                workflows = self.api.listFilterByName('workflow', WORKFLOW_NAMES['publi'])
                workflow = workflows.workflow[0]
                # build a unique set of input artifacts
                input_uri_set = self.getUniqueInputUriListFromProcess(fastq)
                # assign each artifact to publish queue in analyses workflow
                self.routeEachArtifactToWorkflow(input_uri_set, WORKFLOW_NAMES['publi'])
                self.log.info("flow-cell id '%s' assigned to '%s' workflow for publishing." % (_flowcell_id, WORKFLOW_NAMES['publi']))
        else:
            self.log.info("flow-cell id '%s' has already a publishing process '%s'." % (_flowcell_id, publi[0]['id']))
     
    def assignFlowcellToBillingOnlyWorkflow(self, _flowcell_id, _run_type, _update=True):
        # check run process exists
        run = self.getLatestCompleteRunProcessByFlowcellId(_flowcell_id)
        if run:
            if _run_type == 'Historical Sequencing Run':
                self.log.info("OLD: %s" % run)
                # get one output artifact from 'Historical Sequencing Run' process as flowcell
                output_artifact = self.api.loadByUri('artifact', run.input_output_map[0].output.uri)
                billing = self.getBillingProcessByInputArtifact(output_artifact.limsid)
                # build a unique set of output artifacts
                artifact_uri_set = self.getUniqueOutputUriListFromProcess(run)
            else:
                self.log.info("GLS: %s" % run)
                # get one input artifact from run process
                input_artifact = self.api.loadByUri('artifact', run.input_output_map[0].input.uri)
                billing = self.getBillingProcessByInputArtifact(input_artifact.limsid)
                # build a unique set of input artifacts
                artifact_uri_set = self.getUniqueInputUriListFromProcess(run)
            if not billing:
                if _update:
                    self.routeEachArtifactToWorkflow(artifact_uri_set, WORKFLOW_NAMES['bill'])
                    self.log.info("flow-cell id '%s' assigned to '%s' workflow for billing." % (_flowcell_id, WORKFLOW_NAMES['bill']))
            else:
                self.log.info("flow-cell id '%s' has already a billing process '%s'." % (_flowcell_id, billing[0]['id']))
            
    def updateFlowcellSamplesProgressStatus(self, _flowcell_id, _progress_status):
        fastq = self.getSingleAnalysisProcessByFlowcellId('fastq', _flowcell_id)
        if fastq:
            # build a unique set of input artifacts
            input_uri_set = self.getUniqueInputUriListFromProcess(fastq)
            # update each sample progress status to Analysis Underway
            for input_artifact_uri in input_uri_set:
                input_artifact = self.api.loadByUri('artifact', input_artifact_uri)
                for sample in input_artifact.sample:
                    self.log.debug(sample.uri)
                    sample = self.api.loadByUri('sample', sample.uri)
                    update_sample = True
                    for f in sample.field:
                        if f.name == PROGRESS_STATUS:
                            self.log.debug(f.value())
                            if f.value() == _progress_status:
                                update_sample = False
                            elif f.value() == PUBLISHING_UNDERWAY:
                                update_sample = False
                            elif f.value() == DATA_PUBLISHED:
                                update_sample = False 
                            else:
                                sample.field.remove(f)
                    if update_sample:
                        updated_field = glsapi.userdefined.field(_progress_status)
                        updated_field.name = PROGRESS_STATUS
                        sample.field.append(updated_field)
                        updated_sample = self.api.update(sample)
                        for f in updated_sample.field:
                            if f.name == PROGRESS_STATUS:
                                self.log.info("flow-cell id '%s': sample '%s' - Progress Status Updated to %s" % (_flowcell_id, updated_sample.limsid, f.value()))
    
    def isFastqPipelineComplete(self, _run_id):
        """Only check if all Read 1 Sample Fastq files exist for lanes that passed qc on sequencing
        """
        # get latest sequencing process for run id
        run_process = self.getLatestCompleteRunProcessByRunId(_run_id)
        if run_process is None:
            flowcell_id = _run_id.split('_')[-1]
            run_process_by_fc = self.getLatestCompleteRunProcessByFlowcellId(flowcell_id)
            if run_process_by_fc is not None:
                return False
            return None
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputPostProcessUriListFromProcess(run_process)
        for input_artifact_uri in input_uri_set:
            artifact = self.api.loadByUri('artifact', input_artifact_uri)
            self.log.debug(artifact.qc_flag)
            if artifact.qc_flag == 'PASSED':
                location = artifact.location.value_
                self.log.debug(location)
                results = self.db.execute(glssql.UNASSIGNED_FASTQ1_ON_PROCESS_BY_UDF_QUERY % (_run_id, location)).fetchall()
                self.log.debug(results)
                if results: 
                    return False
        return True
        
    def isDemuxPipelineComplete(self, _run_id):
        """Only check if all Read 1 Fastq files exist for lanes that passed qc on sequencing
        """
        # get latest sequencing process for run id
        run_process = self.getLatestCompleteRunProcessByRunId(_run_id)
        if run_process is None:
            flowcell_id = _run_id.split('_')[-1]
            run_process_by_fc = self.getLatestCompleteRunProcessByFlowcellId(flowcell_id)
            if run_process_by_fc is not None:
                return False
            return None
        # build a unique set of input artifacts
        input_uri_set = self.getUniqueInputPostProcessUriListFromProcess(run_process)
        for input_artifact_uri in input_uri_set:
            artifact = self.api.loadByUri('artifact', input_artifact_uri)
            self.log.debug(artifact.qc_flag)
            if artifact.qc_flag == 'PASSED':
                location = artifact.location.value_
                self.log.debug(location)
                results = self.db.execute(glssql.UNASSIGNED_FASTQ1_ON_PROCESS_BY_UDF_QUERY % (ANALYSIS_PROCESS_NAMES['demux'], RUN_ID_FIELD, _run_id, location)).fetchall()
                if results: 
                    return False
        return True
        
    def isPublishingComplete(self, _run_id):
        """Check if publishing process exists
        """
        
        
    def isExternalData(self, _run_id):
        """Return true if external data on this run
        """
        if self.db.execute(glssql.EXTERNAL_DATA_QUERY % (_run_id)).fetchall():
            return True
        return False
        
    def getLaneFastqFiles(self, _run_id):
        """Return lane level files for this run folder name called run id in genologics
        """
        return self.db.execute(glssql.FILES_QUERY % {'processname': 'FASTQ Lane Pipeline','runid': _run_id}).fetchall()
        
    def getSampleFastqFiles(self, _run_id):
        """Return sample level files for this run folder name called run id in genologics
        """
        return self.db.execute(glssql.FILES_QUERY % {'processname': 'FASTQ Sample Pipeline','runid': _run_id}).fetchall()
        
    def getAllExternalFtpDirs(self):
        """Return list of all external ftp directories
        """
        results = self.db.execute(glssql.EXTERNAL_FTPDIR_QUERY).fetchall()
        labftpdirs = {}
        for lab in results: 
            labftpdirs[lab.labid] = {'ftpdir': lab.ftpdir, 'nonpfdata': lab.nonpfdata}
        self.log.debug(labftpdirs)
        return labftpdirs
        
    def getUnasignedSamplesToWorkflows(self):
        query = """
        SELECT waiting.luid 
        FROM artifact waiting 
        WHERE waiting.isoriginal 
        AND NOT EXISTS ( 
            SELECT assigned.artifactid 
            FROM stagetransition assigned 
            WHERE assigned.artifactid = waiting.artifactid
            )
        """
        # list sample processes with only one artifact
        # then use processiotracker to find the one without process
        query_2 = """
        SELECT f.processid FROM (SELECT processid, COUNT(artifactid) AS occurences FROM artifact_sample_map GROUP BY processid) AS f WHERE f.occurences=1
        """
        results = self.db.execute(query).fetchall()
        return results
        
    def getFtpDirUdf(self):
        return self.api.load('configuration', '709')
        

        
################################################################################
# Unit tests for GlsClientApi
################################################################################    
class GlsClientApiTest(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.glsclient = GlsClientApi(HOSTNAME % {'server':SERVERS['limsdev']}, USERNAME, PASSWORD)
        self.unknown_id = 'unknown'
        self.containertype_id = '1' 
        self.containertype_name = '96 well plate'
        self.instrument_id = '3'
        self.instrument_name = 'Hiseq [HWI-ST230]'
        self.lab_id = '2'
        self.lab_name = 'Genomics Core'
        # load project
        self.project_name = 'Python Unit Tests'
        self.projects = self.glsclient.listFilterByName('project', self.project_name)
        self.project = self.projects.project[0]
        # load container type
        self.container_type_name = 'Tube'
        self.container_types = self.glsclient.listFilterByName('container_type', self.container_type_name)
        self.container_type = self.container_types.container_type[0]
        # container name
        self.container_name = 'Container created via Python Unit Test'
        # sample name
        self.sample_name = 'Sample created via Python Unit Test'
        # workflow name
        self.workflow_name = 'BIO: Analyses'
        self.workflows = self.glsclient.listFilterByName('workflow', self.workflow_name)
        self.workflow = self.workflows.workflow[0]
        # process type
        self.process_type_name = 'FASTQ Lane Pipeline'
        self.process_types = self.glsclient.listFilterByName('process_type', self.process_type_name)
        self.process_type = self.process_types.process_type[0]
        
    def test_session(self):
        self.assertEqual(self.glsclient.session.auth, (USERNAME, PASSWORD))
        self.assertEqual(self.glsclient.session.headers, {'content-type': 'application/xml', 'Accept-Encoding': 'gzip, deflate, compress', 'charset': 'UTF-8', 'Accept': 'application/xml', 'User-Agent': 'python-requests/1.2.0 CPython/2.7.5 Darwin/12.5.0'})
        
    def test_session_response(self):
        uri = REST_URI_TEMPLATE % {'hostname': self.glsclient.hostname, 'api_version': API_VERSION, 'resource': 'labs', 'luid': self.lab_id}
        response = self.glsclient.session.get(uri)
        self.assertEqual(response.status_code, requests.codes.ok)
        
    def test_load_unknown(self):
        self.assertRaises(KeyError, self.glsclient.load, 'unknown', self.unknown_id)

    def test_list_containertypes(self):
        containertype_list = self.glsclient.list('container_type')
        containertypename_list = []
        for containertype in containertype_list.container_type:
            containertypename_list.append(containertype.name)
        self.assertIn(self.containertype_name, containertypename_list)
         
    def test_list_instruments(self):
        instrument_list = self.glsclient.list('instrument')
        instrumentname_list = []
        for instrument in instrument_list.instrument:
            instrumentname_list.append(instrument.name)
        self.assertIn(self.instrument_name, instrumentname_list)
        
    def test_load_instrument(self):
        instrument = self.glsclient.load('instrument', self.instrument_id)
        self.assertEqual(instrument.name, self.instrument_name)
        
    def test_list_labs(self):
        lab_list = self.glsclient.list('lab')
        labname_list = []
        for lab in lab_list.lab:
            labname_list.append(lab.name)
        self.assertIn(self.lab_name, labname_list)
        
    def test_load_lab(self):
        lab = self.glsclient.load('lab', self.lab_id)
        self.assertEqual(lab.name, self.lab_name)
        
    def test_load_project_by_name(self):
        self.assertEqual(1, len(self.projects.project))
        self.assertEqual(self.projects.project[0].name, self.project_name)
        self.assertEqual(self.project.name, self.project_name)
        
    def test_load_container_type_by_name(self):
        self.assertEqual(1, len(self.container_types.container_type))
        self.assertEqual(self.container_types.container_type[0].name, self.container_type_name)
        self.assertEqual(self.container_type.name, self.container_type_name)

    def test_create_delete_empty_container(self):
        container = glsapi.container.container(self.container_name)
        container.type = glsapi.container.container_type()
        container.type.name = self.container_type.name
        container.type.uri = self.container_type.uri
        self.assertEqual(container.name, self.container_name)
        created_container = self.glsclient.create('container', container)
        self.assertEqual(created_container.name, container.name)
        delete_response = self.glsclient.delete(created_container)
        self.assertEqual(delete_response.status_code, 204)
        self.assertRaises(requests.exceptions.HTTPError, self.glsclient.load, 'container', created_container.limsid)
        
    def test_create_sample_in_container_within_project(self):
        # This test will create a new sample every times!
        # create container
        container = glsapi.container.container(self.container_name)
        container.type = glsapi.container.container_type()
        container.type.name = self.container_type.name
        container.type.uri = self.container_type.uri
        created_container = self.glsclient.create('container', container)
        self.assertEqual(created_container.name, container.name)
        # associate sample with project
        sample = glsapi.sample.samplecreation(self.sample_name)
        sample.project = glsapi.sample.project()
        sample.project.uri = self.project.uri
        # associate sample with container using location
        sample.location = glsapi.ri.location()
        sample.location.container = glsapi.ri.container()
        sample.location.container.uri = created_container.uri
        sample.location.value_ = '1:1'
        # add required UDF
        # Sample Type = DNA
        sample_type_field = glsapi.userdefined.field('DNA')
        sample_type_field.name = 'Sample Type'
        sample.field.append(sample_type_field)
        # Priority Status = Standard
        priority_status_field = glsapi.userdefined.field('Standard')
        priority_status_field.name = 'Priority Status'
        sample.field.append(priority_status_field)
        created_sample = self.glsclient.create('sample', sample)
        self.assertEqual(created_sample.name, self.sample_name)
        
    def test_load_samples_within_project(self):
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        for sample_link in samples.sample:
            sample = self.glsclient.load('sample', sample_link.limsid)
            self.assertEqual(sample.name, self.sample_name)
        self.assertRaises(requests.exceptions.HTTPError, self.glsclient.load, 'sample', self.unknown_id)
        
    def test_update_sample_names_within_project(self):
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        for sample_link in samples.sample:
            sample = self.glsclient.load('sample', sample_link.limsid)
            original_name = sample.name
            updated_name = '%s - updated via Python Unit Test' % original_name 
            sample.name = updated_name
            updated_sample = self.glsclient.update(sample)
            # revert name back to original one
            sample.name = original_name
            original_sample = self.glsclient.update(sample)
            self.assertEqual(updated_sample.name, updated_name)
            self.assertEqual(original_sample.name, original_name)
            
    def test_list_workflows(self):
        workflows = self.glsclient.list('workflow')
        workflow_names = []
        for workflow in workflows.workflow:
            workflow_names.append(workflow.name)
        self.assertIn(self.workflow_name, workflow_names)
        
    def test_load_artifact_of_sample(self):
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        sample = self.glsclient.load('sample', samples.sample[0].limsid)
        artifact = self.glsclient.load('artifact', sample.artifact.limsid)
        self.assertEqual(sample.artifact.limsid, artifact.limsid)
        self.assertRaises(requests.exceptions.HTTPError, self.glsclient.load, 'artifact', self.unknown_id)

    def test_update_artifact_name(self):
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        sample = self.glsclient.load('sample', samples.sample[0].limsid)
        artifact = self.glsclient.load('artifact', sample.artifact.limsid)
        original_name = artifact.name
        updated_name = '%s - updated via Python Unit Test' % original_name 
        artifact.name = updated_name
        updated_artifact = self.glsclient.update(artifact)
        # revert name back to original one
        artifact.name = original_name
        original_artifact = self.glsclient.update(artifact)
        self.assertEqual(updated_artifact.name, updated_name)
        self.assertEqual(original_artifact.name, original_name)
        
    def test_list_process_types(self):
        process_types = self.glsclient.list('process_type')
        process_type_names = []
        for process_type in process_types.process_type:
            process_type_names.append(process_type.name)
        self.assertIn(self.process_type_name, process_type_names)
        
    def test_list_researchers_by_username(self):
        researcher_links = self.glsclient.listFilter('researcher', 'username', USERNAME)
        researcher = self.glsclient.loadByUri('researcher', researcher_links.researcher[0].uri)
        self.assertEqual(USERNAME, researcher.credentials.username)
        
    def test_create_process_with_resultfile(self):
        technician_uri = self.glsclient.listFilter('researcher', 'username', USERNAME).researcher[0].uri
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        sample = self.glsclient.load('sample', samples.sample[0].limsid)
        io_map = glsapi.processexecution.input_output_map()
        input_artifact = glsapi.processexecution.input() 
        input_artifact.uri = sample.artifact.uri
        io_map.input.append(input_artifact) 
        io_map.output = glsapi.processexecution.output()
        io_map.output.type = 'ResultFile'
        process = glsapi.processexecution.process()
        process.type = self.process_type_name
        process.technician = glsapi.processexecution.technician()
        process.technician.uri = technician_uri
        process.input_output_map.append(io_map)
        self.log.debug(process.toxml('utf-8'))
        created_process = self.glsclient.create('process', process)
        self.assertEqual(process.type, self.process_type_name)
        process_type = self.glsclient.loadByUri('process_type', created_process.type.uri)
        self.assertEqual(process_type.name, self.process_type_name)
        
    def test_add_filetype_to_resultfile(self):
        processes = self.glsclient.listFilter('process', 'type', self.process_type_name)
        process_link = processes.process[0]
        process = self.glsclient.loadByUri('process', process_link.uri)
        process_type = self.glsclient.loadByUri('process_type', process.type.uri)
        self.assertEqual(process_type.name, self.process_type_name)
        output_artifact = self.glsclient.loadByUri('artifact', process.input_output_map[0].output.uri)
        self.assertEqual(output_artifact.type, 'ResultFile')
        create_filetype = True
        for field in output_artifact.field:
            if field.name is 'File Type':
                create_filetype = False
        if create_filetype:
            filetype_field = glsapi.userdefined.field('FASTQ')
            filetype_field.name = 'File Type'
            output_artifact.field.append(filetype_field)
            updated_output_artifact = self.glsclient.update(output_artifact)
            self.assertEqual(updated_output_artifact.type, 'ResultFile')
        
    def test_search_fastq_resultfiles(self):
        filters = {'type':'ResultFile', 'udf.File Type':'FASTQ'}
        result_files = self.glsclient.listFilters('artifact', filters)
        for link in result_files.artifact:
            result_file = self.glsclient.loadByUri('artifact', link.uri)
            self.assertEqual(result_file.type, 'ResultFile')
            
    def test_submit_samples_to_workflow(self):
        samples = self.glsclient.listFilter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        sample = self.glsclient.load('sample', samples.sample[0].limsid)
        artifact = self.glsclient.load('artifact', sample.artifact.limsid)
        routing_artifact = glsapi.routing.artifact()
        routing_artifact.uri = artifact.uri
        routing_assignment = glsapi.routing.extArtifactAssignments()
        routing_assignment.workflow_uri = self.workflow.uri
        routing_assignment.artifact.append(routing_artifact)
        routing = glsapi.routing.routing()
        routing.assign.append(routing_assignment)
        created_route = self.glsclient.create('routing', routing)
        
    def test_list_pending_projects(self):
        filters = {'open-date':'NULL'}
        projects = self.glsclient.listFilters('project', filters)
        self.assertEqual(7, len(projects.project))
        
    def test_list_all_sequencing_runs(self):
        filters = {'type':'Illumina Sequencing Run','type':'MiSeq Run','type':'Historical Sequencing Run'}
        run_processes = self.glsclient.listFilters('process', filters)

################################################################################
# Unit tests for GlsUtil
################################################################################    
class GlsUtilTest(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.glsutil = GlsUtil('limsdev')

    def test_getSamplesByUser(self):
        self.assertIsNotNone(self.glsutil.getSamplesByUser('sarah.moffatt@cruk.cam.ac.uk'))

    def test_getSampleIdsBySlxId(self):
        self.assertIsNotNone(self.glsutil.getSampleIdsBySlxId('SLX-1661'))

    def test_getSlxIdBySampleId(self):
        self.assertIsNotNone(self.glsutil.getSlxIdBySampleId('16903'))

    def test_createBclToFastqPipelineProcess(self):
        # get latest sequencing process id for a flowcell id
        # 000000000-A3KRD
        run = self.glsutil.getCompleteRunProcessByFlowcellId('000000000-A474L')[0]
        self.assertIsNotNone(run)
        # get process object from api
        run_process = self.glsutil.api.load('process',run['id'])
        # build a unique set of input artifacts
        input_uri_list = []
        for io_elem in run_process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        input_uri_set = set(input_uri_list)
        for i in input_uri_set:
            self.log.info(i)
        # create bcl to fastq pipeline process
        technician_uri = self.glsutil.api.listFilter('researcher', 'username', USERNAME).researcher[0].uri
        process = glsapi.processexecution.process()
        process.type = ANALYSIS_PROCESS_NAMES['fastq']
        process.technician = glsapi.processexecution.technician()
        process.technician.uri = technician_uri
        # set udfs
        for run_field in run_process.field:
            self.log.debug(run_field.name)
            self.log.debug(run_field.value())
            if run_field.name == RUN_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == FLOW_CELL_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == REAGENT_CARTRIDGE_ID_FIELD:
                process.field.append(run_field)
        # create input-output-maps
        # 1 shared output result file: 
        # MGA Report
        #io_map_mga = glsapi.processexecution.input_output_map()
        #io_map_fastqc = glsapi.processexecution.input_output_map()
        #for input_artifact_uri in input_uri_set:
        #    input_artifact = glsapi.processexecution.input()
        #    input_artifact.uri = input_artifact_uri
        #    io_map_mga.input.append(input_artifact)
        #    #io_map_fastqc.input.append(input_artifact)
        #io_map_mga.output = glsapi.processexecution.output()
        #io_map_mga.output.type = 'ResultFile'
        #io_map_mga.shared = 'true'
        #process.input_output_map.append(io_map_mga)
        #io_map_fastqc.output = glsapi.processexecution.output()
        #io_map_fastqc.output.type = 'ResultFile'
        #io_map_fastqc.shared = 'true'
        #process.input_output_map.append(io_map_fastqc)
        # 6 output result files per lane for fastq pipeline
        # Forward Reads FASTQ,Reverse reads FASTQ,MD5 Checksums,MGA Lane Report,FASTQC Lane Report,Demultiplex Barcode Summary
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            io_map.output = glsapi.processexecution.output()
            io_map.output.type = 'ResultFile'
            process.input_output_map.append(io_map)
        
        self.log.debug(process.toxml('utf-8'))
        
        created_process = self.glsutil.api.create('process', process)
        self.assertEqual(process.type, ANALYSIS_PROCESS_NAMES['fastq'])
        process_type = self.glsutil.api.loadByUri('process_type', created_process.type.uri)
        self.assertEqual(process_type.name, ANALYSIS_PROCESS_NAMES['fastq'])
        
    def test_createDemuxPipelineProcess(self):
        # get latest sequencing process id for a flowcell id
        results = self.glsutil.getCompleteRunProcessByFlowcellId('000000000-A474L')
        self.assertNotEqual(0, len(results))
        run = results[0]
        # get process object from api
        run_process = self.glsutil.api.load('process',run['id'])
        # build a unique set of input artifacts
        input_uri_list = []
        for io_elem in run_process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        input_uri_set = set(input_uri_list)
        for i in input_uri_set:
            self.log.info(i)
        # create demultiplexing pipeline process
        technician_uri = self.glsutil.api.listFilter('researcher', 'username', USERNAME).researcher[0].uri
        process = glsapi.processexecution.process()
        process.type = ANALYSIS_PROCESS_NAMES['demux']
        process.technician = glsapi.processexecution.technician()
        process.technician.uri = technician_uri
        # set udfs
        for run_field in run_process.field:
            self.log.debug(run_field.name)
            self.log.debug(run_field.value())
            if run_field.name == RUN_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == FLOW_CELL_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == REAGENT_CARTRIDGE_ID_FIELD:
                process.field.append(run_field)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the demultiplexing process is configured to exclusively produce outputs per reagent label
        # PB: cannot create 3 outputs
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(process.toxml('utf-8'))

        created_process = self.glsutil.api.create('process', process)
        self.assertEqual(process.type, ANALYSIS_PROCESS_NAMES['demux'])
        process_type = self.glsutil.api.loadByUri('process_type', created_process.type.uri)
        self.assertEqual(process_type.name, ANALYSIS_PROCESS_NAMES['demux'])
        
    def test_createAlignmentPipelineProcess(self):
        # get latest sequencing process id for a flowcell id
        results = self.glsutil.getCompleteRunProcessByFlowcellId('000000000-A474L')
        self.assertNotEqual(0, len(results))
        run = results[0]
        # get process object from api
        run_process = self.glsutil.api.load('process',run['id'])
        # build a unique set of input artifacts
        input_uri_list = []
        for io_elem in run_process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        input_uri_set = set(input_uri_list)
        for i in input_uri_set:
            self.log.info(i)
        # create alignment pipeline process
        technician_uri = self.glsutil.api.listFilter('researcher', 'username', USERNAME).researcher[0].uri
        process = glsapi.processexecution.process()
        process.type = ANALYSIS_PROCESS_NAMES['align']
        process.technician = glsapi.processexecution.technician()
        process.technician.uri = technician_uri
        # set udfs
        for run_field in run_process.field:
            self.log.debug(run_field.name)
            self.log.debug(run_field.value())
            if run_field.name == RUN_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == FLOW_CELL_ID_FIELD:
                process.field.append(run_field)
            if run_field.name == REAGENT_CARTRIDGE_ID_FIELD:
                process.field.append(run_field)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the demultiplexing process is configured to exclusively produce outputs per reagent label
        # PB: cannot create 3 outputs
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(process.toxml('utf-8'))
        
        created_process = self.glsutil.api.create('process', process)
        self.assertEqual(process.type, ANALYSIS_PROCESS_NAMES['align'])
        process_type = self.glsutil.api.loadByUri('process_type', created_process.type.uri)
        self.assertEqual(process_type.name, ANALYSIS_PROCESS_NAMES['align'])
        
    def test_assignFlowcellToPublishingWorkflow(self):
        # get latest sequencing process id for a flowcell id
        results = self.glsutil.getCompleteRunProcessByFlowcellId('000000000-A474L')
        self.assertNotEqual(0, len(results))
        run = results[0]
        # check fastq & demux processes exist
        results = self.glsutil.getProcessByFlowcellId(ANALYSIS_PROCESS_NAMES['fastq'], '000000000-A474L')
        self.assertEqual(1, len(results))
        fastq = results[0]
        fastq_process = self.glsutil.api.load('process', fastq['id'])
        results = self.glsutil.getProcessByFlowcellId(ANALYSIS_PROCESS_NAMES['demux'], '000000000-A474L')
        self.assertEqual(1, len(results))
        demux = results[0]
        # get workflow
        workflows = self.glsutil.api.listFilterByName('workflow', 'BIO: Analyses')
        workflow = workflows.workflow[0]
        # build a unique set of input artifacts
        input_uri_list = []
        for io_elem in fastq_process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        input_uri_set = set(input_uri_list)
        for i in input_uri_set:
            self.log.info(i)
        # assign each artifact to publish queue in analyses workflow
        for input_artifact_uri in input_uri_set: 
            routing_artifact = glsapi.routing.artifact()
            routing_artifact.uri = input_artifact_uri
            routing_assignment = glsapi.routing.extArtifactAssignments()
            routing_assignment.workflow_uri = workflow.uri
            routing_assignment.artifact.append(routing_artifact)
            routing = glsapi.routing.routing()
            routing.assign.append(routing_assignment)
            self.log.debug(routing.toxml('utf-8'))
            created_route = self.glsutil.api.create('routing', routing)
            
    def test_createAnalysisProcesses(self):
        flowcell_id = '000000000-A474L'
        fastq = self.glsutil.createBclToFastqPipelineProcess(flowcell_id)
        fastq_type = self.glsutil.api.loadByUri('process_type', fastq.type.uri)
        self.assertEqual(fastq_type.name, ANALYSIS_PROCESS_NAMES['fastq'])
        demux = self.glsutil.createDemuxPipelineProcess(flowcell_id)
        demux_type = self.glsutil.api.loadByUri('process_type', demux.type.uri)
        self.assertEqual(demux_type.name, ANALYSIS_PROCESS_NAMES['demux'])
        alignment = self.glsutil.createAlignmentPipelineProcess(flowcell_id)
        alignment_type = self.glsutil.api.loadByUri('process_type', alignment.type.uri)
        self.assertEqual(alignment_type.name, ANALYSIS_PROCESS_NAMES['align'])
        
    def test_getPublishingProcessByInputArtifact(self):
        flowcell_id = '000000000-A474L'
        run = self.glsutil.getLatestCompleteRunProcessByFlowcellId(flowcell_id)
        input_artifact = self.glsutil.api.loadByUri('artifact', run.input_output_map[0].input.uri)
        publi = self.glsutil.getPublishingProcessByInputArtifact(input_artifact.limsid)
        self.log.info(publi)
        
    def test_assignFlowcellForPublishing(self):
        flowcell_id = '000000000-A474L'
        self.glsutil.assignFlowcellToPublishingWorkflow(flowcell_id)
        
    def test_updateFlowcellSampleProgress(self):
        flowcell_id = '000000000-A474L'
        fastq = self.glsutil.getSingleAnalysisProcessByFlowcellId('fastq', flowcell_id)
        if fastq:
            # build a unique set of input artifacts
            input_uri_set = self.glsutil.getUniqueInputUriListFromProcess(fastq)
            # update each sample progress status to Analysis Underway
            for input_artifact_uri in input_uri_set:
                input_artifact = self.glsutil.api.loadByUri('artifact', input_artifact_uri)
                for sample in input_artifact.sample:
                    self.log.debug(sample.uri)
                    sample = self.glsutil.api.loadByUri('sample', sample.uri)
                    update_sample = True
                    for f in sample.field:
                        if f.name == PROGRESS_STATUS:
                            self.log.debug(f.value())
                            if f.value() == ANALYSIS_UNDERWAY:
                                update_sample = False
                            else:
                                sample.field.remove(f)

                    if update_sample:
                        updated_field = glsapi.userdefined.field(ANALYSIS_UNDERWAY)
                        updated_field.name = PROGRESS_STATUS
                        sample.field.append(updated_field)
                        updated_sample = self.glsutil.api.update(sample)
                        for f in updated_sample.field:
                            if f.name == PROGRESS_STATUS:
                                self.log.debug(f.value())
                                
    def test_isSequencingCompleted(self):
        run_id = 'XXX'
        is_sequencing_completed = self.glsutil.isSequencingCompleted(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(None, is_sequencing_completed)
        run_id = '130627_SN1078_0142_C26B3ACXX'
        is_sequencing_completed = self.glsutil.isSequencingCompleted(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(True, is_sequencing_completed)
        run_id = '130703_SN1078_0147_C22TJACXX'
        is_sequencing_completed = self.glsutil.isSequencingCompleted(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(False, is_sequencing_completed)
        run_id = '140107_D00408_0023_H7NV6ADXX'
        
    def test_isFastqPipelineComplete(self):
        run_id = '130529_HWI-ST230_1167_C231WACXX'
        self.assertTrue(self.glsutil.isFastqPipelineComplete(run_id))
        
    def test_getAllExternalFtpDirs(self):
        results = self.glsutil.getAllExternalFtpDirs()
        self.assertEqual(45, len(results))
        self.assertEqual('easih', results[2]['ftpdir'])
        self.assertEqual('gurdon_institute', results[30]['ftpdir'])
        self.assertEqual('True', results[30]['nonpfdata'])
        
    def test_getRawFastqFiles(self):
        run_id = '130529_HWI-ST230_1168_D24MFACXX'
        results = self.glsutil.getRawFastqFiles(run_id)
        for raw in results:
            print raw.artifactid, raw.name, raw.contenturi
        self.assertEqual(8, len(results))
        
    def test_assignFlowcellForBilling(self):
        flowcell_id = 'C23B0ACXX'
        self.glsutil.assignFlowcellToBillingOnlyWorkflow(flowcell_id)
        
    def test_assignOldFlowcellForBilling(self):
        flowcell_id = '664UNAAXX'
        self.glsutil.assignOldFlowcellToBioBillingWorkflow(flowcell_id)
                    
    def test_listWaitingSamples(self):
        results = self.glsutil.getUnasignedSamplesToWorkflows()
        self.log.info(results)
        
    def test_isFastqPipelineComplete(self):
        run_id = '130805_HWI-ST230_0638_C2C8FACXX'
        self.log.info(self.glsutil.isFastqPipelineComplete(run_id))


if __name__ == '__main__':
    unittest.main()
