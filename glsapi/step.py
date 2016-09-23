# ./step.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8918431e508ba51505d6101ffc70374ded684580
# Generated 2016-01-12 17:07:14.290617 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/step

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
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/step', create_if_missing=True)
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


# Atomic simple type: {http://genologics.com/ri/step}action-type
class action_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Special actions for samples.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'action-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 600, 2)
    _Documentation = '\n        Special actions for samples.\n      '
action_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=action_type, enum_prefix=None)
action_type.leave = action_type._CF_enumeration.addEnumeration(unicode_value='leave', tag='leave')
action_type.repeat = action_type._CF_enumeration.addEnumeration(unicode_value='repeat', tag='repeat')
action_type.remove = action_type._CF_enumeration.addEnumeration(unicode_value='remove', tag='remove')
action_type.review = action_type._CF_enumeration.addEnumeration(unicode_value='review', tag='review')
action_type.complete = action_type._CF_enumeration.addEnumeration(unicode_value='complete', tag='complete')
action_type.store = action_type._CF_enumeration.addEnumeration(unicode_value='store', tag='store')
action_type.nextstep = action_type._CF_enumeration.addEnumeration(unicode_value='nextstep', tag='nextstep')
action_type.rework = action_type._CF_enumeration.addEnumeration(unicode_value='rework', tag='rework')
action_type.completerepeat = action_type._CF_enumeration.addEnumeration(unicode_value='completerepeat', tag='completerepeat')
action_type.unknown = action_type._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
action_type._InitializeFacetMap(action_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'action-type', action_type)

# Atomic simple type: {http://genologics.com/ri/step}output-generation-type
class output_generation_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The available options for output-type generation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'output-generation-type')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 866, 2)
    _Documentation = '\n        The available options for output-type generation.\n      '
output_generation_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=output_generation_type, enum_prefix=None)
output_generation_type.PerInput = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerInput', tag='PerInput')
output_generation_type.PerAllInputs = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerAllInputs', tag='PerAllInputs')
output_generation_type.PerReagentLabel = output_generation_type._CF_enumeration.addEnumeration(unicode_value='PerReagentLabel', tag='PerReagentLabel')
output_generation_type._InitializeFacetMap(output_generation_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'output-generation-type', output_generation_type)

# Atomic simple type: {http://genologics.com/ri/step}status
class status (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Describes the different natures of status for an external program.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'status')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1229, 2)
    _Documentation = '\n        Describes the different natures of status for an external program.\n      '
status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=status, enum_prefix=None)
status.OK = status._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
status.ERROR = status._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
status.WARNING = status._CF_enumeration.addEnumeration(unicode_value='WARNING', tag='WARNING')
status.RUNNING = status._CF_enumeration.addEnumeration(unicode_value='RUNNING', tag='RUNNING')
status.QUEUED = status._CF_enumeration.addEnumeration(unicode_value='QUEUED', tag='QUEUED')
status._InitializeFacetMap(status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'status', status)

# Complex type {http://genologics.com/ri/step}step with content type ELEMENT_ONLY
class step_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'step')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_step__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The configuration information for the step run.\n          ')

    
    # Element date-started uses Python identifier date_started
    __date_started = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date-started'), 'date_started', '__httpgenologics_comristep_step__date_started', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6), )

    
    date_started = property(__date_started.value, __date_started.set, None, "\n            The started date of the step, in yyyy-MM-dd'T'HH:mm:ss.SSSXXX format.\n<br/>Always returns with GET: Yes\n          ")

    
    # Element date-completed uses Python identifier date_completed
    __date_completed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date-completed'), 'date_completed', '__httpgenologics_comristep_step__date_completed', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 36, 6), )

    
    date_completed = property(__date_completed.value, __date_completed.set, None, "\n            The completed date of the step, in yyyy-MM-dd'T'HH:mm:ss.SSSXXX format.\n<br/>Always returns with GET: No, if the step has not completed, the date-completed will not show.\n          ")

    
    # Element actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'actions'), 'actions', '__httpgenologics_comristep_step__actions', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6), )

    
    actions = property(__actions.value, __actions.set, None, '\n            The corresponding step actions.\n          ')

    
    # Element reagents uses Python identifier reagents
    __reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagents'), 'reagents', '__httpgenologics_comristep_step__reagents', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6), )

    
    reagents = property(__reagents.value, __reagents.set, None, '\n            The corresponding step reagents.\n          ')

    
    # Element pools uses Python identifier pools
    __pools = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pools'), 'pools', '__httpgenologics_comristep_step__pools', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 58, 6), )

    
    pools = property(__pools.value, __pools.set, None, '\n            The corresponding step pools.\n          ')

    
    # Element placements uses Python identifier placements
    __placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'placements'), 'placements', '__httpgenologics_comristep_step__placements', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 65, 6), )

    
    placements = property(__placements.value, __placements.set, None, '\n            The corresponding step placements.\n          ')

    
    # Element reagent-lots uses Python identifier reagent_lots
    __reagent_lots = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-lots'), 'reagent_lots', '__httpgenologics_comristep_step__reagent_lots', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 72, 6), )

    
    reagent_lots = property(__reagent_lots.value, __reagent_lots.set, None, '\n            The corresponding reagent lots for the step.\n          ')

    
    # Element program-status uses Python identifier program_status
    __program_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'program-status'), 'program_status', '__httpgenologics_comristep_step__program_status', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 79, 6), )

    
    program_status = property(__program_status.value, __program_status.set, None, '\n            The corresponding step program status, if one exists.\n          ')

    
    # Element setup uses Python identifier setup
    __setup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'setup'), 'setup', '__httpgenologics_comristep_step__setup', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 86, 6), )

    
    setup = property(__setup.value, __setup.set, None, '\n            The corresponding step setup.\n          ')

    
    # Element details uses Python identifier details
    __details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'details'), 'details', '__httpgenologics_comristep_step__details', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 93, 6), )

    
    details = property(__details.value, __details.set, None, '\n            The corresponding step details.\n          ')

    
    # Element available-programs uses Python identifier available_programs
    __available_programs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'available-programs'), 'available_programs', '__httpgenologics_comristep_step__available_programs', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 100, 6), )

    
    available_programs = property(__available_programs.value, __available_programs.set, None, '\n            The programs available for direct triggering on the step.\n          ')

    
    # Element automatic-next-step uses Python identifier automatic_next_step
    __automatic_next_step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'automatic-next-step'), 'automatic_next_step', '__httpgenologics_comristep_step__automatic_next_step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 118, 6), )

    
    automatic_next_step = property(__automatic_next_step.value, __automatic_next_step.set, None, '\n            The corresponding step that was automatically begun when the\n"Automatically start Next Step" option is enabled in the step\'s configuration.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_step__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 127, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 127, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'limsid'), 'limsid', '__httpgenologics_comristep_step__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 128, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 128, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, '\n          The LIMS ID of the Step/Process.\n        ')

    
    # Attribute current-state uses Python identifier current_state
    __current_state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'current-state'), 'current_state', '__httpgenologics_comristep_step__current_state', pyxb.binding.datatypes.string)
    __current_state._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 135, 4)
    __current_state._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 135, 4)
    
    current_state = property(__current_state.value, __current_state.set, None, '\n          The current state of the step\n        ')

    _ElementMap.update({
        __configuration.name() : __configuration,
        __date_started.name() : __date_started,
        __date_completed.name() : __date_completed,
        __actions.name() : __actions,
        __reagents.name() : __reagents,
        __pools.name() : __pools,
        __placements.name() : __placements,
        __reagent_lots.name() : __reagent_lots,
        __program_status.name() : __program_status,
        __setup.name() : __setup,
        __details.name() : __details,
        __available_programs.name() : __available_programs,
        __automatic_next_step.name() : __automatic_next_step
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid,
        __current_state.name() : __current_state
    })
