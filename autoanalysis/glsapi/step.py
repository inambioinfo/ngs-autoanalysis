# ./step.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8918431e508ba51505d6101ffc70374ded684580
# Generated 2014-10-02 18:41:08.802510 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/step

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4a029cca-4a5b-11e4-a093-70cd60a9fcda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import userdefined as _ImportedBinding_userdefined
import pyxb.binding.datatypes
import ri as _ImportedBinding_ri

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/step', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/step}action-type
class action_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Special actions for samples.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'action-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 550, 2)
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

# Atomic simple type: {http://genologics.com/ri/step}output-generation-type
class output_generation_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The available options for output-type generation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'output-generation-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 815, 2)
    _Documentation = u'\n        The available options for output-type generation.\n      '
output_generation_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=output_generation_type, enum_prefix=None)
output_generation_type.PerInput = output_generation_type._CF_enumeration.addEnumeration(unicode_value=u'PerInput', tag=u'PerInput')
output_generation_type.PerAllInputs = output_generation_type._CF_enumeration.addEnumeration(unicode_value=u'PerAllInputs', tag=u'PerAllInputs')
output_generation_type.PerReagentLabel = output_generation_type._CF_enumeration.addEnumeration(unicode_value=u'PerReagentLabel', tag=u'PerReagentLabel')
output_generation_type._InitializeFacetMap(output_generation_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'output-generation-type', output_generation_type)

# Atomic simple type: {http://genologics.com/ri/step}status
class status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Describes the different natures of status for an external program.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'status')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1178, 2)
    _Documentation = u'\n        Describes the different natures of status for an external program.\n      '
status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=status, enum_prefix=None)
status.OK = status._CF_enumeration.addEnumeration(unicode_value=u'OK', tag=u'OK')
status.ERROR = status._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
status.WARNING = status._CF_enumeration.addEnumeration(unicode_value=u'WARNING', tag=u'WARNING')
status.RUNNING = status._CF_enumeration.addEnumeration(unicode_value=u'RUNNING', tag=u'RUNNING')
status.QUEUED = status._CF_enumeration.addEnumeration(unicode_value=u'QUEUED', tag=u'QUEUED')
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_step__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The configuration information for the step run.\n          ')

    
    # Element actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'actions'), 'actions', '__httpgenologics_comristep_step__actions', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6), )

    
    actions = property(__actions.value, __actions.set, None, u'\n            The corresponding step actions.\n          ')

    
    # Element reagents uses Python identifier reagents
    __reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagents'), 'reagents', '__httpgenologics_comristep_step__reagents', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 35, 6), )

    
    reagents = property(__reagents.value, __reagents.set, None, u'\n            The corresponding step reagents.\n          ')

    
    # Element pools uses Python identifier pools
    __pools = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pools'), 'pools', '__httpgenologics_comristep_step__pools', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 42, 6), )

    
    pools = property(__pools.value, __pools.set, None, u'\n            The corresponding step pools.\n          ')

    
    # Element placements uses Python identifier placements
    __placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'placements'), 'placements', '__httpgenologics_comristep_step__placements', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 49, 6), )

    
    placements = property(__placements.value, __placements.set, None, u'\n            The corresponding step placements.\n          ')

    
    # Element reagent-lots uses Python identifier reagent_lots
    __reagent_lots = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-lots'), 'reagent_lots', '__httpgenologics_comristep_step__reagent_lots', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 56, 6), )

    
    reagent_lots = property(__reagent_lots.value, __reagent_lots.set, None, u'\n            The corresponding reagent lots for the step.\n          ')

    
    # Element program-status uses Python identifier program_status
    __program_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'program-status'), 'program_status', '__httpgenologics_comristep_step__program_status', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 63, 6), )

    
    program_status = property(__program_status.value, __program_status.set, None, u'\n            The corresponding step program status, if one exists.\n          ')

    
    # Element setup uses Python identifier setup
    __setup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'setup'), 'setup', '__httpgenologics_comristep_step__setup', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 70, 6), )

    
    setup = property(__setup.value, __setup.set, None, u'\n            The corresponding step setup.\n          ')

    
    # Element details uses Python identifier details
    __details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'details'), 'details', '__httpgenologics_comristep_step__details', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 77, 6), )

    
    details = property(__details.value, __details.set, None, u'\n            The corresponding step details.\n          ')

    
    # Element available-programs uses Python identifier available_programs
    __available_programs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'available-programs'), 'available_programs', '__httpgenologics_comristep_step__available_programs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 84, 6), )

    
    available_programs = property(__available_programs.value, __available_programs.set, None, u'\n            The programs available for direct triggering on the step.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_step__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 103, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 103, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comristep_step__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 104, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 104, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Step/Process.\n        ')

    
    # Attribute current-state uses Python identifier current_state
    __current_state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'current-state'), 'current_state', '__httpgenologics_comristep_step__current_state', pyxb.binding.datatypes.string)
    __current_state._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 111, 4)
    __current_state._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 111, 4)
    
    current_state = property(__current_state.value, __current_state.set, None, u'\n          The current state of the step\n        ')

    _ElementMap.update({
        __configuration.name() : __configuration,
        __actions.name() : __actions,
        __reagents.name() : __reagents,
        __pools.name() : __pools,
        __placements.name() : __placements,
        __reagent_lots.name() : __reagent_lots,
        __program_status.name() : __program_status,
        __setup.name() : __setup,
        __details.name() : __details,
        __available_programs.name() : __available_programs
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid,
        __current_state.name() : __current_state
    })
