# ./role.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:62510f3533b7b4cb4b8d284501938c95b21ec449
# Generated 2016-01-12 17:07:14.295025 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/role

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/role', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/role}role with content type ELEMENT_ONLY
class role_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Role
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'role')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comrirole_role__name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6), )

    
    name = property(__name.value, __name.set, None, '\n            Name of the represented role\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element researchers uses Python identifier researchers
    __researchers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'researchers'), 'researchers', '__httpgenologics_comrirole_role__researchers', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 23, 6), )

    
    researchers = property(__researchers.value, __researchers.set, None, '\n            The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element permissions uses Python identifier permissions
    __permissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'permissions'), 'permissions', '__httpgenologics_comrirole_role__permissions', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 51, 6), )

    
    permissions = property(__permissions.value, __permissions.set, None, '\n            The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Attribute built-in uses Python identifier built_in
    __built_in = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'built-in'), 'built_in', '__httpgenologics_comrirole_role__built_in', pyxb.binding.datatypes.boolean)
    __built_in._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 80, 4)
    __built_in._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 80, 4)
    
    built_in = property(__built_in.value, __built_in.set, None, '\n          Whether this role is a built-in role (built-in roles cannot be deleted)\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrirole_role__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 92, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 92, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Role.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __name.name() : __name,
        __researchers.name() : __researchers,
        __permissions.name() : __permissions
    })
    _AttributeMap.update({
        __built_in.name() : __built_in,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'role', role_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            The researchers who have been granted the Role. This field is read-only.
<br/>Always returns with GET: Yes
<br/>Creatable with POST: No
<br/>Required for POST: No
<br/>Updatable with PUT: No
<br/>Required for PUT: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 34, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element researcher uses Python identifier researcher
    __researcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'researcher'), 'researcher', '__httpgenologics_comrirole_CTD_ANON_researcher', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 36, 12), )

    
    researcher = property(__researcher.value, __researcher.set, None, '\n                  The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n                ')

    _ElementMap.update({
        __researcher.name() : __researcher
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.
<br/>Always returns with GET: Yes
<br/>Creatable with POST: Yes
<br/>Required for POST: No
<br/>Updatable with PUT: Yes
<br/>Required for PUT: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 62, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element permission uses Python identifier permission
    __permission = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'permission'), 'permission', '__httpgenologics_comrirole_CTD_ANON__permission', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 64, 12), )

    
    permission = property(__permission.value, __permission.set, None, '\n                  The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ')

    _ElementMap.update({
        __permission.name() : __permission
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/role}permission-link with content type EMPTY
class permission_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Permission-link is a child element type of permissions and provides a URI linking to the detailed representation of a Permission.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'permission-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action'), 'action', '__httpgenologics_comrirole_permission_link_action', pyxb.binding.datatypes.string)
    __action._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 111, 4)
    __action._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 111, 4)
    
    action = property(__action.value, __action.set, None, '\n          The action this Permission is granting\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comrirole_permission_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 123, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 123, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of this Permission\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrirole_permission_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 135, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 135, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Permission\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __action.name() : __action,
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'permission-link', permission_link)


# Complex type {http://genologics.com/ri/role}researcher-link with content type EMPTY
class researcher_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Researcher-link is a child element type of researchers and provides a URI linking to the detailed representation of a researcher.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'researcher-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 148, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last-name'), 'last_name', '__httpgenologics_comrirole_researcher_link_last_name', pyxb.binding.datatypes.string)
    __last_name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 154, 4)
    __last_name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 154, 4)
    
    last_name = property(__last_name.value, __last_name.set, None, '\n          The last name of the researcher.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'first-name'), 'first_name', '__httpgenologics_comrirole_researcher_link_first_name', pyxb.binding.datatypes.string)
    __first_name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 166, 4)
    __first_name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 166, 4)
    
    first_name = property(__first_name.value, __first_name.set, None, '\n          The first name of the researcher.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrirole_researcher_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 178, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 178, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Researcher\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'researcher-link', researcher_link)


# Complex type {http://genologics.com/ri/role}roles with content type ELEMENT_ONLY
class roles_ (pyxb.binding.basis.complexTypeDefinition):
    """
        API representation of a list of Roles
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roles')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 191, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__httpgenologics_comrirole_roles__role', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 198, 6), )

    
    role = property(__role.value, __role.set, None, '\n            The list of Roles\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrirole_roles__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 207, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 207, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Roles LIST endpoint\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __role.name() : __role
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'roles', roles_)


# Complex type {http://genologics.com/ri/role}role-link with content type EMPTY
class role_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Role-link is a child element type of roles and provides a URI linking to the detailed representation of a Role.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'role-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 216, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comrirole_role_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 222, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 222, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of this Role\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comrirole_role_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 230, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 230, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Role\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'role-link', role_link)


role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'role'), role_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', role.name().localName(), role)

roles = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roles'), roles_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', roles.name().localName(), roles)



role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=role_, documentation='\n            Name of the represented role\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6)))

role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'researchers'), CTD_ANON, scope=role_, documentation='\n            The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 23, 6)))

role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'permissions'), CTD_ANON_, scope=role_, documentation='\n            The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 51, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 23, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 51, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, 'researchers')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, 'permissions')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 51, 6))
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
role_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'researcher'), researcher_link, scope=CTD_ANON, documentation='\n                  The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 36, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'researcher')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 36, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'permission'), permission_link, scope=CTD_ANON_, documentation='\n                  The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 64, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 64, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'permission')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 64, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




roles_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), role_link, scope=roles_, documentation='\n            The list of Roles\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 198, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 198, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(roles_._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/role.xsd', 198, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
roles_._Automaton = _BuildAutomaton_3()

