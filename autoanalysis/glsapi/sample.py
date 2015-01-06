# ./sample.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:473fe42cde944a1c5e3f9c6b0c3c89d11db4e77b
# Generated 2015-01-06 15:57:40.183445 by PyXB version 1.2.3
# Namespace http://genologics.com/ri/sample

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:bc8d4bb3-95bc-11e4-bcfd-70cd60a9fcda')

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://genologics.com/ri/sample', create_if_missing=True)
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


# Complex type {http://genologics.com/ri/sample}details with content type ELEMENT_ONLY
class details_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation of a list of resource details.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'details')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sample uses Python identifier sample
    __sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sample'), 'sample', '__httpgenologics_comrisample_details__sample', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 16, 6), )

    
    sample = property(__sample.value, __sample.set, None, u'\n            A list of detailed resource representations for retrieval/update.\n          ')

    
    # Element samplecreation uses Python identifier samplecreation
    __samplecreation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'samplecreation'), 'samplecreation', '__httpgenologics_comrisample_details__samplecreation', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 23, 6), )

    
    samplecreation = property(__samplecreation.value, __samplecreation.set, None, u'\n            A list of detailed resource representations for creation.\n          ')

    _ElementMap.update({
        __sample.name() : __sample,
        __samplecreation.name() : __samplecreation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'details', details_)


# Complex type {http://genologics.com/ri/sample}controlType with content type EMPTY
class controlType (pyxb.binding.basis.complexTypeDefinition):
    """
        Control Type provides a name and a URI linking to the detailed representation of the Control Type associated with the Sample.
If a Control Type is associated, the Sample will not have an associated Project.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'controlType')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 58, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_controlType_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 65, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 65, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Control Type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrisample_controlType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 77, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 77, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The Name of the Control Type.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'controlType', controlType)


# Complex type {http://genologics.com/ri/sample}samplebase with content type ELEMENT_ONLY
class samplebase (pyxb.binding.basis.complexTypeDefinition):
    """
        The base representation of a Sample, defining common elements for both Sample and Sample creation.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'samplebase')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://genologics.com/ri}externalid uses Python identifier externalid
    __externalid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid'), 'externalid', '__httpgenologics_comrisample_samplebase_httpgenologics_comriexternalid', True, pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 230, 2), )

    
    externalid = property(__externalid.value, __externalid.set, None, u'\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ')

    
    # Element {http://genologics.com/ri/file}file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), 'file', '__httpgenologics_comrisample_samplebase_httpgenologics_comrifilefile', True, pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2), )

    
    file = property(__file.value, __file.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrisample_samplebase_name', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6), )

    
    name = property(__name.value, __name.set, None, u'\n            The name of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ')

    
    # Element date-received uses Python identifier date_received
    __date_received = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'date-received'), 'date_received', '__httpgenologics_comrisample_samplebase_date_received', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6), )

    
    date_received = property(__date_received.value, __date_received.set, None, u'\n            The date the Sample was received.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, any previous value is removed.\n          ')

    
    # Element date-completed uses Python identifier date_completed
    __date_completed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'date-completed'), 'date_completed', '__httpgenologics_comrisample_samplebase_date_completed', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6), )

    
    date_completed = property(__date_completed.value, __date_completed.set, None, u'\n            The date the Sample was completed.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, any previous value is removed.\n          ')

    
    # Element project uses Python identifier project
    __project = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'project'), 'project', '__httpgenologics_comrisample_samplebase_project', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6), )

    
    project = property(__project.value, __project.set, None, u'\n            Project provides a URI linking to the detailed representation of the Project for the Sample.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element submitter uses Python identifier submitter
    __submitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'submitter'), 'submitter', '__httpgenologics_comrisample_samplebase_submitter', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6), )

    
    submitter = property(__submitter.value, __submitter.set, None, u'\n            Submitter provides a URI linking to the detailed representation of the submitter for the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but submitter must have valid credentials and if no value is provided, any\nprevious value is removed.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but submitter must have valid credentials and if no value is provided, any\nprevious value is removed.\n          ')

    
    # Element artifact uses Python identifier artifact
    __artifact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'artifact'), 'artifact', '__httpgenologics_comrisample_samplebase_artifact', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6), )

    
    artifact = property(__artifact.value, __artifact.set, None, u'\n            Artifact provides a URI linking to the detailed representation of the Artifact for the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element biosource uses Python identifier biosource
    __biosource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'biosource'), 'biosource', '__httpgenologics_comrisample_samplebase_biosource', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6), )

    
    biosource = property(__biosource.value, __biosource.set, None, u'\n            Deprecated.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), 'field', '__httpgenologics_comrisample_samplebase_httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Element {http://genologics.com/ri/userdefined}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), 'type', '__httpgenologics_comrisample_samplebase_httpgenologics_comriuserdefinedtype', False, pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2), )

    
    type = property(__type.value, __type.set, None, u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrisample_samplebase_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 232, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 232, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_samplebase_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 244, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 244, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __externalid.name() : __externalid,
        __file.name() : __file,
        __name.name() : __name,
        __date_received.name() : __date_received,
        __date_completed.name() : __date_completed,
        __project.name() : __project,
        __submitter.name() : __submitter,
        __artifact.name() : __artifact,
        __biosource.name() : __biosource,
        __field.name() : __field,
        __type.name() : __type
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'samplebase', samplebase)


# Complex type {http://genologics.com/ri/sample}artifact with content type EMPTY
class artifact (pyxb.binding.basis.complexTypeDefinition):
    """
        Artifact is a child element of Sample and provides a URI linking to the detailed representation of the artifact for the Sample.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'artifact')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 257, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_artifact_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 263, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 263, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrisample_artifact_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 275, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 275, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the artifact.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'artifact', artifact)


# Complex type {http://genologics.com/ri/sample}biosource with content type ELEMENT_ONLY
class biosource (pyxb.binding.basis.complexTypeDefinition):
    """
        Deprecated.
Biosource is not supported in Clarity.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'biosource')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 288, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpgenologics_comrisample_biosource_description', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 296, 6), )

    
    description = property(__description.value, __description.set, None, u'\n            The description of the biosource.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element {http://genologics.com/ri/userdefined}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), 'field', '__httpgenologics_comrisample_biosource_httpgenologics_comriuserdefinedfield', True, pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2), )

    
    field = property(__field.value, __field.set, None, u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpgenologics_comrisample_biosource_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 321, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 321, 4)
    
    name = property(__name.value, __name.set, None, u'\n          The name of the biosource.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __description.name() : __description,
        __field.name() : __field
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'biosource', biosource)


# Complex type {http://genologics.com/ri/sample}project with content type EMPTY
class project (pyxb.binding.basis.complexTypeDefinition):
    """
        Project is a child element of Sample and provides a URI linking to the detailed representation of the Project for the Sample.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'project')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 334, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_project_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 340, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 340, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrisample_project_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 352, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 352, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMS ID of the Project.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __limsid.name() : __limsid
    })
Namespace.addCategoryObject('typeBinding', u'project', project)


# Complex type {http://genologics.com/ri/sample}submitter with content type ELEMENT_ONLY
class submitter (pyxb.binding.basis.complexTypeDefinition):
    """
        Submitter is a child element of Sample and provides a URI linking to the detailed representation of the submitter for the Sample.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'submitter')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 365, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'first-name'), 'first_name', '__httpgenologics_comrisample_submitter_first_name', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 372, 6), )

    
    first_name = property(__first_name.value, __first_name.set, None, u'\n            The first name of the submitter.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Element last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last-name'), 'last_name', '__httpgenologics_comrisample_submitter_last_name', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 384, 6), )

    
    last_name = property(__last_name.value, __last_name.set, None, u'\n            The last name of the submitter.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_submitter_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 397, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 397, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the submitter.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but if present submitter must be a valid technician.\n<br/>Updatable with PUT: Yes, but uri of submitter must be a valid technician.\n<br/>Required for PUT: No\n        ')

    _ElementMap.update({
        __first_name.name() : __first_name,
        __last_name.name() : __last_name
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'submitter', submitter)


# Complex type {http://genologics.com/ri/sample}samples with content type ELEMENT_ONLY
class samples_ (pyxb.binding.basis.complexTypeDefinition):
    """
        The representation for a list of sample links.<br/><br/>
The system enforces a maximum number of elements when generating the list of links. When the size of
the request result set is larger than the system maximum, the list represents a paged view of the overall
results, and the previous-page and next-page elements provide URIs linking to the previous or next page
of links in the overall results.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'samples')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 433, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sample uses Python identifier sample
    __sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sample'), 'sample', '__httpgenologics_comrisample_samples__sample', True, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 444, 6), )

    
    sample = property(__sample.value, __sample.set, None, u'\n            Sample provides a URI linking to the detailed representation of a sample.\n          ')

    
    # Element previous-page uses Python identifier previous_page
    __previous_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previous-page'), 'previous_page', '__httpgenologics_comrisample_samples__previous_page', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 451, 6), )

    
    previous_page = property(__previous_page.value, __previous_page.set, None, u'\n            When working with large lists of samples,\nthe previous-page element provides a URI that links to the previous page of samples.\n          ')

    
    # Element next-page uses Python identifier next_page
    __next_page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'next-page'), 'next_page', '__httpgenologics_comrisample_samples__next_page', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 459, 6), )

    
    next_page = property(__next_page.value, __next_page.set, None, u'\n            When working with large lists of samples,\nthe next-page element provides a URI that links to the next page of samples.\n          ')

    _ElementMap.update({
        __sample.name() : __sample,
        __previous_page.name() : __previous_page,
        __next_page.name() : __next_page
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'samples', samples_)


# Complex type {http://genologics.com/ri/sample}sample-link with content type EMPTY
class sample_link (pyxb.binding.basis.complexTypeDefinition):
    """
        Sample-link is a child element type of samples and provides a URI linking to the detailed representation of a sample.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sample-link')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 469, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute limsid uses Python identifier limsid
    __limsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'limsid'), 'limsid', '__httpgenologics_comrisample_sample_link_limsid', pyxb.binding.datatypes.string)
    __limsid._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 475, 4)
    __limsid._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 475, 4)
    
    limsid = property(__limsid.value, __limsid.set, None, u'\n          The LIMSID of the sample.\n        ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpgenologics_comrisample_sample_link_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 482, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 482, 4)
    
    uri = property(__uri.value, __uri.set, None, u'\n          The URI of the sample.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __limsid.name() : __limsid,
        __uri.name() : __uri
    })