Namespace.addCategoryObject('typeBinding', 'step', step_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
            The programs available for direct triggering on the step.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 106, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element available-program uses Python identifier available_program
    __available_program = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'available-program'), 'available_program', '__httpgenologics_comristep_CTD_ANON_available_program', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 108, 12), )

    
    available_program = property(__available_program.value, __available_program.set, None, '\n                  The programs available for direct triggering on the step.\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'available-program')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 143, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_available_program_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 149, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 149, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI to execute the program for this step (via POST, with no request entity).\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comristep_available_program_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 156, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 156, 4)
    
    name = property(__name.value, __name.set, None, "\n          The name of the program to execute. Matches the trigger name\n('name' attribute in the 'epp-trigger' element) in the protocol step configuration.\n        ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'available-program', available_program)


# Complex type {http://genologics.com/ri/step}step-configuration with content type SIMPLE
class step_configuration (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the configuration information for the step run.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'step-configuration')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_step_configuration_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 173, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 173, 8)
    
    uri = property(__uri.value, __uri.set, None, '\n              The URI of the protocol step.\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'step-configuration', step_configuration)


# Complex type {http://genologics.com/ri/step}actions-link with content type EMPTY
class actions_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the actions applied or to be applied by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actions-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 183, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_actions_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 189, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 189, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step actions resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'actions-link', actions_link)


# Complex type {http://genologics.com/ri/step}automatic-next-step-link with content type EMPTY
class automatic_next_step_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the step that was automatically begun when the
"Automatically start Next Step" option is enabled in a step's configuration.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'automatic-next-step-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 197, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_automatic_next_step_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 204, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 204, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the corresponding step resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'automatic-next-step-link', automatic_next_step_link)


# Complex type {http://genologics.com/ri/step}details-link with content type EMPTY
class details_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the details for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'details-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 212, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_details_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 218, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 218, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step details resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'details-link', details_link)


# Complex type {http://genologics.com/ri/step}placements-link with content type EMPTY
class placements_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the output placements for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'placements-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_placements_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 232, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 232, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step placements resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'placements-link', placements_link)


# Complex type {http://genologics.com/ri/step}pools-link with content type EMPTY
class pools_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the pools added by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pools-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 240, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_pools_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 246, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 246, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step pools resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'pools-link', pools_link)


# Complex type {http://genologics.com/ri/step}program-status-link with content type EMPTY
class program_status_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the program status for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'program-status-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 254, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_program_status_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 260, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 260, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step program status resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'program-status-link', program_status_link)


# Complex type {http://genologics.com/ri/step}reagent-lots-link with content type EMPTY
class reagent_lots_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the reagent lots for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagent-lots-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 268, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_reagent_lots_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 274, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 274, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the corresponding reagent lots resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'reagent-lots-link', reagent_lots_link)


# Complex type {http://genologics.com/ri/step}reagents-link with content type EMPTY
class reagents_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the reagents added by the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagents-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 282, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_reagents_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 288, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 288, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step reagents resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'reagents-link', reagents_link)


# Complex type {http://genologics.com/ri/step}setup-link with content type EMPTY
class setup_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Identifies the resource that represents the setup for the step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'setup-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 296, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_setup_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 302, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 302, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of corresponding step setup resource.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'setup-link', setup_link)


# Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY
class actions_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}actions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actions')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 310, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_actions__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 312, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_actions__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 322, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element next-actions uses Python identifier next_actions
    __next_actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'next-actions'), 'next_actions', '__httpgenologics_comristep_actions__next_actions', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 332, 6), )

    
    next_actions = property(__next_actions.value, __next_actions.set, None, '\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ')

    
    # Element escalation uses Python identifier escalation
    __escalation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'escalation'), 'escalation', '__httpgenologics_comristep_actions__escalation', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 354, 6), )

    
    escalation = property(__escalation.value, __escalation.set, None, '\n            The escalation details. When a step is under or completed review,\nescalation details include information on who requested the escalation,\nwho attended to it and what samples were escalated.\n<br/>Always returns with GET: No (only available if set)\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No (omitting means clearing the escalation details)\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_actions__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 367, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 367, 4)
    
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
Namespace.addCategoryObject('typeBinding', 'actions', actions_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 340, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element next-action uses Python identifier next_action
    __next_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'next-action'), 'next_action', '__httpgenologics_comristep_CTD_ANON__next_action', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 342, 12), )

    
    next_action = property(__next_action.value, __next_action.set, None, '\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'escalated-artifact')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 419, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_escalated_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 425, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 425, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'escalated-artifact', escalated_artifact)


# Complex type {http://genologics.com/ri/step}escalation with content type ELEMENT_ONLY
class escalation (pyxb.binding.basis.complexTypeDefinition):
    """
        Escalation details.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'escalation')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 436, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element request uses Python identifier request
    __request = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'request'), 'request', '__httpgenologics_comristep_escalation_request', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 443, 6), )

    
    request = property(__request.value, __request.set, None, '\n            The escalation request details.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element review uses Python identifier review
    __review = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'review'), 'review', '__httpgenologics_comristep_escalation_review', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 453, 6), )

    
    review = property(__review.value, __review.set, None, '\n            The review details. Only available after review is completed.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element escalated-artifacts uses Python identifier escalated_artifacts
    __escalated_artifacts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'escalated-artifacts'), 'escalated_artifacts', '__httpgenologics_comristep_escalation_escalated_artifacts', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 463, 6), )

    
    escalated_artifacts = property(__escalated_artifacts.value, __escalated_artifacts.set, None, '\n            All samples marked for escalation.\n          ')

    _ElementMap.update({
        __request.name() : __request,
        __review.name() : __review,
        __escalated_artifacts.name() : __escalated_artifacts
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'escalation', escalation)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
            All samples marked for escalation.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 469, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element escalated-artifact uses Python identifier escalated_artifact
    __escalated_artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'escalated-artifact'), 'escalated_artifact', '__httpgenologics_comristep_CTD_ANON_2_escalated_artifact', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 471, 12), )

    
    escalated_artifact = property(__escalated_artifact.value, __escalated_artifact.set, None, '\n                  All samples marked for escalation.\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'escalation-request')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 483, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'author'), 'author', '__httpgenologics_comristep_escalation_request_author', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 485, 6), )

    
    author = property(__author.value, __author.set, None, '\n            The user that originated the escalation.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element reviewer uses Python identifier reviewer
    __reviewer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reviewer'), 'reviewer', '__httpgenologics_comristep_escalation_request_reviewer', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 495, 6), )

    
    reviewer = property(__reviewer.value, __reviewer.set, None, '\n            The reviewer originally requested to review samples.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__httpgenologics_comristep_escalation_request_date', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 505, 6), )

    
    date = property(__date.value, __date.set, None, '\n            The time the escalation occurred.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__httpgenologics_comristep_escalation_request_comment', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 515, 6), )

    
    comment = property(__comment.value, __comment.set, None, '\n            The comment entered by the user escalating the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    _ElementMap.update({
        __author.name() : __author,
        __reviewer.name() : __reviewer,
        __date.name() : __date,
        __comment.name() : __comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'escalation-request', escalation_request)


# Complex type {http://genologics.com/ri/step}escalation-review with content type ELEMENT_ONLY
class escalation_review (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}escalation-review with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'escalation-review')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 527, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'author'), 'author', '__httpgenologics_comristep_escalation_review_author', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 529, 6), )

    
    author = property(__author.value, __author.set, None, '\n            The user that actually reviewed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__httpgenologics_comristep_escalation_review_date', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6), )

    
    date = property(__date.value, __date.set, None, '\n            The time the reviewer completed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__httpgenologics_comristep_escalation_review_comment', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6), )

    
    comment = property(__comment.value, __comment.set, None, '\n            The comment entered by the user reviewing the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    _ElementMap.update({
        __author.name() : __author,
        __date.name() : __date,
        __comment.name() : __comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'escalation-review', escalation_review)


# Complex type {http://genologics.com/ri/step}user with content type ELEMENT_ONLY
class user (pyxb.binding.basis.complexTypeDefinition):
    """
        Describes a user as required in the context of step escalations.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'user')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 561, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'first-name'), 'first_name', '__httpgenologics_comristep_user_first_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 568, 6), )

    
    first_name = property(__first_name.value, __first_name.set, None, '\n            The first name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'last-name'), 'last_name', '__httpgenologics_comristep_user_last_name', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 578, 6), )

    
    last_name = property(__last_name.value, __last_name.set, None, '\n            The last name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_user_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 589, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 589, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    _ElementMap.update({
        __first_name.name() : __first_name,
        __last_name.name() : __last_name
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'user', user)


# Complex type {http://genologics.com/ri/step}step-creation with content type ELEMENT_ONLY
class step_creation_ (pyxb.binding.basis.complexTypeDefinition):
    """
        A request to create a step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'step-creation')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 619, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_step_creation__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 626, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n          ')

    
    # Element container-type uses Python identifier container_type
    __container_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'container-type'), 'container_type', '__httpgenologics_comristep_step_creation__container_type', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 633, 6), )

    
    container_type = property(__container_type.value, __container_type.set, None, '\n            The name of the container type to create an initial on-the-fly container for\nplacing outputs in.\n<br/>Required for POST: Yes if the process has placeable outputs\n          ')

    
    # Element reagent-category uses Python identifier reagent_category
    __reagent_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-category'), 'reagent_category', '__httpgenologics_comristep_step_creation__reagent_category', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 642, 6), )

    
    reagent_category = property(__reagent_category.value, __reagent_category.set, None, '\n            The name of the reagent category to use for the step.\n<br/>Required for POST: Yes for any reagent addition steps\n          ')

    
    # Element inputs uses Python identifier inputs
    __inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inputs'), 'inputs', '__httpgenologics_comristep_step_creation__inputs', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 650, 6), )

    
    inputs = property(__inputs.value, __inputs.set, None, '\n            The inputs to the process.\n<br/>Required for POST: Yes\n          ')

    _ElementMap.update({
        __configuration.name() : __configuration,
        __container_type.name() : __container_type,
        __reagent_category.name() : __reagent_category,
        __inputs.name() : __inputs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'step-creation', step_creation_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 657, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__httpgenologics_comristep_CTD_ANON_3_input', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 659, 12), )

    
    input = property(__input.value, __input.set, None, '\n                  The inputs to the process.\n<br/>Required for POST: Yes\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'creation-input')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 672, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_creation_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 680, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 680, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the input artifact.\n<br/>Required for POST: Yes (if the input denotes a regular artifact)\n        ')

    
    # Attribute control-type-uri uses Python identifier control_type_uri
    __control_type_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'control-type-uri'), 'control_type_uri', '__httpgenologics_comristep_creation_input_control_type_uri', pyxb.binding.datatypes.anyURI)
    __control_type_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 688, 4)
    __control_type_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 688, 4)
    
    control_type_uri = property(__control_type_uri.value, __control_type_uri.set, None, '\n          The URI of the control type to use.\n<br/>Required for POST: Yes (if the input denotes a control)\n        ')

    
    # Attribute replicates uses Python identifier replicates
    __replicates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'replicates'), 'replicates', '__httpgenologics_comristep_creation_input_replicates', pyxb.binding.datatypes.long)
    __replicates._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 696, 4)
    __replicates._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 696, 4)
    
    replicates = property(__replicates.value, __replicates.set, None, '\n          The number of replicates to generate for the input.\n<br/>Required for POST: No; If not specified, defaults to 1.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __control_type_uri.name() : __control_type_uri,
        __replicates.name() : __replicates
    })
Namespace.addCategoryObject('typeBinding', 'creation-input', creation_input)


# Complex type {http://genologics.com/ri/step}details with content type ELEMENT_ONLY
class details_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}details with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'details')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 705, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_details__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 707, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_details__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 715, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element input-output-maps uses Python identifier input_output_maps
    __input_output_maps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input-output-maps'), 'input_output_maps', '__httpgenologics_comristep_details__input_output_maps', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 723, 6), )

    
    input_output_maps = property(__input_output_maps.value, __input_output_maps.set, None, '\n            Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element fields uses Python identifier fields
    __fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fields'), 'fields', '__httpgenologics_comristep_details__fields', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 745, 6), )

    
    fields = property(__fields.value, __fields.set, None, '\n            The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n          ')

    
    # Element preset uses Python identifier preset
    __preset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'preset'), 'preset', '__httpgenologics_comristep_details__preset', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 769, 6), )

    
    preset = property(__preset.value, __preset.set, None, '\n            The preset name used for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing preset selection will be cleared\n          ')

    
    # Element instrument uses Python identifier instrument
    __instrument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'instrument'), 'instrument', '__httpgenologics_comristep_details__instrument', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 779, 6), )

    
    instrument = property(__instrument.value, __instrument.set, None, '\n            Instrument provides a URI linking to the detailed representation of the instrument for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing instrument selection will be cleared\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_details__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 790, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 790, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Step Details.\n<br/>Always returns with GET: Yes\n        ')

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
Namespace.addCategoryObject('typeBinding', 'details', details_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 731, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input-output-map uses Python identifier input_output_map
    __input_output_map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input-output-map'), 'input_output_map', '__httpgenologics_comristep_CTD_ANON_4_input_output_map', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 733, 12), )

    
    input_output_map = property(__input_output_map.value, __input_output_map.set, None, '\n                  Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n                ')

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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 754, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'field'), 'field', '__httpgenologics_comristep_CTD_ANON_5_field', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 756, 12), )

    
    field = property(__field.value, __field.set, None, '\n                  The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'input-output-map')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 799, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__httpgenologics_comristep_input_output_map_input', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 808, 6), )

    
    input = property(__input.value, __input.set, None, '\n            Input provides a URI linking to the input Artifact for the input-output-map.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output'), 'output', '__httpgenologics_comristep_input_output_map_output', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 816, 6), )

    
    output = property(__output.value, __output.set, None, '\n            Output provides a URI linking to the output Artifact for the input-output-map.\n<br/>Always returns with GET: No\n          ')

    _ElementMap.update({
        __input.name() : __input,
        __output.name() : __output
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'input-output-map', input_output_map)


# Complex type {http://genologics.com/ri/step}instrument with content type SIMPLE
class instrument (pyxb.binding.basis.complexTypeDefinition):
    """
        The instrument element provides a URI to the selected instrument for the step.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'instrument')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 878, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_instrument_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 886, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 886, 8)
    
    uri = property(__uri.value, __uri.set, None, '\n              The URI of the instrument.\n<br/>Always returns with GET: Yes\n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'instrument', instrument)


# Complex type {http://genologics.com/ri/step}placements with content type ELEMENT_ONLY
class placements_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact container placements
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'placements')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 897, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_placements__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 904, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_placements__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 914, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element selected-containers uses Python identifier selected_containers
    __selected_containers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'selected-containers'), 'selected_containers', '__httpgenologics_comristep_placements__selected_containers', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 924, 6), )

    
    selected_containers = property(__selected_containers.value, __selected_containers.set, None, '\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Element output-placements uses Python identifier output_placements
    __output_placements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-placements'), 'output_placements', '__httpgenologics_comristep_placements__output_placements', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 948, 6), )

    
    output_placements = property(__output_placements.value, __output_placements.set, None, '\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_placements__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 973, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 973, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __selected_containers.name() : __selected_containers,
        __output_placements.name() : __output_placements
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'placements', placements_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 933, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element container uses Python identifier container
    __container = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'container'), 'container', '__httpgenologics_comristep_CTD_ANON_6_container', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 935, 12), )

    
    container = property(__container.value, __container.set, None, '\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ')

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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 957, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output-placement uses Python identifier output_placement
    __output_placement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-placement'), 'output_placement', '__httpgenologics_comristep_CTD_ANON_7_output_placement', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 959, 12), )

    
    output_placement = property(__output_placement.value, __output_placement.set, None, '\n                  The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'container')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 984, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_container_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 990, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 990, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the container.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'container', container)


# Complex type {http://genologics.com/ri/step}output-placement with content type ELEMENT_ONLY
class output_placement (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to the output artifact and container placement.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'output-placement')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1001, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__httpgenologics_comristep_output_placement_location', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1008, 6), )

    
    location = property(__location.value, __location.set, None, '\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_output_placement_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1019, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1019, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'output-placement', output_placement)


# Complex type {http://genologics.com/ri/step}pools with content type ELEMENT_ONLY
class pools_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's pooled inputs.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pools')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1030, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_pools__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1037, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_pools__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1047, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element pooled-inputs uses Python identifier pooled_inputs
    __pooled_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pooled-inputs'), 'pooled_inputs', '__httpgenologics_comristep_pools__pooled_inputs', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1057, 6), )

    
    pooled_inputs = property(__pooled_inputs.value, __pooled_inputs.set, None, '\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ')

    
    # Element available-inputs uses Python identifier available_inputs
    __available_inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'available-inputs'), 'available_inputs', '__httpgenologics_comristep_pools__available_inputs', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1081, 6), )

    
    available_inputs = property(__available_inputs.value, __available_inputs.set, None, '\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_pools__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1102, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1102, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the StepPools.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __pooled_inputs.name() : __pooled_inputs,
        __available_inputs.name() : __available_inputs
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'pools', pools_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1066, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pool uses Python identifier pool
    __pool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pool'), 'pool', '__httpgenologics_comristep_CTD_ANON_8_pool', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 12), )

    
    pool = property(__pool.value, __pool.set, None, '\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ')

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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1088, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__httpgenologics_comristep_CTD_ANON_9_input', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1090, 12), )

    
    input = property(__input.value, __input.set, None, '\n                  The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'input')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_input_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1119, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1119, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute replicates uses Python identifier replicates
    __replicates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'replicates'), 'replicates', '__httpgenologics_comristep_input_replicates', pyxb.binding.datatypes.long)
    __replicates._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1129, 4)
    __replicates._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1129, 4)
    
    replicates = property(__replicates.value, __replicates.set, None, '\n          The number of available replicates for pooling.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __replicates.name() : __replicates
    })
