# ./ri.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0e7cebb1cc6752a9121228ba67d5f7d0a246eb45
# Generated 2014-02-28 18:06:31.776982 by PyXB version 1.2.2
# Namespace http://genologics.com/ri [xmlns:ri]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri', create_if_missing=True)
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


# Complex type {http://genologics.com/ri}address with content type ELEMENT_ONLY
class address (pyxb.binding.basis.complexTypeDefinition):
    """
        Address contains the related fields of a mailing address.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'address')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'street'), 'street', '__httpgenologics_comri_address_street', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 11, 6), )

    
    street = property(__street.value, __street.set, None, u'\n            The street of the address.\n          ')

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'city'), 'city', '__httpgenologics_comri_address_city', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 18, 6), )

    
    city = property(__city.value, __city.set, None, u'\n            The city of the address.\n          ')

    
    # Element state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'state'), 'state', '__httpgenologics_comri_address_state', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 25, 6), )

    
    state = property(__state.value, __state.set, None, u'\n            The state of the address.\n          ')

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__httpgenologics_comri_address_country', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 32, 6), )

    
    country = property(__country.value, __country.set, None, u'\n            The country of the address.\n          ')

    
    # Element postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'postalCode'), 'postalCode', '__httpgenologics_comri_address_postalCode', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 39, 6), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, u'\n            The postal code of the address.\n          ')

    
    # Element institution uses Python identifier institution
    __institution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'institution'), 'institution', '__httpgenologics_comri_address_institution', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 46, 6), )

    
    institution = property(__institution.value, __institution.set, None, u'\n            The institution of the address.\n          ')

    
    # Element department uses Python identifier department
    __department = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'department'), 'department', '__httpgenologics_comri_address_department', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 53, 6), )

    
    department = property(__department.value, __department.set, None, u'\n            The department of the address.\n          ')

    _ElementMap.update({
        __street.name() : __street,
        __city.name() : __city,
        __state.name() : __state,
        __country.name() : __country,
        __postalCode.name() : __postalCode,
        __institution.name() : __institution,
        __department.name() : __department
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'address', address)


# Complex type {http://genologics.com/ri}links with content type ELEMENT_ONLY
class links_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of resource links.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'links')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 62, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link'), 'link', '__httpgenologics_comri_links__link', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 69, 6), )

    
    link = property(__link.value, __link.set, None, u'\n            Link provides a URI linking to the detailed representation of a resource.\n          ')

    _ElementMap.update({
        __link.name() : __link
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'links', links_)


# Complex type {http://genologics.com/ri}location with content type ELEMENT_ONLY
class location (pyxb.binding.basis.complexTypeDefinition):
    """
        <p>Location provides a URI linking to the detailed representation of a Container along with the well location within that Container.</p>
<p>Location is used by representations to describe their location within a Container. For example Artifact and
reagent use location to describe which Container they are located in.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'location')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 78, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container uses Python identifier container
    __container = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container'), 'container', '__httpgenologics_comri_location_container', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 87, 6), )

    
    container = property(__container.value, __container.set, None, u'\n            The Container for the location.\nThe Container element provides a URI linking to the detailed representation\nof the Container for the location.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpgenologics_comri_location_value', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 99, 6), )

    
    value_ = property(__value.value, __value.set, None, u'\n            Placement of Artifact in the Container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    _ElementMap.update({
        __container.name() : __container,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'location', location)


# Complex type {http://genologics.com/ri}container with content type EMPTY
class container (pyxb.binding.basis.complexTypeDefinition):
    """
        Container is a child element of location and provides a URI linking to the detailed representation
of the Container for the location.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'container')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 111, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comri_container_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 118, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 118, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comri_container_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 128, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 128, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'container', container)


# Complex type {http://genologics.com/ri}externalid with content type EMPTY
class externalid_ (pyxb.binding.basis.complexTypeDefinition):
    """
        An external id is a reference to an identifier in an external system that contains additional information