Namespace.addCategoryObject('typeBinding', u'sample-link', sample_link)


# Complex type {http://genologics.com/ri/sample}sample with content type ELEMENT_ONLY
class sample_ (samplebase):
    """
        The detailed representation of a sample.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sample')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 32, 2)
    _ElementMap = samplebase._ElementMap.copy()
    _AttributeMap = samplebase._AttributeMap.copy()
    # Base type is samplebase
    
    # Element externalid ({http://genologics.com/ri}externalid) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element file ({http://genologics.com/ri/file}file) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element control-type uses Python identifier control_type
    __control_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'control-type'), 'control_type', '__httpgenologics_comrisample_sample__control_type', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 41, 10), )

    
    control_type = property(__control_type.value, __control_type.set, None, u'\n                Control Type provides a name and a URI linking to the detailed representation of the Control Type associated with the Sample.\nIf a Control Type is associated, the Sample will not have an associated Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n              ')

    
    # Element name (name) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element date_received (date-received) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element date_completed (date-completed) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element project (project) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element submitter (submitter) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element artifact (artifact) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element biosource (biosource) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element field ({http://genologics.com/ri/userdefined}field) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element type ({http://genologics.com/ri/userdefined}type) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Attribute limsid inherited from {http://genologics.com/ri/sample}samplebase
    
    # Attribute uri inherited from {http://genologics.com/ri/sample}samplebase
    _ElementMap.update({
        __control_type.name() : __control_type
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sample', sample_)


# Complex type {http://genologics.com/ri/sample}samplecreation with content type ELEMENT_ONLY
class samplecreation_ (samplebase):
    """
        Sample creation is the detailed representation required when creating a new Sample in the system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'samplecreation')
    _XSDLocation = pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 410, 2)
    _ElementMap = samplebase._ElementMap.copy()
    _AttributeMap = samplebase._AttributeMap.copy()
    # Base type is samplebase
    
    # Element externalid ({http://genologics.com/ri}externalid) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element file ({http://genologics.com/ri/file}file) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element name (name) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element date_received (date-received) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element date_completed (date-completed) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element project (project) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element submitter (submitter) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element artifact (artifact) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element biosource (biosource) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__httpgenologics_comrisample_samplecreation__location', False, pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 419, 10), )

    
    location = property(__location.value, __location.set, None, u"\n                The location of the Sample's artifact within a container.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n              ")

    
    # Element field ({http://genologics.com/ri/userdefined}field) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Element type ({http://genologics.com/ri/userdefined}type) inherited from {http://genologics.com/ri/sample}samplebase
    
    # Attribute limsid inherited from {http://genologics.com/ri/sample}samplebase
    
    # Attribute uri inherited from {http://genologics.com/ri/sample}samplebase
    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'samplecreation', samplecreation_)


details = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'details'), details_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', details.name().localName(), details)

samples = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'samples'), samples_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', samples.name().localName(), samples)

sample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sample'), sample_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', sample.name().localName(), sample)

samplecreation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'samplecreation'), samplecreation_, location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 7, 2))
Namespace.addCategoryObject('elementBinding', samplecreation.name().localName(), samplecreation)



details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sample'), sample_, scope=details_, documentation=u'\n            A list of detailed resource representations for retrieval/update.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 16, 6)))

details_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'samplecreation'), samplecreation_, scope=details_, documentation=u'\n            A list of detailed resource representations for creation.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 23, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 16, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 23, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'sample')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(details_._UseForTag(pyxb.namespace.ExpandedName(None, u'samplecreation')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 23, 6))
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
details_._Automaton = _BuildAutomaton()




samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid'), _ImportedBinding_ri.externalid_, scope=samplebase, documentation=u'\n        An identifier that allows an external system to retrieve information about the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No\n      ', location=pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/ri.xsd', 230, 2)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_file, u'file'), _ImportedBinding_file.file_, scope=samplebase, location=pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/file.xsd', 4, 2)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=samplebase, documentation=u'\n            The name of the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: Yes\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'date-received'), pyxb.binding.datatypes.string, scope=samplebase, documentation=u'\n            The date the Sample was received.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, any previous value is removed.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'date-completed'), pyxb.binding.datatypes.string, scope=samplebase, documentation=u'\n            The date the Sample was completed.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but if not provided, any previous value is removed.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'project'), project, scope=samplebase, documentation=u'\n            Project provides a URI linking to the detailed representation of the Project for the Sample.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'submitter'), submitter, scope=samplebase, documentation=u'\n            Submitter provides a URI linking to the detailed representation of the submitter for the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, but submitter must have valid credentials and if no value is provided, any\nprevious value is removed.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, but submitter must have valid credentials and if no value is provided, any\nprevious value is removed.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'artifact'), artifact, scope=samplebase, documentation=u'\n            Artifact provides a URI linking to the detailed representation of the Artifact for the Sample.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'biosource'), biosource, scope=samplebase, documentation=u'\n            Deprecated.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), _ImportedBinding_userdefined.field_, scope=samplebase, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

