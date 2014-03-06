# ./step.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8918431e508ba51505d6101ffc70374ded684580
# Generated 2014-03-06 16:48:15.160852 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/step

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/step', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/step}action-type
class action_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Special actions for samples.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'action-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 242, 2)
    _Documentation = u'\n        Special actions for samples.\n      '
action_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=action_type, enum_prefix=None)
action_type.leave = action_type._CF_enumeration.addEnumeration(unicode_value=u'leave', tag=u'leave')
action_type.repeat = action_type._CF_enumeration.addEnumeration(unicode_value=u'repeat', tag=u'repeat')
action_type.remove = action_type._CF_enumeration.addEnumeration(unicode_value=u'remove', tag=u'remove')
action_type.review = action_type._CF_enumeration.addEnumeration(unicode_value=u'review', tag=u'review')
action_type.complete = action_type._CF_enumeration.addEnumeration(unicode_value=u'complete', tag=u'complete')
action_type.store = action_type._CF_enumeration.addEnumeration(unicode_value=u'store', tag=u'store')
action_type.nextstep = action_type._CF_enumeration.addEnumeration(unicode_value=u'nextstep', tag=u'nextstep')
action_type.rework = action_type._CF_enumeration.addEnumeration(unicode_value=u'rework', tag=u'rework')
action_type.unknown = action_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
action_type._InitializeFacetMap(action_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'action-type', action_type)

# Atomic simple type: {http://genologics.com/ri/step}status
class status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Describes the different natures of status for an external program.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'status')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 582, 2)
    _Documentation = u'\n        Describes the different natures of status for an external program.\n      '
status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=status, enum_prefix=None)
status.OK = status._CF_enumeration.addEnumeration(unicode_value=u'OK', tag=u'OK')
status.ERROR = status._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
status.WARNING = status._CF_enumeration.addEnumeration(unicode_value=u'WARNING', tag=u'WARNING')
status.RUNNING = status._CF_enumeration.addEnumeration(unicode_value=u'RUNNING', tag=u'RUNNING')
status._InitializeFacetMap(status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'status', status)