Namespace.addCategoryObject('typeBinding', 'input', input)


# Complex type {http://genologics.com/ri/step}pooled-inputs with content type ELEMENT_ONLY
class pooled_inputs (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides pooled input groups.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pooled-inputs')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1140, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__httpgenologics_comristep_pooled_inputs_input', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1147, 6), )

    
    input = property(__input.value, __input.set, None, '\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comristep_pooled_inputs_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1158, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1158, 4)
    
    name = property(__name.value, __name.set, None, '\n          The pool name.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute output-uri uses Python identifier output_uri
    __output_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'output-uri'), 'output_uri', '__httpgenologics_comristep_pooled_inputs_output_uri', pyxb.binding.datatypes.anyURI)
    __output_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1168, 4)
    __output_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1168, 4)
    
    output_uri = property(__output_uri.value, __output_uri.set, None, '\n          The URI of the pooled output artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __input.name() : __input
    })
    _AttributeMap.update({
        __name.name() : __name,
        __output_uri.name() : __output_uri
    })
Namespace.addCategoryObject('typeBinding', 'pooled-inputs', pooled_inputs)


# Complex type {http://genologics.com/ri/step}program-status with content type ELEMENT_ONLY
class program_status_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The current EPP status for a step (supports automatically triggered programs only).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'program-status')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_program_status__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1186, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_program_status__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1196, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpgenologics_comristep_program_status__status', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6), )

    
    status = property(__status.value, __status.set, None, '\n            The nature of the status.\n          ')

    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpgenologics_comristep_program_status__message', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6), )

    
    message = property(__message.value, __message.set, None, '\n            The user-facing message for this status.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_program_status__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1221, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI to this status.\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __status.name() : __status,
        __message.name() : __message
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'program-status', program_status_)


