# ./project.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:05d18cd4162daf503adc481b4ebccd22986053ca
# Generated 2014-04-04 17:46:47.254649 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/project

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b568e09c-bc18-11e3-b84b-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import file as _ImportedBinding_file
import userdefined as _ImportedBinding_userdefined
import pyxb.binding.datatypes
import ri as _ImportedBinding_ri

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/project', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ri = _ImportedBinding_ri.Namespace
_Namespace_ri.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_file = _ImportedBinding_file.Namespace
_Namespace_file.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_udf = _ImportedBinding_userdefined.Namespace
_Namespace_udf.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://genologics.com/ri/project}project with content type ELEMENT_ONLY
class project_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Project.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'project')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://genologics.com/ri}externalid uses Python identifier externalid
    __externalid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid'), 'externalid', '__httpgenologics_comriproject_project__httpgenologics_comriexternalid', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 231, 2), )

    
    externalid = property(__externalid.value, __externalid.set, None, u'\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ')

    
    # Element {http://genologics.com/ri/file}file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), 'file', '__httpgenologics_comriproject_project__httpgenologics_comrifilefile', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2), )

    
    file = property(__file.value, __file.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriproject_project__name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 14, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element open-date uses Python identifier open_date
    __open_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'open-date'), 'open_date', '__httpgenologics_comriproject_project__open_date', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 26, 6), )

    
    open_date = property(__open_date.value, __open_date.set, None, u'\n            The open date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless a close date is also provided.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless a close date is also provided.\n          ')

    
    # Element close-date uses Python identifier close_date
    __close_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'close-date'), 'close_date', '__httpgenologics_comriproject_project__close_date', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 38, 6), )

    
    close_date = property(__close_date.value, __close_date.set, None, u'\n            The close date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element invoice-date uses Python identifier invoice_date
    __invoice_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'invoice-date'), 'invoice_date', '__httpgenologics_comriproject_project__invoice_date', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 50, 6), )

    
    invoice_date = property(__invoice_date.value, __invoice_date.set, None, u'\n            The invoice date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element researcher uses Python identifier researcher
    __researcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'researcher'), 'researcher', '__httpgenologics_comriproject_project__researcher', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 62, 6), )

    
    researcher = property(__researcher.value, __researcher.set, None, u'\n            Researcher provides a URI linking to the detailed representation of the Researcher for the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), 'field', '__httpgenologics_comriproject_project__httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Element {http://genologics.com/ri/userdefined}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), 'type', '__httpgenologics_comriproject_project__httpgenologics_comriuserdefinedtype', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2), )

    
    type = property(__type.value, __type.set, None, u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriproject_project__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 123, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 123, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriproject_project__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 135, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 135, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __externalid.name() : __externalid,
        __file.name() : __file,
        __name.name() : __name,
        __open_date.name() : __open_date,
        __close_date.name() : __close_date,
        __invoice_date.name() : __invoice_date,
        __researcher.name() : __researcher,
        __field.name() : __field,
        __type.name() : __type
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'project', project_)


# Complex type {http://genologics.com/ri/project}researcher with content type EMPTY
class researcher (pyxb.binding.basis.complexTypeDefinition):
    """
        Researcher is a child element of Project and provides a URI linking to the detailed representation of the Researcher for the Project.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'researcher')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 148, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriproject_researcher_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 154, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 154, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Researcher.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'researcher', researcher)


# Complex type {http://genologics.com/ri/project}projects with content type ELEMENT_ONLY
class projects_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of project links.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'projects')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 167, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element project uses Python identifier project
    __project = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'project'), 'project', '__httpgenologics_comriproject_projects__project', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 179, 6), )

    
    project = property(__project.value, __project.set, None, u'\n            Project provides a URI linking to the detailed representation of a project.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comriproject_projects__previous_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 186, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            When working with large lists of projects,\nthe previous-page element provides a URI that links to the previous page of projects.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comriproject_projects__next_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 194, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            When working with large lists of projects,\nthe next-page element provides a URI that links to the next page of projects.\n          ')

    _ElementMap.update({
        __project.name() : __project,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'projects', projects_)


# Complex type {http://genologics.com/ri/project}project-link with content type ELEMENT_ONLY
class project_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Project-link is a child element type of projects and provides a URI linking to the detailed representation of a project.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'project-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 204, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriproject_project_link_name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 211, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the project.\n          ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriproject_project_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 219, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 219, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMSID of the project.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriproject_project_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 226, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 226, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the project.\n        ')

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'project-link', project_link)


project = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'project'), project_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', project.name().localName(), project)

projects = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'projects'), projects_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', projects.name().localName(), projects)



project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid'), _ImportedBinding_ri.externalid_, scope=project_, documentation=u'\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 231, 2)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), _ImportedBinding_file.file_, scope=project_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=project_, documentation=u'\n            The name of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 14, 6)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'open-date'), pyxb.binding.datatypes.string, scope=project_, documentation=u'\n            The open date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless a close date is also provided.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless a close date is also provided.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 26, 6)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'close-date'), pyxb.binding.datatypes.string, scope=project_, documentation=u'\n            The close date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 38, 6)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'invoice-date'), pyxb.binding.datatypes.string, scope=project_, documentation=u'\n            The invoice date of the Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 50, 6)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'researcher'), researcher, scope=project_, documentation=u'\n            Researcher provides a URI linking to the detailed representation of the Researcher for the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 62, 6)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), _ImportedBinding_userdefined.field_, scope=project_, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), _ImportedBinding_userdefined.type_, scope=project_, documentation=u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 14, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 26, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 38, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 50, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 62, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 74, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 86, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 98, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 110, 6))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(None, u'open-date')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 26, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(None, u'close-date')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 38, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(None, u'invoice-date')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(None, u'researcher')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 62, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 74, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 86, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 98, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_file, u'file')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 110, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
project_._Automaton = _BuildAutomaton()




projects_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'project'), project_link, scope=projects_, documentation=u'\n            Project provides a URI linking to the detailed representation of a project.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 179, 6)))

projects_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=projects_, documentation=u'\n            When working with large lists of projects,\nthe previous-page element provides a URI that links to the previous page of projects.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 186, 6)))

projects_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=projects_, documentation=u'\n            When working with large lists of projects,\nthe next-page element provides a URI that links to the next page of projects.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 194, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 179, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 186, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 194, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projects_._UseForTag(pyxb.namespace.ExpandedName(None, u'project')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 179, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(projects_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 186, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(projects_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 194, 6))
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
projects_._Automaton = _BuildAutomaton_()




project_link._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=project_link, documentation=u'\n            The name of the project.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 211, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 211, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(project_link._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/project.xsd', 211, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
project_link._Automaton = _BuildAutomaton_2()