# Complex type {http://genologics.com/ri/step}step with content type ELEMENT_ONLY
class step_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_step__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 16, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The configuration information for the step run.\n          ')

    
    # Element actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'actions'), 'actions', '__httpgenologics_comristep_step__actions', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 23, 6), )

    
    actions = property(__actions.value, __actions.set, None, u'\n            The corresponding step actions.\n          ')

    
    # Element reagents uses Python identifier reagents
    __reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagents'), 'reagents', '__httpgenologics_comristep_step__reagents', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 30, 6), )

    
    reagents = property(__reagents.value, __reagents.set, None, u'\n            The corresponding step reagents.\n          ')

    
    # Element pools uses Python identifier pools
    __pools = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pools'), 'pools', '__httpgenologics_comristep_step__pools', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 37, 6), )

    
    pools = property(__pools.value, __pools.set, None, u'\n            The corresponding step pools.\n          ')

    
    # Element placements uses Python identifier placements
    __placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'placements'), 'placements', '__httpgenologics_comristep_step__placements', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6), )

    
    placements = property(__placements.value, __placements.set, None, u'\n            The corresponding step placements.\n          ')

    
    # Element program-status uses Python identifier program_status
    __program_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'program-status'), 'program_status', '__httpgenologics_comristep_step__program_status', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6), )

    
    program_status = property(__program_status.value, __program_status.set, None, u'\n            The corresponding step program status, if one exists.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_step__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 59, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 59, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comristep_step__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 60, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 60, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Step/Process.\n        ')

    _ElementMap.update({
        __configuration.name() : __configuration,
        __actions.name() : __actions,
        __reagents.name() : __reagents,
        __pools.name() : __pools,
        __placements.name() : __placements,
        __program_status.name() : __program_status
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'step', step_)


# Complex type {http://genologics.com/ri/step}step-configuration with content type SIMPLE
class step_configuration (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the configuration information for the step run.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step-configuration')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_step_configuration_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 76, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 76, 8)
    
    uri = property(__uri.value, __uri.set, None, u'\n              The URI of the protocol step.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'step-configuration', step_configuration)


# Complex type {http://genologics.com/ri/step}actions-link with content type EMPTY
class actions_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the actions applied or to be applied by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'actions-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 86, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_actions_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step actions resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'actions-link', actions_link)


# Complex type {http://genologics.com/ri/step}placements-link with content type EMPTY
class placements_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the output placements for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'placements-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 100, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_placements_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 106, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 106, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step placements resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'placements-link', placements_link)


# Complex type {http://genologics.com/ri/step}pools-link with content type EMPTY
class pools_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the pools added by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pools-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 114, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_pools_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 120, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 120, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step pools resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'pools-link', pools_link)


# Complex type {http://genologics.com/ri/step}program-status-link with content type EMPTY
class program_status_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the program status for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'program-status-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 128, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_program_status_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 134, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 134, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step program status resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'program-status-link', program_status_link)


# Complex type {http://genologics.com/ri/step}reagents-link with content type EMPTY
class reagents_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the reagents added by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagents-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 142, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagents_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 148, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 148, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step reagents resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagents-link', reagents_link)


# Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY
class actions_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'actions')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 156, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_actions__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 158, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_actions__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 168, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element next-actions uses Python identifier next_actions
    __next_actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-actions'), 'next_actions', '__httpgenologics_comristep_actions__next_actions', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 178, 6), )

    
    next_actions = property(__next_actions.value, __next_actions.set, None, u'\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_actions__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 201, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 201, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __next_actions.name() : __next_actions
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'actions', actions_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            All samples belong to one step; these samples can move forward for another configured step work
or need special handling, such as remove from the workflow they are in, leave in their existing
queue for rework, or require view by a manager, etc...
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 186, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element next-action uses Python identifier next_action
    __next_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-action'), 'next_action', '__httpgenologics_comristep_CTD_ANON_next_action', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 188, 12), )

    
    next_action = property(__next_action.value, __next_action.set, None, u'\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ')

    _ElementMap.update({
        __next_action.name() : __next_action
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}placements with content type ELEMENT_ONLY
class placements_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact container placements
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'placements')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 260, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_placements__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 267, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_placements__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 277, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element selected-containers uses Python identifier selected_containers
    __selected_containers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'selected-containers'), 'selected_containers', '__httpgenologics_comristep_placements__selected_containers', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 287, 6), )

    
    selected_containers = property(__selected_containers.value, __selected_containers.set, None, u'\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element output-placements uses Python identifier output_placements
    __output_placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-placements'), 'output_placements', '__httpgenologics_comristep_placements__output_placements', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 311, 6), )

    
    output_placements = property(__output_placements.value, __output_placements.set, None, u'\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_placements__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 336, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 336, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __selected_containers.name() : __selected_containers,
        __output_placements.name() : __output_placements
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'placements', placements_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            The selected containers for step placement.
<br/>Always returns with GET: Yes
<br/>Creatable with POST: Yes
<br/>Required for POST: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 296, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container uses Python identifier container
    __container = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container'), 'container', '__httpgenologics_comristep_CTD_ANON__container', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 298, 12), )

    
    container = property(__container.value, __container.set, None, u'\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ')

    _ElementMap.update({
        __container.name() : __container
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
            The output artifacts for this step with placement if they have one.
<br/>Always returns with GET: Yes
<br/>Creatable with POST: Yes
<br/>Required for POST: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 320, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output-placement uses Python identifier output_placement
    __output_placement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-placement'), 'output_placement', '__httpgenologics_comristep_CTD_ANON_2_output_placement', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 322, 12), )

    
    output_placement = property(__output_placement.value, __output_placement.set, None, u'\n                  The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ')

    _ElementMap.update({
        __output_placement.name() : __output_placement
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}container with content type EMPTY
class container (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to a selected container to be used for placement.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'container')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 347, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_container_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 353, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 353, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'container', container)


# Complex type {http://genologics.com/ri/step}output-placement with content type ELEMENT_ONLY
class output_placement (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to the output artifact and container placement.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'output-placement')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 364, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__httpgenologics_comristep_output_placement_location', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 371, 6), )

    
    location = property(__location.value, __location.set, None, u'\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_output_placement_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 382, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 382, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'output-placement', output_placement)


# Complex type {http://genologics.com/ri/step}pools with content type ELEMENT_ONLY
class pools_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's pooled inputs.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pools')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 393, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_pools__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 400, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_pools__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 410, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element pooled-inputs uses Python identifier pooled_inputs
    __pooled_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pooled-inputs'), 'pooled_inputs', '__httpgenologics_comristep_pools__pooled_inputs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 420, 6), )

    
    pooled_inputs = property(__pooled_inputs.value, __pooled_inputs.set, None, u'\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element available-inputs uses Python identifier available_inputs
    __available_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'available-inputs'), 'available_inputs', '__httpgenologics_comristep_pools__available_inputs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 444, 6), )

    
    available_inputs = property(__available_inputs.value, __available_inputs.set, None, u'\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_pools__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the StepPools.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __pooled_inputs.name() : __pooled_inputs,
        __available_inputs.name() : __available_inputs
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'pools', pools_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
            The pooled input artifacts for this step.
<br/>Always returns with GET: Yes
<br/>Updatable with PUT: Yes
<br/>Required for PUT: No
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 429, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pool uses Python identifier pool
    __pool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pool'), 'pool', '__httpgenologics_comristep_CTD_ANON_3_pool', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 431, 12), )

    
    pool = property(__pool.value, __pool.set, None, u'\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ')

    _ElementMap.update({
        __pool.name() : __pool
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
            The available input artifacts for this step.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 451, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_CTD_ANON_4_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 453, 12), )

    
    input = property(__input.value, __input.set, None, u'\n                  The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n                ')

    _ElementMap.update({
        __input.name() : __input
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}input with content type EMPTY
class input (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides input URI links.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'input')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 476, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 482, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 482, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'input', input)


# Complex type {http://genologics.com/ri/step}pooled-inputs with content type ELEMENT_ONLY
class pooled_inputs (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides pooled input groups.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pooled-inputs')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 493, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_pooled_inputs_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 500, 6), )

    
    input = property(__input.value, __input.set, None, u'\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_pooled_inputs_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 511, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 511, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The pool name.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute output-uri uses Python identifier output_uri
    __output_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'output-uri'), 'output_uri', '__httpgenologics_comristep_pooled_inputs_output_uri', pyxb.binding.datatypes.anyURI)
    __output_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 521, 4)
    __output_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 521, 4)
    
    output_uri = property(__output_uri.value, __output_uri.set, None, u'\n          The URI of the pooled output artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __input.name() : __input
    })
    _AttributeMap.update({
        __name.name() : __name,
        __output_uri.name() : __output_uri
    })
