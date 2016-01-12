# ./exception.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1e7571504d82bdef8a1168b00aca66147c3c0bba
# Generated 2016-01-12 17:07:14.293149 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://genologics.com/ri/exception

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
Namespace = pyxb.namespace.NamespaceForURI('http://genologics.com/ri/exception', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/exception}exception with content type ELEMENT_ONLY
class exception_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Exception is a descriptive error message that is returned instead of the standard response for
any request that the system was unable to process.<br/><br/>
Exception will include a code corresponding to the HTTP response code of the error. Typical response
codes are 400, indicating that the submitted request was not valid and cannot be reattempted without
corrective action being taken, or 500 indicating that there was an internal error in the server when
attempting to process the request. Refer to the section on HTTP response codes in the API reference
documentation for further details about the categories and meanings of HTTP response codes.<br/><br/>
Exception will include a message element with a textual summary of the error, and may also provide a
suggested-actions element with details on how to correct the problem.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'exception')
    _XSDLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpgenologics_comriexception_exception__message', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 18, 6), )

    
    message = property(__message.value, __message.set, None, '\n            A textual summary of the exception.\n          ')

    
    # Element suggested-actions uses Python identifier suggested_actions
    __suggested_actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'suggested-actions'), 'suggested_actions', '__httpgenologics_comriexception_exception__suggested_actions', False, pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 25, 6), )

    
    suggested_actions = property(__suggested_actions.value, __suggested_actions.set, None, '\n            Suggested actions for how to correct the cause of the exception.\n          ')

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__httpgenologics_comriexception_exception__category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 33, 4)
    __category._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 33, 4)
    
    category = property(__category.value, __category.set, None, '\n          The category of the exception.\n        ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpgenologics_comriexception_exception__code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 40, 4)
    __code._UseLocation = pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 40, 4)
    
    code = property(__code.value, __code.set, None, '\n          The HTTP response code of the exception.\n        ')

    _ElementMap.update({
        __message.name() : __message,
        __suggested_actions.name() : __suggested_actions
    })
    _AttributeMap.update({
        __category.name() : __category,
        __code.name() : __code
    })
Namespace.addCategoryObject('typeBinding', 'exception', exception_)


exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exception'), exception_, location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', exception.name().localName(), exception)



exception_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message'), pyxb.binding.datatypes.string, scope=exception_, documentation='\n            A textual summary of the exception.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 18, 6)))

exception_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'suggested-actions'), pyxb.binding.datatypes.string, scope=exception_, documentation='\n            Suggested actions for how to correct the cause of the exception.\n          ', location=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 25, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 25, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(exception_._UseForTag(pyxb.namespace.ExpandedName(None, 'message')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(exception_._UseForTag(pyxb.namespace.ExpandedName(None, 'suggested-actions')), pyxb.utils.utility.Location('https://genomicsequencing.cruk.cam.ac.uk/glsstatic/lablink/downloads/xsd/exception.xsd', 25, 6))
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
exception_._Automaton = _BuildAutomaton()

