# ./reagentlot.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1fc19fb9085be7b7c633a0af081a40d537b08b36
# Generated 2015-01-06 15:57:40.182660 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/reagentlot

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
import ri as _ImportedBinding_ri

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/reagentlot', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/reagentlot}reagent-lot with content type ELEMENT_ONLY
class reagent_lot_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Reagent Lot
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-lot')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-kit uses Python identifier reagent_kit
    __reagent_kit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-kit'), 'reagent_kit', '__httpgenologics_comrireagentlot_reagent_lot__reagent_kit', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 12, 6), )

    
    reagent_kit = property(__reagent_kit.value, __reagent_kit.set, None, u'\n            The simple representation of the Reagent Kit this lot is associated with.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrireagentlot_reagent_lot__name', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 24, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element lot-number uses Python identifier lot_number
    __lot_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'lot-number'), 'lot_number', '__httpgenologics_comrireagentlot_reagent_lot__lot_number', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 36, 6), )

    
    lot_number = property(__lot_number.value, __lot_number.set, None, u'\n            The lot number of the Reagent Lot.\n<br/>Always returns with GET: NO\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element created-date uses Python identifier created_date
    __created_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'created-date'), 'created_date', '__httpgenologics_comrireagentlot_reagent_lot__created_date', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 48, 6), )

    
    created_date = property(__created_date.value, __created_date.set, None, u'\n            The date the Reagent Lot was created.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element last-modified-date uses Python identifier last_modified_date
    __last_modified_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last-modified-date'), 'last_modified_date', '__httpgenologics_comrireagentlot_reagent_lot__last_modified_date', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 60, 6), )

    
    last_modified_date = property(__last_modified_date.value, __last_modified_date.set, None, u'\n            The date that the Reagent Lot was last modified.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element expiry-date uses Python identifier expiry_date
    __expiry_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'expiry-date'), 'expiry_date', '__httpgenologics_comrireagentlot_reagent_lot__expiry_date', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 72, 6), )

    
    expiry_date = property(__expiry_date.value, __expiry_date.set, None, u'\n            The expiry date of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element created-by uses Python identifier created_by
    __created_by = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'created-by'), 'created_by', '__httpgenologics_comrireagentlot_reagent_lot__created_by', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 84, 6), )

    
    created_by = property(__created_by.value, __created_by.set, None, u'\n            The creator of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element last-modified-by uses Python identifier last_modified_by
    __last_modified_by = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last-modified-by'), 'last_modified_by', '__httpgenologics_comrireagentlot_reagent_lot__last_modified_by', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 96, 6), )

    
    last_modified_by = property(__last_modified_by.value, __last_modified_by.set, None, u'\n            The user to last modify the reagent lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element storage-location uses Python identifier storage_location
    __storage_location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'storage-location'), 'storage_location', '__httpgenologics_comrireagentlot_reagent_lot__storage_location', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 108, 6), )

    
    storage_location = property(__storage_location.value, __storage_location.set, None, u'\n            The storage location of the Reagent Lot.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__httpgenologics_comrireagentlot_reagent_lot__notes', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 120, 6), )

    
    notes = property(__notes.value, __notes.set, None, u'\n            Additional notes on the Reagent Lot\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpgenologics_comrireagentlot_reagent_lot__status', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 132, 6), )

    
    status = property(__status.value, __status.set, None, u'\n            The status of the Reagent Lot. PENDING, ACTIVE, or ARCHIVED.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element usage-count uses Python identifier usage_count
    __usage_count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'usage-count'), 'usage_count', '__httpgenologics_comrireagentlot_reagent_lot__usage_count', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 144, 6), )

    
    usage_count = property(__usage_count.value, __usage_count.set, None, u'\n            The number of times this Reagent Lot has been used.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrireagentlot_reagent_lot__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 157, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 157, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrireagentlot_reagent_lot__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 169, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 169, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The limsid of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __reagent_kit.name() : __reagent_kit,
        __name.name() : __name,
        __lot_number.name() : __lot_number,
        __created_date.name() : __created_date,
        __last_modified_date.name() : __last_modified_date,
        __expiry_date.name() : __expiry_date,
        __created_by.name() : __created_by,
        __last_modified_by.name() : __last_modified_by,
        __storage_location.name() : __storage_location,
        __notes.name() : __notes,
        __status.name() : __status,
        __usage_count.name() : __usage_count
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'reagent-lot', reagent_lot_)


# Complex type {http://genologics.com/ri/reagentlot}reagent-kit-link with content type EMPTY
class reagent_kit_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Reagent-Kit-Link is an element providing a URI linking to
the detailed representation of a reagent kit.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-kit-link')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 182, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrireagentlot_reagent_kit_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 189, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 189, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the Reagent Kit.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrireagentlot_reagent_kit_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 197, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 197, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Reagent Kit.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagent-kit-link', reagent_kit_link)


