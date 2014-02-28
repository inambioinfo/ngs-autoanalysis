# ./protcnf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:05ba7636c7f3de005e4813c202517a26ffbb3595
# Generated 2014-02-28 18:06:31.784279 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/protocolconfiguration

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0c7eb623-a0a3-11e3-bd60-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import protstepcnf as _ImportedBinding_protstepcnf

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/protocolconfiguration', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/protocolconfiguration}protocol with content type ELEMENT_ONLY
class protocol_ (pyxb.binding.basis.complexTypeDefinition):
    """
        <p> Detailed representation of a protocol.</p>
<p> A protocol represents a collection of different steps.
A protocol can be a QC protocol meaning samples go through the process
mostly in parallel or a normal protocol, where samples go
through in series.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element steps uses Python identifier steps
    __steps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'steps'), 'steps', '__httpgenologics_comriprotocolconfiguration_protocol__steps', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 16, 6), )

    
    steps = property(__steps.value, __steps.set, None, u'\n            List of steps the\nprotocols is using\n          ')

    
    # Element protocol-properties uses Python identifier protocol_properties
    __protocol_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol-properties'), 'protocol_properties', '__httpgenologics_comriprotocolconfiguration_protocol__protocol_properties', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 36, 6), )

    
    protocol_properties = property(__protocol_properties.value, __protocol_properties.set, None, u'\n            Protocol configuration properties.\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriprotocolconfiguration_protocol__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 55, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 55, 4)
    
    name = property(__name.value, __name.set, None, u'\n          Name of the represented protocol\n        ')

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'index'), 'index', '__httpgenologics_comriprotocolconfiguration_protocol__index', pyxb.binding.datatypes.int)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 62, 4)
    __index._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 62, 4)
    
    index = property(__index.value, __index.set, None, u'\n          Index of the protocol\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriprotocolconfiguration_protocol__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 69, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 69, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI address of the current protocol\n        ')

    _ElementMap.update({
        __steps.name() : __steps,
        __protocol_properties.name() : __protocol_properties
    })
    _AttributeMap.update({
        __name.name() : __name,
        __index.name() : __index,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'protocol', protocol_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            List of steps the
protocols is using
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 23, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comriprotocolconfiguration_CTD_ANON_step', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 25, 12), )

    
    step = property(__step.value, __step.set, None, u'\n                  List of steps the\nprotocols is using\n                ')

    _ElementMap.update({
        __step.name() : __step
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            Protocol configuration properties.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 42, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element protocol-property uses Python identifier protocol_property
    __protocol_property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol-property'), 'protocol_property', '__httpgenologics_comriprotocolconfiguration_CTD_ANON__protocol_property', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 44, 12), )

    
    protocol_property = property(__protocol_property.value, __protocol_property.set, None, u'\n                  Protocol configuration properties.\n                ')

    _ElementMap.update({
        __protocol_property.name() : __protocol_property
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/protocolconfiguration}protocol-property with content type EMPTY
class protocol_property (pyxb.binding.basis.complexTypeDefinition):
    """
        Protocol-property is a child element of protocol containing key/value pairs for
setting specific attributes of protocols.
This information contains internally used properties that will change. These properties are
suitable for use when copying protocols, but should not be manipulated.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol-property')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 77, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriprotocolconfiguration_protocol_property_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 86, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 86, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The property name.\n        ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpgenologics_comriprotocolconfiguration_protocol_property_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 93, 4)
    __value._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 93, 4)
    
    value_ = property(__value.value, __value.set, None, u'\n          The property value.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', u'protocol-property', protocol_property)


# Complex type {http://genologics.com/ri/protocolconfiguration}protocols with content type ELEMENT_ONLY
class protocols_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Returns the representation of a list of protocols
<p> A list of protocols available in the system,
providing names and URIs to access more detailed representations of the
protocols</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocols')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'protocol'), 'protocol', '__httpgenologics_comriprotocolconfiguration_protocols__protocol', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 111, 6), )

    
    protocol = property(__protocol.value, __protocol.set, None, u'\n            Each protocol provides a URI that links to a\nmore detailed representation of the protocol\n          ')

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'protocols', protocols_)


# Complex type {http://genologics.com/ri/protocolconfiguration}protocol-link with content type EMPTY
class protocol_link (pyxb.binding.basis.complexTypeDefinition):
    """
        This list will contain a list of names and URIs
for all available protocols in the system
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 121, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriprotocolconfiguration_protocol_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 128, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 128, 4)
    
    name = property(__name.value, __name.set, None, u'\n          Name of the protocol\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriprotocolconfiguration_protocol_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 135, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 135, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          the URI to access a more detailed\nrepresentation of the protocol\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'protocol-link', protocol_link)


protocol = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protocol'), protocol_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', protocol.name().localName(), protocol)

protocols = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protocols'), protocols_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', protocols.name().localName(), protocols)



protocol_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'steps'), CTD_ANON, scope=protocol_, documentation=u'\n            List of steps the\nprotocols is using\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 16, 6)))

protocol_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol-properties'), CTD_ANON_, scope=protocol_, documentation=u'\n            Protocol configuration properties.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 36, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 16, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 36, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(protocol_._UseForTag(pyxb.namespace.ExpandedName(None, u'steps')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(protocol_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol-properties')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 36, 6))
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
protocol_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_protstepcnf.step_, scope=CTD_ANON, documentation=u'\n                  List of steps the\nprotocols is using\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 25, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 25, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 25, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol-property'), protocol_property, scope=CTD_ANON_, documentation=u'\n                  Protocol configuration properties.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 44, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 44, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol-property')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 44, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




protocols_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'protocol'), protocol_link, scope=protocols_, documentation=u'\n            Each protocol provides a URI that links to a\nmore detailed representation of the protocol\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 111, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 111, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(protocols_._UseForTag(pyxb.namespace.ExpandedName(None, u'protocol')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/protcnf.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
protocols_._Automaton = _BuildAutomaton_3()

