# ./processtype.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7e4e49d01d5b9b8e6dba9ac3f3852e7b4e349a38
# Generated 2016-01-12 17:07:14.303499 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/processtype

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ec2c6a75-b94e-11e5-ac8d-a0999b0d9515')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import ri as _ImportedBinding_ri
import pyxb.binding.datatypes
import configuration as _ImportedBinding_configuration

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/processtype', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://genologics.com/ri/processtype}invocation-type
class invocation_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The available options for epp invocation type.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'invocation-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 79, 2)
    _Documentation = '\n        The available options for epp invocation type.\n      '
invocation_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=invocation_type, enum_prefix=None)
invocation_type.PostProcess = invocation_type._CF_enumeration.addEnumeration(unicode_value='PostProcess', tag='PostProcess')
invocation_type.PreProcess = invocation_type._CF_enumeration.addEnumeration(unicode_value='PreProcess', tag='PreProcess')
invocation_type._InitializeFacetMap(invocation_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'invocation-type', invocation_type)

# Atomic simple type: {http://genologics.com/ri/processtype}output-generation-type
class output_generation_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The available options for output-type generation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'output-generation-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 90, 2)
    _Documentation = '\n        The available options for output-type generation.\n      '
output_generation_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=output_generation_type, enum_prefix=None)
output_generation_type.PerInput = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerInput', tag='PerInput')
output_generation_type.PerAllInputs = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerAllInputs', tag='PerAllInputs')
output_generation_type.PerReagentLabel = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerReagentLabel', tag='PerReagentLabel')
output_generation_type._InitializeFacetMap(output_generation_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'output-generation-type', output_generation_type)

# Atomic simple type: {http://genologics.com/ri/processtype}variability-type
class variability_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The available options for output-type variability.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'variability-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 320, 2)
    _Documentation = '\n        The available options for output-type variability.\n      '
variability_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=variability_type, enum_prefix=None)
variability_type.Fixed = variability_type._CF_enumeration.addEnumeration(unicode_value='Fixed', tag='Fixed')
variability_type.Variable = variability_type._CF_enumeration.addEnumeration(unicode_value='Variable', tag='Variable')
variability_type.VariableByInput = variability_type._CF_enumeration.addEnumeration(unicode_value='VariableByInput', tag='VariableByInput')
variability_type._InitializeFacetMap(variability_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'variability-type', variability_type)

# Complex type {http://genologics.com/ri/processtype}process-type with content type ELEMENT_ONLY
class process_type_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The process-type element contains the XML representation of a type of process configured in the system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field-definition uses Python identifier field_definition
    __field_definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'field-definition'), 'field_definition', '__httpgenologics_comriprocesstype_process_type__field_definition', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 13, 6), )

    
    field_definition = property(__field_definition.value, __field_definition.set, None, '\n            Each field definition provides a URI linking to the configuration of a user-defined field for the process type.\n<br/>Always returns with GET: No\n          ')

    
    # Element parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameter'), 'parameter', '__httpgenologics_comriprocesstype_process_type__parameter', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 21, 6), )

    
    parameter = property(__parameter.value, __parameter.set, None, '\n            Each parameter is a named value or file for the process type.\n<br/>Always returns with GET: No\n          ')

    
    # Element type-definition uses Python identifier type_definition
    __type_definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type-definition'), 'type_definition', '__httpgenologics_comriprocesstype_process_type__type_definition', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 29, 6), )

    
    type_definition = property(__type_definition.value, __type_definition.set, None, '\n            Each type definition provides a URI linking to the configuration of a user-defined type for the process type.\n<br/>Always returns with GET: No\n          ')

    
    # Element process-input uses Python identifier process_input
    __process_input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'process-input'), 'process_input', '__httpgenologics_comriprocesstype_process_type__process_input', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 37, 6), )

    
    process_input = property(__process_input.value, __process_input.set, None, '\n            List of enabled inputs for this process type.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element process-output uses Python identifier process_output
    __process_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'process-output'), 'process_output', '__httpgenologics_comriprocesstype_process_type__process_output', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 45, 6), )

    
    process_output = property(__process_output.value, __process_output.set, None, '\n            List of enabled outputs for this process type.\n<br/>Always returns with GET: No\n          ')

    
    # Element process-type-attribute uses Python identifier process_type_attribute
    __process_type_attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'process-type-attribute'), 'process_type_attribute', '__httpgenologics_comriprocesstype_process_type__process_type_attribute', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 53, 6), )

    
    process_type_attribute = property(__process_type_attribute.value, __process_type_attribute.set, None, '\n            List of configuration attributes for this process type.\n<br/>Always returns with GET: No\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriprocesstype_process_type__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 62, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 62, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the process type.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriprocesstype_process_type__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 70, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 70, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the process type.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __field_definition.name() : __field_definition,
        __parameter.name() : __parameter,
        __type_definition.name() : __type_definition,
        __process_input.name() : __process_input,
        __process_output.name() : __process_output,
        __process_type_attribute.name() : __process_type_attribute
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'process-type', process_type_)