Namespace.addCategoryObject('typeBinding', u'step', step_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            The programs available for direct triggering on the step.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 90, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element available-program uses Python identifier available_program
    __available_program = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'available-program'), 'available_program', '__httpgenologics_comristep_CTD_ANON_available_program', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 12), )

    
    available_program = property(__available_program.value, __available_program.set, None, u'\n                  The programs available for direct triggering on the step.\n                ')

    _ElementMap.update({
        __available_program.name() : __available_program
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}available-program with content type EMPTY
class available_program (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies a program that is available for a step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'available-program')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_available_program_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 125, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 125, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI to execute the program for this step (via POST, with no request entity).\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_available_program_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 132, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 132, 4)
    
    name = property(__name.value, __name.set, None, u"\n          The name of the program to execute. Matches the trigger name\n('name' attribute in the 'epp-trigger' element) in the protocol step configuration.\n        ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'available-program', available_program)


# Complex type {http://genologics.com/ri/step}step-configuration with content type SIMPLE
class step_configuration (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the configuration information for the step run.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step-configuration')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_step_configuration_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 149, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 149, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 159, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_actions_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 165, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 165, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step actions resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'actions-link', actions_link)


# Complex type {http://genologics.com/ri/step}details-link with content type EMPTY
class details_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the details for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'details-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 173, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_details_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 179, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 179, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step details resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'details-link', details_link)


# Complex type {http://genologics.com/ri/step}placements-link with content type EMPTY
class placements_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the output placements for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'placements-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 187, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_placements_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 193, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 193, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 201, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_pools_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 207, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 207, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 215, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_program_status_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 221, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 221, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step program status resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'program-status-link', program_status_link)


# Complex type {http://genologics.com/ri/step}reagent-lots-link with content type EMPTY
class reagent_lots_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the reagent lots for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-lots-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 229, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagent_lots_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 235, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 235, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the corresponding reagent lots resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagent-lots-link', reagent_lots_link)


# Complex type {http://genologics.com/ri/step}reagents-link with content type EMPTY
class reagents_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the reagents added by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagents-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagents_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 249, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 249, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step reagents resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagents-link', reagents_link)


# Complex type {http://genologics.com/ri/step}setup-link with content type EMPTY
class setup_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the setup for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'setup-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 257, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_setup_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 263, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 263, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of corresponding step setup resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'setup-link', setup_link)


# Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY
class actions_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'actions')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 271, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_actions__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 273, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_actions__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 283, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element next-actions uses Python identifier next_actions
    __next_actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-actions'), 'next_actions', '__httpgenologics_comristep_actions__next_actions', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 293, 6), )

    
    next_actions = property(__next_actions.value, __next_actions.set, None, u'\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ')

    
    # Element escalation uses Python identifier escalation
    __escalation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'escalation'), 'escalation', '__httpgenologics_comristep_actions__escalation', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 315, 6), )

    
    escalation = property(__escalation.value, __escalation.set, None, u'\n            The escalation details. When a step is under or completed review,\nescalation details include information on who requested the escalation,\nwho attended to it and what samples were escalated.\n<br/>Always returns with GET: No (only available if set)\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No (omitting means clearing the escalation details)\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_actions__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 328, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 328, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __next_actions.name() : __next_actions,
        __escalation.name() : __escalation
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'actions', actions_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            All samples belong to one step; these samples can move forward for another configured step work
or need special handling, such as remove from the workflow they are in, leave in their existing
queue for rework, or require view by a manager, etc...
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 301, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element next-action uses Python identifier next_action
    __next_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-action'), 'next_action', '__httpgenologics_comristep_CTD_ANON__next_action', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 303, 12), )

    
    next_action = property(__next_action.value, __next_action.set, None, u'\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ')

    _ElementMap.update({
        __next_action.name() : __next_action
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}escalated-artifact with content type EMPTY
class escalated_artifact (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample next action or step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'escalated-artifact')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 369, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_escalated_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 375, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 375, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'escalated-artifact', escalated_artifact)


# Complex type {http://genologics.com/ri/step}escalation with content type ELEMENT_ONLY
class escalation (pyxb.binding.basis.complexTypeDefinition):
    """
        Escalation details.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'escalation')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 386, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element request uses Python identifier request
    __request = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'request'), 'request', '__httpgenologics_comristep_escalation_request', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 393, 6), )

    
    request = property(__request.value, __request.set, None, u'\n            The escalation request details.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element review uses Python identifier review
    __review = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'review'), 'review', '__httpgenologics_comristep_escalation_review', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 403, 6), )

    
    review = property(__review.value, __review.set, None, u'\n            The review details. Only available after review is completed.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element escalated-artifacts uses Python identifier escalated_artifacts
    __escalated_artifacts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'escalated-artifacts'), 'escalated_artifacts', '__httpgenologics_comristep_escalation_escalated_artifacts', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 413, 6), )

    
    escalated_artifacts = property(__escalated_artifacts.value, __escalated_artifacts.set, None, u'\n            All samples marked for escalation.\n          ')

    _ElementMap.update({
        __request.name() : __request,
        __review.name() : __review,
        __escalated_artifacts.name() : __escalated_artifacts
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'escalation', escalation)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
            All samples marked for escalation.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 419, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element escalated-artifact uses Python identifier escalated_artifact
    __escalated_artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'escalated-artifact'), 'escalated_artifact', '__httpgenologics_comristep_CTD_ANON_2_escalated_artifact', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 421, 12), )

    
    escalated_artifact = property(__escalated_artifact.value, __escalated_artifact.set, None, u'\n                  All samples marked for escalation.\n                ')

    _ElementMap.update({
        __escalated_artifact.name() : __escalated_artifact
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}escalation-request with content type ELEMENT_ONLY
class escalation_request (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}escalation-request with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'escalation-request')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 433, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'author'), 'author', '__httpgenologics_comristep_escalation_request_author', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 435, 6), )

    
    author = property(__author.value, __author.set, None, u'\n            The user that originated the escalation.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element reviewer uses Python identifier reviewer
    __reviewer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reviewer'), 'reviewer', '__httpgenologics_comristep_escalation_request_reviewer', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 445, 6), )

    
    reviewer = property(__reviewer.value, __reviewer.set, None, u'\n            The reviewer originally requested to review samples.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'date'), 'date', '__httpgenologics_comristep_escalation_request_date', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 455, 6), )

    
    date = property(__date.value, __date.set, None, u'\n            The time the escalation occurred.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'comment'), 'comment', '__httpgenologics_comristep_escalation_request_comment', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 6), )

    
    comment = property(__comment.value, __comment.set, None, u'\n            The comment entered by the user escalating the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    _ElementMap.update({
        __author.name() : __author,
        __reviewer.name() : __reviewer,
        __date.name() : __date,
        __comment.name() : __comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'escalation-request', escalation_request)


# Complex type {http://genologics.com/ri/step}escalation-review with content type ELEMENT_ONLY
class escalation_review (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}escalation-review with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'escalation-review')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 477, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'author'), 'author', '__httpgenologics_comristep_escalation_review_author', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 479, 6), )

    
    author = property(__author.value, __author.set, None, u'\n            The user that actually reviewed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'date'), 'date', '__httpgenologics_comristep_escalation_review_date', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 489, 6), )

    
    date = property(__date.value, __date.set, None, u'\n            The time the reviewer completed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'comment'), 'comment', '__httpgenologics_comristep_escalation_review_comment', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 499, 6), )

    
    comment = property(__comment.value, __comment.set, None, u'\n            The comment entered by the user reviewing the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    _ElementMap.update({
        __author.name() : __author,
        __date.name() : __date,
        __comment.name() : __comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'escalation-review', escalation_review)


# Complex type {http://genologics.com/ri/step}user with content type ELEMENT_ONLY
class user (pyxb.binding.basis.complexTypeDefinition):
    """
        Describes a user as required in the context of step escalations.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'user')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 511, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'first-name'), 'first_name', '__httpgenologics_comristep_user_first_name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 518, 6), )

    
    first_name = property(__first_name.value, __first_name.set, None, u'\n            The first name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last-name'), 'last_name', '__httpgenologics_comristep_user_last_name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 528, 6), )

    
    last_name = property(__last_name.value, __last_name.set, None, u'\n            The last name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_user_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 539, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        __first_name.name() : __first_name,
        __last_name.name() : __last_name
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'user', user)


