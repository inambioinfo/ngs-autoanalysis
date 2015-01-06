# ./routing.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b9ea9adfd9a15d9a0b8998bd9820ee0f8ccf1db4
# Generated 2015-01-06 15:57:40.182356 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/routing

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:bc8d4bb3-95bc-11e4-bcfd-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/routing', create_if_missing=True)
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
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
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


# Complex type {http://genologics.com/ri/routing}routing with content type ELEMENT_ONLY
class routing_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The root element for a routing API call
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'routing')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element assign uses Python identifier assign
    __assign = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'assign'), 'assign', '__httpgenologics_comrirouting_routing__assign', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 10, 6), )

    
    assign = property(__assign.value, __assign.set, None, u'\n            A group of new Artifact to Workflow/Stage assignments\n          ')

    
    # Element unassign uses Python identifier unassign
    __unassign = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'unassign'), 'unassign', '__httpgenologics_comrirouting_routing__unassign', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 17, 6), )

    
    unassign = property(__unassign.value, __unassign.set, None, u'\n            A group of Artifacts to unassign from Workflows/Stages\n          ')

    _ElementMap.update({
        __assign.name() : __assign,
        __unassign.name() : __unassign
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'routing', routing_)


# Complex type {http://genologics.com/ri/routing}extArtifactAssignments with content type ELEMENT_ONLY
class extArtifactAssignments (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/routing}extArtifactAssignments with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extArtifactAssignments')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 26, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element artifact uses Python identifier artifact
    __artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'artifact'), 'artifact', '__httpgenologics_comrirouting_extArtifactAssignments_artifact', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 28, 6), )

    
    artifact = property(__artifact.value, __artifact.set, None, u'\n            A collection of artifacts to assign/unassign. Only the uri element is needed for each artifact.\n          ')

    
    # Attribute workflow-uri uses Python identifier workflow_uri
    __workflow_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'workflow-uri'), 'workflow_uri', '__httpgenologics_comrirouting_extArtifactAssignments_workflow_uri', pyxb.binding.datatypes.anyURI)
    __workflow_uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 36, 4)
    __workflow_uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 36, 4)
    
    workflow_uri = property(__workflow_uri.value, __workflow_uri.set, None, u'\n          The workflow to use for (un)assigning the samples. Is not needed if stage URI is set. If stageURI is not\nspecified, the default stage in the workflow will be used for assignment.\n        ')

    
    # Attribute stage-uri uses Python identifier stage_uri
    __stage_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'stage-uri'), 'stage_uri', '__httpgenologics_comrirouting_extArtifactAssignments_stage_uri', pyxb.binding.datatypes.anyURI)
    __stage_uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 44, 4)
    __stage_uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 44, 4)
    
    stage_uri = property(__stage_uri.value, __stage_uri.set, None, u'\n          The stage to assign the samples to. The stage is tied to a workflow, so workflowURI is not needed if this\nattribute is set.\n        ')

    _ElementMap.update({
        __artifact.name() : __artifact
    })
    _AttributeMap.update({
        __workflow_uri.name() : __workflow_uri,
        __stage_uri.name() : __stage_uri
    })
Namespace.addCategoryObject('typeBinding', u'extArtifactAssignments', extArtifactAssignments)


# Complex type {http://genologics.com/ri/routing}artifact with content type EMPTY
class artifact (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/routing}artifact with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifact')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 53, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirouting_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 54, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 54, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Artifact.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'artifact', artifact)


routing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routing'), routing_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', routing.name().localName(), routing)



routing_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'assign'), extArtifactAssignments, scope=routing_, documentation=u'\n            A group of new Artifact to Workflow/Stage assignments\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 10, 6)))

routing_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'unassign'), extArtifactAssignments, scope=routing_, documentation=u'\n            A group of Artifacts to unassign from Workflows/Stages\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 17, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 10, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 17, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routing_._UseForTag(pyxb.namespace.ExpandedName(None, u'assign')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 10, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(routing_._UseForTag(pyxb.namespace.ExpandedName(None, u'unassign')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 17, 6))
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
routing_._Automaton = _BuildAutomaton()




extArtifactAssignments._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'artifact'), artifact, scope=extArtifactAssignments, documentation=u'\n            A collection of artifacts to assign/unassign. Only the uri element is needed for each artifact.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 28, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 28, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extArtifactAssignments._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/routing.xsd', 28, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extArtifactAssignments._Automaton = _BuildAutomaton_()

