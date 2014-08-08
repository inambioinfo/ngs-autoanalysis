# ./processexecution.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:36fc4c9e1230107065d3a4630a5cc6ec8b60107e
# Generated 2014-08-06 17:32:28.835244 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/processexecution

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:40a41507-1d87-11e4-8a92-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import ri as _ImportedBinding_ri
import userdefined as _ImportedBinding_userdefined

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/processexecution', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_udf = _ImportedBinding_userdefined.Namespace
_Namespace_udf.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://genologics.com/ri/processexecution}qc-flag
class qc_flag (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The qc-flag element defines a QC value to apply to the input or output of the Process.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'qc-flag')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 109, 2)
    _Documentation = u'\n        The qc-flag element defines a QC value to apply to the input or output of the Process.\n      '
qc_flag._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=qc_flag, enum_prefix=None)
qc_flag.UNKNOWN = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
qc_flag.PASSED = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'PASSED', tag=u'PASSED')
qc_flag.FAILED = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'FAILED', tag=u'FAILED')
qc_flag.CONTINUE = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'CONTINUE', tag=u'CONTINUE')
qc_flag._InitializeFacetMap(qc_flag._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'qc-flag', qc_flag)

# Complex type {http://genologics.com/ri/processexecution}process with content type ELEMENT_ONLY
class process_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The process element defines the XML needed to run a process.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'process')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comriprocessexecution_process__type', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 12, 6), )

    
    type = property(__type.value, __type.set, None, u'\n            The name of the Process (process type) that you want to run.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element technician uses Python identifier technician
    __technician = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'technician'), 'technician', '__httpgenologics_comriprocessexecution_process__technician', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 21, 6), )

    
    technician = property(__technician.value, __technician.set, None, u'\n            The Technician element provides a URI to the user that is responsible for the Process.\nOnce the Process completes, this user is listed as the Technician that ran the Process.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element date-run uses Python identifier date_run
    __date_run = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'date-run'), 'date_run', '__httpgenologics_comriprocessexecution_process__date_run', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 31, 6), )

    
    date_run = property(__date_run.value, __date_run.set, None, u'\n            The date associated with the running of the Process, in YYYY-MM-DD format.\nIf omitted, the current date will be used.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No , will default to the current date.\n          ')

    
    # Element input-output-map uses Python identifier input_output_map
    __input_output_map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input-output-map'), 'input_output_map', '__httpgenologics_comriprocessexecution_process__input_output_map', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 41, 6), )

    
    input_output_map = property(__input_output_map.value, __input_output_map.set, None, u'\n            The relationship of Process inputs to Process outputs.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element instrument uses Python identifier instrument
    __instrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'instrument'), 'instrument', '__httpgenologics_comriprocessexecution_process__instrument', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 69, 6), )

    
    instrument = property(__instrument.value, __instrument.set, None, u'\n            Instrument provides a URI linking to the detailed representation of the instrument that ran the Process.\nThis instrument must have a single software defined to be valid for process execution.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element process-parameter uses Python identifier process_parameter
    __process_parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'process-parameter'), 'process_parameter', '__httpgenologics_comriprocessexecution_process__process_parameter', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 79, 6), )

    
    process_parameter = property(__process_parameter.value, __process_parameter.set, None, u'\n            The process parameter configured for EPP for the Process Type of the Process\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), 'field', '__httpgenologics_comriprocessexecution_process__httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Element {http://genologics.com/ri/userdefined}type uses Python identifier type_
    __type_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), 'type_', '__httpgenologics_comriprocessexecution_process__httpgenologics_comriuserdefinedtype', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2), )

    
    type_ = property(__type_.value, __type_.set, None, u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ')

    _ElementMap.update({
        __type.name() : __type,
        __technician.name() : __technician,
        __date_run.name() : __date_run,
        __input_output_map.name() : __input_output_map,
        __instrument.name() : __instrument,
        __process_parameter.name() : __process_parameter,
        __field.name() : __field,
        __type_.name() : __type_
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'process', process_)


# Complex type {http://genologics.com/ri/processexecution}artifactbase with content type ELEMENT_ONLY
class artifactbase (pyxb.binding.basis.complexTypeDefinition):
    """
        The base representation of an Artifact in the context of Process execution, defining common elements for both input and output Artifacts.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifactbase')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element qc-flag uses Python identifier qc_flag
    __qc_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'qc-flag'), 'qc_flag', '__httpgenologics_comriprocessexecution_artifactbase_qc_flag', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6), )

    
    qc_flag = property(__qc_flag.value, __qc_flag.set, None, u'\n            The QC flag for the Artifact being created. You can apply a QC flag to any Artifact in the system.\nThis is an optional element.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    _ElementMap.update({
        __qc_flag.name() : __qc_flag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'artifactbase', artifactbase)


# Complex type {http://genologics.com/ri/processexecution}input-output-map with content type ELEMENT_ONLY
class input_output_map (pyxb.binding.basis.complexTypeDefinition):
    """
        Processes link inputs to outputs and this relationship is called an input-output map.
Input-output-map is a child element of the Process element.<br/><br/>
When a Process creates multiple outputs per input, there is a distinct input-output map for each input to output relationship.
When a Process produces a shared output, there is a single input-output map for the shared output and all its related inputs.<br/><br/>
In situations where a Process is used to affect the properties of inputs only and therefore, does not create outputs, you can omit the output element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'input-output-map')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 143, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comriprocessexecution_input_output_map_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 154, 6), )

    
    input = property(__input.value, __input.set, None, u'\n            This element provides a URI for input Artifacts in the input-output map.\nThere may be cases where multiple inputs are associated with a single output, such as when working with a shared output.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output'), 'output', '__httpgenologics_comriprocessexecution_input_output_map_output', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 164, 6), )

    
    output = property(__output.value, __output.set, None, u'\n            This element provides information about the output Artifact that will be created by the Process.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Attribute shared uses Python identifier shared
    __shared = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shared'), 'shared', '__httpgenologics_comriprocessexecution_input_output_map_shared', pyxb.binding.datatypes.boolean)
    __shared._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 174, 4)
    __shared._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 174, 4)
    
    shared = property(__shared.value, __shared.set, None, u'\n          A value that specifies whether the input-output map applies to a single or shared output. To define a shared input-output map,\nuse true. To define a single input-output map, use false. If the value is omitted, the system will default to false.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __input.name() : __input,
        __output.name() : __output
    })
    _AttributeMap.update({
        __shared.name() : __shared
    })
