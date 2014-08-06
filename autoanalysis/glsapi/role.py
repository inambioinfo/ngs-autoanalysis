# ./role.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:62510f3533b7b4cb4b8d284501938c95b21ec449
# Generated 2014-08-06 17:32:28.834864 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/role

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:40a41507-1d87-11e4-8a92-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/role', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/role}role with content type ELEMENT_ONLY
class role_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a Role
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'role')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrirole_role__name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            Name of the represented role\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element researchers uses Python identifier researchers
    __researchers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'researchers'), 'researchers', '__httpgenologics_comrirole_role__researchers', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 21, 6), )

    
    researchers = property(__researchers.value, __researchers.set, None, u'\n            The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element permissions uses Python identifier permissions
    __permissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'permissions'), 'permissions', '__httpgenologics_comrirole_role__permissions', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 45, 6), )

    
    permissions = property(__permissions.value, __permissions.set, None, u'\n            The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Attribute built-in uses Python identifier built_in
    __built_in = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'built-in'), 'built_in', '__httpgenologics_comrirole_role__built_in', pyxb.binding.datatypes.boolean)
    __built_in._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 70, 4)
    __built_in._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 70, 4)
    
    built_in = property(__built_in.value, __built_in.set, None, u'\n          Whether this role is a built-in role (built-in roles cannot be deleted)\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirole_role__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 80, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 80, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Role.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __name.name() : __name,
        __researchers.name() : __researchers,
        __permissions.name() : __permissions
    })
    _AttributeMap.update({
        __built_in.name() : __built_in,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'role', role_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            The researchers who have been granted the Role. This field is read-only.
<br/>Always returns with GET: Yes
<br/>Updatable with PUT: No
<br/>Required for PUT: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 30, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element researcher uses Python identifier researcher
    __researcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'researcher'), 'researcher', '__httpgenologics_comrirole_CTD_ANON_researcher', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 32, 12), )

    
    researcher = property(__researcher.value, __researcher.set, None, u'\n                  The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n                ')

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
<br/>Updatable with PUT: Yes
<br/>Required for PUT: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 54, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element permission uses Python identifier permission
    __permission = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'permission'), 'permission', '__httpgenologics_comrirole_CTD_ANON__permission', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 56, 12), )

    
    permission = property(__permission.value, __permission.set, None, u'\n                  The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'permission-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 91, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__httpgenologics_comrirole_permission_link_action', pyxb.binding.datatypes.string)
    __action._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 97, 4)
    __action._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 97, 4)
    
    action = property(__action.value, __action.set, None, u'\n          The action this Permission is granting\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrirole_permission_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 107, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 107, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of this Permission\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirole_permission_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 117, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 117, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Permission\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __action.name() : __action,
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'permission-link', permission_link)


# Complex type {http://genologics.com/ri/role}researcher-link with content type EMPTY
class researcher_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Researcher-link is a child element type of researchers and provides a URI linking to the detailed representation of a researcher.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'researcher-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 128, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'last-name'), 'last_name', '__httpgenologics_comrirole_researcher_link_last_name', pyxb.binding.datatypes.string)
    __last_name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 134, 4)
    __last_name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 134, 4)
    
    last_name = property(__last_name.value, __last_name.set, None, u'\n          The last name of the researcher.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'first-name'), 'first_name', '__httpgenologics_comrirole_researcher_link_first_name', pyxb.binding.datatypes.string)
    __first_name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 144, 4)
    __first_name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 144, 4)
    
    first_name = property(__first_name.value, __first_name.set, None, u'\n          The first name of the researcher.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirole_researcher_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 154, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 154, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Researcher\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'researcher-link', researcher_link)


# Complex type {http://genologics.com/ri/role}roles with content type ELEMENT_ONLY
class roles_ (pyxb.binding.basis.complexTypeDefinition):
    """
        API representation of a list of Roles
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'roles')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__httpgenologics_comrirole_roles__role', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 172, 6), )

    
    role = property(__role.value, __role.set, None, u'\n            The list of Roles\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirole_roles__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 181, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 181, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Roles LIST endpoint\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __role.name() : __role
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'roles', roles_)


# Complex type {http://genologics.com/ri/role}role-link with content type EMPTY
class role_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Role-link is a child element type of roles and provides a URI linking to the detailed representation of a Role.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'role-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 190, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrirole_role_link_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 196, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 196, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of this Role\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrirole_role_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 204, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 204, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Role\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'role-link', role_link)


role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'role'), role_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', role.name().localName(), role)

roles = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'roles'), roles_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', roles.name().localName(), roles)



role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=role_, documentation=u'\n            Name of the represented role\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6)))

role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'researchers'), CTD_ANON, scope=role_, documentation=u'\n            The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 21, 6)))

role_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'permissions'), CTD_ANON_, scope=role_, documentation=u'\n            The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 45, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 45, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 11, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, u'researchers')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(role_._UseForTag(pyxb.namespace.ExpandedName(None, u'permissions')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 45, 6))
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




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'researcher'), researcher_link, scope=CTD_ANON, documentation=u'\n                  The researchers who have been granted the Role. This field is read-only.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 32, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 32, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'researcher')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'permission'), permission_link, scope=CTD_ANON_, documentation=u'\n                  The permissions assigned to the Role. If omitted from a PUT, all permissions will be unassigned from the Role.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 56, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 56, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'permission')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 56, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




roles_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'role'), role_link, scope=roles_, documentation=u'\n            The list of Roles\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 172, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 172, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(roles_._UseForTag(pyxb.namespace.ExpandedName(None, u'role')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/role.xsd', 172, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
roles_._Automaton = _BuildAutomaton_3()