# Complex type {http://genologics.com/ri/step}reagents-lots with content type ELEMENT_ONLY
class reagents_lots (pyxb.binding.basis.complexTypeDefinition):
    """
        The list representation of a step's reagent lots.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagents-lots')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_reagents_lots_step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1250, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_reagents_lots_configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1257, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n          ')

    
    # Element reagent-lots uses Python identifier reagent_lots
    __reagent_lots = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-lots'), 'reagent_lots', '__httpgenologics_comristep_reagents_lots_reagent_lots', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1264, 6), )

    
    reagent_lots = property(__reagent_lots.value, __reagent_lots.set, None, '\n            The reagent lots for this step.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_reagents_lots_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1283, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1283, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the StepReagentLots.\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __reagent_lots.name() : __reagent_lots
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'reagents-lots', reagents_lots)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """
            The reagent lots for this step.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1270, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-lot uses Python identifier reagent_lot
    __reagent_lot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-lot'), 'reagent_lot', '__httpgenologics_comristep_CTD_ANON_10_reagent_lot', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1272, 12), )

    
    reagent_lot = property(__reagent_lot.value, __reagent_lot.set, None, '\n                  The reagent lots for this step.\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagent-lot-link')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1291, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_reagent_lot_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1297, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1297, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the reagent lot.\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'limsid'), 'limsid', '__httpgenologics_comristep_reagent_lot_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1304, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1304, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, '\n          The limsid of the reagent lot.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', 'reagent-lot-link', reagent_lot_link)


# Complex type {http://genologics.com/ri/step}reagents with content type ELEMENT_ONLY
class reagents_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of a step's output artifact reagents.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagents')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1312, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_reagents__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_reagents__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1329, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element reagent-category uses Python identifier reagent_category
    __reagent_category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-category'), 'reagent_category', '__httpgenologics_comristep_reagents__reagent_category', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1339, 6), )

    
    reagent_category = property(__reagent_category.value, __reagent_category.set, None, '\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ')

    
    # Element output-reagents uses Python identifier output_reagents
    __output_reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-reagents'), 'output_reagents', '__httpgenologics_comristep_reagents__output_reagents', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1349, 6), )

    
    output_reagents = property(__output_reagents.value, __output_reagents.set, None, '\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_reagents__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1370, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1370, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the StepReagents.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __reagent_category.name() : __reagent_category,
        __output_reagents.name() : __output_reagents
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'reagents', reagents_)


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
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1356, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output'), 'output', '__httpgenologics_comristep_CTD_ANON_11_output', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1358, 12), )

    
    output = property(__output.value, __output.set, None, '\n                  The output artifacts for this step.\n<br/>Always returns with GET: Yes\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reagent-label')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1381, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comristep_reagent_label_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1388, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1388, 4)
    
    name = property(__name.value, __name.set, None, '\n          The reagent label name for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a reagent label.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'reagent-label', reagent_label)


# Complex type {http://genologics.com/ri/step}output with content type ELEMENT_ONLY
class output (pyxb.binding.basis.complexTypeDefinition):
    """
        Provides a URI linking to the output artifact and reagent label.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'output')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1399, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reagent-label uses Python identifier reagent_label
    __reagent_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reagent-label'), 'reagent_label', '__httpgenologics_comristep_output_reagent_label', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1406, 6), )

    
    reagent_label = property(__reagent_label.value, __reagent_label.set, None, '\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_output_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1417, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1417, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: Yes\n        ')

    _ElementMap.update({
        __reagent_label.name() : __reagent_label
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'output', output)


# Complex type {http://genologics.com/ri/step}setup with content type ELEMENT_ONLY
class setup_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/step}setup with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'setup')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1428, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__httpgenologics_comristep_setup__step', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6), )

    
    step = property(__step.value, __step.set, None, '\n            The step (process).\n<br/>Always returns with GET: Yes\n          ')

    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'configuration'), 'configuration', '__httpgenologics_comristep_setup__configuration', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1438, 6), )

    
    configuration = property(__configuration.value, __configuration.set, None, '\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ')

    
    # Element files uses Python identifier files
    __files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'files'), 'files', '__httpgenologics_comristep_setup__files', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1446, 6), )

    
    files = property(__files.value, __files.set, None, '\n            Collection of shared result file outputs.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_setup__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1465, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1465, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the Step Setup.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __step.name() : __step,
        __configuration.name() : __configuration,
        __files.name() : __files
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'setup', setup_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """
            Collection of shared result file outputs.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1452, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__httpgenologics_comristep_CTD_ANON_12_file', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1454, 12), )

    
    file = property(__file.value, __file.set, None, '\n                  Collection of shared result file outputs.\n                ')

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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'file')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1474, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpgenologics_comristep_file_message', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1481, 6), )

    
    message = property(__message.value, __message.set, None, '\n            The message to display for this shared result file in the step-setup view.\n<br/>Always returns with GET: Yes\n          ')

    
    # Attribute shared-result-file-index uses Python identifier shared_result_file_index
    __shared_result_file_index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shared-result-file-index'), 'shared_result_file_index', '__httpgenologics_comristep_file_shared_result_file_index', pyxb.binding.datatypes.string)
    __shared_result_file_index._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1490, 4)
    __shared_result_file_index._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1490, 4)
    
    shared_result_file_index = property(__shared_result_file_index.value, __shared_result_file_index.set, None, '\n          The shared result file output index of the step output.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute artifact-uri uses Python identifier artifact_uri
    __artifact_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artifact-uri'), 'artifact_uri', '__httpgenologics_comristep_file_artifact_uri', pyxb.binding.datatypes.anyURI)
    __artifact_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1498, 4)
    __artifact_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1498, 4)
    
    artifact_uri = property(__artifact_uri.value, __artifact_uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'limsid'), 'limsid', '__httpgenologics_comristep_file_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1506, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1506, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, '\n          The LIMS ID of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpgenologics_comristep_file_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1514, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1514, 4)
    
    name = property(__name.value, __name.set, None, '\n          The name of the file.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        __shared_result_file_index.name() : __shared_result_file_index,
        __artifact_uri.name() : __artifact_uri,
        __limsid.name() : __limsid,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'file', file)


