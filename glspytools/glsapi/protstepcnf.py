# ./protstepcnf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b40a4f9427295a291407fc3444b9031d697bd00b
# Generated 2013-05-14 16:17:05.795436 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/stepconfiguration [xmlns:protstepcnf]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5529b46e-bca9-11e2-9d0d-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/stepconfiguration', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://genologics.com/ri/stepconfiguration}trigger-point
class trigger_point (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The trigger-point enumeration lists the possible values of the EPP Trigger point attribute.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trigger-point')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 399, 2)
    _Documentation = u'\n        The trigger-point enumeration lists the possible values of the EPP Trigger point attribute.\n      '
trigger_point._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=trigger_point, enum_prefix=None)
trigger_point.BEFORE = trigger_point._CF_enumeration.addEnumeration(unicode_value=u'BEFORE', tag=u'BEFORE')
trigger_point.AFTER = trigger_point._CF_enumeration.addEnumeration(unicode_value=u'AFTER', tag=u'AFTER')
trigger_point._InitializeFacetMap(trigger_point._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'trigger-point', trigger_point)

# Atomic simple type: {http://genologics.com/ri/stepconfiguration}trigger-status
class trigger_status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The trigger-status enumeration lists the possible values of the EPP Trigger status attribute.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trigger-status')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 410, 2)
    _Documentation = u'\n        The trigger-status enumeration lists the possible values of the EPP Trigger status attribute.\n      '
trigger_status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=trigger_status, enum_prefix=None)
trigger_status.STARTED = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'STARTED', tag=u'STARTED')
trigger_status.STEP_SETUP = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'STEP_SETUP', tag=u'STEP_SETUP')
trigger_status.POOLING = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'POOLING', tag=u'POOLING')
trigger_status.PLACEMENT = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'PLACEMENT', tag=u'PLACEMENT')
trigger_status.ADD_REAGENT = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'ADD_REAGENT', tag=u'ADD_REAGENT')
trigger_status.RECORD_DETAILS = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'RECORD_DETAILS', tag=u'RECORD_DETAILS')
trigger_status.COMPLETE = trigger_status._CF_enumeration.addEnumeration(unicode_value=u'COMPLETE', tag=u'COMPLETE')
trigger_status._InitializeFacetMap(trigger_status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'trigger-status', trigger_status)

# Atomic simple type: {http://genologics.com/ri/stepconfiguration}trigger-type
class trigger_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The trigger-type enumeration lists the possible values of the EPP Trigger type attribute.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trigger-type')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 426, 2)
    _Documentation = u'\n        The trigger-type enumeration lists the possible values of the EPP Trigger type attribute.\n      '
trigger_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=trigger_type, enum_prefix=None)
trigger_type.MANUAL = trigger_type._CF_enumeration.addEnumeration(unicode_value=u'MANUAL', tag=u'MANUAL')
trigger_type.AUTOMATIC = trigger_type._CF_enumeration.addEnumeration(unicode_value=u'AUTOMATIC', tag=u'AUTOMATIC')
trigger_type.UNUSED = trigger_type._CF_enumeration.addEnumeration(unicode_value=u'UNUSED', tag=u'UNUSED')
trigger_type._InitializeFacetMap(trigger_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'trigger-type', trigger_type)

