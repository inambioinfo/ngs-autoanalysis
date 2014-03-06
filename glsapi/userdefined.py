# ./userdefined.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b23275bb00a8891855ee2acdf583a42fd5406be7
# Generated 2014-03-06 16:48:15.141972 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/userdefined [xmlns:udf]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1b9f0e11-a54f-11e3-925d-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import configuration as _ImportedBinding_configuration
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/userdefined', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/userdefined}type with content type ELEMENT_ONLY
class type_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Type is the name and user-defined fields of a user-defined type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'type')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 35, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'field'), 'field', '__httpgenologics_comriuserdefined_type__field', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 42, 6), )

    
    field = property(__field.value, __field.set, None, u'\n            The user-defined fields for the user-defined type.\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriuserdefined_type__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 50, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 50, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user-defined type.\n        ')

    _ElementMap.update({
        __field.name() : __field
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'type', type_)


# Complex type {http://genologics.com/ri/userdefined}field with content type SIMPLE
class field_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Field is the value and data type of a user-defined field.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'field')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpgenologics_comriuserdefined_field__unit', pyxb.binding.datatypes.string)
    __unit._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 11, 8)
    __unit._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 11, 8)
    
    unit = property(__unit.value, __unit.set, None, u"\n              For numeric type fields, the unit of measure for the user-defined field's value.\n            ")

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriuserdefined_field__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 18, 8)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 18, 8)
    
    name = property(__name.value, __name.set, None, u'\n              The name of the user-defined field.\n            ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comriuserdefined_field__type', _ImportedBinding_configuration.field_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 25, 8)
    __type._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 25, 8)
    
    type = property(__type.value, __type.set, None, u'\n              The type of data in the user-defined field.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unit.name() : __unit,
        __name.name() : __name,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'field', field_)


type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), type_, documentation=u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

field = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'field'), field_, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2))
Namespace.addCategoryObject('elementBinding', field.name().localName(), field)



type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'field'), field_, scope=type_, documentation=u'\n            The user-defined fields for the user-defined type.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 42, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 42, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(type_._UseForTag(pyxb.namespace.ExpandedName(None, u'field')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 42, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
type_._Automaton = _BuildAutomaton()

