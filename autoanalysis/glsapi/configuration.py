# ./configuration.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:189aea9f95ffa14f014fe0d42da96aec9cc76c08
# Generated 2014-03-06 16:48:15.141641 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/configuration [xmlns:cnf]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/configuration', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/configuration}field-type
class field_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The data types available for a user-defined field.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'field-type')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 213, 2)
    _Documentation = u'\n        The data types available for a user-defined field.\n      '
field_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=field_type, enum_prefix=None)
field_type.String = field_type._CF_enumeration.addEnumeration(unicode_value=u'String', tag=u'String')
field_type.Text = field_type._CF_enumeration.addEnumeration(unicode_value=u'Text', tag=u'Text')
field_type.Boolean = field_type._CF_enumeration.addEnumeration(unicode_value=u'Boolean', tag=u'Boolean')
field_type.Numeric = field_type._CF_enumeration.addEnumeration(unicode_value=u'Numeric', tag=u'Numeric')
field_type.Date = field_type._CF_enumeration.addEnumeration(unicode_value=u'Date', tag=u'Date')
field_type.URI = field_type._CF_enumeration.addEnumeration(unicode_value=u'URI', tag=u'URI')
field_type._InitializeFacetMap(field_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'field-type', field_type)

# Complex type {http://genologics.com/ri/configuration}type-definition with content type EMPTY
class type_definition (pyxb.binding.basis.complexTypeDefinition):
    """
        Type-definition provides a URI linking to the user defined type associated with the user-defined field, if applicable.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'type-definition')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 192, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_type_definition_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 198, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 198, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user defined type.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_type_definition_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 205, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 205, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user defined type.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'type-definition', type_definition)


# Complex type {http://genologics.com/ri/configuration}field-link with content type EMPTY
class field_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Field definition represents a user-defined field configured in the parent entity.
It includes the name and a URI linking to the detailed representation
of the configuration of a user defined field.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'field-link')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 228, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_field_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 236, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 236, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user-defined field.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_field_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 243, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 243, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI linking to the configuration of the user-defined field.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'field-link', field_link)


# Complex type {http://genologics.com/ri/configuration}type with content type ELEMENT_ONLY
class type_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of the configuration of a user defined type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'type')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 251, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field-definition uses Python identifier field_definition
    __field_definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'field-definition'), 'field_definition', '__httpgenologics_comriconfiguration_type__field_definition', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 258, 6), )

    
    field_definition = property(__field_definition.value, __field_definition.set, None, u'\n            Each field definition provides a URI linking to the detailed representation of the configuration of a user defined\nfield for the user defined type.\n          ')

    
    # Element attach-to-name uses Python identifier attach_to_name
    __attach_to_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attach-to-name'), 'attach_to_name', '__httpgenologics_comriconfiguration_type__attach_to_name', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 266, 6), )

    
    attach_to_name = property(__attach_to_name.value, __attach_to_name.set, None, u"\n            The item in the system that the User-Defined Type can be used with such as Sample, Project, Container\nor the name of a process.\nValues for this element can be divided into three categories: predefined values, dynamic values and unsupported/deprecated values.\n<p>\nPredefined values - predefined values are supported in the API and describe the kind of resource\nassociated with the user-defined type. The currently supported values are: Project, Sample, and Container.\n</p>\n<p>Dynamic values - a dynamic value is used for user-defined types configured on process types, and\ncorrespond to the process type name. When working with user-defined types on process types, the attach-to-category element must\nbe specified with a value of 'ProcessType'.</p>\n<p>Unsupported values - there are other values which associate user-defined types with other items in the data model.\nThese values may or may not correspond to the resources provided in the API. These values should not be relied on and may change\nin the future.</p>\n          ")

    
    # Element attach-to-category uses Python identifier attach_to_category
    __attach_to_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attach-to-category'), 'attach_to_category', '__httpgenologics_comriconfiguration_type__attach_to_category', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 285, 6), )

    
    attach_to_category = property(__attach_to_category.value, __attach_to_category.set, None, u'\n            Specifies whether the User-Defined Type can be used with processes. If you want the UDT applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDTs, do not specify an attach-to-category value.\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_type__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 295, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 295, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user defined type.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_type__uri', pyxb.binding.datatypes.string)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 302, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 302, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user defined type.\n        ')

    _ElementMap.update({
        __field_definition.name() : __field_definition,
        __attach_to_name.name() : __attach_to_name,
        __attach_to_category.name() : __attach_to_category
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'type', type_)


# Complex type {http://genologics.com/ri/configuration}udfs with content type ELEMENT_ONLY
class udfs_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of user defined field configuration links.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'udfs')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 310, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element udfconfig uses Python identifier udfconfig
    __udfconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'udfconfig'), 'udfconfig', '__httpgenologics_comriconfiguration_udfs__udfconfig', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 322, 6), )

    
    udfconfig = property(__udfconfig.value, __udfconfig.set, None, u'\n            Udfconfig provides a URI linking to the detailed representation of the configuration for a user defined field.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comriconfiguration_udfs__previous_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 329, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            Previous-page provides a URI linking to the previous page of user defined field configuration links.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comriconfiguration_udfs__next_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 336, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            Next-page provides a URI linking to the next page of user defined field configuration links.\n          ')

    _ElementMap.update({
        __udfconfig.name() : __udfconfig,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'udfs', udfs_)


# Complex type {http://genologics.com/ri/configuration}udfconfig-link with content type EMPTY
class udfconfig_link_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Udfconfig-link is a child element type of udfs and provides a URI linking to the detailed representation of the configuration for a user defined field.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'udfconfig-link')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 345, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_udfconfig_link__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 351, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 351, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user defined field configuration.\n        ')

    
    # Attribute attach-to-name uses Python identifier attach_to_name
    __attach_to_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attach-to-name'), 'attach_to_name', '__httpgenologics_comriconfiguration_udfconfig_link__attach_to_name', pyxb.binding.datatypes.string)
    __attach_to_name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 358, 4)
    __attach_to_name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 358, 4)
    
    attach_to_name = property(__attach_to_name.value, __attach_to_name.set, None, u'\n          The attach to name for the user defined field.\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_udfconfig_link__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 365, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 365, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user defined field.\n        ')

    
    # Attribute attach-to-category uses Python identifier attach_to_category
    __attach_to_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attach-to-category'), 'attach_to_category', '__httpgenologics_comriconfiguration_udfconfig_link__attach_to_category', pyxb.binding.datatypes.string)
    __attach_to_category._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 372, 4)
    __attach_to_category._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 372, 4)
    
    attach_to_category = property(__attach_to_category.value, __attach_to_category.set, None, u'\n          Specifies whether the User-Defined Field can be used with processes. If you want the UDF applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDFs, do not specify an attach-to-category value.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __attach_to_name.name() : __attach_to_name,
        __name.name() : __name,
        __attach_to_category.name() : __attach_to_category
    })
Namespace.addCategoryObject('typeBinding', u'udfconfig-link', udfconfig_link_)


# Complex type {http://genologics.com/ri/configuration}udts with content type ELEMENT_ONLY
class udts_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of user defined type configuration links.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'udts')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 382, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element udtconfig uses Python identifier udtconfig
    __udtconfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'udtconfig'), 'udtconfig', '__httpgenologics_comriconfiguration_udts__udtconfig', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 394, 6), )

    
    udtconfig = property(__udtconfig.value, __udtconfig.set, None, u'\n            Udtconfig provides a URI linking to the detailed representation of the configuration for a user defined type.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comriconfiguration_udts__previous_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 401, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            Previous-page provides a URI linking to the previous page of user defined type configuration links.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comriconfiguration_udts__next_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 408, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            Next-page provides a URI linking to the next page of user defined type configuration links.\n          ')

    _ElementMap.update({
        __udtconfig.name() : __udtconfig,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'udts', udts_)


# Complex type {http://genologics.com/ri/configuration}udtconfig-link with content type EMPTY
class udtconfig_link_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Udtconfig-link is a child element type of udts and provides a URI linking to the detailed representation of the configuration for a user defined type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'udtconfig-link')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 417, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_udtconfig_link__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 423, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 423, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user defined type configuration.\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_udtconfig_link__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 430, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 430, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the user defined type.\n        ')

    
    # Attribute attach-to-name uses Python identifier attach_to_name
    __attach_to_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attach-to-name'), 'attach_to_name', '__httpgenologics_comriconfiguration_udtconfig_link__attach_to_name', pyxb.binding.datatypes.string)
    __attach_to_name._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 437, 4)
    __attach_to_name._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 437, 4)
    
    attach_to_name = property(__attach_to_name.value, __attach_to_name.set, None, u'\n          The attach to name for the user defined field.\n        ')

    
    # Attribute attach-to-category uses Python identifier attach_to_category
    __attach_to_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'attach-to-category'), 'attach_to_category', '__httpgenologics_comriconfiguration_udtconfig_link__attach_to_category', pyxb.binding.datatypes.string)
    __attach_to_category._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 444, 4)
    __attach_to_category._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 444, 4)
    
    attach_to_category = property(__attach_to_category.value, __attach_to_category.set, None, u'\n          Specifies whether the User-Defined Type can be used with processes. If you want the UDT applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDTs, do not specify an attach-to-category value.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name,
        __attach_to_name.name() : __attach_to_name,
        __attach_to_category.name() : __attach_to_category
    })
Namespace.addCategoryObject('typeBinding', u'udtconfig-link', udtconfig_link_)


# Complex type {http://genologics.com/ri/configuration}field with content type ELEMENT_ONLY
class field_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of the configuration of a user-defined field.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'field')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriconfiguration_field__name', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 16, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the user-defined field.\n          ')

    
    # Element attach-to-name uses Python identifier attach_to_name
    __attach_to_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attach-to-name'), 'attach_to_name', '__httpgenologics_comriconfiguration_field__attach_to_name', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 23, 6), )

    
    attach_to_name = property(__attach_to_name.value, __attach_to_name.set, None, u"\n            The item in the system that the User-Defined Field can be used with such as Sample, Project, Container\nor the name of a process.\nValues for this element can be divided into three categories: predefined values, dynamic values and unsupported/deprecated values.\n<p>\nPredefined values - predefined values are supported in the API and describe the kind of resource\nassociated with the user-defined field. The currently supported values are: Project, Sample, Analyte, ResultFile and Container.\n</p>\n<p>Dynamic values - a dynamic value is used for user-defined fields configured on process types, and\ncorrespond to the process type name. When working with user-defined fields on process types, the attach-to-category element must\nbe specified with a value of 'ProcessType'.</p>\n<p>Unsupported values - there are other values which associate user-defined fields with other items in the data model.\nThese values may or may not correspond to the resources provided in the API. These values should not be relied on and may change\nin the future.</p>\n          ")

    
    # Element precision uses Python identifier precision
    __precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'precision'), 'precision', '__httpgenologics_comriconfiguration_field__precision', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 42, 6), )

    
    precision = property(__precision.value, __precision.set, None, u'\n            The number of decimal places used when displaying numeric values.\n<p>Only numeric user-defined fields support precision.</p>\n          ')

    
    # Element unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__httpgenologics_comriconfiguration_field__unit', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 50, 6), )

    
    unit = property(__unit.value, __unit.set, None, u'\n            The unit of measurement associated with the user-defined field.\n<p>Only numeric user-defined fields support units.</p>\n          ')

    
    # Element type-definition uses Python identifier type_definition
    __type_definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'type-definition'), 'type_definition', '__httpgenologics_comriconfiguration_field__type_definition', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 58, 6), )

    
    type_definition = property(__type_definition.value, __type_definition.set, None, u'\n            Type-definition provides a URI linking to the user-defined type associated with the User-Defined Field.\nThis will only be populated if the UDF has been configured for a UDT.\n          ')

    
    # Element show-in-lablink uses Python identifier show_in_lablink
    __show_in_lablink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'show-in-lablink'), 'show_in_lablink', '__httpgenologics_comriconfiguration_field__show_in_lablink', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 66, 6), )

    
    show_in_lablink = property(__show_in_lablink.value, __show_in_lablink.set, None, u'\n            Specifies whether the user-defined field is displayed in LabLink.\n          ')

    
    # Element allow-non-preset-values uses Python identifier allow_non_preset_values
    __allow_non_preset_values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'allow-non-preset-values'), 'allow_non_preset_values', '__httpgenologics_comriconfiguration_field__allow_non_preset_values', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 73, 6), )

    
    allow_non_preset_values = property(__allow_non_preset_values.value, __allow_non_preset_values.set, None, u'\n            Specifies whether the User-Defined Field can accept manually-entered values or preset values.\n          ')

    
    # Element first-preset-is-default-value uses Python identifier first_preset_is_default_value
    __first_preset_is_default_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'first-preset-is-default-value'), 'first_preset_is_default_value', '__httpgenologics_comriconfiguration_field__first_preset_is_default_value', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 80, 6), )

    
    first_preset_is_default_value = property(__first_preset_is_default_value.value, __first_preset_is_default_value.set, None, u'\n            Specifies that when multiple preset values are entered for a User-Defined Field, the first preset value is selected by default.\n          ')

    
    # Element show-in-tables uses Python identifier show_in_tables
    __show_in_tables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'show-in-tables'), 'show_in_tables', '__httpgenologics_comriconfiguration_field__show_in_tables', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 87, 6), )

    
    show_in_tables = property(__show_in_tables.value, __show_in_tables.set, None, u'\n            Specifies whether the user-defined field is added to a column when information is displayed in a table in the LIMS.\n          ')

    
    # Element is-editable uses Python identifier is_editable
    __is_editable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-editable'), 'is_editable', '__httpgenologics_comriconfiguration_field__is_editable', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 94, 6), )

    
    is_editable = property(__is_editable.value, __is_editable.set, None, u'\n            When working with user-defined field associated with the outputs of a process, this option allows users to manually change UDF values.\n          ')

    
    # Element is-deviation uses Python identifier is_deviation
    __is_deviation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-deviation'), 'is_deviation', '__httpgenologics_comriconfiguration_field__is_deviation', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 101, 6), )

    
    is_deviation = property(__is_deviation.value, __is_deviation.set, None, u'\n            Specifies whether the User-Defined Field contains a deviation value.\n<p>When working with deviations, two values are collected for the user-defined field (parent-uri and child-uri).</p>\n<p>Only numeric user-defined fields support deviation</p>\n          ')

    
    # Element is-controlled-vocabulary uses Python identifier is_controlled_vocabulary
    __is_controlled_vocabulary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-controlled-vocabulary'), 'is_controlled_vocabulary', '__httpgenologics_comriconfiguration_field__is_controlled_vocabulary', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 110, 6), )

    
    is_controlled_vocabulary = property(__is_controlled_vocabulary.value, __is_controlled_vocabulary.set, None, u'\n            Specifies whether the user-defined field contains preset values that adhere to a hierarchical set of terms.\n          ')

    
    # Element parent-uri uses Python identifier parent_uri
    __parent_uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'parent-uri'), 'parent_uri', '__httpgenologics_comriconfiguration_field__parent_uri', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 117, 6), )

    
    parent_uri = property(__parent_uri.value, __parent_uri.set, None, u"\n            Parent-uri provides a URI linking to the parent user-defined field for the UDF.\n<p>Parent-uri is used to support standard deviation for numeric user-defined fields With standard deviation,\nthe numeric value will be stored in the parent user-defined field, and the deviation value will be stored in the\nchild user-defined field. The child user-defined field's is-deviation flag will be true.</p>\n          ")

    
    # Element child-uri uses Python identifier child_uri
    __child_uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'child-uri'), 'child_uri', '__httpgenologics_comriconfiguration_field__child_uri', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 127, 6), )

    
    child_uri = property(__child_uri.value, __child_uri.set, None, u"\n            Child-uri provides a URI linking to any child user-defined fields for the user-defined field.\n<p>Child-uri is used to support standard deviation for numeric user-defined fields. With standard deviation,\nthe numeric value will be stored in the parent user-defined field, and the deviation value will be in the\nchild user-defined field. The child user-defined field's is-deviation flag will be true.</p>\n          ")

    
    # Element preset uses Python identifier preset
    __preset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'preset'), 'preset', '__httpgenologics_comriconfiguration_field__preset', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 137, 6), )

    
    preset = property(__preset.value, __preset.set, None, u'\n            Displays preset values associated with the user-defined field.\n          ')

    
    # Element min-value uses Python identifier min_value
    __min_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'min-value'), 'min_value', '__httpgenologics_comriconfiguration_field__min_value', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 144, 6), )

    
    min_value = property(__min_value.value, __min_value.set, None, u'\n            The minimum value for the user-defined field. This is the lowest value that can be recorded for the UDF.\n<p>Only numeric user-defined fields support minValue.</p>\n          ')

    
    # Element max-value uses Python identifier max_value
    __max_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'max-value'), 'max_value', '__httpgenologics_comriconfiguration_field__max_value', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 152, 6), )

    
    max_value = property(__max_value.value, __max_value.set, None, u'\n            The maximum value for the user-defined field. This is the highest value that can be recorded for the UDF.\n<p>Only numeric type user-defined fields support minValue.</p>\n          ')

    
    # Element is-required uses Python identifier is_required
    __is_required = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-required'), 'is_required', '__httpgenologics_comriconfiguration_field__is_required', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 160, 6), )

    
    is_required = property(__is_required.value, __is_required.set, None, u'\n            Specifies whether the user-defined field is a mandatory field.\n          ')

    
    # Element attach-to-category uses Python identifier attach_to_category
    __attach_to_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attach-to-category'), 'attach_to_category', '__httpgenologics_comriconfiguration_field__attach_to_category', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 167, 6), )

    
    attach_to_category = property(__attach_to_category.value, __attach_to_category.set, None, u'\n            Specifies whether the User-Defined Field can be used with processes. If you want the UDF applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDFs, do not specify an attach-to-category value.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comriconfiguration_field__type', field_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 177, 4)
    __type._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 177, 4)
    
    type = property(__type.value, __type.set, None, u'\n          The type of user-defined field.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriconfiguration_field__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 184, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 184, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user-defined field.\n        ')

    _ElementMap.update({
        __name.name() : __name,
        __attach_to_name.name() : __attach_to_name,
        __precision.name() : __precision,
        __unit.name() : __unit,
        __type_definition.name() : __type_definition,
        __show_in_lablink.name() : __show_in_lablink,
        __allow_non_preset_values.name() : __allow_non_preset_values,
        __first_preset_is_default_value.name() : __first_preset_is_default_value,
        __show_in_tables.name() : __show_in_tables,
        __is_editable.name() : __is_editable,
        __is_deviation.name() : __is_deviation,
        __is_controlled_vocabulary.name() : __is_controlled_vocabulary,
        __parent_uri.name() : __parent_uri,
        __child_uri.name() : __child_uri,
        __preset.name() : __preset,
        __min_value.name() : __min_value,
        __max_value.name() : __max_value,
        __is_required.name() : __is_required,
        __attach_to_category.name() : __attach_to_category
    })
    _AttributeMap.update({
        __type.name() : __type,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'field', field_)


type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), type_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', type.name().localName(), type)

udfs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'udfs'), udfs_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', udfs.name().localName(), udfs)

udfconfig_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'udfconfig-link'), udfconfig_link_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', udfconfig_link.name().localName(), udfconfig_link)

udts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'udts'), udts_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', udts.name().localName(), udts)

udtconfig_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'udtconfig-link'), udtconfig_link_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', udtconfig_link.name().localName(), udtconfig_link)

field = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'field'), field_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', field.name().localName(), field)



type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'field-definition'), field_link, scope=type_, documentation=u'\n            Each field definition provides a URI linking to the detailed representation of the configuration of a user defined\nfield for the user defined type.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 258, 6)))

type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attach-to-name'), pyxb.binding.datatypes.string, scope=type_, documentation=u"\n            The item in the system that the User-Defined Type can be used with such as Sample, Project, Container\nor the name of a process.\nValues for this element can be divided into three categories: predefined values, dynamic values and unsupported/deprecated values.\n<p>\nPredefined values - predefined values are supported in the API and describe the kind of resource\nassociated with the user-defined type. The currently supported values are: Project, Sample, and Container.\n</p>\n<p>Dynamic values - a dynamic value is used for user-defined types configured on process types, and\ncorrespond to the process type name. When working with user-defined types on process types, the attach-to-category element must\nbe specified with a value of 'ProcessType'.</p>\n<p>Unsupported values - there are other values which associate user-defined types with other items in the data model.\nThese values may or may not correspond to the resources provided in the API. These values should not be relied on and may change\nin the future.</p>\n          ", location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 266, 6)))

type_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attach-to-category'), pyxb.binding.datatypes.string, scope=type_, documentation=u'\n            Specifies whether the User-Defined Type can be used with processes. If you want the UDT applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDTs, do not specify an attach-to-category value.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 285, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 258, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 266, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 285, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(type_._UseForTag(pyxb.namespace.ExpandedName(None, u'field-definition')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 258, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(type_._UseForTag(pyxb.namespace.ExpandedName(None, u'attach-to-name')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 266, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(type_._UseForTag(pyxb.namespace.ExpandedName(None, u'attach-to-category')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 285, 6))
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
type_._Automaton = _BuildAutomaton()




udfs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'udfconfig'), udfconfig_link_, scope=udfs_, documentation=u'\n            Udfconfig provides a URI linking to the detailed representation of the configuration for a user defined field.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 322, 6)))

udfs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=udfs_, documentation=u'\n            Previous-page provides a URI linking to the previous page of user defined field configuration links.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 329, 6)))

udfs_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=udfs_, documentation=u'\n            Next-page provides a URI linking to the next page of user defined field configuration links.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 336, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 322, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 329, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 336, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(udfs_._UseForTag(pyxb.namespace.ExpandedName(None, u'udfconfig')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 322, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(udfs_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 329, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(udfs_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 336, 6))
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
udfs_._Automaton = _BuildAutomaton_()




udts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'udtconfig'), udtconfig_link_, scope=udts_, documentation=u'\n            Udtconfig provides a URI linking to the detailed representation of the configuration for a user defined type.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 394, 6)))

udts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=udts_, documentation=u'\n            Previous-page provides a URI linking to the previous page of user defined type configuration links.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 401, 6)))

udts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=udts_, documentation=u'\n            Next-page provides a URI linking to the next page of user defined type configuration links.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 408, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 394, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 401, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 408, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(udts_._UseForTag(pyxb.namespace.ExpandedName(None, u'udtconfig')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 394, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(udts_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 401, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(udts_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 408, 6))
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
udts_._Automaton = _BuildAutomaton_2()




field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=field_, documentation=u'\n            The name of the user-defined field.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 16, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attach-to-name'), pyxb.binding.datatypes.string, scope=field_, documentation=u"\n            The item in the system that the User-Defined Field can be used with such as Sample, Project, Container\nor the name of a process.\nValues for this element can be divided into three categories: predefined values, dynamic values and unsupported/deprecated values.\n<p>\nPredefined values - predefined values are supported in the API and describe the kind of resource\nassociated with the user-defined field. The currently supported values are: Project, Sample, Analyte, ResultFile and Container.\n</p>\n<p>Dynamic values - a dynamic value is used for user-defined fields configured on process types, and\ncorrespond to the process type name. When working with user-defined fields on process types, the attach-to-category element must\nbe specified with a value of 'ProcessType'.</p>\n<p>Unsupported values - there are other values which associate user-defined fields with other items in the data model.\nThese values may or may not correspond to the resources provided in the API. These values should not be relied on and may change\nin the future.</p>\n          ", location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 23, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'precision'), pyxb.binding.datatypes.int, scope=field_, documentation=u'\n            The number of decimal places used when displaying numeric values.\n<p>Only numeric user-defined fields support precision.</p>\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 42, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'unit'), pyxb.binding.datatypes.string, scope=field_, documentation=u'\n            The unit of measurement associated with the user-defined field.\n<p>Only numeric user-defined fields support units.</p>\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 50, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'type-definition'), type_definition, scope=field_, documentation=u'\n            Type-definition provides a URI linking to the user-defined type associated with the User-Defined Field.\nThis will only be populated if the UDF has been configured for a UDT.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 58, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'show-in-lablink'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the user-defined field is displayed in LabLink.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 66, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'allow-non-preset-values'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the User-Defined Field can accept manually-entered values or preset values.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 73, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'first-preset-is-default-value'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies that when multiple preset values are entered for a User-Defined Field, the first preset value is selected by default.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 80, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'show-in-tables'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the user-defined field is added to a column when information is displayed in a table in the LIMS.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 87, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-editable'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            When working with user-defined field associated with the outputs of a process, this option allows users to manually change UDF values.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 94, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-deviation'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the User-Defined Field contains a deviation value.\n<p>When working with deviations, two values are collected for the user-defined field (parent-uri and child-uri).</p>\n<p>Only numeric user-defined fields support deviation</p>\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 101, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-controlled-vocabulary'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the user-defined field contains preset values that adhere to a hierarchical set of terms.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 110, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'parent-uri'), pyxb.binding.datatypes.anyURI, scope=field_, documentation=u"\n            Parent-uri provides a URI linking to the parent user-defined field for the UDF.\n<p>Parent-uri is used to support standard deviation for numeric user-defined fields With standard deviation,\nthe numeric value will be stored in the parent user-defined field, and the deviation value will be stored in the\nchild user-defined field. The child user-defined field's is-deviation flag will be true.</p>\n          ", location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 117, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'child-uri'), pyxb.binding.datatypes.string, scope=field_, documentation=u"\n            Child-uri provides a URI linking to any child user-defined fields for the user-defined field.\n<p>Child-uri is used to support standard deviation for numeric user-defined fields. With standard deviation,\nthe numeric value will be stored in the parent user-defined field, and the deviation value will be in the\nchild user-defined field. The child user-defined field's is-deviation flag will be true.</p>\n          ", location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 127, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'preset'), pyxb.binding.datatypes.string, scope=field_, documentation=u'\n            Displays preset values associated with the user-defined field.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 137, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'min-value'), pyxb.binding.datatypes.double, scope=field_, documentation=u'\n            The minimum value for the user-defined field. This is the lowest value that can be recorded for the UDF.\n<p>Only numeric user-defined fields support minValue.</p>\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 144, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'max-value'), pyxb.binding.datatypes.double, scope=field_, documentation=u'\n            The maximum value for the user-defined field. This is the highest value that can be recorded for the UDF.\n<p>Only numeric type user-defined fields support minValue.</p>\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 152, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-required'), pyxb.binding.datatypes.boolean, scope=field_, documentation=u'\n            Specifies whether the user-defined field is a mandatory field.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 160, 6)))

field_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attach-to-category'), pyxb.binding.datatypes.string, scope=field_, documentation=u'\n            Specifies whether the User-Defined Field can be used with processes. If you want the UDF applied to a\nprocess, specify a value of ProcessType, and for the attach-to-name element, specify the name of the\nprocess. For all other UDFs, do not specify an attach-to-category value.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 167, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 16, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 23, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 42, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 50, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 58, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 66, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 73, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 80, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 87, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 94, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 101, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 110, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 117, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 127, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 137, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 144, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 152, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 160, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 167, 6))
    counters.add(cc_18)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'attach-to-name')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'precision')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 42, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'unit')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'type-definition')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 58, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'show-in-lablink')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 66, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'allow-non-preset-values')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 73, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'first-preset-is-default-value')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 80, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'show-in-tables')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 87, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-editable')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 94, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-deviation')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 101, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-controlled-vocabulary')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 110, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'parent-uri')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 117, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'child-uri')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 127, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'preset')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 137, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'min-value')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 144, 6))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'max-value')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 152, 6))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-required')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 160, 6))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(field_._UseForTag(pyxb.namespace.ExpandedName(None, u'attach-to-category')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/configuration.xsd', 167, 6))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
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
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
field_._Automaton = _BuildAutomaton_3()