# Complex type {http://genologics.com/ri/stepconfiguration}step with content type ELEMENT_ONLY
class step_ (pyxb.binding.basis.complexTypeDefinition):
    """
        <p>Detailed representation of a Step</p>
<p>Steps are the elements that compose
protocols. They have various properties
regarding different UDFs contained on each view of the step
as well as configuration option and filters</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element protocol-step-index uses Python identifier protocol_step_index
    __protocol_step_index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol-step-index'), 'protocol_step_index', '__httpgenologics_comristepconfiguration_step__protocol_step_index', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 14, 6), )

    
    protocol_step_index = property(__protocol_step_index.value, __protocol_step_index.set, None, u'\n            The index of the step within the actual protocol\n          ')

    
    # Element process-type uses Python identifier process_type
    __process_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'process-type'), 'process_type', '__httpgenologics_comristepconfiguration_step__process_type', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 21, 6), )

    
    process_type = property(__process_type.value, __process_type.set, None, u'\n            The type of the Process.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element permitted-containers uses Python identifier permitted_containers
    __permitted_containers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'permitted-containers'), 'permitted_containers', '__httpgenologics_comristepconfiguration_step__permitted_containers', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 31, 6), )

    
    permitted_containers = property(__permitted_containers.value, __permitted_containers.set, None, u'\n            List of permitted containers for this specific protocol step\n          ')

    
    # Element transitions uses Python identifier transitions
    __transitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'transitions'), 'transitions', '__httpgenologics_comristepconfiguration_step__transitions', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 49, 6), )

    
    transitions = property(__transitions.value, __transitions.set, None, u'\n            List of available transitions to next steps\nupon completion of this current step\n          ')

    
    # Element queue-fields uses Python identifier queue_fields
    __queue_fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'queue-fields'), 'queue_fields', '__httpgenologics_comristepconfiguration_step__queue_fields', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 69, 6), )

    
    queue_fields = property(__queue_fields.value, __queue_fields.set, None, u'\n            UDF columns that will be displayed on\nthe queue view\n          ')

    
    # Element step-fields uses Python identifier step_fields
    __step_fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step-fields'), 'step_fields', '__httpgenologics_comristepconfiguration_step__step_fields', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 89, 6), )

    
    step_fields = property(__step_fields.value, __step_fields.set, None, u'\n            Fields that will be displayed on the\nwork view of the step\n          ')

    
    # Element sample-fields uses Python identifier sample_fields
    __sample_fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sample-fields'), 'sample_fields', '__httpgenologics_comristepconfiguration_step__sample_fields', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 109, 6), )

    
    sample_fields = property(__sample_fields.value, __sample_fields.set, None, u'\n            Editable Fields that will be displayed\non the samples contained in the work view\n          ')

    
    # Element step-properties uses Python identifier step_properties
    __step_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step-properties'), 'step_properties', '__httpgenologics_comristepconfiguration_step__step_properties', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 129, 6), )

    
    step_properties = property(__step_properties.value, __step_properties.set, None, u'\n            A list of extra properties relevant to the step\n          ')

    
    # Element step-setup uses Python identifier step_setup
    __step_setup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step-setup'), 'step_setup', '__httpgenologics_comristepconfiguration_step__step_setup', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 147, 6), )

    
    step_setup = property(__step_setup.value, __step_setup.set, None, u'\n            The step setup details.\n          ')

    
    # Element epp-triggers uses Python identifier epp_triggers
    __epp_triggers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'epp-triggers'), 'epp_triggers', '__httpgenologics_comristepconfiguration_step__epp_triggers', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 154, 6), )

    
    epp_triggers = property(__epp_triggers.value, __epp_triggers.set, None, u'\n            A list of EPP triggers for the step.\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristepconfiguration_step__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 173, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 173, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the current step\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristepconfiguration_step__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 180, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 180, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI address of the current step\n        ')

    
    # Attribute protocol-uri uses Python identifier protocol_uri
    __protocol_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'protocol-uri'), 'protocol_uri', '__httpgenologics_comristepconfiguration_step__protocol_uri', pyxb.binding.datatypes.anyURI)
    __protocol_uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 187, 4)
    __protocol_uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 187, 4)
    
    protocol_uri = property(__protocol_uri.value, __protocol_uri.set, None, u'\n          The URI address of the current protocol\n        ')

    _ElementMap.update({
        __protocol_step_index.name() : __protocol_step_index,
        __process_type.name() : __process_type,
        __permitted_containers.name() : __permitted_containers,
        __transitions.name() : __transitions,
        __queue_fields.name() : __queue_fields,
        __step_fields.name() : __step_fields,
        __sample_fields.name() : __sample_fields,
        __step_properties.name() : __step_properties,
        __step_setup.name() : __step_setup,
        __epp_triggers.name() : __epp_triggers
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri,
        __protocol_uri.name() : __protocol_uri
    })
Namespace.addCategoryObject('typeBinding', u'step', step_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            List of permitted containers for this specific protocol step
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 37, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container-type uses Python identifier container_type
    __container_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container-type'), 'container_type', '__httpgenologics_comristepconfiguration_CTD_ANON_container_type', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 39, 12), )

    
    container_type = property(__container_type.value, __container_type.set, None, u'\n                  List of permitted containers for this specific protocol step\n                ')

    _ElementMap.update({
        __container_type.name() : __container_type
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            List of available transitions to next steps
upon completion of this current step
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 56, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'transition'), 'transition', '__httpgenologics_comristepconfiguration_CTD_ANON__transition', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 58, 12), )

    
    transition = property(__transition.value, __transition.set, None, u'\n                  List of available transitions to next steps\nupon completion of this current step\n                ')

    _ElementMap.update({
        __transition.name() : __transition
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
            UDF columns that will be displayed on
the queue view
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 76, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element queue-field uses Python identifier queue_field
    __queue_field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'queue-field'), 'queue_field', '__httpgenologics_comristepconfiguration_CTD_ANON_2_queue_field', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 78, 12), )

    
    queue_field = property(__queue_field.value, __queue_field.set, None, u'\n                  UDF columns that will be displayed on\nthe queue view\n                ')

    _ElementMap.update({
        __queue_field.name() : __queue_field
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
            Fields that will be displayed on the
work view of the step
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 96, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step-field uses Python identifier step_field
    __step_field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step-field'), 'step_field', '__httpgenologics_comristepconfiguration_CTD_ANON_3_step_field', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 98, 12), )

    
    step_field = property(__step_field.value, __step_field.set, None, u'\n                  Fields that will be displayed on the\nwork view of the step\n                ')

    _ElementMap.update({
        __step_field.name() : __step_field
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
            Editable Fields that will be displayed
on the samples contained in the work view
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 116, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sample-field uses Python identifier sample_field
    __sample_field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sample-field'), 'sample_field', '__httpgenologics_comristepconfiguration_CTD_ANON_4_sample_field', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 118, 12), )

    
    sample_field = property(__sample_field.value, __sample_field.set, None, u'\n                  Editable Fields that will be displayed\non the samples contained in the work view\n                ')

    _ElementMap.update({
        __sample_field.name() : __sample_field
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
            A list of extra properties relevant to the step
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 135, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step-property uses Python identifier step_property
    __step_property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step-property'), 'step_property', '__httpgenologics_comristepconfiguration_CTD_ANON_5_step_property', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 137, 12), )

    
    step_property = property(__step_property.value, __step_property.set, None, u'\n                  A list of extra properties relevant to the step\n                ')

    _ElementMap.update({
        __step_property.name() : __step_property
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
            A list of EPP triggers for the step.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 160, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element epp-trigger uses Python identifier epp_trigger
    __epp_trigger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'epp-trigger'), 'epp_trigger', '__httpgenologics_comristepconfiguration_CTD_ANON_6_epp_trigger', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 162, 12), )

    
    epp_trigger = property(__epp_trigger.value, __epp_trigger.set, None, u'\n                  A list of EPP triggers for the step.\n                ')

    _ElementMap.update({
        __epp_trigger.name() : __epp_trigger
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/stepconfiguration}field with content type EMPTY
class field (pyxb.binding.basis.complexTypeDefinition):
    """
        A field has a name and an attach to value,