# Complex type {http://genologics.com/ri/step}next-action with content type EMPTY
class next_action (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample next action or step.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'next-action')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 369, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute artifact-uri uses Python identifier artifact_uri
    __artifact_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artifact-uri'), 'artifact_uri', '__httpgenologics_comristep_next_action_artifact_uri', pyxb.binding.datatypes.anyURI)
    __artifact_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 375, 4)
    __artifact_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 375, 4)
    
    artifact_uri = property(__artifact_uri.value, __artifact_uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: no\n<br/>Required for PUT: yes\n        ')

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action'), 'action', '__httpgenologics_comristep_next_action_action', action_type)
    __action._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 385, 4)
    __action._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 385, 4)
    
    action = property(__action.value, __action.set, None, '\n          The next action for the sample.\n<br/>Always returns with GET: no; the sample may not have a next action.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the action is not present during an update, the existing action for the sample\nwill be removed if there is one.\n        ')

    
    # Attribute step-uri uses Python identifier step_uri
    __step_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'step-uri'), 'step_uri', '__httpgenologics_comristep_next_action_step_uri', pyxb.binding.datatypes.anyURI)
    __step_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 396, 4)
    __step_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 396, 4)
    
    step_uri = property(__step_uri.value, __step_uri.set, None, '\n          The next protocol step for the sample.\n<br/>Always returns with GET: no; the sample may not have a next step.\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the step is not present during an update, the existing step for the sample\nwill be removed if there is one.\n        ')

    
    # Attribute rework-step-uri uses Python identifier rework_step_uri
    __rework_step_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rework-step-uri'), 'rework_step_uri', '__httpgenologics_comristep_next_action_rework_step_uri', pyxb.binding.datatypes.anyURI)
    __rework_step_uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 407, 4)
    __rework_step_uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 407, 4)
    
    rework_step_uri = property(__rework_step_uri.value, __rework_step_uri.set, None, '\n          The rework step instance uri (ie http://severname:8080/api/v2/steps/{ID}) for the sample.\n<br/>Always returns with GET: no; the sample may not have a rework step\n<br/>Updatable with PUT: yes\n<br/>Required for PUT. If the rework step is not present during an update, the existing rework step for the sample\nwill be removed if there is one.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __artifact_uri.name() : __artifact_uri,
        __action.name() : __action,
        __step_uri.name() : __step_uri,
        __rework_step_uri.name() : __rework_step_uri
    })
Namespace.addCategoryObject('typeBinding', 'next-action', next_action)


