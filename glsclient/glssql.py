#!/usr/bin/env python
# encoding: utf-8
"""
glssql.py

Created by Anne Pajon on 2013-06-21.
"""

PROCESS_BY_UDF_QUERY = """
SELECT process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate, process_udf_view.udfvalue
FROM process, processtype, process_udf_view
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%s'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = '%s'
AND process_udf_view.udfvalue = '%s'
ORDER BY process.createddate
"""

COMPLETE_RUNPROCESS_BY_UDF_QUERY = """
SELECT process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate, pudf2.udfvalue
FROM process
--LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Finish Date')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname = '%s')
LEFT OUTER JOIN process_udf_view as pudf3 on (pudf3.processid=process.processid AND pudf3.udfname = 'Status'), processtype
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%%Run%%'
--AND pudf1.udfvalue is not null
AND pudf2.udfvalue = '%s'
AND pudf3.udfvalue is not null
AND split_part(pudf3.udfvalue, ' ', 2) = split_part(pudf3.udfvalue, ' ', 4) -- should be at end of cycle
ORDER BY process.createddate
"""

RUNSTATUS_BYRUNID_QUERY = """
SELECT artifact.artifactid, artifact.name, pudf1.udfvalue as runid, split_part(pudf2.udfvalue, ' ', 2) as currentcycle, split_part(pudf2.udfvalue, ' ', 4) as totalcycle, artifactstate.qcflag, pudf3.udfvalue as finishdate, process.workstatus
FROM process
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Run ID')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname = 'Status')
LEFT OUTER JOIN process_udf_view as pudf3 on (pudf3.processid=process.processid AND pudf3.udfname = 'Finish Date'), 
processtype, processiotracker, artifact, artifactstate
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%%Run%%'
AND pudf1.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND processiotracker.inputartifactid=artifact.artifactid
AND artifactstate.artifactid=artifact.artifactid
AND artifact.currentstateid=artifactstate.stateid
"""

PUBLISHINGPROCESS_BY_INPUTARTIFACTLUID_QUERY = """
SELECT process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate
FROM processiotracker, process, processtype, artifact
WHERE processiotracker.processid=process.processid 
AND process.typeid=processtype.typeid 
AND processtype.displayname='Publishing' 
AND processiotracker.inputartifactid=artifact.artifactid 
AND artifact.luid='%s'
"""

BILLINGPROCESS_BY_INPUTARTIFACTLUID_QUERY = """
SELECT process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate
FROM processiotracker, process, processtype, artifact
WHERE processiotracker.processid=process.processid 
AND process.typeid=processtype.typeid 
AND processtype.displayname='Billing' 
AND processiotracker.inputartifactid=artifact.artifactid 
AND artifact.luid='%s'
"""

UNASSIGNED_FASTQ1_ON_PROCESS_BY_UDF_QUERY = """
SELECT process.processid, processiotracker.trackerid, artifact.artifactid, artifact.name, glsfile.server, glsfile.contenturi  
FROM process, processtype, process_udf_view, processiotracker, outputmapping, artifact, resultfile
LEFT OUTER JOIN glsfile on (resultfile.glsfileid=glsfile.fileid)
WHERE process.typeid = processtype.typeid
AND processtype.displayname = 'FASTQ Sample Pipeline'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = 'Run ID'
AND process_udf_view.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND outputmapping.trackerid=processiotracker.trackerid 
AND outputmapping.outputartifactid=artifact.artifactid 
AND artifact.artifactid=resultfile.artifactid 
AND artifact.name like '%s %% Read 1 FASTQ'
AND resultfile.glsfileid IS NULL
"""

PUBLISHED_RUNS_WITHOUT_FASTQ_ATTACHED = """
WITH publishing as (
	SELECT artifact.luid as artifactluid, process.daterun as daterun
	FROM processiotracker, process, processtype, artifact
	WHERE processiotracker.processid=process.processid
	AND process.typeid=processtype.typeid
	AND processtype.displayname='Publishing'
	AND processiotracker.inputartifactid=artifact.artifactid
)

SELECT process_udf_view.udfvalue as run_id
FROM process, publishing, processtype, process_udf_view, processiotracker, outputmapping, artifact, artifact as inputartifact, resultfile
LEFT OUTER JOIN glsfile on (resultfile.glsfileid=glsfile.fileid)
WHERE process.typeid = processtype.typeid
AND processtype.displayname in ('FASTQ Sample Pipeline', 'Demultiplexing Pipeline')
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = 'Run ID'
AND process.processid=processiotracker.processid
AND outputmapping.trackerid=processiotracker.trackerid
AND outputmapping.outputartifactid=artifact.artifactid
AND artifact.artifactid=resultfile.artifactid
AND processiotracker.inputartifactid=inputartifact.artifactid
AND inputartifact.luid=publishing.artifactluid
AND artifact.name like '%% Read 1 FASTQ'
AND resultfile.glsfileid IS NULL
GROUP BY process_udf_view.udfvalue
ORDER BY process_udf_view.udfvalue DESC
"""