these fields are used to keep track of all the UDF
values for samples in queue and work view as well as
those on the actual step
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'field')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 234, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristepconfiguration_field_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 243, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 243, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the UDF Field.\n        ')

    
    # Attribute attach-to uses Python identifier attach_to
    __attach_to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attach-to'), 'attach_to', '__httpgenologics_comristepconfiguration_field_attach_to', pyxb.binding.datatypes.string)
    __attach_to._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 250, 4)
    __attach_to._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 250, 4)
    
    attach_to = property(__attach_to.value, __attach_to.set, None, u'\n          The element that the UDF Field will attach to.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __attach_to.name() : __attach_to
    })
Namespace.addCategoryObject('typeBinding', u'field', field)


# Complex type {http://genologics.com/ri/stepconfiguration}file with content type ELEMENT_ONLY
class file (pyxb.binding.basis.complexTypeDefinition):
    """
        The file element describes the shared result file outputs for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'file')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 258, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpgenologics_comristepconfiguration_file_message', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 265, 6), )

    
    message = property(__message.value, __message.set, None, u'\n            The message to display for the shared result file.\n          ')

    
    # Attribute shared-result-file-index uses Python identifier shared_result_file_index
    __shared_result_file_index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shared-result-file-index'), 'shared_result_file_index', '__httpgenologics_comristepconfiguration_file_shared_result_file_index', pyxb.binding.datatypes.string)
    __shared_result_file_index._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 273, 4)
    __shared_result_file_index._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 273, 4)
    
    shared_result_file_index = property(__shared_result_file_index.value, __shared_result_file_index.set, None, u'\n          The shared result file output index of the step output.\n        ')

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        __shared_result_file_index.name() : __shared_result_file_index
    })
Namespace.addCategoryObject('typeBinding', u'file', file)


# Complex type {http://genologics.com/ri/stepconfiguration}next-step with content type EMPTY
class next_step (pyxb.binding.basis.complexTypeDefinition):
    """
        List of step transitions including the URI allowing
