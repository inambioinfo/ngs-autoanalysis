# ./controltype.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:86e663922ca00fa10b60fbec59dcbe0245dfefcc
# Generated 2014-10-02 18:41:08.799209 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/controltype

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4a029cca-4a5b-11e4-a093-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/controltype', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/controltype}control-type with content type ELEMENT_ONLY
class control_type_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a ControlType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'control-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element supplier uses Python identifier supplier
    __supplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'supplier'), 'supplier', '__httpgenologics_comricontroltype_control_type__supplier', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 11, 6), )

    
    supplier = property(__supplier.value, __supplier.set, None, u'\n            The supplier of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element catalogue-number uses Python identifier catalogue_number
    __catalogue_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'catalogue-number'), 'catalogue_number', '__httpgenologics_comricontroltype_control_type__catalogue_number', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 23, 6), )

    
    catalogue_number = property(__catalogue_number.value, __catalogue_number.set, None, u'\n            The catalogue number of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'website'), 'website', '__httpgenologics_comricontroltype_control_type__website', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 35, 6), )

    
    website = property(__website.value, __website.set, None, u'\n            The website of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element archived uses Python identifier archived
    __archived = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'archived'), 'archived', '__httpgenologics_comricontroltype_control_type__archived', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 47, 6), )

    
    archived = property(__archived.value, __archived.set, None, u'\n            The archived flag specifies whether a ControlType is archived.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element single-step uses Python identifier single_step
    __single_step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'single-step'), 'single_step', '__httpgenologics_comricontroltype_control_type__single_step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 59, 6), )

    
    single_step = property(__single_step.value, __single_step.set, None, u'\n            The single step flag specifies whether a control sample can only be used in a single protocol step.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comricontroltype_control_type__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 72, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 72, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the ControlType.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comricontroltype_control_type__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 84, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 84, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the ControlType.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        __supplier.name() : __supplier,
        __catalogue_number.name() : __catalogue_number,
        __website.name() : __website,
        __archived.name() : __archived,
        __single_step.name() : __single_step
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'control-type', control_type_)


# Complex type {http://genologics.com/ri/controltype}control-types with content type ELEMENT_ONLY
class control_types_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of ControlTypes
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'control-types')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element control-type uses Python identifier control_type
    __control_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'control-type'), 'control_type', '__httpgenologics_comricontroltype_control_types__control_type', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 104, 6), )

    
    control_type = property(__control_type.value, __control_type.set, None, u'\n            The list of ControlTypes.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comricontroltype_control_types__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 113, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 113, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the ControlTypes.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __control_type.name() : __control_type
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'control-types', control_types_)


# Complex type {http://genologics.com/ri/controltype}control-type-link with content type EMPTY
class control_type_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Control-type-link is a child element type of controlTypes and provides a URI linking to the detailed representation of a ControlType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'control-type-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 122, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comricontroltype_control_type_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 128, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 128, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the ControlType.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comricontroltype_control_type_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 136, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 136, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the ControlType.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'control-type-link', control_type_link)


control_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'control-type'), control_type_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', control_type.name().localName(), control_type)

control_types = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'control-types'), control_types_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', control_types.name().localName(), control_types)



control_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'supplier'), pyxb.binding.datatypes.string, scope=control_type_, documentation=u'\n            The supplier of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 11, 6)))

control_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'catalogue-number'), pyxb.binding.datatypes.string, scope=control_type_, documentation=u'\n            The catalogue number of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 23, 6)))

control_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'website'), pyxb.binding.datatypes.anyURI, scope=control_type_, documentation=u'\n            The website of the ControlType.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 35, 6)))

control_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'archived'), pyxb.binding.datatypes.boolean, scope=control_type_, documentation=u'\n            The archived flag specifies whether a ControlType is archived.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 47, 6)))

control_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'single-step'), pyxb.binding.datatypes.boolean, scope=control_type_, documentation=u'\n            The single step flag specifies whether a control sample can only be used in a single protocol step.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 59, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 23, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 35, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 47, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 59, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(control_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'supplier')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(control_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'catalogue-number')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(control_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'website')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 35, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(control_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'archived')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 47, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(control_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'single-step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 59, 6))
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
control_type_._Automaton = _BuildAutomaton()




control_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'control-type'), control_type_link, scope=control_types_, documentation=u'\n            The list of ControlTypes.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 104, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 104, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(control_types_._UseForTag(pyxb.namespace.ExpandedName(None, u'control-type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/controltype.xsd', 104, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
control_types_._Automaton = _BuildAutomaton_()

