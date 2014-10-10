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

import psycopg2
from psycopg2.extras import RealDictCursor

# Append root project to PYTHONPATH
ROOT_PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
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
SERVERS = {'lims': 'genomicsequencing.cruk.cam.ac.uk',
           'limsdev': 'limsdev.cruk.cam.ac.uk'}

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

ANALYSIS_PROCESS_NAMES = {'lanfq': 'FASTQ Lane Pipeline',
                          'samfq': 'FASTQ Sample Pipeline',
                          'align': 'Alignment Pipeline',
                          'publi': 'Publishing'}
                          
WORKFLOW_NAMES = {'publi': 'BIO: Publishing and Billing',
                  'bill': 'BIO: Billing Only'}
                          

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
        self.session.headers.update({'content-type': 'application/xml', 'Accept': 'application/xml', 'Accept-Encoding': 'gzip, deflate, compress', 'charset': 'UTF-8'})
        
        ### set resources
        self.resources = {
            'artifact': {'uri': 'artifacts', 'mod': 'artifact'},
            'container': {'uri': 'containers', 'mod': 'container'},
            'container_type': {'uri': 'containertypes', 'mod': 'containertype'},
            'configuration': {'uri': 'configuration/udfs', 'mod': 'configuration'},
            'instrument': {'uri': 'instruments', 'mod': 'instrument'},
            'lab': {'uri': 'labs', 'mod': 'lab'},
            'process': {'uri': 'processes', 'mod': 'process'},
            'process_type': {'uri': 'processtypes', 'mod': 'processtype'},
            'project': {'uri': 'projects', 'mod': 'project'},
            'researcher': {'uri': 'researchers', 'mod': 'researcher'},
            'routing': {'uri': 'route/artifacts', 'mod': 'routing'},
            'sample': {'uri': 'samples', 'mod': 'sample'},
            'workflow': {'uri': 'configuration/workflows', 'mod': 'wkfcnf'},
            #'': {'uri': '', 'mod': ''},
        }
        ### set filters
        self.sample_filter_by_projectname = 'projectname'
        self.artifact_filter_by_samplename = 'sample-name'
        
    def list(self, _resource_name):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': ''}
        response = self.session.get(uri)
        return self._create_from_doc(_resource_name, response)
        
    def list_filter_by_name(self, _resource_name, _name):
        return self.list_filter(_resource_name, 'name', _name)

    def list_filter(self, _resource_name, _filter_key, _filter_value):
        filters = {_filter_key: _filter_value}
        return self.list_filters(_resource_name, filters)

    def list_filters(self, _resource_name, _filters):
        filters_uri = ''
        for key, value in _filters.iteritems():
            filters_uri += '%(key)s=%(value)s&' % {'key': key, 'value': value}
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_FILTER_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'filters': filters_uri[:-1]}
        response = self.session.get(uri)
        return self._create_from_doc(_resource_name, response)

    def load(self, _resource_name, _limsid):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': _limsid}
        response = self.session.get(uri)
        return self._create_from_doc(_resource_name, response)
        
    def load_by_uri(self, _resource_name, _uri):
        response = self.session.get(_uri)
        return self._create_from_doc(_resource_name, response)
        
    def update(self, _object):
        response = self.session.put(_object.uri, data=_object.toxml('utf-8'))
        resource = _object.__class__.__module__.split('.')[-1]
        return self._create_from_doc(resource, response)
    
    def create(self, _resource_name, _object):
        resource = self.resources[_resource_name]['uri']
        uri = REST_URI_TEMPLATE % {'hostname': self.hostname, 'api_version': API_VERSION, 'resource': resource, 'luid': ''}
        self.log.debug(self.pretty_xml(_object.toxml('utf-8')))
        response = self.session.post(uri, _object.toxml('utf-8'))
        return self._create_from_doc(_resource_name, response)
        
    def delete(self, _object):
        try:
            self.log.debug(_object.uri)
            response = self.session.delete(_object.uri)
            response.raise_for_status()
            return response
        except:
            self.log.exception(_object)
            raise
            
    def _create_from_doc(self, _resource_name, _response):
        try:
            resource = self.resources[_resource_name]['mod']
            self.log.debug(_response.status_code)
            self.log.debug(self.pretty_xml(_response.text))
            _response.raise_for_status()
            return getattr(glsapi, resource).CreateFromDocument(_response.text.encode('utf-8'))
        except:
            self.log.exception(_response.text)
            self.log.error(_response.raise_for_status())
            raise
            
    def pretty_xml(self, _rough_xml):
        reparsed = minidom.parseString(_rough_xml.encode('utf-8'))
        return reparsed.toprettyxml(indent="    ")
        

