# ./stage.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:974072d1e538923d7dbf784906c28585b52801c6
# Generated 2013-05-14 16:17:05.790727 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/stage

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/stage', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/stage}stage with content type ELEMENT_ONLY
class stage_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a stage.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stage')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element workflow uses Python identifier workflow
    __workflow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'workflow'), 'workflow', '__httpgenologics_comristage_stage__workflow', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 10, 6), )

    
    workflow = property(__workflow.value, __workflow.set, None, u'\n            Workflow link for the stage.\n          ')

    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol'), 'protocol', '__httpgenologics_comristage_stage__protocol', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 17, 6), )

    
    protocol = property(__protocol.value, __protocol.set, None, u'\n            Protocol link for the stage.\n          ')

    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristage_stage__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 24, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            Protocol Step link for the stage.\nThis is optional; only provided if non-QC protocol.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristage_stage__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 33, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 33, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the stage.\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristage_stage__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 40, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 40, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The stage name will be the protocol step name if it exists, otherwise the protocol name.\n        ')

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'index'), 'index', '__httpgenologics_comristage_stage__index', pyxb.binding.datatypes.int)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 47, 4)
    __index._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 47, 4)
    
    index = property(__index.value, __index.set, None, u'\n          The index of the stage.\n        ')

    _ElementMap.update({
        __workflow.name() : __workflow,
        __protocol.name() : __protocol,
        __step.name() : __step
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name,
        __index.name() : __index
    })
Namespace.addCategoryObject('typeBinding', u'stage', stage_)


# Complex type {http://genologics.com/ri/stage}protocol with content type EMPTY
class protocol (pyxb.binding.basis.complexTypeDefinition):
    """
        Protocol link for the stage.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristage_protocol_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 61, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 61, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the protocol.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'protocol', protocol)


# Complex type {http://genologics.com/ri/stage}step with content type EMPTY
class step (pyxb.binding.basis.complexTypeDefinition):
    """
        Protocol Step link for the stage.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristage_step_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 75, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 75, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the protocol step.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'step', step)


# Complex type {http://genologics.com/ri/stage}workflow with content type EMPTY
class workflow (pyxb.binding.basis.complexTypeDefinition):
    """
        Workflow link for the stage.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'workflow')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristage_workflow_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 89, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 89, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the workflow.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'workflow', workflow)


stage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stage'), stage_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', stage.name().localName(), stage)



stage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'workflow'), workflow, scope=stage_, documentation=u'\n            Workflow link for the stage.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 10, 6)))

stage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol'), protocol, scope=stage_, documentation=u'\n            Protocol link for the stage.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 17, 6)))

stage_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), step, scope=stage_, documentation=u'\n            Protocol Step link for the stage.\nThis is optional; only provided if non-QC protocol.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 24, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 10, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 17, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 24, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(stage_._UseForTag(pyxb.namespace.ExpandedName(None, u'workflow')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 10, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(stage_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 17, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(stage_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/stage.xsd', 24, 6))
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
stage_._Automaton = _BuildAutomaton()