Namespace.addCategoryObject('typeBinding', u'input-output-map', input_output_map)


# Complex type {http://genologics.com/ri/processexecution}instrument with content type EMPTY
class instrument (pyxb.binding.basis.complexTypeDefinition):
    """
        The instrument element provides a URI to the instrument that is responsible for running the process.
This instrument must have a single software defined to be valid for process execution.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'instrument')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 185, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriprocessexecution_instrument_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 192, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 192, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          A URI that identifies and links to the desired Instrument.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'instrument', instrument)


# Complex type {http://genologics.com/ri/processexecution}parameter with content type EMPTY
class parameter (pyxb.binding.basis.complexTypeDefinition):
    """
        The parameter is a child element of process execution that integrates the Process with the External Program Integration
plug-in (EPP). When a user runs the Process, the system automatically issues a command configured in the
process parameter this element represents.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'parameter')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 236, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriprocessexecution_parameter_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 244, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 244, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the process type parameter.\nMust match a parameter declared in the corresponding process type.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'parameter', parameter)


# Complex type {http://genologics.com/ri/processexecution}technician with content type EMPTY
class technician (pyxb.binding.basis.complexTypeDefinition):
    """
        The technician element provides a URI to the user that is responsible for the Process.
Once the Process completes, this user is listed as the technician that ran the Process.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'technician')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 253, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriprocessexecution_technician_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 260, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 260, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          A URI that identifies and links to the desired technician.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'technician', technician)


# Complex type {http://genologics.com/ri/processexecution}input with content type ELEMENT_ONLY
class input (artifactbase):
    """
        The input element provides URIs to one or more Artifacts that will be used by the Process.
