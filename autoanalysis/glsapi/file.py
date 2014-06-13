# ./file.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c5f66b6fac21a828f4419f18a908eb5e18a05151
# Generated 2014-04-04 17:46:47.254100 by PyXB version 1.2.2
# Namespace http://genologics.com/ri/file [xmlns:file]

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
import pyxb.binding.datatypes
import ri as _ImportedBinding_ri

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/file', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/file}details with content type ELEMENT_ONLY
class details_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a batch of file resources.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'details')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'file'), 'file', '__httpgenologics_comrifile_details__file', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 13, 6), )

    
    file = property(__file.value, __file.set, None, None)

    _ElementMap.update({
        __file.name() : __file
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'details', details_)


# Complex type {http://genologics.com/ri/file}file with content type ELEMENT_ONLY
class file_ (pyxb.binding.basis.complexTypeDefinition):
    """
        <p>The file element contains information about a file in the system.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'file')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element attached-to uses Python identifier attached_to
    __attached_to = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attached-to'), 'attached_to', '__httpgenologics_comrifile_file__attached_to', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 23, 6), )

    
    attached_to = property(__attached_to.value, __attached_to.set, None, u'\n            This element contains a URI that identifies and links to further information about the resource that\nthe file is attached to, such as a project, sample, process, or file-based artifact.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes, a file must always be attached to an entity, or capturedfile record.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes, a file must always be attached to an entity, or capturedfile record.\n          ')

    
    # Element content-location uses Python identifier content_location
    __content_location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'content-location'), 'content_location', '__httpgenologics_comrifile_file__content_location', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 36, 6), )

    
    content_location = property(__content_location.value, __content_location.set, None, u'\n            This element contains a URI that identifies and links to the network location of the file,\nwhich can be used to retrieve the file and process its contents.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes, must be valid location for system to read inbound file uri\ninformation from.\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element original-location uses Python identifier original_location
    __original_location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'original-location'), 'original_location', '__httpgenologics_comrifile_file__original_location', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 50, 6), )

    
    original_location = property(__original_location.value, __original_location.set, None, u'\n            This element provides the original name and location of the file before it was imported into the system.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes, must be valid location for system to read inbound file location from.\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element is-published uses Python identifier is_published
    __is_published = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is-published'), 'is_published', '__httpgenologics_comrifile_file__is_published', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 62, 6), )

    
    is_published = property(__is_published.value, __is_published.set, None, u"\n            This element specifies whether the file is displayed in LabLink.\nTo publish a file to LabLink, use 'true'.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided or empty, value is set to false.\n          ")

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrifile_file__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 76, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 76, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the file.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrifile_file__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 88, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 88, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          A URI that identifies the file.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __attached_to.name() : __attached_to,
        __content_location.name() : __content_location,
        __original_location.name() : __original_location,
        __is_published.name() : __is_published
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'file', file_)


# Complex type {http://genologics.com/ri/file}file-link with content type EMPTY
class file_link (pyxb.binding.basis.complexTypeDefinition):
    """
        The file-link type provides a URI that links to information about a file in the system.
<p>Elements of this type are used for lists of files, or by resources that have attached files to
identify and link to further information about the file.</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'file-link')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrifile_file_link_uri', pyxb.binding.datatypes.string)
    __uri._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 109, 4)
    __uri._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 109, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          A URI that identifies and links to further information about the file.\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrifile_file_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 116, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 116, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMSID of the file.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'file-link', file_link)


# Complex type {http://genologics.com/ri/file}files with content type ELEMENT_ONLY
class files_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation for a list of file links.
<p>The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
</p>
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'files')
    _XSDLocation = pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 124, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'file'), 'file', '__httpgenologics_comrifile_files__file', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 136, 6), )

    
    file = property(__file.value, __file.set, None, u'\n            File provides a URI linking to the detailed representation of a file.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comrifile_files__previous_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 143, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            When working with large lists of files,\nthe previous-page element provides a URI that links to the previous page of files.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comrifile_files__next_page', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 151, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            When working with large lists of files,\nthe next-page element provides a URI that links to the next page of files.\n          ')

    _ElementMap.update({
        __file.name() : __file,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'files', files_)


details = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), details_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', details.name().localName(), details)

file = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'file'), file_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', file.name().localName(), file)

files = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'files'), files_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', files.name().localName(), files)



details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'file'), file_, scope=details_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 13, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 13, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'file')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 13, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
details_._Automaton = _BuildAutomaton()




file_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attached-to'), pyxb.binding.datatypes.anyURI, scope=file_, documentation=u'\n            This element contains a URI that identifies and links to further information about the resource that\nthe file is attached to, such as a project, sample, process, or file-based artifact.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes, a file must always be attached to an entity, or capturedfile record.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes, a file must always be attached to an entity, or capturedfile record.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 23, 6)))

file_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'content-location'), pyxb.binding.datatypes.anyURI, scope=file_, documentation=u'\n            This element contains a URI that identifies and links to the network location of the file,\nwhich can be used to retrieve the file and process its contents.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes, must be valid location for system to read inbound file uri\ninformation from.\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 36, 6)))

file_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'original-location'), pyxb.binding.datatypes.string, scope=file_, documentation=u'\n            This element provides the original name and location of the file before it was imported into the system.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes, must be valid location for system to read inbound file location from.\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 50, 6)))

file_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is-published'), pyxb.binding.datatypes.boolean, scope=file_, documentation=u"\n            This element specifies whether the file is displayed in LabLink.\nTo publish a file to LabLink, use 'true'.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided or empty, value is set to false.\n          ", location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 62, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 23, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 36, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 50, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 62, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(file_._UseForTag(pyxb.namespace.ExpandedName(None, u'attached-to')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 23, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(file_._UseForTag(pyxb.namespace.ExpandedName(None, u'content-location')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(file_._UseForTag(pyxb.namespace.ExpandedName(None, u'original-location')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 50, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(file_._UseForTag(pyxb.namespace.ExpandedName(None, u'is-published')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 62, 6))
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
file_._Automaton = _BuildAutomaton_()




files_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'file'), file_link, scope=files_, documentation=u'\n            File provides a URI linking to the detailed representation of a file.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 136, 6)))

files_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=files_, documentation=u'\n            When working with large lists of files,\nthe previous-page element provides a URI that links to the previous page of files.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 143, 6)))

files_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=files_, documentation=u'\n            When working with large lists of files,\nthe next-page element provides a URI that links to the next page of files.\n          ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 151, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 136, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 143, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 151, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(files_._UseForTag(pyxb.namespace.ExpandedName(None, u'file')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 136, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(files_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 143, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(files_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 151, 6))
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
files_._Automaton = _BuildAutomaton_2()

