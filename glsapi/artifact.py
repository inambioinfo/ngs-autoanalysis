# ./artifact.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7a2a5ba0321ae1837db4fc6a222a04675f452018
# Generated 2014-10-02 18:41:08.834469 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/artifact

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
import file as _ImportedBinding_file
import pyxb.binding.datatypes
import ri as _ImportedBinding_ri

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/artifact', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_file = _ImportedBinding_file.Namespace
_Namespace_file.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_udf = _ImportedBinding_userdefined.Namespace
_Namespace_udf.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://genologics.com/ri/artifact}qc-flag
class qc_flag (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The qc-flag enumeration lists the possible values of the qc-flag element for the Artifact.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'qc-flag')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 315, 2)
    _Documentation = u'\n        The qc-flag enumeration lists the possible values of the qc-flag element for the Artifact.\n      '
qc_flag._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=qc_flag, enum_prefix=None)
qc_flag.UNKNOWN = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
qc_flag.PASSED = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'PASSED', tag=u'PASSED')
qc_flag.FAILED = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'FAILED', tag=u'FAILED')
qc_flag.CONTINUE = qc_flag._CF_enumeration.addEnumeration(unicode_value=u'CONTINUE', tag=u'CONTINUE')
qc_flag._InitializeFacetMap(qc_flag._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'qc-flag', qc_flag)