access to the specific next step
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'next-step')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 281, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristepconfiguration_next_step_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 288, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 288, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the next step.\n        ')

    
    # Attribute sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sequence'), 'sequence', '__httpgenologics_comristepconfiguration_next_step_sequence', pyxb.binding.datatypes.int)
    __sequence._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 295, 4)
    __sequence._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 295, 4)
    
    sequence = property(__sequence.value, __sequence.set, None, u'\n          The sequence of the next step.\n        ')

    
    # Attribute next-step-uri uses Python identifier next_step_uri
    __next_step_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'next-step-uri'), 'next_step_uri', '__httpgenologics_comristepconfiguration_next_step_next_step_uri', pyxb.binding.datatypes.anyURI)
    __next_step_uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 302, 4)
    __next_step_uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 302, 4)
    
    next_step_uri = property(__next_step_uri.value, __next_step_uri.set, None, u'\n          The URI of the next step.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __sequence.name() : __sequence,
        __next_step_uri.name() : __next_step_uri
    })
Namespace.addCategoryObject('typeBinding', u'next-step', next_step)


# Complex type {http://genologics.com/ri/stepconfiguration}process-type with content type SIMPLE
class process_type (pyxb.binding.basis.complexTypeDefinition):
    """
        Process-type is a child element that provides a URI linking to the detailed
representation of the process type that the step is associated with.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'process-type')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 310, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristepconfiguration_process_type_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 319, 8)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 319, 8)
    
    uri = property(__uri.value, __uri.set, None, u'\n              The URI of the process type.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'process-type', process_type)


# Complex type {http://genologics.com/ri/stepconfiguration}step-property with content type EMPTY
class step_property (pyxb.binding.basis.complexTypeDefinition):
    """
        A step configuration property, containing a name value pair specific to the property.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step-property')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 350, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristepconfiguration_step_property_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 356, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 356, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The property name.\n        ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpgenologics_comristepconfiguration_step_property_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 363, 4)
    __value._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 363, 4)
    
    value_ = property(__value.value, __value.set, None, u'\n          The property value.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', u'step-property', step_property)


# Complex type {http://genologics.com/ri/stepconfiguration}step-setup with content type ELEMENT_ONLY
class step_setup (pyxb.binding.basis.complexTypeDefinition):
    """
        Step-setup is a child element that provides shared result file placeholder
information for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step-setup')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 371, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'files'), 'files', '__httpgenologics_comristepconfiguration_step_setup_files', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 379, 6), )

    
    files = property(__files.value, __files.set, None, u'\n            List of shared result file outputs.\n          ')

    _ElementMap.update({
        __files.name() : __files
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'step-setup', step_setup)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
            List of shared result file outputs.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 385, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'file'), 'file', '__httpgenologics_comristepconfiguration_CTD_ANON_7_file', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 387, 12), )

    
    file = property(__file.value, __file.set, None, u'\n                  List of shared result file outputs.\n                ')

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/stepconfiguration}epp-trigger with content type EMPTY
class epp_trigger (pyxb.binding.basis.complexTypeDefinition):
    """
        EPP trigger configuration for the Protocol Step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'epp-trigger')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 195, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristepconfiguration_epp_trigger_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 201, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 201, 4)
    
    name = property(__name.value, __name.set, None, u"\n          The protocol step's process parameter name.\n<br/>Always returns with GET: Yes\n        ")

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comristepconfiguration_epp_trigger_type', trigger_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 209, 4)
    __type._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 209, 4)
    
    type = property(__type.value, __type.set, None, u"\n          The protocol step's trigger type.\n<br/>Always returns with GET: Yes\n        ")

    
    # Attribute point uses Python identifier point
    __point = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'point'), 'point', '__httpgenologics_comristepconfiguration_epp_trigger_point', trigger_point)
    __point._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 217, 4)
    __point._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 217, 4)
    
    point = property(__point.value, __point.set, None, u"\n          The protocol step's trigger point.\n<br/>Always returns with GET: No; if the type is <tt>TriggerType.MANUAL</tt> or <tt>TriggerType.UNUSED</tt>, the trigger point will not have a value.\n        ")

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpgenologics_comristepconfiguration_epp_trigger_status', trigger_status)
    __status._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 225, 4)
    __status._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 225, 4)
    
    status = property(__status.value, __status.set, None, u"\n          The protocol step's trigger status.\n<br/>Always returns with GET: No; if the type is <tt>TriggerType.MANUAL</tt> or <tt>TriggerType.UNUSED</tt>, the trigger status will not have a value.\n        ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type,
        __point.name() : __point,
        __status.name() : __status
    })
Namespace.addCategoryObject('typeBinding', u'epp-trigger', epp_trigger)