Namespace.addCategoryObject('typeBinding', u'pooled-inputs', pooled_inputs)


# Complex type {http://genologics.com/ri/step}program-status with content type ELEMENT_ONLY
class program_status_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The current EPP status for a step (supports automatically triggered programs only).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'program-status')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 532, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_program_status__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_program_status__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpgenologics_comristep_program_status__status', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 559, 6), )

    
    status = property(__status.value, __status.set, None, u'\n            The nature of the status.\n          ')

    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpgenologics_comristep_program_status__message', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 566, 6), )

    
    message = property(__message.value, __message.set, None, u'\n            The user-facing message for this status.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_program_status__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 574, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 574, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI to this status.\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __status.name() : __status,
        __message.name() : __message
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'program-status', program_status_)


# Complex type {http://genologics.com/ri/step}reagents with content type ELEMENT_ONLY
class reagents_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact reagents.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagents')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 595, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_reagents__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 602, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_reagents__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 612, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element reagent-category uses Python identifier reagent_category
    __reagent_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-category'), 'reagent_category', '__httpgenologics_comristep_reagents__reagent_category', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 622, 6), )

    
    reagent_category = property(__reagent_category.value, __reagent_category.set, None, u'\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element output-reagents uses Python identifier output_reagents
    __output_reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-reagents'), 'output_reagents', '__httpgenologics_comristep_reagents__output_reagents', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 632, 6), )

    
    output_reagents = property(__output_reagents.value, __output_reagents.set, None, u'\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagents__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 653, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 653, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the StepReagents.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __reagent_category.name() : __reagent_category,
        __output_reagents.name() : __output_reagents
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagents', reagents_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
            The output artifacts for this step.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 639, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output'), 'output', '__httpgenologics_comristep_CTD_ANON_5_output', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 641, 12), )

    
    output = property(__output.value, __output.set, None, u'\n                  The output artifacts for this step.\n<br/>Always returns with GET: Yes\n                ')

    _ElementMap.update({
        __output.name() : __output
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}reagent-label with content type EMPTY
class reagent_label (pyxb.binding.basis.complexTypeDefinition):
    """
        Reagent-label is a child element of ExtStepReagentListElement and provides the name of a
label or reagent that has been added to the Artifact.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-label')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 664, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_reagent_label_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 671, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 671, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The reagent label name for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a reagent label.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'reagent-label', reagent_label)


# Complex type {http://genologics.com/ri/step}output with content type ELEMENT_ONLY
class output (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to the output artifact and reagent label.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'output')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 682, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-label uses Python identifier reagent_label
    __reagent_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-label'), 'reagent_label', '__httpgenologics_comristep_output_reagent_label', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 689, 6), )

    
    reagent_label = property(__reagent_label.value, __reagent_label.set, None, u'\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_output_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 700, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 700, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        __reagent_label.name() : __reagent_label
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'output', output)


# Complex type {http://genologics.com/ri/step}next-action with content type EMPTY
class next_action (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample next action or step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'next-action')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 203, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute artifact-uri uses Python identifier artifact_uri
    __artifact_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'artifact-uri'), 'artifact_uri', '__httpgenologics_comristep_next_action_artifact_uri', pyxb.binding.datatypes.anyURI)
    __artifact_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 209, 4)
    __artifact_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 209, 4)
    
    artifact_uri = property(__artifact_uri.value, __artifact_uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: no\n<br/>Required for PUT: yes\n        ')

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__httpgenologics_comristep_next_action_action', action_type)
    __action._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 219, 4)
    __action._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 219, 4)
    
    action = property(__action.value, __action.set, None, u'\n          The next action for the sample.\n<br/>Always returns with GET: no; the sample may not have a next action.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the action is not present during an update, the existing action for the sample\nwill be removed if there is one.\n        ')

    
    # Attribute step-uri uses Python identifier step_uri
    __step_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'step-uri'), 'step_uri', '__httpgenologics_comristep_next_action_step_uri', pyxb.binding.datatypes.anyURI)
    __step_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 230, 4)
    __step_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 230, 4)
    
    step_uri = property(__step_uri.value, __step_uri.set, None, u'\n          The next protocol step for the sample.\n<br/>Always returns with GET: no; the sample may not have a next step.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the step is not present during an update, the existing step for the sample\nwill be removed if there is one.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __artifact_uri.name() : __artifact_uri,
        __action.name() : __action,
        __step_uri.name() : __step_uri
    })
Namespace.addCategoryObject('typeBinding', u'next-action', next_action)


step = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'step'), step_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', step.name().localName(), step)

actions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actions'), actions_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', actions.name().localName(), actions)

placements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'placements'), placements_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', placements.name().localName(), placements)

pools = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pools'), pools_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', pools.name().localName(), pools)

program_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'program-status'), program_status_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', program_status.name().localName(), program_status)

reagents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reagents'), reagents_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', reagents.name().localName(), reagents)



step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=step_, documentation=u'\n            The configuration information for the step run.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 16, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'actions'), actions_link, scope=step_, documentation=u'\n            The corresponding step actions.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 23, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagents'), reagents_link, scope=step_, documentation=u'\n            The corresponding step reagents.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 30, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pools'), pools_link, scope=step_, documentation=u'\n            The corresponding step pools.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 37, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'placements'), placements_link, scope=step_, documentation=u'\n            The corresponding step placements.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'program-status'), program_status_link, scope=step_, documentation=u'\n            The corresponding step program status, if one exists.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 16, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 23, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 30, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 37, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'actions')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagents')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 30, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'pools')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 37, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'placements')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'program-status')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
step_._Automaton = _BuildAutomaton()




actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=actions_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 158, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=actions_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 168, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-actions'), CTD_ANON, scope=actions_, documentation=u'\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 178, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 158, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 168, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 178, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 158, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 168, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-actions')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 178, 6))
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
actions_._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-action'), next_action, scope=CTD_ANON, documentation=u'\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 188, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 188, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'next-action')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 188, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()




placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=placements_, documentation=u'\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 267, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=placements_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 277, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'selected-containers'), CTD_ANON_, scope=placements_, documentation=u'\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 287, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-placements'), CTD_ANON_2, scope=placements_, documentation=u'\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 311, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 267, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 277, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 287, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 311, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 267, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 277, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'selected-containers')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 287, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'output-placements')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 311, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
placements_._Automaton = _BuildAutomaton_3()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container'), container, scope=CTD_ANON_, documentation=u'\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 298, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 298, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'container')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 298, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-placement'), output_placement, scope=CTD_ANON_2, documentation=u'\n                  The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 322, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 322, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'output-placement')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 322, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




output_placement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), _ImportedBinding_ri.location, scope=output_placement, documentation=u'\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 371, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 371, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output_placement._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 371, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output_placement._Automaton = _BuildAutomaton_6()




pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=pools_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 400, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=pools_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 410, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pooled-inputs'), CTD_ANON_3, scope=pools_, documentation=u'\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 420, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'available-inputs'), CTD_ANON_4, scope=pools_, documentation=u'\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 444, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 400, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 410, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 420, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 444, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 400, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 410, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'pooled-inputs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 420, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'available-inputs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 444, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pools_._Automaton = _BuildAutomaton_7()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pool'), pooled_inputs, scope=CTD_ANON_3, documentation=u'\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 431, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 431, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'pool')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 431, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_8()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), input, scope=CTD_ANON_4, documentation=u'\n                  The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 453, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 453, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 453, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_9()




pooled_inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), input, scope=pooled_inputs, documentation=u'\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 500, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 500, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pooled_inputs._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 500, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pooled_inputs._Automaton = _BuildAutomaton_10()




program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=program_status_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=program_status_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'), status, scope=program_status_, documentation=u'\n            The nature of the status.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 559, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'message'), pyxb.binding.datatypes.string, scope=program_status_, documentation=u'\n            The user-facing message for this status.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 566, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 559, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 566, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'status')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 559, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'message')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 566, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
program_status_._Automaton = _BuildAutomaton_11()




reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=reagents_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 602, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=reagents_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 612, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-category'), pyxb.binding.datatypes.string, scope=reagents_, documentation=u'\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 622, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-reagents'), CTD_ANON_5, scope=reagents_, documentation=u'\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 632, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 602, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 612, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 622, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 632, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 602, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 612, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-category')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 622, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'output-reagents')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 632, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
reagents_._Automaton = _BuildAutomaton_12()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output'), output, scope=CTD_ANON_5, documentation=u'\n                  The output artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 641, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 641, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'output')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 641, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_13()




output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-label'), reagent_label, scope=output, documentation=u'\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 689, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 689, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-label')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 689, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output._Automaton = _BuildAutomaton_14()