about a representation within the API.
<p>External id is supported on representations that contain links back to external systems.</p>
<p>External id consists of two different URI type elements: id and URI. ID is the URI referencing
the external system, and provides context and identification of the representation within that system. URI
is the URI within the system, and provides a means of looking up the representation that the external id
is associated with.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'externalid')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 139, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpgenologics_comri_externalid__id', pyxb.binding.datatypes.anyURI)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 151, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 151, 4)
    
    id = property(__id.value, __id.set, None, u'\n          A URI identifying the representation in an external system.\n<p>The form of the id URI can be either a URL or URN, but it must include\nsufficient information to identify both the external system and the representation\nwithin that system.</p>\n<p>For a URN, the namespace identifier component should identify the external system.</p>\n<p>For a URL, the URL should be an absolute URL and not a relative URL to identify the external system.</p>\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comri_externalid__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 163, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 163, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI providing a link to the detailed representation that is identified by the external id.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'externalid', externalid_)


# Complex type {http://genologics.com/ri}index with content type ELEMENT_ONLY
class index_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Index is the entry point to a supported version of the API, providing a list of links to the available resources in that version in the system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'index')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 171, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link'), 'link', '__httpgenologics_comri_index__link', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 178, 6), )

    
    link = property(__link.value, __link.set, None, u'\n            Each link provides a URI to an available resource in the system.\n          ')

    _ElementMap.update({
        __link.name() : __link
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'index', index_)


# Complex type {http://genologics.com/ri}link with content type EMPTY
class link (pyxb.binding.basis.complexTypeDefinition):
    """
        A link provides a URI linking to an additional resource.
<p>The link is modelled on the link element defined by the
<a href="http://atompub.org/rfc4287.html">Atom Syndication Format</a>. The link includes
a rel attribute that describes the URI of the link.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'link')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 187, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rel'), 'rel', '__httpgenologics_comri_link_rel', pyxb.binding.datatypes.string)
    __rel._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 196, 4)
    __rel._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 196, 4)
    
    rel = property(__rel.value, __rel.set, None, u'\n          The rel of the link.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comri_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 203, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 203, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the link.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rel.name() : __rel,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'link', link)


# Complex type {http://genologics.com/ri}page with content type EMPTY
class page (pyxb.binding.basis.complexTypeDefinition):
    """
        The link to a page of additional content.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
<p>The previous-page and next-page elements are represented using the page type.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'page')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 211, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comri_page_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 223, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 223, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI linking to the page of additional content.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'page', page)


links = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'links'), links_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', links.name().localName(), links)

index = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'index'), index_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', index.name().localName(), index)

externalid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'externalid'), externalid_, documentation=u'\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 231, 2))
Namespace.addCategoryObject('elementBinding', externalid.name().localName(), externalid)



address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'street'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The street of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 11, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'city'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The city of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 18, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'state'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The state of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 25, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'country'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The country of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 32, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'postalCode'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The postal code of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 39, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'institution'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The institution of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 46, 6)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'department'), pyxb.binding.datatypes.string, scope=address, documentation=u'\n            The department of the address.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 53, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 18, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 25, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 32, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 39, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 46, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 53, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'street')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'city')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 18, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'state')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 25, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'country')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 32, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'postalCode')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 39, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'institution')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 46, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(None, u'department')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 53, 6))
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
address._Automaton = _BuildAutomaton()




links_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link'), link, scope=links_, documentation=u'\n            Link provides a URI linking to the detailed representation of a resource.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 69, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 69, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(links_._UseForTag(pyxb.namespace.ExpandedName(None, u'link')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 69, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
links_._Automaton = _BuildAutomaton_()




location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container'), container, scope=location, documentation=u'\n            The Container for the location.\nThe Container element provides a URI linking to the detailed representation\nof the Container for the location.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 87, 6)))

location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'value'), pyxb.binding.datatypes.string, scope=location, documentation=u'\n            Placement of Artifact in the Container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 99, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 87, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 99, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(location._UseForTag(pyxb.namespace.ExpandedName(None, u'container')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 87, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(location._UseForTag(pyxb.namespace.ExpandedName(None, u'value')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 99, 6))
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
location._Automaton = _BuildAutomaton_2()




index_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link'), link, scope=index_, documentation=u'\n            Each link provides a URI to an available resource in the system.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 178, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 178, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(index_._UseForTag(pyxb.namespace.ExpandedName(None, u'link')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 178, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
index_._Automaton = _BuildAutomaton_3()

