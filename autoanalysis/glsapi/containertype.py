# ./containertype.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8d231f4d4f3ec59c26bf3cf217bda8d9ae3bbf1c
# Generated 2014-03-06 16:48:15.154029 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/containertype

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
import ri as _ImportedBinding_ri
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/containertype', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/containertype}unavailable-well
class unavailable_well (pyxb.binding.datatypes.string):

    """
        Unavailable-well is a child element of container type and identifies a well location that
cannot be used by containers of the container type to store artifacts or reagents.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unavailable-well')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 176, 2)
    _Documentation = u'\n        Unavailable-well is a child element of container type and identifies a well location that\ncannot be used by containers of the container type to store artifacts or reagents.\n      '
unavailable_well._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'unavailable-well', unavailable_well)

# Complex type {http://genologics.com/ri/containertype}container-type with content type ELEMENT_ONLY
class container_type_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a container type.
<p>The container type describes the physical characteristics of a class of containers such as
the number of wells in the container as well as describing the coordinate system used for identifying
those wells.</p>
<p>The container type is described using a rectangular coordinate system. The
characteristics of the horizontal axis are described by the x-dimension element, and the characteristics
of the vertical dimension are described by the y-dimension child elements. The characteristics of
each dimension included both the size in that dimension as well as the identification method for
values in that dimension. Values can be identified either numerically where 0 is the first item or
alphabetically where A is the first element. Additionally an offset can be specified which shifts the
value of the first element by a fixed amount. When a well location is represented using the coordinate
system, it is shown as Y-Value:X-Value (for example A:1).<p>
<p>The following are examples of the coordinate system:<p>
<ul>
<li>Y-Dimension: alphabetic, size 1, offset 0. X-Dimension: numeric, size 1, offset 0. Size: 1. Valid value: A:0</li>
<li>Y-Dimension: alphabetic, size 12, offset 0. X-Dimension: numeric, size 8, offset 0. Size: 96. Valid values: A:0 ... L:7</li>
<li>Y-Dimension: alphabetic, size 8, offset 0. X-Dimension: numeric, size 12, offset 1. Size: 96. Valid values: A:1 ... H:12</li>
</ul>
<p>The container type also identifies wells in the container that are not available for storing
samples or reagents, either because the configuration of the container requires those wells to
be empty for the instrument configuration or because the well contains specific calibrants that
are required by the instrument. The well location of the calibrant or unavailable wells is specified
using the coordinate system that is described by the x-dimension and y-dimension of the container
type.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'container-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element is-tube uses Python identifier is_tube
    __is_tube = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-tube'), 'is_tube', '__httpgenologics_comricontainertype_container_type__is_tube', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 35, 6), )

    
    is_tube = property(__is_tube.value, __is_tube.set, None, u'\n            is-tube describes if this container-type should be treated as a tube in the client interface.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element calibrant-well uses Python identifier calibrant_well
    __calibrant_well = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'calibrant-well'), 'calibrant_well', '__httpgenologics_comricontainertype_container_type__calibrant_well', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 45, 6), )

    
    calibrant_well = property(__calibrant_well.value, __calibrant_well.set, None, u'\n            Deprecated, this property is no longer supported.\nEach calibrant well identifies a well location that is reserved for calibrants in containers of the container type.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element unavailable-well uses Python identifier unavailable_well
    __unavailable_well = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'unavailable-well'), 'unavailable_well', '__httpgenologics_comricontainertype_container_type__unavailable_well', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 56, 6), )

    
    unavailable_well = property(__unavailable_well.value, __unavailable_well.set, None, u'\n            Each unavailable well identifies a well location that cannot be used by containers of the container type to store artifacts or reagents.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element x-dimension uses Python identifier x_dimension
    __x_dimension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'x-dimension'), 'x_dimension', '__httpgenologics_comricontainertype_container_type__x_dimension', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 66, 6), )

    
    x_dimension = property(__x_dimension.value, __x_dimension.set, None, u'\n            X-dimension describes the size and identification method of the horizontal axis of the coordinate system for the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element y-dimension uses Python identifier y_dimension
    __y_dimension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'y-dimension'), 'y_dimension', '__httpgenologics_comricontainertype_container_type__y_dimension', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 76, 6), )

    
    y_dimension = property(__y_dimension.value, __y_dimension.set, None, u'\n            Y-dimension describes the size and identification method of the vertical axis of the coordinate system for the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comricontainertype_container_type__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 87, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 87, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comricontainertype_container_type__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 97, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 97, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __is_tube.name() : __is_tube,
        __calibrant_well.name() : __calibrant_well,
        __unavailable_well.name() : __unavailable_well,
        __x_dimension.name() : __x_dimension,
        __y_dimension.name() : __y_dimension
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'container-type', container_type_)


# Complex type {http://genologics.com/ri/containertype}calibrant-well with content type SIMPLE
class calibrant_well (pyxb.binding.basis.complexTypeDefinition):
    """
        Deprecated, this property is no longer supported.