# Complex type {http://genologics.com/ri/processtype}process-input with content type ELEMENT_ONLY
class process_input (pyxb.binding.basis.complexTypeDefinition):
    """
        Process-input is a child element of process type specifying the available input types for the process
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-input')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 102, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element artifact-type uses Python identifier artifact_type
    __artifact_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'artifact-type'), 'artifact_type', '__httpgenologics_comriprocesstype_process_input_artifact_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 109, 6), )

    
    artifact_type = property(__artifact_type.value, __artifact_type.set, None, '\n            The artifact type for the input.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element display-name uses Python identifier display_name
    __display_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'display-name'), 'display_name', '__httpgenologics_comriprocesstype_process_input_display_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 117, 6), )

    
    display_name = property(__display_name.value, __display_name.set, None, '\n            The display name for the input.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element remove-working-flag uses Python identifier remove_working_flag
    __remove_working_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-working-flag'), 'remove_working_flag', '__httpgenologics_comriprocesstype_process_input_remove_working_flag', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 125, 6), )

    
    remove_working_flag = property(__remove_working_flag.value, __remove_working_flag.set, None, '\n            Deprecated, this property is no longer supported.\nWhether the working flag should be removed from the input when the process runs.\n<br/>Always returns with GET: No\n          ')

    _ElementMap.update({
        __artifact_type.name() : __artifact_type,
        __display_name.name() : __display_name,
        __remove_working_flag.name() : __remove_working_flag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'process-input', process_input)


# Complex type {http://genologics.com/ri/processtype}process-output with content type ELEMENT_ONLY
class process_output (pyxb.binding.basis.complexTypeDefinition):
    """
        Process-output is a child element of process type specifying the configured output generation types for the process
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-output')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element artifact-type uses Python identifier artifact_type
    __artifact_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'artifact-type'), 'artifact_type', '__httpgenologics_comriprocesstype_process_output_artifact_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 143, 6), )

    
    artifact_type = property(__artifact_type.value, __artifact_type.set, None, '\n            Artifact type for this output.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element display-name uses Python identifier display_name
    __display_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'display-name'), 'display_name', '__httpgenologics_comriprocesstype_process_output_display_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 151, 6), )

    
    display_name = property(__display_name.value, __display_name.set, None, '\n            The display name for the input.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element output-generation-type uses Python identifier output_generation_type
    __output_generation_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-generation-type'), 'output_generation_type', '__httpgenologics_comriprocesstype_process_output_output_generation_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 159, 6), )

    
    output_generation_type = property(__output_generation_type.value, __output_generation_type.set, None, '\n            Specifies how the outputs are generated in\nrelation to the inputs (COMPOUND, PER_REAGENT_LABEL, or PER_INPUT).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element variability-type uses Python identifier variability_type
    __variability_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'variability-type'), 'variability_type', '__httpgenologics_comriprocesstype_process_output_variability_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 168, 6), )

    
    variability_type = property(__variability_type.value, __variability_type.set, None, '\n            Specifies how the process determines the\nnumber of outputs to generated (FIXED, VARIABLE, or VARIABLE_BY_INPUT).\n<br/>Always returns with GET: Yes for FIXED output, No otherwise\n          ')

    
    # Element number-of-outputs uses Python identifier number_of_outputs
    __number_of_outputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number-of-outputs'), 'number_of_outputs', '__httpgenologics_comriprocesstype_process_output_number_of_outputs', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 177, 6), )

    
    number_of_outputs = property(__number_of_outputs.value, __number_of_outputs.set, None, '\n            Number of outputs to generate (only applies if variabilityType is FIXED).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element output-name uses Python identifier output_name
    __output_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-name'), 'output_name', '__httpgenologics_comriprocesstype_process_output_output_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 185, 6), )

    
    output_name = property(__output_name.value, __output_name.set, None, '\n            Pattern for specifying how the output name is generated.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element field-definition uses Python identifier field_definition
    __field_definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'field-definition'), 'field_definition', '__httpgenologics_comriprocesstype_process_output_field_definition', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 193, 6), )

    
    field_definition = property(__field_definition.value, __field_definition.set, None, '\n            Each field definition provides a URI linking to the configuration of a user-defined field for the output type.\n<br/>Always returns with GET: No\n          ')

    
    # Element assign-working-flag uses Python identifier assign_working_flag
    __assign_working_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'assign-working-flag'), 'assign_working_flag', '__httpgenologics_comriprocesstype_process_output_assign_working_flag', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 201, 6), )

    
    assign_working_flag = property(__assign_working_flag.value, __assign_working_flag.set, None, '\n            Deprecated, this property is no longer supported.\nWhether the working flag should be assigned to the output when the process runs.\n<br/>Always returns with GET: No\n          ')

    _ElementMap.update({
        __artifact_type.name() : __artifact_type,
        __display_name.name() : __display_name,
        __output_generation_type.name() : __output_generation_type,
        __variability_type.name() : __variability_type,
        __number_of_outputs.name() : __number_of_outputs,
        __output_name.name() : __output_name,
        __field_definition.name() : __field_definition,
        __assign_working_flag.name() : __assign_working_flag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'process-output', process_output)


# Complex type {http://genologics.com/ri/processtype}parameter with content type ELEMENT_ONLY
class parameter (pyxb.binding.basis.complexTypeDefinition):
    """
        The parameter element integrates the process with the External Program Integration plug-in (EPP).
When a user runs the process, the system automatically issue a command, or submits files and
scripts to third-party programs for further processing. The parameter element is a child
element of process-type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'parameter')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 212, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__httpgenologics_comriprocesstype_parameter_file', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 222, 6), )

    
    file = property(__file.value, __file.set, None, '\n            Deprecated, this property is no longer supported.\nThe file of the parameter.\n<br/>Always returns with GET: No\n          ')

    
    # Element string uses Python identifier string
    __string = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'string'), 'string', '__httpgenologics_comriprocesstype_parameter_string', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 231, 6), )

    
    string = property(__string.value, __string.set, None, '\n            The value of the parameter.\n<br/>Always returns with GET: No\n          ')

    
    # Element run-program-per-event uses Python identifier run_program_per_event
    __run_program_per_event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'run-program-per-event'), 'run_program_per_event', '__httpgenologics_comriprocesstype_parameter_run_program_per_event', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 239, 6), )

    
    run_program_per_event = property(__run_program_per_event.value, __run_program_per_event.set, None, '\n            Deprecated, this property is no longer supported.\nShould the EPP run once for each process related event?\n<br/>Always returns with GET: No\n          ')

    
    # Element channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'channel'), 'channel', '__httpgenologics_comriprocesstype_parameter_channel', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 248, 6), )

    
    channel = property(__channel.value, __channel.set, None, '\n            The epp channel of this script.\n<br/>Always returns with GET: No\n          ')

    
    # Element invocation-type uses Python identifier invocation_type
    __invocation_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'invocation-type'), 'invocation_type', '__httpgenologics_comriprocesstype_parameter_invocation_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 256, 6), )

    
    invocation_type = property(__invocation_type.value, __invocation_type.set, None, '\n            Deprecated, this property is no longer supported.\nThe epp invocation type of this script.\n<br/>Always returns with GET: No\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriprocesstype_parameter_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 266, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 266, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the process type parameter.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __file.name() : __file,
        __string.name() : __string,
        __run_program_per_event.name() : __run_program_per_event,
        __channel.name() : __channel,
        __invocation_type.name() : __invocation_type
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'parameter', parameter)


# Complex type {http://genologics.com/ri/processtype}process-type-attribute with content type SIMPLE
class process_type_attribute (pyxb.binding.basis.complexTypeDefinition):
    """
        Process-type-attributes is a child element of process type containing key/value pairs for
setting specific attributes that can be set for process types. This information
contains internally used parameters that will change. These parameters are
suitable for use when copying process types, but should not be manipulated.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-type-attribute')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 275, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriprocesstype_process_type_attribute_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 286, 8)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 286, 8)
    
    name = property(__name.value, __name.set, None, '\n              Specifies which attribute that the value will be set to.\n<br/>Always returns with GET: Yes\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'process-type-attribute', process_type_attribute)


# Complex type {http://genologics.com/ri/processtype}type-definition with content type EMPTY
class type_definition (pyxb.binding.basis.complexTypeDefinition):
    """
        Type-definition is a child element of process type providing a URI linking to the configuration of a user-defined type for the process type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'type-definition')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 297, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriprocesstype_type_definition_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 303, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 303, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the user-defined type.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriprocesstype_type_definition_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 311, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 311, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI linking to the configuration of a user-defined type for the process type.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'type-definition', type_definition)


# Complex type {http://genologics.com/ri/processtype}process-types with content type ELEMENT_ONLY
class process_types_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation for a list of process type links.<br/><br/>
The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-types')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 332, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element process-type uses Python identifier process_type
    __process_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'process-type'), 'process_type', '__httpgenologics_comriprocesstype_process_types__process_type', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 343, 6), )

    
    process_type = property(__process_type.value, __process_type.set, None, '\n            Process-type provides a URI linking to the detailed representation of a process type.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'previous-page'), 'previous_page', '__httpgenologics_comriprocesstype_process_types__previous_page', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 350, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, '\n            When working with large lists of process types,\nthe previous-page element provides a URI that links to the previous page of process types.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'next-page'), 'next_page', '__httpgenologics_comriprocesstype_process_types__next_page', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 358, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, '\n            When working with large lists of process types,\nthe next-page element provides a URI that links to the next page of process types.\n          ')

    _ElementMap.update({
        __process_type.name() : __process_type,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'process-types', process_types_)


# Complex type {http://genologics.com/ri/processtype}process-type-link with content type EMPTY
class process_type_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Process-type-link is a child element type of process types and provides a URI linking to the detailed representation of a process type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'process-type-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 368, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriprocesstype_process_type_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 374, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 374, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the process type.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriprocesstype_process_type_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 381, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 381, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the process type.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'process-type-link', process_type_link)


process_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'process-type'), process_type_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', process_type.name().localName(), process_type)

process_types = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'process-types'), process_types_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', process_types.name().localName(), process_types)



process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'field-definition'), _ImportedBinding_configuration.field_link, scope=process_type_, documentation='\n            Each field definition provides a URI linking to the configuration of a user-defined field for the process type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 13, 6)))

process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameter'), parameter, scope=process_type_, documentation='\n            Each parameter is a named value or file for the process type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 21, 6)))

process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type-definition'), type_definition, scope=process_type_, documentation='\n            Each type definition provides a URI linking to the configuration of a user-defined type for the process type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 29, 6)))

process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'process-input'), process_input, scope=process_type_, documentation='\n            List of enabled inputs for this process type.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 37, 6)))

process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'process-output'), process_output, scope=process_type_, documentation='\n            List of enabled outputs for this process type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 45, 6)))

process_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'process-type-attribute'), process_type_attribute, scope=process_type_, documentation='\n            List of configuration attributes for this process type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 53, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 13, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 29, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 37, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 45, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 53, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'field-definition')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 13, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'parameter')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'type-definition')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 29, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'process-input')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 37, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'process-output')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 45, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(process_type_._UseForTag(pyxb.namespace.ExpandedName(None, 'process-type-attribute')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 53, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
process_type_._Automaton = _BuildAutomaton()




process_input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'artifact-type'), pyxb.binding.datatypes.string, scope=process_input, documentation='\n            The artifact type for the input.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 109, 6)))

process_input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'display-name'), pyxb.binding.datatypes.string, scope=process_input, documentation='\n            The display name for the input.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 117, 6)))

process_input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-working-flag'), pyxb.binding.datatypes.boolean, scope=process_input, documentation='\n            Deprecated, this property is no longer supported.\nWhether the working flag should be removed from the input when the process runs.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 125, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 109, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 117, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 125, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(process_input._UseForTag(pyxb.namespace.ExpandedName(None, 'artifact-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 109, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(process_input._UseForTag(pyxb.namespace.ExpandedName(None, 'display-name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 117, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(process_input._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-working-flag')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 125, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
process_input._Automaton = _BuildAutomaton_()




process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'artifact-type'), pyxb.binding.datatypes.string, scope=process_output, documentation='\n            Artifact type for this output.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 143, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'display-name'), pyxb.binding.datatypes.string, scope=process_output, documentation='\n            The display name for the input.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 151, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-generation-type'), output_generation_type, scope=process_output, documentation='\n            Specifies how the outputs are generated in\nrelation to the inputs (COMPOUND, PER_REAGENT_LABEL, or PER_INPUT).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 159, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'variability-type'), variability_type, scope=process_output, documentation='\n            Specifies how the process determines the\nnumber of outputs to generated (FIXED, VARIABLE, or VARIABLE_BY_INPUT).\n<br/>Always returns with GET: Yes for FIXED output, No otherwise\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 168, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number-of-outputs'), pyxb.binding.datatypes.int, scope=process_output, documentation='\n            Number of outputs to generate (only applies if variabilityType is FIXED).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 177, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-name'), pyxb.binding.datatypes.string, scope=process_output, documentation='\n            Pattern for specifying how the output name is generated.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 185, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'field-definition'), _ImportedBinding_configuration.field_link, scope=process_output, documentation='\n            Each field definition provides a URI linking to the configuration of a user-defined field for the output type.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 193, 6)))

process_output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'assign-working-flag'), pyxb.binding.datatypes.boolean, scope=process_output, documentation='\n            Deprecated, this property is no longer supported.\nWhether the working flag should be assigned to the output when the process runs.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 201, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 143, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 151, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 159, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 168, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 177, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 185, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 193, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 201, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'artifact-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 143, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'display-name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 151, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'output-generation-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 159, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'variability-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 168, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'number-of-outputs')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 177, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'output-name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 185, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'field-definition')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 193, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(process_output._UseForTag(pyxb.namespace.ExpandedName(None, 'assign-working-flag')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 201, 6))
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
process_output._Automaton = _BuildAutomaton_2()




parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), pyxb.binding.datatypes.string, scope=parameter, documentation='\n            Deprecated, this property is no longer supported.\nThe file of the parameter.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 222, 6)))

parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'string'), pyxb.binding.datatypes.string, scope=parameter, documentation='\n            The value of the parameter.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 231, 6)))

parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'run-program-per-event'), pyxb.binding.datatypes.boolean, scope=parameter, documentation='\n            Deprecated, this property is no longer supported.\nShould the EPP run once for each process related event?\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 239, 6)))

parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'channel'), pyxb.binding.datatypes.string, scope=parameter, documentation='\n            The epp channel of this script.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 248, 6)))

parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'invocation-type'), invocation_type, scope=parameter, documentation='\n            Deprecated, this property is no longer supported.\nThe epp invocation type of this script.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 256, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 222, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 231, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 239, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 248, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 256, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(parameter._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 222, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(parameter._UseForTag(pyxb.namespace.ExpandedName(None, 'string')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 231, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(parameter._UseForTag(pyxb.namespace.ExpandedName(None, 'run-program-per-event')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 239, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(parameter._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 248, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(parameter._UseForTag(pyxb.namespace.ExpandedName(None, 'invocation-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 256, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
parameter._Automaton = _BuildAutomaton_3()




process_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'process-type'), process_type_link, scope=process_types_, documentation='\n            Process-type provides a URI linking to the detailed representation of a process type.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 343, 6)))

process_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'previous-page'), _ImportedBinding_ri.page, scope=process_types_, documentation='\n            When working with large lists of process types,\nthe previous-page element provides a URI that links to the previous page of process types.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 350, 6)))

process_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'next-page'), _ImportedBinding_ri.page, scope=process_types_, documentation='\n            When working with large lists of process types,\nthe next-page element provides a URI that links to the next page of process types.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 358, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 343, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 350, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 358, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(process_types_._UseForTag(pyxb.namespace.ExpandedName(None, 'process-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 343, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(process_types_._UseForTag(pyxb.namespace.ExpandedName(None, 'previous-page')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 350, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(process_types_._UseForTag(pyxb.namespace.ExpandedName(None, 'next-page')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/processtype.xsd', 358, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
process_types_._Automaton = _BuildAutomaton_4()

