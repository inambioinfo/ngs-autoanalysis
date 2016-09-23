# ./lab.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:09b4ec6a03e2b94a8089882fb5e37b9c062c8ab0
# Generated 2016-01-12 17:07:14.302227 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/lab

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
import userdefined as _ImportedBinding_userdefined

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/lab', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ri = _ImportedBinding_ri.Namespace
_Namespace_ri.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_udf = _ImportedBinding_userdefined.Namespace
_Namespace_udf.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://genologics.com/ri/lab}lab with content type ELEMENT_ONLY
class lab_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a lab.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lab')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://genologics.com/ri}externalid uses Python identifier externalid
    __externalid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ri, 'externalid'), 'externalid', '__httpgenologics_comrilab_lab__httpgenologics_comriexternalid', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ri.xsd', 230, 2), )

    
    externalid = property(__externalid.value, __externalid.set, None, '\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comrilab_lab__name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 13, 6), )

    
    name = property(__name.value, __name.set, None, '\n            The name of the lab.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element billing-address uses Python identifier billing_address
    __billing_address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'billing-address'), 'billing_address', '__httpgenologics_comrilab_lab__billing_address', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 25, 6), )

    
    billing_address = property(__billing_address.value, __billing_address.set, None, "\n            The lab's billing address.\n<br/>Always returns with GET: No, but can be empty if it returns\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but system will return nodes with empty data\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but system will return nodes with empty data\n          ")

    
    # Element shipping-address uses Python identifier shipping_address
    __shipping_address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shipping-address'), 'shipping_address', '__httpgenologics_comrilab_lab__shipping_address', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 37, 6), )

    
    shipping_address = property(__shipping_address.value, __shipping_address.set, None, "\n            The lab's shipping address.\n<br/>Always returns with GET: No, but can be empty if it returns\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but system will return nodes with empty data\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but system will return nodes with empty data\n          ")

    
    # Element website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'website'), 'website', '__httpgenologics_comrilab_lab__website', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 86, 6), )

    
    website = property(__website.value, __website.set, None, "\n            The lab's website.\n<br/>Always returns with GET: Yes, but can be empty\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ")

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, 'field'), 'field', '__httpgenologics_comrilab_lab__httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, '\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Element {http://genologics.com/ri/userdefined}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, 'type'), 'type', '__httpgenologics_comrilab_lab__httpgenologics_comriuserdefinedtype', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2), )

    
    type = property(__type.value, __type.set, None, '\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrilab_lab__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 99, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 99, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the lab.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __externalid.name() : __externalid,
        __name.name() : __name,
        __billing_address.name() : __billing_address,
        __shipping_address.name() : __shipping_address,
        __website.name() : __website,
        __field.name() : __field,
        __type.name() : __type
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'lab', lab_)


# Complex type {http://genologics.com/ri/lab}labs with content type ELEMENT_ONLY
class labs_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of lab links.<br/><br/>
The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'labs')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 112, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lab uses Python identifier lab
    __lab = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lab'), 'lab', '__httpgenologics_comrilab_labs__lab', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 123, 6), )

    
    lab = property(__lab.value, __lab.set, None, '\n            Lab provides a URI linking to the detailed representation of a lab.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'previous-page'), 'previous_page', '__httpgenologics_comrilab_labs__previous_page', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 130, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, '\n            When working with large lists of labs,\nthe previous-page element provides a URI that links to the previous page of labs.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'next-page'), 'next_page', '__httpgenologics_comrilab_labs__next_page', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 138, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, '\n            When working with large lists of labs,\nthe next-page element provides a URI that links to the next page of labs.\n          ')

    _ElementMap.update({
        __lab.name() : __lab,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'labs', labs_)


# Complex type {http://genologics.com/ri/lab}lab-link with content type ELEMENT_ONLY
class lab_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Lab-link is a child element type of labs and provides a URI linking to the detailed representation of a lab.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lab-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 148, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comrilab_lab_link_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 155, 6), )

    
    name = property(__name.value, __name.set, None, '\n            The name of the lab.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrilab_lab_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 163, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 163, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the lab.\n        ')

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'lab-link', lab_link)


lab = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lab'), lab_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', lab.name().localName(), lab)

labs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labs'), labs_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', labs.name().localName(), labs)



lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ri, 'externalid'), _ImportedBinding_ri.externalid_, scope=lab_, documentation='\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ri.xsd', 230, 2)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=lab_, documentation='\n            The name of the lab.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 13, 6)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'billing-address'), _ImportedBinding_ri.address, scope=lab_, documentation="\n            The lab's billing address.\n<br/>Always returns with GET: No, but can be empty if it returns\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but system will return nodes with empty data\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but system will return nodes with empty data\n          ", location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 25, 6)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shipping-address'), _ImportedBinding_ri.address, scope=lab_, documentation="\n            The lab's shipping address.\n<br/>Always returns with GET: No, but can be empty if it returns\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but system will return nodes with empty data\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but system will return nodes with empty data\n          ", location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 37, 6)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'website'), pyxb.binding.datatypes.string, scope=lab_, documentation="\n            The lab's website.\n<br/>Always returns with GET: Yes, but can be empty\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ", location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 86, 6)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, 'field'), _ImportedBinding_userdefined.field_, scope=lab_, documentation='\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

lab_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, 'type'), _ImportedBinding_userdefined.type_, scope=lab_, documentation='\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 13, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 25, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 37, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 61, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 74, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 86, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 13, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(None, 'billing-address')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 25, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(None, 'shipping-address')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 37, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, 'type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 49, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, 'field')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 61, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ri, 'externalid')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 74, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(lab_._UseForTag(pyxb.namespace.ExpandedName(None, 'website')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 86, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
lab_._Automaton = _BuildAutomaton()




labs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lab'), lab_link, scope=labs_, documentation='\n            Lab provides a URI linking to the detailed representation of a lab.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 123, 6)))

labs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'previous-page'), _ImportedBinding_ri.page, scope=labs_, documentation='\n            When working with large lists of labs,\nthe previous-page element provides a URI that links to the previous page of labs.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 130, 6)))

labs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'next-page'), _ImportedBinding_ri.page, scope=labs_, documentation='\n            When working with large lists of labs,\nthe next-page element provides a URI that links to the next page of labs.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 138, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 123, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 130, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 138, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(labs_._UseForTag(pyxb.namespace.ExpandedName(None, 'lab')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 123, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(labs_._UseForTag(pyxb.namespace.ExpandedName(None, 'previous-page')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 130, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(labs_._UseForTag(pyxb.namespace.ExpandedName(None, 'next-page')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 138, 6))
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
labs_._Automaton = _BuildAutomaton_()




lab_link._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=lab_link, documentation='\n            The name of the lab.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 155, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 155, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lab_link._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/lab.xsd', 155, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
lab_link._Automaton = _BuildAutomaton_2()