################################################################################
# Class
################################################################################
class GlsUtil(object):

    def __init__(self, server, username=USERNAME, password=PASSWORD):
        self.log = logging.getLogger(__name__)
        self.server = server
        self.hostname = HOSTNAME % {'server': SERVERS[self.server]}
        self.username = username
        self.password = password
        self.api = GlsClientApi(self.hostname, self.username, self.password)
        self.db_connection = psycopg2.connect(database='clarityDB', user="readonly", password="readonly", host=SERVERS[self.server], cursor_factory=RealDictCursor)
        self.db = self.db_connection.cursor()

    def close_db_connection(self):
        self.db.close()
        self.db_connection.close()

    def get_process_by_flowcell_id(self, _process_name, _flowcell_id):
        self.db.execute(glssql.PROCESS_BY_UDF_QUERY % (_process_name, FLOW_CELL_ID_FIELD, _flowcell_id))
        return self.db.fetchall()

    def get_complete_run_process_by_flowcell_id(self, _flowcell_id):
        self.db.execute(glssql.COMPLETE_RUNPROCESS_BY_UDF_QUERY % (FLOW_CELL_ID_FIELD, _flowcell_id))
        return self.db.fetchall()

    def get_complete_run_process_by_run_id(self, _run_id):
        self.db.execute(glssql.COMPLETE_RUNPROCESS_BY_UDF_QUERY % (RUN_ID_FIELD, _run_id))
        return self.db.fetchall()

    def get_publishing_process_by_input_artifact(self, _artifact_luid):
        self.db.execute(glssql.PUBLISHINGPROCESS_BY_INPUTARTIFACTLUID_QUERY % _artifact_luid)
        return self.db.fetchall()

    def get_billing_process_by_input_artifact(self, _artifact_luid):
        self.db.execute(glssql.BILLINGPROCESS_BY_INPUTARTIFACTLUID_QUERY % _artifact_luid)
        return self.db.fetchall()

    def get_latest_complete_run_process_by_run_id(self, _run_id):
        results = self.get_complete_run_process_by_run_id(_run_id)
        if not results:
            self.log.warning('no run process found for run id %s' % _run_id)
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one run processes found for run id %s' % _run_id)
            return self.api.load('process', results[0]['luid'])
            
    def get_latest_complete_run_process_by_flowcell_id(self, _flowcell_id):
        results = self.get_complete_run_process_by_flowcell_id(_flowcell_id)
        if not results:
            self.log.warning('no run process found for flow-cell id %s' % _flowcell_id)
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one run processes found for flow-cell id %s' % _flowcell_id)
            return self.api.load('process', results[0]['luid'])

    def get_single_analysis_process_by_flowcell_id(self, _name, _flowcell_id):
        results = self.get_process_by_flowcell_id(ANALYSIS_PROCESS_NAMES[_name], _flowcell_id)
        if not results:
            self.log.debug('no %s process found for flow-cell id %s' % (_name, _flowcell_id))
            return None
        else:
            if not len(results) == 1:
                self.log.warning('more than one %s processes found for flow-cell id %s' % (_name, _flowcell_id))
            return self.api.load('process', results[0]['luid'])

    def get_unique_input_uri_from_process(self, _process):
        input_uri_list = []
        for io_elem in _process.input_output_map:
            input_uri_list.append(io_elem.input.uri)
        return set(input_uri_list)
        
    def get_unique_output_uri_from_process(self, _process):
        output_uri_list = []
        for io_elem in _process.input_output_map:
            output_uri_list.append(io_elem.output.uri)
        return set(output_uri_list)

    def get_unique_input_post_process_uri_from_process(self, _process):
        input_uri_list = []
        for io_elem in _process.input_output_map:
            input_uri_list.append(io_elem.input.post_process_uri)
        return set(input_uri_list)

    def is_sequencing_completed(self, _run_id):
        # return True if run process at the end of cycle; False if all lanes qc failed; None otherwise
        self.db.execute(glssql.RUNSTATUS_BYRUNID_QUERY % _run_id)
        results = self.db.fetchall()
        if results:
            # run process at the end of cycle - sequencing COMPLETE
            if int(results[0]['currentcycle']) == int(results[0]['totalcycle']):
                self.log.debug('Run ID: %s - finished - status: cycle %s of %s' % (_run_id, results[0]['currentcycle'], results[0]['totalcycle']))
                return True
            else:
                # run process not at the end of cycle but completed in clarity
                if results[0]['workstatus'] == 'COMPLETE':
                    # check if all lanes qc failed = 2
                    all_lanes_failed = True
                    all_lanes_passed = True
                    for lane in results:
                        if not lane['qcflag'] == 2:
                            all_lanes_failed = False
                        if not lane['qcflag'] == 1:
                            all_lanes_passed = False
                    # all lanes failed - sequencing FAILED
                    if all_lanes_failed:
                        self.log.debug('Run ID: %s - failed - status: cycle %s of %s' % (_run_id, results[0]['currentcycle'], results[0]['totalcycle']))
                        return False
                    elif all_lanes_passed:
                        self.log.debug('Run ID: %s - all lanes passed; sequencing underway - status: cycle %s of %s' % (_run_id, results[0]['currentcycle'], results[0]['totalcycle']))
                        return None
                    else:
                        self.log.debug('Run ID: %s - some lanes failed but not all - status: cycle %s of %s' % (_run_id, results[0]['currentcycle'], results[0]['totalcycle']))
                        return None
                else:
                    self.log.debug('Run ID: %s - still open in clarity - status: cycle %s of %s' % (_run_id, results[0]['currentcycle'], results[0]['totalcycle']))
                    return None
        else:
            self.log.debug('Run ID: %s - no process found in lims for this run id' % _run_id)
            return None
        
    def create_analysis_process(self, _name, _run_process):
        technician_uri = self.api.list_filter('researcher', 'username', USERNAME).researcher[0].uri
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
        
    def create_fastq_lane_pipeline_process(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.get_latest_complete_run_process_by_flowcell_id(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.get_unique_input_uri_from_process(run_process)
        # create fastq lane pipeline process
        process = self.create_analysis_process('lanfq', run_process)
        # create input-output-maps
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            # 8 output result files per lane for fastq pipeline
            # Lost Reads 1 FASTQ,Lost Reads 2 FASTQ,Lost Reads MD5 Checksums,Lane Contents,Demultiplex Barcode Summary,MGA Lane Report,FASTQC Lane Report 1,FASTQC Lane Report 2
            for i in range(8):
                io_map = glsapi.processexecution.input_output_map()
                io_map.input.append(input_artifact) 
                io_map.output = glsapi.processexecution.output()
                io_map.output.type = 'ResultFile'
                process.input_output_map.append(io_map)
        self.log.debug(self.api.pretty_xml(process.toxml('utf-8')))
        return self.api.create('process', process)
        
    def create_fastq_sample_pipeline_process(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.get_latest_complete_run_process_by_flowcell_id(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.get_unique_input_uri_from_process(run_process)
        # create fastq sample pipeline process
        process = self.create_analysis_process('samfq', run_process)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the process is configured to exclusively produce outputs per reagent label
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(self.api.pretty_xml(process.toxml('utf-8')))
        return self.api.create('process', process)
        
    def create_alignment_pipeline_process(self, _flowcell_id):
        # get latest sequencing process for a flowcell id
        run_process = self.get_latest_complete_run_process_by_flowcell_id(_flowcell_id)
        # build a unique set of input artifacts
        input_uri_set = self.get_unique_input_uri_from_process(run_process)
        # create alignment pipeline process
        process = self.create_analysis_process('align', run_process)
        # create input-output-maps
        # the input-output-map only refers to inputs, not outputs, 
        # because the process is configured to exclusively produce outputs per reagent label
        for input_artifact_uri in input_uri_set: 
            input_artifact = glsapi.processexecution.input()
            input_artifact.uri = input_artifact_uri
            io_map = glsapi.processexecution.input_output_map()
            io_map.input.append(input_artifact) 
            process.input_output_map.append(io_map)

        self.log.debug(self.api.pretty_xml(process.toxml('utf-8')))
        return self.api.create('process', process)

    def route_each_artifact_to_workflow(self, _artifact_uri_set, _workflow_name):
        # get workflow
        workflows = self.api.list_filter_by_name('workflow', _workflow_name)
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
            self.log.debug(self.api.pretty_xml(routing.toxml('utf-8')))
            self.api.create('routing', routing)

    def assign_flowcell_to_publishing_workflow(self, _flowcell_id):
        # get run process
        run = self.get_latest_complete_run_process_by_flowcell_id(_flowcell_id)
        # get one input artifact from run process
        input_artifact = self.api.load_by_uri('artifact', run.input_output_map[0].input.uri)
        publi = self.get_publishing_process_by_input_artifact(input_artifact.limsid)
        # if publishing process do not already exist
        if not publi:
            # get main alignment processes
            lanfq = self.get_single_analysis_process_by_flowcell_id('lanfq', _flowcell_id)
            samfq = self.get_single_analysis_process_by_flowcell_id('samfq', _flowcell_id)
            # check fastq & demux & alignment processes exist
            if lanfq and samfq:
                # build a unique set of input artifacts
                input_uri_set = self.get_unique_input_uri_from_process(fastq)
                # assign each artifact to publish queue in analyses workflow
                self.route_each_artifact_to_workflow(input_uri_set, WORKFLOW_NAMES['publi'])
                self.log.info("flow-cell id '%s' assigned to '%s' workflow for publishing." % (_flowcell_id, WORKFLOW_NAMES['publi']))
        else:
            self.log.info("flow-cell id '%s' has already a publishing process '%s'." % (_flowcell_id, publi[0]['luid']))

    def are_sample_fastq_files_attached(self, _run_id):
        """Only check if all Read 1 Sample Fastq files exist for lanes that passed qc on sequencing
        """
        # get latest sequencing process for run id
        run_process = self.get_latest_complete_run_process_by_run_id(_run_id)
        if run_process is None:
            flowcell_id = _run_id.split('_')[-1]
            run_process_by_fc = self.get_latest_complete_run_process_by_flowcell_id(flowcell_id)
            if run_process_by_fc is not None:
                return False
            return None
        # build a unique set of input artifacts
        input_uri_set = self.get_unique_input_post_process_uri_from_process(run_process)
        for input_artifact_uri in input_uri_set:
            artifact = self.api.load_by_uri('artifact', input_artifact_uri)
            self.log.debug(artifact.qc_flag)
            if artifact.qc_flag == 'PASSED':
                location = artifact.location.value_
                self.log.debug(location)
                self.db.execute(glssql.UNASSIGNED_FASTQ1_ON_PROCESS_BY_UDF_QUERY % (_run_id, location))
                results = self.db.fetchall()
                self.log.debug(results)
                if results: 
                    return False
        return True

    def is_external_data(self, _run_id):
        """Return true if external data on this run
        """
        self.db.execute(glssql.EXTERNAL_DATA_QUERY % _run_id)
        if self.db.fetchall():
            return True
        return False
        
    def get_lane_fastq_files(self, run_id, is_published=False):
        """Return lane level files for this run folder name called run id in genologics
        """
        if is_published:
            self.db.execute(glssql.PUBLISHED_FILES_QUERY % {'processname': 'FASTQ Lane Pipeline', 'runid': run_id})
            return self.db.fetchall()
        self.db.execute(glssql.FILES_QUERY % {'processname': 'FASTQ Lane Pipeline', 'runid': run_id})
        return self.db.fetchall()
        
    def get_sample_fastq_files(self, run_id, is_published=False):
        """Return sample level files for this run folder name called run id in genologics
        """
        if is_published:
            self.db.execute(glssql.PUBLISHED_FILES_QUERY % {'processname': 'FASTQ Sample Pipeline', 'runid': run_id})
            return self.db.fetchall()
        self.db.execute(glssql.FILES_QUERY % {'processname': 'FASTQ Sample Pipeline', 'runid': run_id})
        return self.db.fetchall()
        
    def get_all_external_ftp_dirs(self):
        """Return list of all external ftp directories
        """
        self.db.execute(glssql.EXTERNAL_FTPDIR_QUERY)
        results = self.db.fetchall()
        labftpdirs = {}
        for lab in results: 
            labftpdirs[lab['labid']] = {'ftpdir': lab['ftpdir'], 'nonpfdata': lab['nonpfdata']}
        self.log.debug(labftpdirs)
        return labftpdirs

    def is_alignment_active(self, _run_id):
        self.db.execute(glssql.IS_ALIGNMENT_ACTIVE_QUERY % _run_id)
        if self.db.fetchall():
            return True
        return False


################################################################################
# Unit tests for GlsClientApi
################################################################################    
class GlsClientApiTest(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.glsclient = GlsClientApi(HOSTNAME % {'server': SERVERS['limsdev']}, USERNAME, PASSWORD)
        self.unknown_id = 'unknown'
        self.containertype_id = '1' 
        self.containertype_name = '96 well plate'
        self.instrument_id = '5'
        self.instrument_name = 'Luke-Leia [HWI-ST230]'
        self.lab_id = '11'
        self.lab_name = 'Core - Genomics'
        # load project
        self.project_name = 'Python Unit Tests'
        self.projects = self.glsclient.list_filter_by_name('project', self.project_name)
        self.project = self.projects.project[0]
        # load container type
        self.container_type_name = 'Tube'
        self.container_types = self.glsclient.list_filter_by_name('container_type', self.container_type_name)
        self.container_type = self.container_types.container_type[0]
        # container name
        self.container_name = 'Container created via Python Unit Test'
        # sample name
        self.sample_name = 'Sample created via Python Unit Test'
        # workflow name
        self.workflow_name = 'BIO: Analyses'
        self.workflows = self.glsclient.list_filter_by_name('workflow', self.workflow_name)
        self.workflow = self.workflows.workflow[0]
        # process type
        self.process_type_name = 'FASTQ Lane Pipeline'
        self.process_types = self.glsclient.list_filter_by_name('process_type', self.process_type_name)
        self.process_type = self.process_types.process_type[0]
        
    def test_session(self):
        self.assertEqual(self.glsclient.session.auth, (USERNAME, PASSWORD))
        self.assertDictContainsSubset({'content-type': 'application/xml', 'Accept-Encoding': 'gzip, deflate, compress', 'charset': 'UTF-8', 'Accept': 'application/xml'}, self.glsclient.session.headers)

    def test_session_response(self):
        uri = REST_URI_TEMPLATE % {'hostname': self.glsclient.hostname, 'api_version': API_VERSION, 'resource': 'labs', 'luid': self.lab_id}
        response = self.glsclient.session.get(uri)
        self.assertEqual(response.status_code, requests.codes.ok)
        
    def test_list_container_types(self):
        container_type_list = self.glsclient.list('container_type')
        container_type_name_list = []
        for containertype in container_type_list.container_type:
            container_type_name_list.append(containertype.name)
        self.assertIn(self.containertype_name, container_type_name_list)
         
    def test_list_instruments(self):
        instrument_list = self.glsclient.list('instrument')
        instrument_name_list = []
        for instrument in instrument_list.instrument:
            instrument_name_list.append(instrument.name)
        self.assertIn(self.instrument_name, instrument_name_list)
        
    def test_list_labs(self):
        lab_list = self.glsclient.list('lab')
        lab_name_list = []
        for lab in lab_list.lab:
            lab_name_list.append(lab.name)
        self.assertIn(self.lab_name, lab_name_list)

    def test_list_workflows(self):
        workflows = self.glsclient.list('workflow')
        workflow_names = []
        for workflow in workflows.workflow:
            workflow_names.append(workflow.name)
        self.assertIn(self.workflow_name, workflow_names)

    def test_list_process_types(self):
        process_types = self.glsclient.list('process_type')
        process_type_names = []
        for process_type in process_types.process_type:
            process_type_names.append(process_type.name)
        self.assertIn(self.process_type_name, process_type_names)

    def test_list_filter_researchers_by_username(self):
        researcher_links = self.glsclient.list_filter('researcher', 'username', USERNAME)
        researcher = self.glsclient.load_by_uri('researcher', researcher_links.researcher[0].uri)
        self.assertEqual(USERNAME, researcher.credentials.username)
        pass

    def test_list_filters_open_projects(self):
        filters = {'close-date': 'NULL'}
        projects = self.glsclient.list_filters('project', filters)
        self.assertEqual(500, len(projects.project))

    def test_list_filters_sequencing_runs(self):
        filters = {'type': 'Illumina Sequencing Run', 'type': 'MiSeq Run', 'type': 'Historical Sequencing Run'}
        self.glsclient.list_filters('process', filters)

    def test_list_filters_fastq_result_files(self):
        filters = {'type': 'ResultFile', 'File Type': 'FASTQ'}
        result_files = self.glsclient.list_filters('artifact', filters)
        for link in result_files.artifact:
            result_file = self.glsclient.load_by_uri('artifact', link.uri)
            self.assertEqual(result_file.type, 'ResultFile')

    def test_load_unknown(self):
        self.assertRaises(KeyError, self.glsclient.load, 'unknown', self.unknown_id)

    def test_load_instrument(self):
        instrument = self.glsclient.load('instrument', self.instrument_id)
        self.assertEqual(instrument.name, self.instrument_name)
        
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

    def test_load_samples_within_project(self):
        samples = self.glsclient.list_filter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        for sample_link in samples.sample:
            sample = self.glsclient.load('sample', sample_link.limsid)
            self.assertEqual(sample.name, self.sample_name)
        self.assertRaises(requests.exceptions.HTTPError, self.glsclient.load, 'sample', self.unknown_id)

    def test_load_artifact_of_sample(self):
        samples = self.glsclient.list_filter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
        sample = self.glsclient.load('sample', samples.sample[0].limsid)
        artifact = self.glsclient.load('artifact', sample.artifact.limsid)
        self.assertEqual(sample.artifact.limsid, artifact.limsid)
        self.assertRaises(requests.exceptions.HTTPError, self.glsclient.load, 'artifact', self.unknown_id)

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
        samples_required_fields = {'Sample Type': 'DNA',
                                   'Priority Status': 'Standard',
                                   'Read Length': '10',
                                   'Sequencing Type': 'Not Assigned',
                                   'Index Type': 'Not Assigned',
                                   'Concentration': '1',
                                   'Number of Lanes': '1',
                                   'Pool Size': '1',
                                   'Reference Genome': 'Homo sapiens [GRCh37]',
                                   'Row': '1',
                                   'Sample Source': 'Not Assigned',
                                   'Sequencer': 'Not Assigned',
                                   'SLX Identifier': 'SLX-9999',
                                   'Volume': '1',
                                   'Average Library Length': '10',
                                   'Version Number': 'SLX Version 19',
                                   'Workflow': 'HiSeq'}
        for name, value in samples_required_fields.items():
            field = glsapi.userdefined.field(value)
            field.name = name
            sample.field.append(field)
        created_sample = self.glsclient.create('sample', sample)
        self.assertEqual(created_sample.name, self.sample_name)
        
    def test_update_sample_names_within_project(self):
        samples = self.glsclient.list_filter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
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
            
    def test_update_artifact_name(self):
        samples = self.glsclient.list_filter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
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
        
    def test_create_process_with_result_file(self):
        technician_uri = self.glsclient.list_filter('researcher', 'username', USERNAME).researcher[0].uri
        samples = self.glsclient.list_filter('sample', self.glsclient.sample_filter_by_projectname, self.project.name)
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
        # add required UDF
        required_fields = {'Flow Cell ID': 'C4EKWANXX',
                           'Run ID': '140702_D00491_0074_C4EKWANXX',
                           }
        for name, value in required_fields.items():
            field = glsapi.userdefined.field(value)
            field.name = name
            process.field.append(field)
        self.log.debug(process.toxml('utf-8'))
        created_process = self.glsclient.create('process', process)
        self.assertEqual(process.type, self.process_type_name)
        process_type = self.glsclient.load_by_uri('process_type', created_process.type.uri)
        self.assertEqual(process_type.name, self.process_type_name)


################################################################################
# Unit tests for GlsUtil
################################################################################    
class GlsUtilTest(unittest.TestCase):

    def setUp(self):
        import log as logger
        self.log = logger.get_custom_logger()
        self.glsutil = GlsUtil('limsdev')

    def test_assign_flowcell_to_publishing_workflow(self):
        flowcell_id = 'H9VT6ADXX' # not published yet on dev server
        self.glsutil.assign_flowcell_to_publishing_workflow(flowcell_id)

    def test_create_alignment_pipeline_process(self):
        flowcell_id = 'C3JGEACXX'
        process = self.glsutil.create_alignment_pipeline_process(flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)

    def test_create_fastq_sample_pipeline_process(self):
        flowcell_id = 'C3JGEACXX'
        process = self.glsutil.create_fastq_sample_pipeline_process(flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)

    def test_create_fastq_lane_pipeline_process(self):
        flowcell_id = 'C3JGEACXX'
        process = self.glsutil.create_fastq_lane_pipeline_process(flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)

    def test_get_latest_complete_run_process_by_flowcell_id(self):
        flowcell_id = 'C3JGEACXX'
        process = self.glsutil.get_latest_complete_run_process_by_flowcell_id(flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)

    def test_get_single_analysis_process_by_flowcell_id(self):
        flowcell_id = 'C3JGEACXX'
        process = self.glsutil.get_single_analysis_process_by_flowcell_id('lanfq', flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)
        process = self.glsutil.get_single_analysis_process_by_flowcell_id('samfq', flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)
        process = self.glsutil.get_single_analysis_process_by_flowcell_id('align', flowcell_id)
        self.log.debug(process)
        self.assertIsNotNone(process)

    def test_get_lane_fastq_files(self):
        run_id = '140618_D00408_0148_C4W0MACXX'
        files = self.glsutil.get_lane_fastq_files(run_id)
        self.assertIsNotNone(files)
        files = self.glsutil.get_lane_fastq_files(run_id, True)
        self.assertIsNotNone(files)

    def test_get_sample_fastq_files(self):
        run_id = '140618_D00408_0148_C4W0MACXX'
        files = self.glsutil.get_sample_fastq_files(run_id)
        self.assertIsNotNone(files)
        files = self.glsutil.get_sample_fastq_files(run_id, True)
        self.assertIsNotNone(files)

    def test_is_external_data(self):
        run_id = '140618_D00408_0148_C4W0MACXX'
        self.assertTrue(self.glsutil.is_external_data(run_id))
        run_id = '140617_M01686_0117_000000000-A9YVK'
        self.assertFalse(self.glsutil.is_external_data(run_id))
        
    def test_is_sample_fastq_files_attached(self):
        run_id = '140618_D00408_0148_C4W0MACXX'
        self.assertTrue(self.glsutil.are_sample_fastq_files_attached(run_id))
        
    def test_is_sequencing_completed(self):
        run_id = 'XXX'
        is_sequencing_completed = self.glsutil.is_sequencing_completed(run_id)
        self.log.info(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(None, is_sequencing_completed)
        run_id = '130627_SN1078_0142_C26B3ACXX'
        is_sequencing_completed = self.glsutil.is_sequencing_completed(run_id)
        self.log.info(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(True, is_sequencing_completed)
        run_id = '131105_HWI-ST230_0674_D2GAVACXX'
        is_sequencing_completed = self.glsutil.is_sequencing_completed(run_id)
        self.log.info(run_id)
        self.log.info(is_sequencing_completed)
        self.assertEqual(False, is_sequencing_completed)

    def test_get_all_external_ftp_dirs(self):
        results = self.glsutil.get_all_external_ftp_dirs()
        self.assertEqual(44, len(results))
        self.assertEqual('lmb_debono', results[4]['ftpdir'])
        self.assertEqual('gurdon_institute', results[30]['ftpdir'])
        self.assertEqual('True', results[30]['nonpfdata'])

    def test_is_alignment_active(self):
        self.assertTrue(self.glsutil.is_alignment_active('140815_D00408_0163_C4EYLANXX'))
        self.assertFalse(self.glsutil.is_alignment_active('140813_M01712_0104_000000000-A9YBB'))

if __name__ == '__main__':
    unittest.main()