# Complex type {http://genologics.com/ri/stepconfiguration}queuefield with content type EMPTY
class queuefield (field):
    """
        A field has a name and an attach to value,
these fields are used to keep track of all the UDF
values for samples in queue and work view as well as
those on the actual step
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'queuefield')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 329, 2)
    _ElementMap = field._ElementMap.copy()
    _AttributeMap = field._AttributeMap.copy()
    # Base type is field
    
    # Attribute name inherited from {http://genologics.com/ri/stepconfiguration}field
    
    # Attribute attach_to inherited from {http://genologics.com/ri/stepconfiguration}field
    
    # Attribute detail uses Python identifier detail
    __detail = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'detail'), 'detail', '__httpgenologics_comristepconfiguration_queuefield_detail', pyxb.binding.datatypes.boolean)
    __detail._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 340, 8)
    __detail._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 340, 8)
    
    detail = property(__detail.value, __detail.set, None, u'\n              A flag indicating if this field is for detail or not.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __detail.name() : __detail
    })
Namespace.addCategoryObject('typeBinding', u'queuefield', queuefield)


step = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'step'), step_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', step.name().localName(), step)



step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol-step-index'), pyxb.binding.datatypes.int, scope=step_, documentation=u'\n            The index of the step within the actual protocol\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 14, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'process-type'), process_type, scope=step_, documentation=u'\n            The type of the Process.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 21, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'permitted-containers'), CTD_ANON, scope=step_, documentation=u'\n            List of permitted containers for this specific protocol step\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 31, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'transitions'), CTD_ANON_, scope=step_, documentation=u'\n            List of available transitions to next steps\nupon completion of this current step\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 49, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'queue-fields'), CTD_ANON_2, scope=step_, documentation=u'\n            UDF columns that will be displayed on\nthe queue view\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 69, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step-fields'), CTD_ANON_3, scope=step_, documentation=u'\n            Fields that will be displayed on the\nwork view of the step\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 89, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sample-fields'), CTD_ANON_4, scope=step_, documentation=u'\n            Editable Fields that will be displayed\non the samples contained in the work view\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 109, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step-properties'), CTD_ANON_5, scope=step_, documentation=u'\n            A list of extra properties relevant to the step\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 129, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step-setup'), step_setup, scope=step_, documentation=u'\n            The step setup details.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 147, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'epp-triggers'), CTD_ANON_6, scope=step_, documentation=u'\n            A list of EPP triggers for the step.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 154, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 14, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 31, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 69, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 89, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 109, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 129, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 147, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 154, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol-step-index')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'process-type')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'permitted-containers')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 31, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'transitions')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 49, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'queue-fields')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 69, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'step-fields')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 89, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'sample-fields')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 109, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'step-properties')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 129, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'step-setup')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 147, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'epp-triggers')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 154, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
step_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container-type'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation=u'\n                  List of permitted containers for this specific protocol step\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 39, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 39, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'container-type')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'transition'), next_step, scope=CTD_ANON_, documentation=u'\n                  List of available transitions to next steps\nupon completion of this current step\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 58, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 58, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'transition')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 58, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'queue-field'), queuefield, scope=CTD_ANON_2, documentation=u'\n                  UDF columns that will be displayed on\nthe queue view\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 78, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 78, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'queue-field')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 78, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step-field'), field, scope=CTD_ANON_3, documentation=u'\n                  Fields that will be displayed on the\nwork view of the step\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 98, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 98, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'step-field')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 98, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sample-field'), field, scope=CTD_ANON_4, documentation=u'\n                  Editable Fields that will be displayed\non the samples contained in the work view\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 118, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 118, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'sample-field')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step-property'), step_property, scope=CTD_ANON_5, documentation=u'\n                  A list of extra properties relevant to the step\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 137, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 137, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'step-property')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 137, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'epp-trigger'), epp_trigger, scope=CTD_ANON_6, documentation=u'\n                  A list of EPP triggers for the step.\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 162, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 162, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'epp-trigger')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 162, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




file._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'message'), pyxb.binding.datatypes.string, scope=file, documentation=u'\n            The message to display for the shared result file.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 265, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 265, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(file._UseForTag(pyxb.namespace.ExpandedName(None, u'message')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 265, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
file._Automaton = _BuildAutomaton_8()




step_setup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'files'), CTD_ANON_7, scope=step_setup, documentation=u'\n            List of shared result file outputs.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 379, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 379, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_setup._UseForTag(pyxb.namespace.ExpandedName(None, u'files')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 379, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
step_setup._Automaton = _BuildAutomaton_9()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'file'), file, scope=CTD_ANON_7, documentation=u'\n                  List of shared result file outputs.\n                ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 387, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 387, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'file')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protstepcnf.xsd', 387, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_10()