# Complex type {http://genologics.com/ri/step}step-creation with content type ELEMENT_ONLY
class step_creation_ (pyxb.binding.basis.complexTypeDefinition):
    """
        A request to create a step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'step-creation')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 568, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_step_creation__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 575, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n          ')

    
    # Element container-type uses Python identifier container_type
    __container_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container-type'), 'container_type', '__httpgenologics_comristep_step_creation__container_type', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 582, 6), )

    
    container_type = property(__container_type.value, __container_type.set, None, u'\n            The name of the container type to create an initial on-the-fly container for\nplacing outputs in.\n<br/>Required for POST: Yes if the process has placeable outputs\n          ')

    
    # Element reagent-category uses Python identifier reagent_category
    __reagent_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-category'), 'reagent_category', '__httpgenologics_comristep_step_creation__reagent_category', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 591, 6), )

    
    reagent_category = property(__reagent_category.value, __reagent_category.set, None, u'\n            The name of the reagent category to use for the step.\n<br/>Required for POST: Yes for any reagent addition steps\n          ')

    
    # Element inputs uses Python identifier inputs
    __inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'inputs'), 'inputs', '__httpgenologics_comristep_step_creation__inputs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 599, 6), )

    
    inputs = property(__inputs.value, __inputs.set, None, u'\n            The inputs to the process.\n<br/>Required for POST: Yes\n          ')

    _ElementMap.update({
        __configuration.name() : __configuration,
        __container_type.name() : __container_type,
        __reagent_category.name() : __reagent_category,
        __inputs.name() : __inputs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'step-creation', step_creation_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
            The inputs to the process.
<br/>Required for POST: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 606, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_CTD_ANON_3_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 608, 12), )

    
    input = property(__input.value, __input.set, None, u'\n                  The inputs to the process.\n<br/>Required for POST: Yes\n                ')

    _ElementMap.update({
        __input.name() : __input
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}creation-input with content type EMPTY
class creation_input (pyxb.binding.basis.complexTypeDefinition):
    """
        Typically, provides a URI linking to the input artifact.
Can also be used to designate control sample inputs (via its control type).
One of 'uri' or 'control-type-uri' attributes must be provided, but not both.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'creation-input')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 621, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_creation_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 629, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 629, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the input artifact.\n<br/>Required for POST: Yes (if the input denotes a regular artifact)\n        ')

    
    # Attribute control-type-uri uses Python identifier control_type_uri
    __control_type_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'control-type-uri'), 'control_type_uri', '__httpgenologics_comristep_creation_input_control_type_uri', pyxb.binding.datatypes.anyURI)
    __control_type_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 637, 4)
    __control_type_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 637, 4)
    
    control_type_uri = property(__control_type_uri.value, __control_type_uri.set, None, u'\n          The URI of the control type to use.\n<br/>Required for POST: Yes (if the input denotes a control)\n        ')

    
    # Attribute replicates uses Python identifier replicates
    __replicates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'replicates'), 'replicates', '__httpgenologics_comristep_creation_input_replicates', pyxb.binding.datatypes.long)
    __replicates._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 645, 4)
    __replicates._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 645, 4)
    
    replicates = property(__replicates.value, __replicates.set, None, u'\n          The number of replicates to generate for the input.\n<br/>Required for POST: No; If not specified, defaults to 1.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __control_type_uri.name() : __control_type_uri,
        __replicates.name() : __replicates
    })
