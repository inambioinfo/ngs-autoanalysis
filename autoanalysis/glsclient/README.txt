### Dependencies

### Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.
### http://docs.python-requests.org

### For generating the xml binding classes:
### http://pyxb.sourceforge.net/
# based on REST API v2r19 - Introduced in Clarity LIMS 3.1

cd glsapi/
rm *

pyxbgen --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location artifact.xsd --module artifact \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location artifactgroup.xsd --module artifactgroup \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location configuration.xsd --module configuration \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location container.xsd --module container \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location containertype.xsd --module containertype \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location controltype.xsd --module controltype \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location exception.xsd --module exception \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location file.xsd --module file \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location instrument.xsd --module instrument \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location lab.xsd --module lab \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location permission.xsd --module permission \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location process.xsd --module process \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location processexecution.xsd --module processexecution \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location processtemplate.xsd --module processtemplate \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location processtype.xsd --module processtype \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location project.xsd --module project \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location property.xsd --module property \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location protcnf.xsd --module protcnf \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location protstepcnf.xsd --module protstepcnf \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location queue.xsd --module queue \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location reagentkit.xsd --module reagentkit \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location reagentlot.xsd --module reagentlot \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location reagenttype.xsd --module reagenttype \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location researcher.xsd --module researcher \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location ri.xsd --module ri \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location role.xsd --module role \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location routing.xsd --module routing \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location sample.xsd --module sample \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location stage.xsd --module stage \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location step.xsd --module step \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location userdefined.xsd --module userdefined \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location ver.xsd --module ver \
        --schema-root=http://lims.cri.camres.org:8080/glsstatic/lablink/downloads/xsd/ --schema-location wkfcnf.xsd --module wkfcnf

touch __init__.py

### For accessing the database directly:
### http://www.sqlalchemy.org/ 0.7.10 with SqlSoup included

### For running the unit tests:
### Before testing you need a 'unittest' user and a 'Python Unit Tests' project 
python -m unittest --verbose glsclient
# or to only test one method
python -m unittest --verbose glsclient.GlsClientApiTest.test_search_fastq_resultfiles

### REST API Documentation
http://developer.genologics.com