# Complex type {http://genologics.com/ri/step}artifact with content type EMPTY
class artifact (pyxb.binding.basis.complexTypeDefinition):
    """
        Artifact is a child element of input-output-map and provides a link to an Artifact that was either
an input or output of the Step for the input-output-map.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'artifact')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 826, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'limsid'), 'limsid', '__httpgenologics_comristep_artifact_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 833, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 833, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, '\n          The LIMS ID of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpgenologics_comristep_artifact_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 841, 4)
    __type._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 841, 4)
    
    type = property(__type.value, __type.set, None, '\n          The type of the Artifact.\n<br/>Always returns with GET: No\n        ')

    
    # Attribute output-generation-type uses Python identifier output_generation_type
    __output_generation_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'output-generation-type'), 'output_generation_type', '__httpgenologics_comristep_artifact_output_generation_type', output_generation_type)
    __output_generation_type._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 849, 4)
    __output_generation_type._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 849, 4)
    
    output_generation_type = property(__output_generation_type.value, __output_generation_type.set, None, '\n          Specifies how the outputs were generated in relation to the inputs.\n<br/>Always returns with GET: Yes\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comristep_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 857, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 857, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __type.name() : __type,
        __output_generation_type.name() : __output_generation_type,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', 'artifact', artifact)


step = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'step'), step_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', step.name().localName(), step)

actions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), actions_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', actions.name().localName(), actions)

step_creation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'step-creation'), step_creation_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', step_creation.name().localName(), step_creation)

details = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'details'), details_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', details.name().localName(), details)

placements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'placements'), placements_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', placements.name().localName(), placements)

pools = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pools'), pools_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', pools.name().localName(), pools)

program_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'program-status'), program_status_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 10, 2))
Namespace.addCategoryObject('elementBinding', program_status.name().localName(), program_status)

lots = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lots'), reagents_lots, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', lots.name().localName(), lots)

reagents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reagents'), reagents_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 12, 2))
Namespace.addCategoryObject('elementBinding', reagents.name().localName(), reagents)

setup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'setup'), setup_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 13, 2))
Namespace.addCategoryObject('elementBinding', setup.name().localName(), setup)



step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=step_, documentation='\n            The configuration information for the step run.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date-started'), pyxb.binding.datatypes.dateTime, scope=step_, documentation="\n            The started date of the step, in yyyy-MM-dd'T'HH:mm:ss.SSSXXX format.\n<br/>Always returns with GET: Yes\n          ", location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date-completed'), pyxb.binding.datatypes.dateTime, scope=step_, documentation="\n            The completed date of the step, in yyyy-MM-dd'T'HH:mm:ss.SSSXXX format.\n<br/>Always returns with GET: No, if the step has not completed, the date-completed will not show.\n          ", location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 36, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'actions'), actions_link, scope=step_, documentation='\n            The corresponding step actions.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagents'), reagents_link, scope=step_, documentation='\n            The corresponding step reagents.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pools'), pools_link, scope=step_, documentation='\n            The corresponding step pools.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 58, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'placements'), placements_link, scope=step_, documentation='\n            The corresponding step placements.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 65, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-lots'), reagent_lots_link, scope=step_, documentation='\n            The corresponding reagent lots for the step.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 72, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'program-status'), program_status_link, scope=step_, documentation='\n            The corresponding step program status, if one exists.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 79, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'setup'), setup_link, scope=step_, documentation='\n            The corresponding step setup.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 86, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'details'), details_link, scope=step_, documentation='\n            The corresponding step details.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 93, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'available-programs'), CTD_ANON, scope=step_, documentation='\n            The programs available for direct triggering on the step.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 100, 6)))

step_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'automatic-next-step'), automatic_next_step_link, scope=step_, documentation='\n            The corresponding step that was automatically begun when the\n"Automatically start Next Step" option is enabled in the step\'s configuration.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 118, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 36, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 58, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 65, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 72, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 79, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 86, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 93, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 100, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 118, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'date-started')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 28, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'date-completed')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 36, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'actions')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 44, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'reagents')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 51, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'pools')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 58, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'placements')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 65, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-lots')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 72, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'program-status')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 79, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'setup')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 86, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'details')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 93, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'available-programs')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 100, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(step_._UseForTag(pyxb.namespace.ExpandedName(None, 'automatic-next-step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 118, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
step_._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'available-program'), available_program, scope=CTD_ANON, documentation='\n                  The programs available for direct triggering on the step.\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 108, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 108, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'available-program')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 108, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=actions_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 312, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=actions_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 322, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'next-actions'), CTD_ANON_, scope=actions_, documentation='\n            All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 332, 6)))

actions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'escalation'), escalation, scope=actions_, documentation='\n            The escalation details. When a step is under or completed review,\nescalation details include information on who requested the escalation,\nwho attended to it and what samples were escalated.\n<br/>Always returns with GET: No (only available if set)\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No (omitting means clearing the escalation details)\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 354, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 312, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 322, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 332, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 354, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 312, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 322, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, 'next-actions')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 332, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(actions_._UseForTag(pyxb.namespace.ExpandedName(None, 'escalation')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 354, 6))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'next-action'), next_action, scope=CTD_ANON_, documentation='\n                  All samples belong to one step; these samples can move forward for another configured step work\nor need special handling, such as remove from the workflow they are in, leave in their existing\nqueue for rework, or require view by a manager, etc...\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 342, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 342, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'next-action')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 342, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'request'), escalation_request, scope=escalation, documentation='\n            The escalation request details.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 443, 6)))

escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'review'), escalation_review, scope=escalation, documentation='\n            The review details. Only available after review is completed.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 453, 6)))

escalation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'escalated-artifacts'), CTD_ANON_2, scope=escalation, documentation='\n            All samples marked for escalation.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 463, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 443, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 453, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 463, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, 'request')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 443, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, 'review')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 453, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation._UseForTag(pyxb.namespace.ExpandedName(None, 'escalated-artifacts')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 463, 6))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'escalated-artifact'), escalated_artifact, scope=CTD_ANON_2, documentation='\n                  All samples marked for escalation.\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 471, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 471, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'escalated-artifact')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 471, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'author'), user, scope=escalation_request, documentation='\n            The user that originated the escalation.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 485, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reviewer'), user, scope=escalation_request, documentation='\n            The reviewer originally requested to review samples.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 495, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date'), pyxb.binding.datatypes.dateTime, scope=escalation_request, documentation='\n            The time the escalation occurred.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 505, 6)))

escalation_request._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'comment'), pyxb.binding.datatypes.string, scope=escalation_request, documentation='\n            The comment entered by the user escalating the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 515, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 485, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 495, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 505, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 515, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, 'author')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 485, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, 'reviewer')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 495, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, 'date')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 505, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(escalation_request._UseForTag(pyxb.namespace.ExpandedName(None, 'comment')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 515, 6))
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




escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'author'), user, scope=escalation_review, documentation='\n            The user that actually reviewed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 529, 6)))

escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'date'), pyxb.binding.datatypes.dateTime, scope=escalation_review, documentation='\n            The time the reviewer completed the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6)))

escalation_review._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'comment'), pyxb.binding.datatypes.string, scope=escalation_review, documentation='\n            The comment entered by the user reviewing the step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 529, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, 'author')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 529, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, 'date')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 539, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(escalation_review._UseForTag(pyxb.namespace.ExpandedName(None, 'comment')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 549, 6))
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




user._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'first-name'), pyxb.binding.datatypes.string, scope=user, documentation='\n            The first name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 568, 6)))

user._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'last-name'), pyxb.binding.datatypes.string, scope=user, documentation='\n            The last name of the user.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 578, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 568, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 578, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(user._UseForTag(pyxb.namespace.ExpandedName(None, 'first-name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 568, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(user._UseForTag(pyxb.namespace.ExpandedName(None, 'last-name')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 578, 6))
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




step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=step_creation_, documentation='\n            The protocol step configuration.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 626, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'container-type'), pyxb.binding.datatypes.string, scope=step_creation_, documentation='\n            The name of the container type to create an initial on-the-fly container for\nplacing outputs in.\n<br/>Required for POST: Yes if the process has placeable outputs\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 633, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-category'), pyxb.binding.datatypes.string, scope=step_creation_, documentation='\n            The name of the reagent category to use for the step.\n<br/>Required for POST: Yes for any reagent addition steps\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 642, 6)))

step_creation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inputs'), CTD_ANON_3, scope=step_creation_, documentation='\n            The inputs to the process.\n<br/>Required for POST: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 650, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 626, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 633, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 642, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 650, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 626, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, 'container-type')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 633, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-category')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 642, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(step_creation_._UseForTag(pyxb.namespace.ExpandedName(None, 'inputs')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 650, 6))
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




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), creation_input, scope=CTD_ANON_3, documentation='\n                  The inputs to the process.\n<br/>Required for POST: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 659, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 659, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 659, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_10()




details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=details_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 707, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=details_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 715, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input-output-maps'), CTD_ANON_4, scope=details_, documentation='\n            Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 723, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fields'), CTD_ANON_5, scope=details_, documentation='\n            The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 745, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'preset'), pyxb.binding.datatypes.string, scope=details_, documentation='\n            The preset name used for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing preset selection will be cleared\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 769, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'instrument'), instrument, scope=details_, documentation='\n            Instrument provides a URI linking to the detailed representation of the instrument for the step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, if not provided, an existing instrument selection will be cleared\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 779, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 707, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 715, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 723, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 745, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 769, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 779, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 707, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 715, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'input-output-maps')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 723, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'fields')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 745, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'preset')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 769, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, 'instrument')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 779, 6))
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




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input-output-map'), input_output_map, scope=CTD_ANON_4, documentation='\n                  Each input-output-map relates one of the step inputs to one of the outputs that was produced for that input.\nThere will be a distinct input-output-map for each pairing of step input to step output.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 733, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 733, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'input-output-map')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 733, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'field'), _ImportedBinding_userdefined.field_, scope=CTD_ANON_5, documentation='\n                  The user-defined fields of this Step.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless UDFs have been configured as required.\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 756, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 756, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'field')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 756, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_13()




input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), artifact, scope=input_output_map, documentation='\n            Input provides a URI linking to the input Artifact for the input-output-map.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 808, 6)))

input_output_map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output'), artifact, scope=input_output_map, documentation='\n            Output provides a URI linking to the output Artifact for the input-output-map.\n<br/>Always returns with GET: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 816, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 808, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 816, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 808, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(input_output_map._UseForTag(pyxb.namespace.ExpandedName(None, 'output')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 816, 6))
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




placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=placements_, documentation='\n            The protocol step of the StepPlacements.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 904, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=placements_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 914, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'selected-containers'), CTD_ANON_6, scope=placements_, documentation='\n            The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 924, 6)))

placements_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-placements'), CTD_ANON_7, scope=placements_, documentation='\n            The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 948, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 904, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 914, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 924, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 948, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 904, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 914, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, 'selected-containers')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 924, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(placements_._UseForTag(pyxb.namespace.ExpandedName(None, 'output-placements')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 948, 6))
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




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'container'), container, scope=CTD_ANON_6, documentation='\n                  The selected containers for step placement.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 935, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 935, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'container')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 935, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_16()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-placement'), output_placement, scope=CTD_ANON_7, documentation='\n                  The output artifacts for this step with placement if they have one.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 959, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 959, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'output-placement')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 959, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_17()




output_placement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), _ImportedBinding_ri.location, scope=output_placement, documentation='\n            The container placement for the artifact.\n<br/>Always returns with GET: No; the artifact may not have a placement.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, any existing placement will be replaced with the new placement. If not specified, any existing placement will be removed.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1008, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1008, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output_placement._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1008, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output_placement._Automaton = _BuildAutomaton_18()




pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=pools_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1037, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=pools_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1047, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pooled-inputs'), CTD_ANON_8, scope=pools_, documentation='\n            The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1057, 6)))

pools_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'available-inputs'), CTD_ANON_9, scope=pools_, documentation='\n            The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1081, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1037, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1047, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1057, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1081, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1037, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1047, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, 'pooled-inputs')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1057, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pools_._UseForTag(pyxb.namespace.ExpandedName(None, 'available-inputs')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1081, 6))
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




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pool'), pooled_inputs, scope=CTD_ANON_8, documentation='\n                  The pooled input artifacts for this step.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'pool')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1068, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_20()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), input, scope=CTD_ANON_9, documentation='\n                  The available input artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1090, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1090, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1090, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_21()




pooled_inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), input, scope=pooled_inputs, documentation='\n            The pooled input artifacts for this pool.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1147, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1147, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pooled_inputs._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1147, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pooled_inputs._Automaton = _BuildAutomaton_22()




program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=program_status_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1186, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=program_status_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1196, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'status'), status, scope=program_status_, documentation='\n            The nature of the status.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6)))

program_status_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message'), pyxb.binding.datatypes.string, scope=program_status_, documentation='\n            The user-facing message for this status.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1186, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1196, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1186, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1196, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, 'status')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1206, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(program_status_._UseForTag(pyxb.namespace.ExpandedName(None, 'message')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1213, 6))
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




reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=reagents_lots, documentation='\n            The step (process).\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1250, 6)))

reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=reagents_lots, documentation='\n            The protocol step configuration.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1257, 6)))

reagents_lots._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-lots'), CTD_ANON_10, scope=reagents_lots, documentation='\n            The reagent lots for this step.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1264, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1250, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1257, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1264, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1250, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1257, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagents_lots._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-lots')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1264, 6))
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




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-lot'), reagent_lot_link, scope=CTD_ANON_10, documentation='\n                  The reagent lots for this step.\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1272, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1272, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-lot')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1272, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_25()




reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=reagents_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=reagents_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1329, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-category'), pyxb.binding.datatypes.string, scope=reagents_, documentation='\n            The permitted reagent category of the step. Reagent labels used in the POST must be from this reagent category.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1339, 6)))

reagents_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-reagents'), CTD_ANON_11, scope=reagents_, documentation='\n            The output artifacts for this step.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1349, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1329, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1339, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1349, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1319, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1329, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-category')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1339, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(reagents_._UseForTag(pyxb.namespace.ExpandedName(None, 'output-reagents')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1349, 6))
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




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output'), output, scope=CTD_ANON_11, documentation='\n                  The output artifacts for this step.\n<br/>Always returns with GET: Yes\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1358, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1358, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'output')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1358, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_27()




output._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reagent-label'), reagent_label, scope=output, documentation='\n            The reagent labels for the artifact.\n<br/>Always returns with GET: No; the artifact may not have reagent labels.\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No; If specified, an existing reagent label will be replaced with the new label. If not specified, existing labels will be removed.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1406, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1406, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(output._UseForTag(pyxb.namespace.ExpandedName(None, 'reagent-label')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1406, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
output._Automaton = _BuildAutomaton_28()




setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), _ImportedBinding_ri.link, scope=setup_, documentation='\n            The step (process).\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6)))

setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'configuration'), step_configuration, scope=setup_, documentation='\n            The protocol step configuration.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1438, 6)))

setup_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'files'), CTD_ANON_12, scope=setup_, documentation='\n            Collection of shared result file outputs.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1446, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1438, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1446, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1430, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, 'configuration')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1438, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(setup_._UseForTag(pyxb.namespace.ExpandedName(None, 'files')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1446, 6))
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




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), file, scope=CTD_ANON_12, documentation='\n                  Collection of shared result file outputs.\n                ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1454, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1454, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1454, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_30()




file._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message'), pyxb.binding.datatypes.string, scope=file, documentation='\n            The message to display for this shared result file in the step-setup view.\n<br/>Always returns with GET: Yes\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1481, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1481, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(file._UseForTag(pyxb.namespace.ExpandedName(None, 'message')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/step.xsd', 1481, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
file._Automaton = _BuildAutomaton_31()

