# ./ver.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:381c942b531cca3d7411c1ea854e1a0cdf36777b
# Generated 2016-01-12 17:07:14.289505 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/version

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
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/version', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/version}version with content type EMPTY
class version_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://genologics.com/ri/version}version with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'version')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpgenologics_comriversion_version__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 5, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 5, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The URI of the version.\n        ')

    
    # Attribute major uses Python identifier major
    __major = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'major'), 'major', '__httpgenologics_comriversion_version__major', pyxb.binding.datatypes.string)
    __major._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 12, 4)
    __major._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 12, 4)
    
    major = property(__major.value, __major.set, None, '\n          The major version of the version.<br/><br/>\nMajor version indicates forward and backwards compatibility for API clients among minor versions\nwithin the major version.\n        ')

    
    # Attribute minor uses Python identifier minor
    __minor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minor'), 'minor', '__httpgenologics_comriversion_version__minor', pyxb.binding.datatypes.string)
    __minor._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 21, 4)
    __minor._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 21, 4)
    
    minor = property(__minor.value, __minor.set, None, '\n          The minor version of the version.<br/><br/>\nMinor version indicates additional non-breaking changes to the version.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __major.name() : __major,
        __minor.name() : __minor
    })
Namespace.addCategoryObject('typeBinding', 'version', version_)


# Complex type {http://genologics.com/ri/version}versions with content type ELEMENT_ONLY
class versions_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Index is the base entry point to the API, providing a list of supported versions in the system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'versions')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpgenologics_comriversion_versions__version', True, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 37, 6), )

    
    version = property(__version.value, __version.set, None, '\n            Each version provides a URI to a supported version in the system.\n          ')

    _ElementMap.update({
        __version.name() : __version
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'versions', versions_)


version = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), version_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', version.name().localName(), version)

versions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'versions'), versions_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', versions.name().localName(), versions)



versions_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), version_, scope=versions_, documentation='\n            Each version provides a URI to a supported version in the system.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 37, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 37, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(versions_._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/ver.xsd', 37, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
versions_._Automaton = _BuildAutomaton()

