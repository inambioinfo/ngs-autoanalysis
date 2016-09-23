# ./wkfcnf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e81c4072ff8d943837cacb8c1b8bbd7a908c6d25
# Generated 2016-01-12 17:07:14.298151 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/workflowconfiguration

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/workflowconfiguration', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/workflowconfiguration}status
class status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The workflow status enumeration lists the possible workflow states.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'status')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 124, 2)
    _Documentation = '\n        The workflow status enumeration lists the possible workflow states.\n      '
status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=status, enum_prefix=None)
status.PENDING = status._CF_enumeration.addEnumeration(unicode_value='PENDING', tag='PENDING')
status.ACTIVE = status._CF_enumeration.addEnumeration(unicode_value='ACTIVE', tag='ACTIVE')
status.ARCHIVED = status._CF_enumeration.addEnumeration(unicode_value='ARCHIVED', tag='ARCHIVED')
status._InitializeFacetMap(status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'status', status)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            The Protocols that belong to this Workflow.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 18, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'protocol'), 'protocol', '__httpgenologics_comriworkflowconfiguration_CTD_ANON_protocol', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 20, 12), )

    
    protocol = property(__protocol.value, __protocol.set, None, '\n                  The Protocols that belong to this Workflow.\n<br/>Always returns with GET: Yes\n                ')

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            The Stages that belong to this Workflow.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 38, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stage uses Python identifier stage
    __stage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stage'), 'stage', '__httpgenologics_comriworkflowconfiguration_CTD_ANON__stage', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 40, 12), )

    
    stage = property(__stage.value, __stage.set, None, '\n                  The Stages that belong to this Workflow.\n<br/>Always returns with GET: Yes\n                ')

    _ElementMap.update({
        __stage.name() : __stage
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/workflowconfiguration}protocol-link with content type EMPTY
class protocol_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Protocol-link is a child element type of workflow and provides a URI linking to the detailed representation of a protocol.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'protocol-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 77, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriworkflowconfiguration_protocol_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 83, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 83, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the Protocol.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriworkflowconfiguration_protocol_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 91, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 91, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Protocol.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'protocol-link', protocol_link)


# Complex type {http://genologics.com/ri/workflowconfiguration}stage-link with content type EMPTY
class stage_link (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Stage (the portion of a workflow to which samples can be associated in order to
be queued)
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stage-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriworkflowconfiguration_stage_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 107, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 107, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the stage. This is the name of the Protocol Step to which the stage is assigned, except in the case\nof a QC Protocol where the name of the Protocol is used.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriworkflowconfiguration_stage_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 115, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 115, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Stage.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'stage-link', stage_link)


# Complex type {http://genologics.com/ri/workflowconfiguration}workflows with content type ELEMENT_ONLY
class workflows_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of Workflow links.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflows')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'workflow'), 'workflow', '__httpgenologics_comriworkflowconfiguration_workflows__workflow', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 143, 6), )

    
    workflow = property(__workflow.value, __workflow.set, None, '\n            The list of Workflows.\n<br/>Always returns with GET: Yes\n          ')

    _ElementMap.update({
        __workflow.name() : __workflow
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'workflows', workflows_)


# Complex type {http://genologics.com/ri/workflowconfiguration}workflow with content type ELEMENT_ONLY
class workflow_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Workflow.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflow')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element protocols uses Python identifier protocols
    __protocols = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'protocols'), 'protocols', '__httpgenologics_comriworkflowconfiguration_workflow__protocols', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 11, 6), )

    
    protocols = property(__protocols.value, __protocols.set, None, '\n            The Protocols that belong to this Workflow.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element stages uses Python identifier stages
    __stages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stages'), 'stages', '__httpgenologics_comriworkflowconfiguration_workflow__stages', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 31, 6), )

    
    stages = property(__stages.value, __stages.set, None, '\n            The Stages that belong to this Workflow.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriworkflowconfiguration_workflow__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 52, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 52, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriworkflowconfiguration_workflow__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 60, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 60, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpgenologics_comriworkflowconfiguration_workflow__status', status)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 68, 4)
    __status._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 68, 4)
    
    status = property(__status.value, __status.set, None, '\n          The status of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __protocols.name() : __protocols,
        __stages.name() : __stages
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri,
        __status.name() : __status
    })
Namespace.addCategoryObject('typeBinding', 'workflow', workflow_)


# Complex type {http://genologics.com/ri/workflowconfiguration}workflow-link with content type EMPTY
class workflow_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Workflow-link is a child element type of workflows and provides a URI linking to the detailed representation of a workflow.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflow-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 153, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comriworkflowconfiguration_workflow_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 159, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 159, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriworkflowconfiguration_workflow_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 167, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 167, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpgenologics_comriworkflowconfiguration_workflow_link_status', status)
    __status._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 175, 4)
    __status._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 175, 4)
    
    status = property(__status.value, __status.set, None, '\n          The status of the Workflow.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri,
        __status.name() : __status
    })
Namespace.addCategoryObject('typeBinding', 'workflow-link', workflow_link)


workflows = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflows'), workflows_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', workflows.name().localName(), workflows)

workflow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflow'), workflow_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', workflow.name().localName(), workflow)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'protocol'), protocol_link, scope=CTD_ANON, documentation='\n                  The Protocols that belong to this Workflow.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 20, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'protocol')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 20, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stage'), stage_link, scope=CTD_ANON_, documentation='\n                  The Stages that belong to this Workflow.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 40, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 40, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'stage')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 40, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




workflows_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'workflow'), workflow_link, scope=workflows_, documentation='\n            The list of Workflows.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 143, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 143, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(workflows_._UseForTag(pyxb.namespace.ExpandedName(None, 'workflow')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 143, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
workflows_._Automaton = _BuildAutomaton_2()




workflow_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'protocols'), CTD_ANON, scope=workflow_, documentation='\n            The Protocols that belong to this Workflow.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 11, 6)))

workflow_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stages'), CTD_ANON_, scope=workflow_, documentation='\n            The Stages that belong to this Workflow.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 31, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 31, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(workflow_._UseForTag(pyxb.namespace.ExpandedName(None, 'protocols')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(workflow_._UseForTag(pyxb.namespace.ExpandedName(None, 'stages')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/wkfcnf.xsd', 31, 6))
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
workflow_._Automaton = _BuildAutomaton_3()