samplebase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'type'), _ImportedBinding_userdefined.type_, scope=samplebase, documentation=u'\n        The User-Defined Type that is associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDT has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDT has been configured as required. If a current UDT is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 71, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'date-received')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'date-completed')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'project')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'submitter')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(None, u'biosource')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'type')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(samplebase._UseForTag(pyxb.namespace.ExpandedName(_Namespace_file, u'file')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
samplebase._Automaton = _BuildAutomaton_()




biosource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=biosource, documentation=u'\n            The description of the biosource.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 296, 6)))

biosource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_udf, u'field'), _ImportedBinding_userdefined.field_, scope=biosource, documentation=u'\n        A User-Defined Field that is associated with the researcher.\nThis element is repeated for each UDF associated with the researcher.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: No, unless the UDF has been configured as required.\n<br/>Updatable with PUT: Yes\n<br/>Required for PUT: No, unless the UDF has been configured as required. If a current UDF is not provided, existing values are deleted.\n      ', location=pyxb.utils.utility.Location(u'http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/userdefined.xsd', 58, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 296, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 308, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(biosource._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 296, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(biosource._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 308, 6))
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
biosource._Automaton = _BuildAutomaton_2()




submitter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'first-name'), pyxb.binding.datatypes.string, scope=submitter, documentation=u'\n            The first name of the submitter.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 372, 6)))