Namespace.addCategoryObject('typeBinding', u'creation-input', creation_input)


# Complex type {http://genologics.com/ri/step}details with content type ELEMENT_ONLY
class details_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}details with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'details')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 654, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_details__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 656, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_details__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 664, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element input-output-maps uses Python identifier input_output_maps
    __input_output_maps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input-output-maps'), 'input_output_maps', '__httpgenologics_comristep_details__input_output_maps', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 672, 6), )

    
    input_output_maps = property(__input_output_maps.value, __input_output_maps.set, None, u'\n            Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element fields uses Python identifier fields
    __fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'fields'), 'fields', '__httpgenologics_comristep_details__fields', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 694, 6), )

    
    fields = property(__fields.value, __fields.set, None, u'\n            The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n          ')

    
    # Element preset uses Python identifier preset
    __preset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'preset'), 'preset', '__httpgenologics_comristep_details__preset', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 718, 6), )

    
    preset = property(__preset.value, __preset.set, None, u'\n            The preset name used for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing preset selection will be cleared\n          ')

    
    # Element instrument uses Python identifier instrument
    __instrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'instrument'), 'instrument', '__httpgenologics_comristep_details__instrument', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 728, 6), )

    
    instrument = property(__instrument.value, __instrument.set, None, u'\n            Instrument provides a URI linking to the detailed representation of the instrument for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing instrument selection will be cleared\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_details__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 739, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 739, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Step Details.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __input_output_maps.name() : __input_output_maps,
        __fields.name() : __fields,
        __preset.name() : __preset,
        __instrument.name() : __instrument
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'details', details_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
            Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.
There will be a distinct input-output-map for each pairing of step input to step output.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 680, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input-output-map uses Python identifier input_output_map
    __input_output_map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input-output-map'), 'input_output_map', '__httpgenologics_comristep_CTD_ANON_4_input_output_map', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 682, 12), )

    
    input_output_map = property(__input_output_map.value, __input_output_map.set, None, u'\n                  Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n                ')

    _ElementMap.update({
        __input_output_map.name() : __input_output_map
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
            The user-defined fields of this Step.
<br/>Always returns with GET: No
<br/>Updatable with PUT: Yes
<br/>Required for PUT: No, unless UDFs have been configured as required.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 703, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'field'), 'field', '__httpgenologics_comristep_CTD_ANON_5_field', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 705, 12), )

    
    field = property(__field.value, __field.set, None, u'\n                  The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n                ')

    _ElementMap.update({
        __field.name() : __field
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}input-output-map with content type ELEMENT_ONLY
class input_output_map (pyxb.binding.basis.complexTypeDefinition):
    """
        Input-output-map is a child element of Step and relates one of the Step inputs to one of the outputs that was produced for that input.<br/><br/>
There will be a distinct input-output-map for each pairing of Step input to Step output.
If an input is not mapped to any outputs, the input will be listed with no outputs.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'input-output-map')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 748, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_input_output_map_input', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 757, 6), )

    
    input = property(__input.value, __input.set, None, u'\n            Input provides a URI linking to the input Artifact for the input-output-map.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output'), 'output', '__httpgenologics_comristep_input_output_map_output', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 765, 6), )

    
    output = property(__output.value, __output.set, None, u'\n            Output provides a URI linking to the output Artifact for the input-output-map.\n<br/>Always returns with GET: No\n          ')

    _ElementMap.update({
        __input.name() : __input,
        __output.name() : __output
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'input-output-map', input_output_map)


# Complex type {http://genologics.com/ri/step}instrument with content type SIMPLE
class instrument (pyxb.binding.basis.complexTypeDefinition):
    """
        The instrument element provides a URI to the selected instrument for the step.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'instrument')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 827, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_instrument_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 835, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 835, 8)
    
    uri = property(__uri.value, __uri.set, None, u'\n              The URI of the instrument.\n<br/>Always returns with GET: Yes\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'instrument', instrument)


# Complex type {http://genologics.com/ri/step}placements with content type ELEMENT_ONLY
class placements_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact container placements
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'placements')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 846, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_placements__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 853, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_placements__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 863, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element selected-containers uses Python identifier selected_containers
    __selected_containers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'selected-containers'), 'selected_containers', '__httpgenologics_comristep_placements__selected_containers', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 873, 6), )

    
    selected_containers = property(__selected_containers.value, __selected_containers.set, None, u'\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element output-placements uses Python identifier output_placements
    __output_placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-placements'), 'output_placements', '__httpgenologics_comristep_placements__output_placements', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 897, 6), )

    
    output_placements = property(__output_placements.value, __output_placements.set, None, u'\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_placements__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 922, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 922, 4)
    
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
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 882, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container uses Python identifier container
    __container = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'container'), 'container', '__httpgenologics_comristep_CTD_ANON_6_container', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 884, 12), )

    
    container = property(__container.value, __container.set, None, u'\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ')

    _ElementMap.update({
        __container.name() : __container
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 906, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output-placement uses Python identifier output_placement
    __output_placement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-placement'), 'output_placement', '__httpgenologics_comristep_CTD_ANON_7_output_placement', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 908, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 933, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_container_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 939, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 939, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 950, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__httpgenologics_comristep_output_placement_location', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 957, 6), )

    
    location = property(__location.value, __location.set, None, u'\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_output_placement_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 968, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 968, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 979, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_pools__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 986, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_pools__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 996, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element pooled-inputs uses Python identifier pooled_inputs
    __pooled_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pooled-inputs'), 'pooled_inputs', '__httpgenologics_comristep_pools__pooled_inputs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1006, 6), )

    
    pooled_inputs = property(__pooled_inputs.value, __pooled_inputs.set, None, u'\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element available-inputs uses Python identifier available_inputs
    __available_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'available-inputs'), 'available_inputs', '__httpgenologics_comristep_pools__available_inputs', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1030, 6), )

    
    available_inputs = property(__available_inputs.value, __available_inputs.set, None, u'\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_pools__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1051, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1051, 4)
    
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
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1015, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pool uses Python identifier pool
    __pool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pool'), 'pool', '__httpgenologics_comristep_CTD_ANON_8_pool', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1017, 12), )

    
    pool = property(__pool.value, __pool.set, None, u'\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ')

    _ElementMap.update({
        __pool.name() : __pool
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """
            The available input artifacts for this step.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1037, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_CTD_ANON_9_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1039, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1062, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute replicates uses Python identifier replicates
    __replicates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'replicates'), 'replicates', '__httpgenologics_comristep_input_replicates', pyxb.binding.datatypes.long)
    __replicates._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1078, 4)
    __replicates._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1078, 4)
    
    replicates = property(__replicates.value, __replicates.set, None, u'\n          The number of available replicates for pooling.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __replicates.name() : __replicates
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1089, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpgenologics_comristep_pooled_inputs_input', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1096, 6), )

    
    input = property(__input.value, __input.set, None, u'\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_pooled_inputs_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1107, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1107, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The pool name.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute output-uri uses Python identifier output_uri
    __output_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'output-uri'), 'output_uri', '__httpgenologics_comristep_pooled_inputs_output_uri', pyxb.binding.datatypes.anyURI)
    __output_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1117, 4)
    __output_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1117, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1128, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_program_status__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1135, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_program_status__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1145, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpgenologics_comristep_program_status__status', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1155, 6), )

    
    status = property(__status.value, __status.set, None, u'\n            The nature of the status.\n          ')

    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpgenologics_comristep_program_status__message', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1162, 6), )

    
    message = property(__message.value, __message.set, None, u'\n            The user-facing message for this status.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_program_status__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1170, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1170, 4)
    
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


# Complex type {http://genologics.com/ri/step}reagents-lots with content type ELEMENT_ONLY
class reagents_lots (pyxb.binding.basis.complexTypeDefinition):
    """
        The list representation of a step's reagent lots.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagents-lots')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1192, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_reagents_lots_step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1199, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_reagents_lots_configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n          ')

    
    # Element reagent-lots uses Python identifier reagent_lots
    __reagent_lots = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-lots'), 'reagent_lots', '__httpgenologics_comristep_reagents_lots_reagent_lots', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6), )

    
    reagent_lots = property(__reagent_lots.value, __reagent_lots.set, None, u'\n            The reagent lots for this step.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagents_lots_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1232, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1232, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the StepReagentLots.\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __reagent_lots.name() : __reagent_lots
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'reagents-lots', reagents_lots)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """
            The reagent lots for this step.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1219, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-lot uses Python identifier reagent_lot
    __reagent_lot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-lot'), 'reagent_lot', '__httpgenologics_comristep_CTD_ANON_10_reagent_lot', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 12), )

    
    reagent_lot = property(__reagent_lot.value, __reagent_lot.set, None, u'\n                  The reagent lots for this step.\n                ')

    _ElementMap.update({
        __reagent_lot.name() : __reagent_lot
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}reagent-lot-link with content type EMPTY
class reagent_lot_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to the reagent lot details.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-lot-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1240, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagent_lot_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1246, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1246, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the reagent lot.\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comristep_reagent_lot_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1253, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1253, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The limsid of the reagent lot.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'reagent-lot-link', reagent_lot_link)


# Complex type {http://genologics.com/ri/step}reagents with content type ELEMENT_ONLY
class reagents_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact reagents.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagents')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1261, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_reagents__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1268, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_reagents__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1278, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element reagent-category uses Python identifier reagent_category
    __reagent_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-category'), 'reagent_category', '__httpgenologics_comristep_reagents__reagent_category', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1288, 6), )

    
    reagent_category = property(__reagent_category.value, __reagent_category.set, None, u'\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element output-reagents uses Python identifier output_reagents
    __output_reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-reagents'), 'output_reagents', '__httpgenologics_comristep_reagents__output_reagents', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1298, 6), )

    
    output_reagents = property(__output_reagents.value, __output_reagents.set, None, u'\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_reagents__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 4)
    
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
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """
            The output artifacts for this step.
<br/>Always returns with GET: Yes
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1305, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output'), 'output', '__httpgenologics_comristep_CTD_ANON_11_output', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1307, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1330, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_reagent_label_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1337, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1337, 4)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1348, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-label uses Python identifier reagent_label
    __reagent_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-label'), 'reagent_label', '__httpgenologics_comristep_output_reagent_label', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1355, 6), )

    
    reagent_label = property(__reagent_label.value, __reagent_label.set, None, u'\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_output_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1366, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1366, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        __reagent_label.name() : __reagent_label
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'output', output)


# Complex type {http://genologics.com/ri/step}setup with content type ELEMENT_ONLY
class setup_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}setup with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'setup')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1377, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'step'), 'step', '__httpgenologics_comristep_setup__step', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1379, 6), )

    
    step = property(__step.value, __step.set, None, u'\n            The step (process).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__httpgenologics_comristep_setup__configuration', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1387, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'files'), 'files', '__httpgenologics_comristep_setup__files', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1395, 6), )

    
    files = property(__files.value, __files.set, None, u'\n            Collection of shared result file outputs.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_setup__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1414, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1414, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Step Setup.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __files.name() : __files
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'setup', setup_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """
            Collection of shared result file outputs.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1401, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'file'), 'file', '__httpgenologics_comristep_CTD_ANON_12_file', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1403, 12), )

    
    file = property(__file.value, __file.set, None, u'\n                  Collection of shared result file outputs.\n                ')

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })



# Complex type {http://genologics.com/ri/step}file with content type ELEMENT_ONLY
class file (pyxb.binding.basis.complexTypeDefinition):
    """
        The file element describes a shared result file output that will be displayed in the step-setup view.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'file')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1423, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpgenologics_comristep_file_message', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6), )

    
    message = property(__message.value, __message.set, None, u'\n            The message to display for this shared result file in the step-setup view.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute shared-result-file-index uses Python identifier shared_result_file_index
    __shared_result_file_index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shared-result-file-index'), 'shared_result_file_index', '__httpgenologics_comristep_file_shared_result_file_index', pyxb.binding.datatypes.string)
    __shared_result_file_index._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1439, 4)
    __shared_result_file_index._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1439, 4)
    
    shared_result_file_index = property(__shared_result_file_index.value, __shared_result_file_index.set, None, u'\n          The shared result file output index of the step output.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute artifact-uri uses Python identifier artifact_uri
    __artifact_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'artifact-uri'), 'artifact_uri', '__httpgenologics_comristep_file_artifact_uri', pyxb.binding.datatypes.anyURI)
    __artifact_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1447, 4)
    __artifact_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1447, 4)
    
    artifact_uri = property(__artifact_uri.value, __artifact_uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comristep_file_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1455, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1455, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comristep_file_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1463, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1463, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the file.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        __shared_result_file_index.name() : __shared_result_file_index,
        __artifact_uri.name() : __artifact_uri,
        __limsid.name() : __limsid,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'file', file)