# Complex type {http://genologics.com/ri/reagentlot}researcher with content type EMPTY
class researcher (pyxb.binding.basis.complexTypeDefinition):
    """
        Researcher is a child element of the reagent lot. It provides a URI
linking to the detailed representation of the required researcher.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'researcher')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 206, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrireagentlot_researcher_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 213, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 213, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the researcher.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'researcher', researcher)


# Complex type {http://genologics.com/ri/reagentlot}reagent-lots with content type ELEMENT_ONLY
class reagent_lots_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of Reagent Lots
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-lots')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 222, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-lot uses Python identifier reagent_lot
    __reagent_lot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-lot'), 'reagent_lot', '__httpgenologics_comrireagentlot_reagent_lots__reagent_lot', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 229, 6), )

    
    reagent_lot = property(__reagent_lot.value, __reagent_lot.set, None, u'\n            The list of Reagent Lots.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comrireagentlot_reagent_lots__previous_page', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 237, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            The previous page element, contains a link to the previous page of reagent lots, if required.\n<br/>Always returns with GET: No\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comrireagentlot_reagent_lots__next_page', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 245, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            The next page element, contains a link to the next page of reagent lots, if required.\n<br/>Always returns with GET: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrireagentlot_reagent_lots__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 254, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 254, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Reagent Lots.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __reagent_lot.name() : __reagent_lot,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagent-lots', reagent_lots_)


# Complex type {http://genologics.com/ri/reagentlot}reagent-lot-link with content type EMPTY
class reagent_lot_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Reagent-lot-link is a child element type of Reagent Lots and provides a URI linking to
the detailed representation of a Reagent Lot.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-lot-link')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 263, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrireagentlot_reagent_lot_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 270, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 270, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The limsid of the Reagent Lot.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrireagentlot_reagent_lot_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 278, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 278, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Reagent Lot.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagent-lot-link', reagent_lot_link)


reagent_lot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reagent-lot'), reagent_lot_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', reagent_lot.name().localName(), reagent_lot)

reagent_lots = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reagent-lots'), reagent_lots_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', reagent_lots.name().localName(), reagent_lots)



reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-kit'), reagent_kit_link, scope=reagent_lot_, documentation=u'\n            The simple representation of the Reagent Kit this lot is associated with.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 12, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The name of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 24, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'lot-number'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The lot number of the Reagent Lot.\n<br/>Always returns with GET: NO\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 36, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'created-date'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The date the Reagent Lot was created.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 48, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last-modified-date'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The date that the Reagent Lot was last modified.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 60, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'expiry-date'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The expiry date of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 72, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'created-by'), researcher, scope=reagent_lot_, documentation=u'\n            The creator of the Reagent Lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 84, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last-modified-by'), researcher, scope=reagent_lot_, documentation=u'\n            The user to last modify the reagent lot.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 96, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'storage-location'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The storage location of the Reagent Lot.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 108, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            Additional notes on the Reagent Lot\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 120, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'), pyxb.binding.datatypes.string, scope=reagent_lot_, documentation=u'\n            The status of the Reagent Lot. PENDING, ACTIVE, or ARCHIVED.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 132, 6)))

reagent_lot_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'usage-count'), pyxb.binding.datatypes.long, scope=reagent_lot_, documentation=u'\n            The number of times this Reagent Lot has been used.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 144, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 24, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 36, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 48, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 60, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 72, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 84, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 96, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 108, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 120, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 132, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 144, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-kit')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 24, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'lot-number')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 36, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'created-date')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 48, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'last-modified-date')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 60, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'expiry-date')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 72, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'created-by')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 84, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'last-modified-by')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 96, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'storage-location')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 108, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 120, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'status')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 132, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lot_._UseForTag(pyxb.namespace.ExpandedName(None, u'usage-count')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 144, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
reagent_lot_._Automaton = _BuildAutomaton()




reagent_lots_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-lot'), reagent_lot_link, scope=reagent_lots_, documentation=u'\n            The list of Reagent Lots.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 229, 6)))

reagent_lots_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=reagent_lots_, documentation=u'\n            The previous page element, contains a link to the previous page of reagent lots, if required.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 237, 6)))

reagent_lots_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=reagent_lots_, documentation=u'\n            The next page element, contains a link to the next page of reagent lots, if required.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 245, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 229, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 237, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 245, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lots_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-lot')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 229, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lots_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 237, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagent_lots_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/reagentlot.xsd', 245, 6))
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
reagent_lots_._Automaton = _BuildAutomaton_()