Input is a child element of input-output-map.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'input')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 122, 2)
    _ElementMap = artifactbase._ElementMap.copy()
    _AttributeMap = artifactbase._AttributeMap.copy()
    # Base type is artifactbase
    
    # Element qc_flag (qc-flag) inherited from {http://genologics.com/ri/processexecution}artifactbase
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriprocessexecution_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 131, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 131, 8)
    
    uri = property(__uri.value, __uri.set, None, u'\n              A URI that identifies and links to further information about the input Artifact.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'input', input)


# Complex type {http://genologics.com/ri/processexecution}output with content type ELEMENT_ONLY
class output (artifactbase):
    """
        The output element provides information about the Artifacts that will be created by the Process.
Output is a child element of the input-output-map element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'output')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 202, 2)
    _ElementMap = artifactbase._ElementMap.copy()
    _AttributeMap = artifactbase._AttributeMap.copy()
    # Base type is artifactbase
    
    # Element qc_flag (qc-flag) inherited from {http://genologics.com/ri/processexecution}artifactbase
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__httpgenologics_comriprocessexecution_output_location', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 212, 10), )

    
    location = property(__location.value, __location.set, None, u'\n                The container where the output Artifact will be placed.\nThis child element is only used when working with Analyte or ResultFile outputs.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes for Analyte, No for ResultFile outputs.\n              ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comriprocessexecution_output_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 223, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 223, 8)
    
    type = property(__type.value, __type.set, None, u'\n              The type of output the system is creating. This value is case sensitive.\nValid values are: ResultFile, SearchResultFile, Analyte, Gel 1D, Gel 2D, Gel Spot, and Image.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n            ')

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'output', output)


process = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'process'), process_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', process.name().localName(), process)



process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'type'), pyxb.binding.datatypes.string, scope=process_, documentation=u'\n            The name of the Process (process type) that you want to run.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 12, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'technician'), technician, scope=process_, documentation=u'\n            The Technician element provides a URI to the user that is responsible for the Process.\nOnce the Process completes, this user is listed as the Technician that ran the Process.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 21, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'date-run'), pyxb.binding.datatypes.string, scope=process_, documentation=u'\n            The date associated with the running of the Process, in YYYY-MM-DD format.\nIf omitted, the current date will be used.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No , will default to the current date.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 31, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input-output-map'), input_output_map, scope=process_, documentation=u'\n            The relationship of Process inputs to Process outputs.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 41, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'instrument'), instrument, scope=process_, documentation=u'\n            Instrument provides a URI linking to the detailed representation of the instrument that ran the Process.\nThis instrument must have a single software defined to be valid for process execution.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 69, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'process-parameter'), parameter, scope=process_, documentation=u'\n            The process parameter configured for EPP for the Process Type of the Process\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 79, 6)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), _ImportedBinding_userdefined.field_, scope=process_, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

process_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), _ImportedBinding_userdefined.type_, scope=process_, documentation=u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 31, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 41, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 50, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 60, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 69, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 79, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'technician')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'date-run')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 31, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'input-output-map')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 50, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 60, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'instrument')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 69, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(process_._UseForTag(pyxb.namespace.ExpandedName(None, u'process-parameter')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 79, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
process_._Automaton = _BuildAutomaton()




artifactbase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'qc-flag'), qc_flag, scope=artifactbase, documentation=u'\n            The QC flag for the Artifact being created. You can apply a QC flag to any Artifact in the system.\nThis is an optional element.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(artifactbase._UseForTag(pyxb.namespace.ExpandedName(None, u'qc-flag')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
artifactbase._Automaton = _BuildAutomaton_()




input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), input, scope=input_output_map, documentation=u'\n            This element provides a URI for input Artifacts in the input-output map.\nThere may be cases where multiple inputs are associated with a single output, such as when working with a shared output.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 154, 6)))

input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output'), output, scope=input_output_map, documentation=u'\n            This element provides information about the output Artifact that will be created by the Process.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 164, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 154, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 164, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 154, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, u'output')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 164, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
input_output_map._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(input._UseForTag(pyxb.namespace.ExpandedName(None, u'qc-flag')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
input._Automaton = _BuildAutomaton_3()




output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), _ImportedBinding_ri.location, scope=output, documentation=u'\n                The container where the output Artifact will be placed.\nThis child element is only used when working with Analyte or ResultFile outputs.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes for Analyte, No for ResultFile outputs.\n              ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 212, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 212, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output._UseForTag(pyxb.namespace.ExpandedName(None, u'qc-flag')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(output._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/processexecution.xsd', 212, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output._Automaton = _BuildAutomaton_4()