# Complex type {http://genologics.com/ri/step}next-action with content type EMPTY
class next_action (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample next action or step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'next-action')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 330, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute artifact-uri uses Python identifier artifact_uri
    __artifact_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'artifact-uri'), 'artifact_uri', '__httpgenologics_comristep_next_action_artifact_uri', pyxb.binding.datatypes.anyURI)
    __artifact_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 336, 4)
    __artifact_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 336, 4)
    
    artifact_uri = property(__artifact_uri.value, __artifact_uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: no\n<br/>Required for PUT: yes\n        ')

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__httpgenologics_comristep_next_action_action', action_type)
    __action._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 346, 4)
    __action._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 346, 4)
    
    action = property(__action.value, __action.set, None, u'\n          The next action for the sample.\n<br/>Always returns with GET: no; the sample may not have a next action.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the action is not present during an update, the existing action for the sample\nwill be removed if there is one.\n        ')

    
    # Attribute step-uri uses Python identifier step_uri
    __step_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'step-uri'), 'step_uri', '__httpgenologics_comristep_next_action_step_uri', pyxb.binding.datatypes.anyURI)
    __step_uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 357, 4)
    __step_uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 357, 4)
    
    step_uri = property(__step_uri.value, __step_uri.set, None, u'\n          The next protocol step for the sample.\n<br/>Always returns with GET: no; the sample may not have a next step.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the step is not present during an update, the existing step for the sample\nwill be removed if there is one.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __artifact_uri.name() : __artifact_uri,
        __action.name() : __action,
        __step_uri.name() : __step_uri
    })