FILES_QUERY = """
SELECT artifact.artifactid, lab.labid, project.name as projectname, '/' || glsfile.contenturi as runfolder
FROM process, processtype, process_udf_view, processiotracker, outputmapping, artifact, 
resultfile LEFT OUTER JOIN glsfile on (resultfile.glsfileid=glsfile.fileid), 
artifact_sample_map, sample, project, researcher, lab
WHERE process.typeid = processtype.typeid
AND processtype.displayname = '%(processname)s'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = 'Run ID'
AND process_udf_view.udfvalue = '%(runid)s'
AND process.processid=processiotracker.processid 
AND outputmapping.trackerid=processiotracker.trackerid 
AND outputmapping.outputartifactid=artifact.artifactid 
AND artifact.artifactid=resultfile.artifactid 
AND (artifact.name like '%% FASTQ' OR artifact.name like '%% Checksums' OR artifact.name like '%% Lane Contents')
AND resultfile.glsfileid IS NOT NULL
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND lab.labid=researcher.labid
"""

PUBLISHED_FILES_QUERY = FILES_QUERY + """
AND glsfile.ispublished='t'
"""

EXTERNAL_FTPDIR_QUERY = """
SELECT lab.labid, lab.name, ludf2.udfvalue as ftpdir, ludf3.udfvalue as nonpfdata
FROM lab 
LEFT OUTER JOIN entity_udf_view as ludf1 on (ludf1.attachtoid=lab.labid and ludf1.udfname='External')
LEFT OUTER JOIN entity_udf_view as ludf2 on (ludf2.attachtoid=lab.labid and ludf2.udfname='FTP Directory')
LEFT OUTER JOIN entity_udf_view as ludf3 on (ludf3.attachtoid=lab.labid and ludf3.udfname='Non PF Data')
LEFT OUTER JOIN entity_udf_view as ludf4 on (ludf4.attachtoid=lab.labid and ludf4.udfname='Internal - Send to FTP')
WHERE
(ludf1.udfvalue='True' OR ludf4.udfvalue='True')
AND ludf2.udfvalue IS NOT NULL
"""

EXTERNAL_DATA_QUERY = """
SELECT distinct (pudf1.udfvalue || '_' || 'Lane' || containerplacement.wellyposition + 1 || '_' || sample_udf_view.udfvalue) as key, 
ludf1.udfvalue as external
FROM process
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Flow Cell ID')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname = 'Run ID'),
processtype, processiotracker, artifact, containerplacement, container, artifact_sample_map, 
sample LEFT OUTER JOIN sample_udf_view on (sample_udf_view.sampleid=sample.sampleid), project, researcher, 
lab LEFT OUTER JOIN entity_udf_view as ludf1 on (lab.labid=ludf1.attachtoid AND ludf1.udfname='External')
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%%Run%%'
AND pudf2.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND processiotracker.inputartifactid=artifact.artifactid
AND containerplacement.processartifactid=artifact.artifactid
AND containerplacement.containerid=container.containerid
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample_udf_view.udfname = 'SLX Identifier'
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND researcher.labid=lab.labid
AND ludf1.udfvalue = 'True'
"""