# Complex type {http://genologics.com/ri/artifact}artifact with content type ELEMENT_ONLY
class artifact_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The detailed representation of an Artifact.<br/><br/>
An Artifact represents the inputs to or outputs from a process. An Artifact is
classified by its type (Analyte, ResultFile, etc).<br/><br/>
Artifacts do not support HTTP POST requests.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifact')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriartifact_artifact__name', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 18, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpgenologics_comriartifact_artifact__type', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 28, 6), )

    
    type = property(__type.value, __type.set, None, u'\n            The type of Artifact.\nArtifact type describes the characteristics of the Artifact. For example, the\ntype of the Artifact can be Analyte indicating it is a sample or submitted sample\nthat resides in a container. Alternately, the type could be ResultFile indicating\nit is the output of instrument processing. Refer to the GenoLogics LIMS\nHelp file for information on process inputs and outputs.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element output-type uses Python identifier output_type
    __output_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'output-type'), 'output_type', '__httpgenologics_comriartifact_artifact__output_type', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 43, 6), )

    
    output_type = property(__output_type.value, __output_type.set, None, u'\n            The output-type of the Artifact. In the client, this is a custom Display Name given to the Artifact type when\nconfiguring the process.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element parent-process uses Python identifier parent_process
    __parent_process = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'parent-process'), 'parent_process', '__httpgenologics_comriartifact_artifact__parent_process', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 54, 6), )

    
    parent_process = property(__parent_process.value, __parent_process.set, None, u'\n            The process that produced the Artifact.\nThe parent-process provides a URI linking to the detailed representation\nof the process that produced the Artifact.\n<br/>Always returns with GET: No, It is returned in all cases except the analyte artifact of the submitted\nsample case, which by definition cannot have a parent-process\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element qc-flag uses Python identifier qc_flag
    __qc_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'qc-flag'), 'qc_flag', '__httpgenologics_comriartifact_artifact__qc_flag', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 67, 6), )

    
    qc_flag = property(__qc_flag.value, __qc_flag.set, None, u'\n            The qc-flag applied to the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, QC is set to UNKNOWN.\n          ')

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__httpgenologics_comriartifact_artifact__location', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 77, 6), )

    
    location = property(__location.value, __location.set, None, u"\n            The Artifact's location in a container.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ")

    
    # Element working-flag uses Python identifier working_flag
    __working_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'working-flag'), 'working_flag', '__httpgenologics_comriartifact_artifact__working_flag', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 87, 6), )

    
    working_flag = property(__working_flag.value, __working_flag.set, None, u'\n            The working-flag of the Artifact. In the client, this is referred to as the working status of an artifact.\nWorking-flag indicates whether the Artifact is ready for use\nin additional Processes.\n<br/>Always returns with GET: No, only for Analytes\n<br/>Updatable with PUT: Yes, only supported for Analyte type Artifacts.\n<br/>Required for PUT: Yes, for Analyte only.\n          ')

    
    # Element sample uses Python identifier sample
    __sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sample'), 'sample', '__httpgenologics_comriartifact_artifact__sample', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 99, 6), )

    
    sample = property(__sample.value, __sample.set, None, u'\n            A submitted sample related to the Artifact.\nThis element is repeated for each submitted sample that the artifact is related to.\nEach Sample provides a URI linking to the detailed representation of a\nsubmitted Sample for the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element reagent-label uses Python identifier reagent_label
    __reagent_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reagent-label'), 'reagent_label', '__httpgenologics_comriartifact_artifact__reagent_label', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 112, 6), )

    
    reagent_label = property(__reagent_label.value, __reagent_label.set, None, u'\n            A reagent label applied to the Artifact.\nThis element is repeated for each reagent label applied to the Artifact.<br/><br/>\nReagent labels can be explicitly added to Artifacts in different ways:\n<ul>\n<li>in the client, when importing Samples;</li>\n<li>in the client, when running any Processes for adding Reagents;</li>\n<li>in the API, by updating an artifact representation to include reagent labels.</li>\n</ul>\n<br/><br/>\nAdditionally, reagent labels will be automatically copied from inputs to outputs when a Process is run.\nReagent labels are conventionally named after the type of reagent (see the Reagent Type endpoint) they correspond to.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, reagent labels are cleared\n          ')

    
    # Element control-type uses Python identifier control_type
    __control_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'control-type'), 'control_type', '__httpgenologics_comriartifact_artifact__control_type', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 132, 6), )

    
    control_type = property(__control_type.value, __control_type.set, None, u'\n            The control type of the Artifact. Only control sample has control type.\n<br/>Always returns with GET: No, only for control sample\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element artifact-group uses Python identifier artifact_group
    __artifact_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'artifact-group'), 'artifact_group', '__httpgenologics_comriartifact_artifact__artifact_group', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 163, 6), )

    
    artifact_group = property(__artifact_group.value, __artifact_group.set, None, u'\n            The artifact group that the Artifact belongs to. In the client, artifact groups are referred to as experiments.\nThis element is repeated for each artifact group that the Artifact belongs to.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, existing ArtifactGroups are cleared from Artifact.\n          ')

    
    # Element {http://genologics.com/ri/file}file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), 'file', '__httpgenologics_comriartifact_artifact__httpgenologics_comrifilefile', False, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2), )

    
    file = property(__file.value, __file.set, None, None)

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), 'field', '__httpgenologics_comriartifact_artifact__httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriartifact_artifact__limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 175, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 175, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_artifact__uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 185, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 185, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __name.name() : __name,
        __type.name() : __type,
        __output_type.name() : __output_type,
        __parent_process.name() : __parent_process,
        __qc_flag.name() : __qc_flag,
        __location.name() : __location,
        __working_flag.name() : __working_flag,
        __sample.name() : __sample,
        __reagent_label.name() : __reagent_label,
        __control_type.name() : __control_type,
        __artifact_group.name() : __artifact_group,
        __file.name() : __file,
        __field.name() : __field
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'artifact', artifact_)


# Complex type {http://genologics.com/ri/artifact}artifactgroup with content type EMPTY
class artifactgroup (pyxb.binding.basis.complexTypeDefinition):
    """
        Artifact group is a child element of Artifact and provides a URI linking to the detailed representation of the artifact group that the Artifact belongs to.
In the client, artifact groups are referred to as experiments.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifactgroup')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 196, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_artifactgroup_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 203, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 203, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact group.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriartifact_artifactgroup_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 213, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 213, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the artifact group.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'artifactgroup', artifactgroup)


# Complex type {http://genologics.com/ri/artifact}control-type with content type EMPTY
class control_type (pyxb.binding.basis.complexTypeDefinition):
    """
        Provide a URI linking to the control type if this artifact is a control sample
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'control-type')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 224, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_control_type_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 230, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 230, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the control type.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'control-type', control_type)