Namespace.addCategoryObject('typeBinding', u'next-action', next_action)


# Complex type {http://genologics.com/ri/step}artifact with content type EMPTY
class artifact (pyxb.binding.basis.complexTypeDefinition):
    """
        Artifact is a child element of input-output-map and provides a link to an Artifact that was either
an input or output of the Step for the input-output-map.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifact')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 775, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comristep_artifact_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 782, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 782, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comristep_artifact_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 790, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 790, 4)
    
    type = property(__type.value, __type.set, None, u'\n          The type of the Artifact.\n<br/>Always returns with GET: No\n        ')

    
    # Attribute output-generation-type uses Python identifier output_generation_type
    __output_generation_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'output-generation-type'), 'output_generation_type', '__httpgenologics_comristep_artifact_output_generation_type', output_generation_type)
    __output_generation_type._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 798, 4)
    __output_generation_type._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 798, 4)
    
    output_generation_type = property(__output_generation_type.value, __output_generation_type.set, None, u'\n          Specifies how the outputs were generated in relation to the inputs.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comristep_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 806, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 806, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __type.name() : __type,
        __output_generation_type.name() : __output_generation_type,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'artifact', artifact)


step = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'step'), step_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', step.name().localName(), step)

actions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actions'), actions_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', actions.name().localName(), actions)

step_creation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'step-creation'), step_creation_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', step_creation.name().localName(), step_creation)

details = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), details_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', details.name().localName(), details)

placements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'placements'), placements_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', placements.name().localName(), placements)

pools = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pools'), pools_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', pools.name().localName(), pools)

program_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'program-status'), program_status_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 10, 2))
Namespace.addCategoryObject('elementBinding', program_status.name().localName(), program_status)

lots = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lots'), reagents_lots, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', lots.name().localName(), lots)

reagents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reagents'), reagents_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 12, 2))
Namespace.addCategoryObject('elementBinding', reagents.name().localName(), reagents)

setup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'setup'), setup_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 13, 2))
Namespace.addCategoryObject('elementBinding', setup.name().localName(), setup)



step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=step_, documentation=u'\n            The configuration information for the step run.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'actions'), actions_link, scope=step_, documentation=u'\n            The corresponding step actions.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagents'), reagents_link, scope=step_, documentation=u'\n            The corresponding step reagents.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 35, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pools'), pools_link, scope=step_, documentation=u'\n            The corresponding step pools.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 42, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'placements'), placements_link, scope=step_, documentation=u'\n            The corresponding step placements.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 49, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-lots'), reagent_lots_link, scope=step_, documentation=u'\n            The corresponding reagent lots for the step.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 56, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'program-status'), program_status_link, scope=step_, documentation=u'\n            The corresponding step program status, if one exists.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 63, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'setup'), setup_link, scope=step_, documentation=u'\n            The corresponding step setup.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 70, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'details'), details_link, scope=step_, documentation=u'\n            The corresponding step details.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 77, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'available-programs'), CTD_ANON, scope=step_, documentation=u'\n            The programs available for direct triggering on the step.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 84, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 35, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 42, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 49, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 56, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 63, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 70, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 77, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 84, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'actions')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagents')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 35, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'pools')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 42, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'placements')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 49, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-lots')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 56, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'program-status')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 63, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'setup')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 70, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'details')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 77, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, u'available-programs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 84, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
step_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'available-program'), available_program, scope=CTD_ANON, documentation=u'\n                  The programs available for direct triggering on the step.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'available-program')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 92, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=actions_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 273, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=actions_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 283, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-actions'), CTD_ANON_, scope=actions_, documentation=u'\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 293, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'escalation'), escalation, scope=actions_, documentation=u'\n            The escalation details. When a step is under or completed review,\nescalation details include information on who requested the escalation,\nwho attended to it and what samples were escalated.\n<br/>Always returns with GET: No (only available if set)\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No (omitting means clearing the escalation details)\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 315, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 273, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 283, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 293, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 315, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 273, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 283, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-actions')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 293, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, u'escalation')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 315, 6))
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
actions_._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-action'), next_action, scope=CTD_ANON_, documentation=u'\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 303, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 303, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-action')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 303, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'request'), escalation_request, scope=escalation, documentation=u'\n            The escalation request details.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 393, 6)))

escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'review'), escalation_review, scope=escalation, documentation=u'\n            The review details. Only available after review is completed.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 403, 6)))

escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'escalated-artifacts'), CTD_ANON_2, scope=escalation, documentation=u'\n            All samples marked for escalation.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 413, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 393, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 403, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 413, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, u'request')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 393, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, u'review')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 403, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, u'escalated-artifacts')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 413, 6))
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
escalation._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'escalated-artifact'), escalated_artifact, scope=CTD_ANON_2, documentation=u'\n                  All samples marked for escalation.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 421, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 421, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'escalated-artifact')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 421, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'author'), user, scope=escalation_request, documentation=u'\n            The user that originated the escalation.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 435, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reviewer'), user, scope=escalation_request, documentation=u'\n            The reviewer originally requested to review samples.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 445, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'date'), pyxb.binding.datatypes.dateTime, scope=escalation_request, documentation=u'\n            The time the escalation occurred.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 455, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'comment'), pyxb.binding.datatypes.string, scope=escalation_request, documentation=u'\n            The comment entered by the user escalating the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 435, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 445, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 455, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, u'author')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 435, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, u'reviewer')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 445, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, u'date')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 455, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, u'comment')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 465, 6))
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
escalation_request._Automaton = _BuildAutomaton_6()




escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'author'), user, scope=escalation_review, documentation=u'\n            The user that actually reviewed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 479, 6)))

escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'date'), pyxb.binding.datatypes.dateTime, scope=escalation_review, documentation=u'\n            The time the reviewer completed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 489, 6)))

escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'comment'), pyxb.binding.datatypes.string, scope=escalation_review, documentation=u'\n            The comment entered by the user reviewing the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 499, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 479, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 489, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 499, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, u'author')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 479, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, u'date')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 489, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, u'comment')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 499, 6))
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
escalation_review._Automaton = _BuildAutomaton_7()




user._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'first-name'), pyxb.binding.datatypes.string, scope=user, documentation=u'\n            The first name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 518, 6)))

user._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last-name'), pyxb.binding.datatypes.string, scope=user, documentation=u'\n            The last name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 528, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 518, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 528, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(user._UseForTag(pyxb.namespace.ExpandedName(None, u'first-name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 518, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(user._UseForTag(pyxb.namespace.ExpandedName(None, u'last-name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 528, 6))
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
user._Automaton = _BuildAutomaton_8()




step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=step_creation_, documentation=u'\n            The protocol step configuration.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 575, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container-type'), pyxb.binding.datatypes.string, scope=step_creation_, documentation=u'\n            The name of the container type to create an initial on-the-fly container for\nplacing outputs in.\n<br/>Required for POST: Yes if the process has placeable outputs\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 582, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-category'), pyxb.binding.datatypes.string, scope=step_creation_, documentation=u'\n            The name of the reagent category to use for the step.\n<br/>Required for POST: Yes for any reagent addition steps\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 591, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'inputs'), CTD_ANON_3, scope=step_creation_, documentation=u'\n            The inputs to the process.\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 599, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 575, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 582, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 591, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 599, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 575, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, u'container-type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 582, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-category')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 591, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, u'inputs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 599, 6))
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
step_creation_._Automaton = _BuildAutomaton_9()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), creation_input, scope=CTD_ANON_3, documentation=u'\n                  The inputs to the process.\n<br/>Required for POST: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 608, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 608, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 608, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_10()




details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=details_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 656, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=details_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 664, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input-output-maps'), CTD_ANON_4, scope=details_, documentation=u'\n            Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 672, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'fields'), CTD_ANON_5, scope=details_, documentation=u'\n            The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 694, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'preset'), pyxb.binding.datatypes.string, scope=details_, documentation=u'\n            The preset name used for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing preset selection will be cleared\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 718, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'instrument'), instrument, scope=details_, documentation=u'\n            Instrument provides a URI linking to the detailed representation of the instrument for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing instrument selection will be cleared\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 728, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 656, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 664, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 672, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 694, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 718, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 728, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 656, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 664, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'input-output-maps')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 672, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'fields')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 694, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'preset')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 718, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'instrument')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 728, 6))
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
details_._Automaton = _BuildAutomaton_11()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input-output-map'), input_output_map, scope=CTD_ANON_4, documentation=u'\n                  Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 682, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 682, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'input-output-map')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 682, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'field'), _ImportedBinding_userdefined.field_, scope=CTD_ANON_5, documentation=u'\n                  The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 705, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 705, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'field')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 705, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_13()




input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), artifact, scope=input_output_map, documentation=u'\n            Input provides a URI linking to the input Artifact for the input-output-map.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 757, 6)))

input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output'), artifact, scope=input_output_map, documentation=u'\n            Output provides a URI linking to the output Artifact for the input-output-map.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 765, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 757, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 765, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 757, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, u'output')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 765, 6))
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
input_output_map._Automaton = _BuildAutomaton_14()




placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=placements_, documentation=u'\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 853, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=placements_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 863, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'selected-containers'), CTD_ANON_6, scope=placements_, documentation=u'\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 873, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-placements'), CTD_ANON_7, scope=placements_, documentation=u'\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 897, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 853, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 863, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 873, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 897, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 853, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 863, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'selected-containers')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 873, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, u'output-placements')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 897, 6))
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
placements_._Automaton = _BuildAutomaton_15()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'container'), container, scope=CTD_ANON_6, documentation=u'\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 884, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 884, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'container')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 884, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_16()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-placement'), output_placement, scope=CTD_ANON_7, documentation=u'\n                  The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 908, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 908, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'output-placement')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 908, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_17()




output_placement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), _ImportedBinding_ri.location, scope=output_placement, documentation=u'\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 957, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 957, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output_placement._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 957, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output_placement._Automaton = _BuildAutomaton_18()




pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=pools_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 986, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=pools_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 996, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pooled-inputs'), CTD_ANON_8, scope=pools_, documentation=u'\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1006, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'available-inputs'), CTD_ANON_9, scope=pools_, documentation=u'\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1030, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 986, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 996, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1006, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1030, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 986, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 996, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'pooled-inputs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1006, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, u'available-inputs')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1030, 6))
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
pools_._Automaton = _BuildAutomaton_19()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pool'), pooled_inputs, scope=CTD_ANON_8, documentation=u'\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1017, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1017, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'pool')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1017, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_20()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), input, scope=CTD_ANON_9, documentation=u'\n                  The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1039, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1039, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1039, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_21()




pooled_inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'input'), input, scope=pooled_inputs, documentation=u'\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1096, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1096, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pooled_inputs._UseForTag(pyxb.namespace.ExpandedName(None, u'input')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1096, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pooled_inputs._Automaton = _BuildAutomaton_22()




program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=program_status_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1135, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=program_status_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1145, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'), status, scope=program_status_, documentation=u'\n            The nature of the status.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1155, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'message'), pyxb.binding.datatypes.string, scope=program_status_, documentation=u'\n            The user-facing message for this status.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1162, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1135, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1145, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1155, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1162, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1135, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1145, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'status')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1155, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, u'message')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1162, 6))
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
program_status_._Automaton = _BuildAutomaton_23()




reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=reagents_lots, documentation=u'\n            The step (process).\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1199, 6)))

reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=reagents_lots, documentation=u'\n            The protocol step configuration.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6)))

reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-lots'), CTD_ANON_10, scope=reagents_lots, documentation=u'\n            The reagent lots for this step.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1199, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1199, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-lots')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6))
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
reagents_lots._Automaton = _BuildAutomaton_24()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-lot'), reagent_lot_link, scope=CTD_ANON_10, documentation=u'\n                  The reagent lots for this step.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-lot')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_25()




reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=reagents_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1268, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=reagents_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1278, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-category'), pyxb.binding.datatypes.string, scope=reagents_, documentation=u'\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1288, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-reagents'), CTD_ANON_11, scope=reagents_, documentation=u'\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1298, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1268, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1278, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1288, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1298, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1268, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1278, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-category')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1288, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, u'output-reagents')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1298, 6))
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
reagents_._Automaton = _BuildAutomaton_26()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output'), output, scope=CTD_ANON_11, documentation=u'\n                  The output artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1307, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1307, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'output')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1307, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_27()




output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-label'), reagent_label, scope=output, documentation=u'\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1355, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1355, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-label')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1355, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output._Automaton = _BuildAutomaton_28()




setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'step'), _ImportedBinding_ri.link, scope=setup_, documentation=u'\n            The step (process).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1379, 6)))

setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), step_configuration, scope=setup_, documentation=u'\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1387, 6)))

setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'files'), CTD_ANON_12, scope=setup_, documentation=u'\n            Collection of shared result file outputs.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1395, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1379, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1387, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1395, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, u'step')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1379, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1387, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, u'files')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1395, 6))
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
setup_._Automaton = _BuildAutomaton_29()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'file'), file, scope=CTD_ANON_12, documentation=u'\n                  Collection of shared result file outputs.\n                ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1403, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1403, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, u'file')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_30()




file._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'message'), pyxb.binding.datatypes.string, scope=file, documentation=u'\n            The message to display for this shared result file in the step-setup view.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(file._UseForTag(pyxb.namespace.ExpandedName(None, u'message')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
file._Automaton = _BuildAutomaton_31()