UNASSIGNED_SAMPLES_QUERY = """
SELECT 
project.name as projectname,
researcher.firstname || ' ' || researcher.lastname as researcher,
artifact.luid as artifactid,
sample.name as samplename,
sudf1.udfvalue as slxid,
sudf3.udfvalue as workflow,
sudf4.udfvalue as readlength,
sudf5.udfvalue as seqtype,
case when sudf5.udfvalue = 'Paired End' then 'PE' else 'SE' end || sudf4.udfvalue as seqinfo,
sample.datereceived as submissiondate,
researcher.email

FROM 
(	SELECT processid, COUNT(artifactid) AS occurences 
	FROM artifact_sample_map 
	GROUP BY processid
) AS samplewithoneartifact,
(
 	SELECT artifact.artifactid, COUNT(processiotracker.processid) AS occurences
 	FROM artifact LEFT OUTER JOIN processiotracker on (processiotracker.inputartifactid=artifact.artifactid)
 	LEFT OUTER JOIN process on (processiotracker.processid=process.processid)
 	GROUP BY artifactid
) AS processnumberperartifact,
sample
LEFT OUTER JOIN sample_udf_view as sudf1 on (sudf1.sampleid=sample.sampleid AND sudf1.udfname = 'SLX Identifier')
LEFT OUTER JOIN sample_udf_view as sudf2 on (sudf2.sampleid=sample.sampleid AND sudf2.udfname = 'Progress')
LEFT OUTER JOIN sample_udf_view as sudf3 on (sudf3.sampleid=sample.sampleid AND sudf3.udfname = 'Workflow')
LEFT OUTER JOIN sample_udf_view as sudf4 on (sudf4.sampleid=sample.sampleid AND sudf4.udfname = 'Read Length')
LEFT OUTER JOIN sample_udf_view as sudf5 on (sudf5.sampleid=sample.sampleid AND sudf5.udfname = 'Sequencing Type'),
project,
researcher,
artifact_sample_map,
artifact
LEFT OUTER JOIN stagetransition on (stagetransition.artifactid=artifact.artifactid)

WHERE samplewithoneartifact.occurences=1
AND processnumberperartifact.occurences<1
AND (sample.datereceived is NULL OR sample.datereceived >= '2013-08-01')
AND sample.processid=samplewithoneartifact.processid
AND artifact.artifactid=processnumberperartifact.artifactid
AND sudf2.udfvalue is NULL
AND sample.projectid=project.projectid
AND artifact_sample_map.processid=sample.processid
AND artifact_sample_map.artifactid=artifact.artifactid
AND project.researcherid=researcher.researcherid

ORDER BY slxid
"""

SAMPLES_WITH_NODATE_QUERY = """
WITH accept as (
	SELECT artifact.luid as artifactluid, process.daterun as daterun
	FROM processiotracker, process, processtype, artifact
	WHERE processiotracker.processid=process.processid 
	AND process.typeid=processtype.typeid 
	AND (processtype.displayname='Accept SLX' or processtype.displayname='Aggregate QC (Library Validation)')
	AND processiotracker.inputartifactid=artifact.artifactid 
) 
SELECT 
artifact.luid as artifactid,
sample.name as samplename,
sample.datereceived as submissiondate,
to_char(accept.daterun, 'YYYY-MM-DD') as acceptancedate
FROM 
sample,
artifact_sample_map,
artifact,
accept
WHERE
sample.datereceived is NULL
AND artifact_sample_map.processid=sample.processid
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact.luid=accept.artifactluid
"""

IS_ALIGNMENT_ACTIVE_QUERY = """
SELECT
artifact.artifactid,
artifact.name,
pudf1.udfvalue as runid,
artifactstate.qcflag,
ludf2.udfvalue as externallab,
judf1.udfvalue as coresupported,
ludf1.udfvalue as alignment
FROM process
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Run ID'),
processtype, processiotracker, artifact, artifactstate, artifact_sample_map, sample, project
LEFT OUTER JOIN entity_udf_view as judf1 on (judf1.attachtoid=project.projectid and judf1.udfname='Core Supported'),
researcher, lab
LEFT OUTER JOIN entity_udf_view as ludf1 on (ludf1.attachtoid=lab.labid and ludf1.udfname='Auto Alignment')
LEFT OUTER JOIN entity_udf_view as ludf2 on (ludf2.attachtoid=lab.labid and ludf2.udfname='External')
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%%Run%%'
AND pudf1.udfvalue = '%s'
AND process.processid=processiotracker.processid
AND processiotracker.inputartifactid=artifact.artifactid
AND artifactstate.artifactid=artifact.artifactid
AND artifact.currentstateid=artifactstate.stateid
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND researcher.labid=lab.labid
AND NOT artifactstate.qcflag = 2 -- not a failed lane (either passed or unknown)
AND ludf2.udfvalue = 'False' -- non external
AND (judf1.udfvalue = 'True' OR ludf1.udfvalue = 'True') -- project supported by core OR auto alignment set for this lab
"""