submitter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last-name'), pyxb.binding.datatypes.string, scope=submitter, documentation=u'\n            The last name of the submitter.\n<br/>Always returns with GET: Yes\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 384, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 372, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 384, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(submitter._UseForTag(pyxb.namespace.ExpandedName(None, u'first-name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 372, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(submitter._UseForTag(pyxb.namespace.ExpandedName(None, u'last-name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 384, 6))
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
submitter._Automaton = _BuildAutomaton_3()




samples_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sample'), sample_link, scope=samples_, documentation=u'\n            Sample provides a URI linking to the detailed representation of a sample.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 444, 6)))

samples_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previous-page'), _ImportedBinding_ri.page, scope=samples_, documentation=u'\n            When working with large lists of samples,\nthe previous-page element provides a URI that links to the previous page of samples.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 451, 6)))

samples_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'next-page'), _ImportedBinding_ri.page, scope=samples_, documentation=u'\n            When working with large lists of samples,\nthe next-page element provides a URI that links to the next page of samples.\n          ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 459, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 444, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 451, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 459, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(samples_._UseForTag(pyxb.namespace.ExpandedName(None, u'sample')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 444, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(samples_._UseForTag(pyxb.namespace.ExpandedName(None, u'previous-page')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 451, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(samples_._UseForTag(pyxb.namespace.ExpandedName(None, u'next-page')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 459, 6))
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
samples_._Automaton = _BuildAutomaton_4()




sample_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'control-type'), controlType, scope=sample_, documentation=u'\n                Control Type provides a name and a URI linking to the detailed representation of the Control Type associated with the Sample.\nIf a Control Type is associated, the Sample will not have an associated Project.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: No\n<br/>Required for POST: No\n<br/>Updatable with PUT: No\n<br/>Required for PUT: No\n              ', location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 41, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 41, 10))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'date-received')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'date-completed')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'project')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'submitter')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'biosource')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'type')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_file, u'file')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(sample_._UseForTag(pyxb.namespace.ExpandedName(None, u'control-type')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 41, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
sample_._Automaton = _BuildAutomaton_5()




samplecreation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), _ImportedBinding_ri.location, scope=samplecreation_, documentation=u"\n                The location of the Sample's artifact within a container.\n<br/>Always returns with GET: No\n<br/>Creatable with POST: Yes\n<br/>Required for POST: Yes\n              ", location=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 419, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 419, 10))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'date-received')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 109, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'date-completed')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'project')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 133, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'submitter')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 145, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'artifact')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 159, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'biosource')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 171, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'type')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 183, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_udf, u'field')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 195, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ri, u'externalid')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 207, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_file, u'file')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 219, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(samplecreation_._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://genomicsequencing.cruk.cam.ac.uk:8080/glsstatic/lablink/downloads/xsd/sample.xsd', 419, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
samplecreation_._Automaton = _BuildAutomaton_6()