# Complex type {http://genologics.com/ri/artifact}parent-process with content type EMPTY
class parent_process (pyxb.binding.basis.complexTypeDefinition):
    """
        Parent-process is a child element of Artifact and provides a URI
linking to the detailed representation of the process that produced the Artifact.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'parent-process')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 241, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriartifact_parent_process_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 248, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 248, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the process.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_parent_process_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 258, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 258, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the process.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'parent-process', parent_process)


# Complex type {http://genologics.com/ri/artifact}reagent-label with content type EMPTY
class reagent_label (pyxb.binding.basis.complexTypeDefinition):
    """
        Reagent-label is a child element of Artifact and provides the name of a
label or reagent that has been added to the Artifact.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reagent-label')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 269, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comriartifact_reagent_label_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 276, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 276, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the label or reagent.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'reagent-label', reagent_label)


# Complex type {http://genologics.com/ri/artifact}sample with content type EMPTY
class sample (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample is a child element of Artifact and provides a URI linking
to the detailed representation of a submitted Sample for the Artifact.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sample')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 287, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriartifact_sample_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 294, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 294, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_sample_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 304, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 304, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'sample', sample)


# Complex type {http://genologics.com/ri/artifact}artifacts with content type ELEMENT_ONLY
class artifacts_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of artifact links.<br/><br/>
The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifacts')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 328, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element artifact uses Python identifier artifact
    __artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'artifact'), 'artifact', '__httpgenologics_comriartifact_artifacts__artifact', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 339, 6), )

    
    artifact = property(__artifact.value, __artifact.set, None, u'\n            Artifact provides a URI linking to the detailed representation of an artifact.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comriartifact_artifacts__previous_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 346, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            When working with large lists of artifacts,\nthe previous-page element provides a URI that links to the previous page of artifacts.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comriartifact_artifacts__next_page', False, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 354, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            When working with large lists of artifacts,\nthe next-page element provides a URI that links to the next page of artifacts.\n          ')

    _ElementMap.update({
        __artifact.name() : __artifact,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'artifacts', artifacts_)


# Complex type {http://genologics.com/ri/artifact}artifact-link with content type EMPTY
class artifact_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Artifact-link is a child element type of artifacts and provides a URI linking to the detailed representation of an artifact.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifact-link')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 364, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comriartifact_artifact_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 370, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 370, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comriartifact_artifact_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 377, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 377, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMSID of the artifact.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'artifact-link', artifact_link)


# Complex type {http://genologics.com/ri/artifact}details with content type ELEMENT_ONLY
class details_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of resource details.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'details')
    _XSDLocation = pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 385, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element artifact uses Python identifier artifact
    __artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'artifact'), 'artifact', '__httpgenologics_comriartifact_details__artifact', True, pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 392, 6), )

    
    artifact = property(__artifact.value, __artifact.set, None, u'\n            A list of detailed resource representations.\n          ')

    _ElementMap.update({
        __artifact.name() : __artifact
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'details', details_)


artifact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'artifact'), artifact_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', artifact.name().localName(), artifact)

artifacts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'artifacts'), artifacts_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', artifacts.name().localName(), artifacts)

details = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), details_, location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', details.name().localName(), details)



artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=artifact_, documentation=u'\n            The name of the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 18, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'type'), pyxb.binding.datatypes.string, scope=artifact_, documentation=u'\n            The type of Artifact.\nArtifact type describes the characteristics of the Artifact. For example, the\ntype of the Artifact can be Analyte indicating it is a sample or submitted sample\nthat resides in a container. Alternately, the type could be ResultFile indicating\nit is the output of instrument processing. Refer to the GenoLogics LIMS\nHelp file for information on process inputs and outputs.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 28, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'output-type'), pyxb.binding.datatypes.string, scope=artifact_, documentation=u'\n            The output-type of the Artifact. In the client, this is a custom Display Name given to the Artifact type when\nconfiguring the process.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 43, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'parent-process'), parent_process, scope=artifact_, documentation=u'\n            The process that produced the Artifact.\nThe parent-process provides a URI linking to the detailed representation\nof the process that produced the Artifact.\n<br/>Always returns with GET: No, It is returned in all cases except the analyte artifact of the submitted\nsample case, which by definition cannot have a parent-process\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 54, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'qc-flag'), qc_flag, scope=artifact_, documentation=u'\n            The qc-flag applied to the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, QC is set to UNKNOWN.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 67, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), _ImportedBinding_ri.location, scope=artifact_, documentation=u"\n            The Artifact's location in a container.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ", location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 77, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'working-flag'), pyxb.binding.datatypes.boolean, scope=artifact_, documentation=u'\n            The working-flag of the Artifact. In the client, this is referred to as the working status of an artifact.\nWorking-flag indicates whether the Artifact is ready for use\nin additional Processes.\n<br/>Always returns with GET: No, only for Analytes\n<br/>Updatable with PUT: Yes, only supported for Analyte type Artifacts.\n<br/>Required for PUT: Yes, for Analyte only.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 87, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sample'), sample, scope=artifact_, documentation=u'\n            A submitted sample related to the Artifact.\nThis element is repeated for each submitted sample that the artifact is related to.\nEach Sample provides a URI linking to the detailed representation of a\nsubmitted Sample for the Artifact.\n<br/>Always returns with GET: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 99, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reagent-label'), reagent_label, scope=artifact_, documentation=u'\n            A reagent label applied to the Artifact.\nThis element is repeated for each reagent label applied to the Artifact.<br/><br/>\nReagent labels can be explicitly added to Artifacts in different ways:\n<ul>\n<li>in the client, when importing Samples;</li>\n<li>in the client, when running any Processes for adding Reagents;</li>\n<li>in the API, by updating an artifact representation to include reagent labels.</li>\n</ul>\n<br/><br/>\nAdditionally, reagent labels will be automatically copied from inputs to outputs when a Process is run.\nReagent labels are conventionally named after the type of reagent (see the Reagent Type endpoint) they correspond to.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, reagent labels are cleared\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 112, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'control-type'), control_type, scope=artifact_, documentation=u'\n            The control type of the Artifact. Only control sample has control type.\n<br/>Always returns with GET: No, only for control sample\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 132, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'artifact-group'), artifactgroup, scope=artifact_, documentation=u'\n            The artifact group that the Artifact belongs to. In the client, artifact groups are referred to as experiments.\nThis element is repeated for each artifact group that the Artifact belongs to.\n<br/>Always returns with GET: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, existing ArtifactGroups are cleared from Artifact.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 163, 6)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), _ImportedBinding_file.file_, scope=artifact_, location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2)))

artifact_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), _ImportedBinding_userdefined.field_, scope=artifact_, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 28, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 54, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 67, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 77, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 87, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 99, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 112, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 132, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 142, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 153, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 163, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 28, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'output-type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'parent-process')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 54, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'qc-flag')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 67, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 77, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'working-flag')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 87, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'sample')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 99, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'reagent-label')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 112, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'control-type')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 132, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 142, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_file, u'file')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 153, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(artifact_._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact-group')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 163, 6))
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
artifact_._Automaton = _BuildAutomaton()




artifacts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'artifact'), artifact_link, scope=artifacts_, documentation=u'\n            Artifact provides a URI linking to the detailed representation of an artifact.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 339, 6)))

artifacts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=artifacts_, documentation=u'\n            When working with large lists of artifacts,\nthe previous-page element provides a URI that links to the previous page of artifacts.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 346, 6)))

artifacts_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=artifacts_, documentation=u'\n            When working with large lists of artifacts,\nthe next-page element provides a URI that links to the next page of artifacts.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 354, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 339, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 346, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 354, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(artifacts_._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 339, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(artifacts_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 346, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(artifacts_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 354, 6))
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
artifacts_._Automaton = _BuildAutomaton_()




details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'artifact'), artifact_, scope=details_, documentation=u'\n            A list of detailed resource representations.\n          ', location=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 392, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 392, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/artifact.xsd', 392, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
details_._Automaton = _BuildAutomaton_2()