Calibrant-well is a child element of container type and identifies a well location that is
reserved for calibrants in containers of the container type.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calibrant-well')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 108, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comricontainertype_calibrant_well_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 118, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 118, 8)
    
    name = property(__name.value, __name.set, None, u'\n              The name of the calibrant in the well.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'calibrant-well', calibrant_well)


# Complex type {http://genologics.com/ri/containertype}dimension with content type ELEMENT_ONLY
class dimension (pyxb.binding.basis.complexTypeDefinition):
    """
        Dimension is a child element of container type and describes the size and identification method
of the horizontal and vertical dimensions of the coordinate system of the container type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dimension')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 131, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element is-alpha uses Python identifier is_alpha
    __is_alpha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-alpha'), 'is_alpha', '__httpgenologics_comricontainertype_dimension_is_alpha', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 139, 6), )

    
    is_alpha = property(__is_alpha.value, __is_alpha.set, None, u'\n            The is-alpha flag is used for identifying well location.\n<p>When is-alpha is true, the component of the well location from the dimension is represented\nusing letters where A is the first value. Whe is-alpha is false, the component of the well\nlocation from the dimension is represented using numbers where 0 is the first value.</p>\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'offset'), 'offset', '__httpgenologics_comricontainertype_dimension_offset', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 152, 6), )

    
    offset = property(__offset.value, __offset.set, None, u'\n            The offset of this dimension.\n<p>If is-alpha is true, the system\nwill ignore any value provided for POST and use 0 for alpha offset.</p>\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__httpgenologics_comricontainertype_dimension_size', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 164, 6), )

    
    size = property(__size.value, __size.set, None, u'\n            The size of this dimension, 1-100\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ')

    _ElementMap.update({
        __is_alpha.name() : __is_alpha,
        __offset.name() : __offset,
        __size.name() : __size
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'dimension', dimension)


# Complex type {http://genologics.com/ri/containertype}container-types with content type ELEMENT_ONLY
class container_types_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation for a list of container type links.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'container-types')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 185, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container-type uses Python identifier container_type
    __container_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container-type'), 'container_type', '__httpgenologics_comricontainertype_container_types__container_type', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 197, 6), )

    
    container_type = property(__container_type.value, __container_type.set, None, u'\n            Container-type provides a URI linking to the detailed representation of a container type.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comricontainertype_container_types__previous_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 204, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            When working with large lists of container types,\nthe previous-page element provides a URI that links to the previous page of container types.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comricontainertype_container_types__next_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 212, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            When working with large lists of container types,\nthe next-page element provides a URI that links to the next page of container types.\n          ')

    _ElementMap.update({
        __container_type.name() : __container_type,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'container-types', container_types_)


# Complex type {http://genologics.com/ri/containertype}container-type-link with content type EMPTY
class container_type_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Container-type-link is a child element type of containers and provides a URI linking to the detailed representation of a container type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'container-type-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 222, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comricontainertype_container_type_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 228, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 228, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the container type.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comricontainertype_container_type_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 235, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 235, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the container type.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'container-type-link', container_type_link)


container_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'container-type'), container_type_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', container_type.name().localName(), container_type)

container_types = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'container-types'), container_types_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', container_types.name().localName(), container_types)



container_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-tube'), pyxb.binding.datatypes.boolean, scope=container_type_, documentation=u'\n            is-tube describes if this container-type should be treated as a tube in the client interface.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 35, 6)))

container_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'calibrant-well'), calibrant_well, scope=container_type_, documentation=u'\n            Deprecated, this property is no longer supported.\nEach calibrant well identifies a well location that is reserved for calibrants in containers of the container type.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 45, 6)))

container_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'unavailable-well'), unavailable_well, scope=container_type_, documentation=u'\n            Each unavailable well identifies a well location that cannot be used by containers of the container type to store artifacts or reagents.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 56, 6)))

container_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'x-dimension'), dimension, scope=container_type_, documentation=u'\n            X-dimension describes the size and identification method of the horizontal axis of the coordinate system for the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 66, 6)))

container_type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'y-dimension'), dimension, scope=container_type_, documentation=u'\n            Y-dimension describes the size and identification method of the vertical axis of the coordinate system for the container type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 76, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 45, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 56, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 76, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(container_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-tube')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(container_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'calibrant-well')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 45, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(container_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'unavailable-well')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 56, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(container_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'x-dimension')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(container_type_._UseForTag(pyxb.namespace.ExpandedName(None, u'y-dimension')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 76, 6))
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
container_type_._Automaton = _BuildAutomaton()




dimension._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-alpha'), pyxb.binding.datatypes.boolean, scope=dimension, documentation=u'\n            The is-alpha flag is used for identifying well location.\n<p>When is-alpha is true, the component of the well location from the dimension is represented\nusing letters where A is the first value. Whe is-alpha is false, the component of the well\nlocation from the dimension is represented using numbers where 0 is the first value.</p>\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 139, 6)))

dimension._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'offset'), pyxb.binding.datatypes.int, scope=dimension, documentation=u'\n            The offset of this dimension.\n<p>If is-alpha is true, the system\nwill ignore any value provided for POST and use 0 for alpha offset.</p>\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 152, 6)))

dimension._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'size'), pyxb.binding.datatypes.int, scope=dimension, documentation=u'\n            The size of this dimension, 1-100\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 164, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 139, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 152, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 164, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dimension._UseForTag(pyxb.namespace.ExpandedName(None, u'is-alpha')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 139, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dimension._UseForTag(pyxb.namespace.ExpandedName(None, u'offset')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 152, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(dimension._UseForTag(pyxb.namespace.ExpandedName(None, u'size')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 164, 6))
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
dimension._Automaton = _BuildAutomaton_()




container_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container-type'), container_type_link, scope=container_types_, documentation=u'\n            Container-type provides a URI linking to the detailed representation of a container type.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 197, 6)))

container_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=container_types_, documentation=u'\n            When working with large lists of container types,\nthe previous-page element provides a URI that links to the previous page of container types.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 204, 6)))

container_types_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=container_types_, documentation=u'\n            When working with large lists of container types,\nthe next-page element provides a URI that links to the next page of container types.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 212, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 197, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 204, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 212, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(container_types_._UseForTag(pyxb.namespace.ExpandedName(None, u'container-type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 197, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(container_types_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 204, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(container_types_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/containertype.xsd', 212, 6))
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
container_types_._Automaton = _BuildAutomaton_2()

