#!/usr/bin/env python
# encoding: utf-8
"""
glssql.py

Created by Anne Pajon on 2013-06-21.
"""

SAMPLE_BY_USER_QUERY = """
SELECT sample.projectid, sample.sampleid, artifact.luid, sample.name, sample.datereceived, sample.datecompleted, sample.maximumanalyteid, sample.bisourceid, sample.processid
FROM sample, project, researcher, artifact, artifact_sample_map
WHERE sample.projectid = project.projectid
AND project.researcherid = researcher.researcherid
AND researcher.email = '%s' 
AND artifact_sample_map.processid = sample.processid
AND artifact_sample_map.artifactid = artifact.artifactid
ORDER BY project.name
"""

SAMPLEID_UDF_QUERY = """
SELECT udfname as key, udfvalue as value
FROM sample_udf_view
WHERE sampleid = %s
"""

SAMPLEID_BY_SLXID_QUERY = """
SELECT sampleid
FROM sample_udf_view
WHERE udfname = 'SLX Identifier'
AND udfvalue = '%s'
"""

SLXID_BY_SAMPLEID_QUERY = """
SELECT DISTINCT(udfvalue) as slxid
FROM sample_udf_view 
WHERE udfname = 'SLX Identifier'
AND sampleid = %s 
"""

RUNPROCESS_BY_SAMPLEID_QUERY = """
SELECT process.processid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate
FROM process, processtype, processiotracker, artifact, artifact_sample_map, sample
WHERE process.typeid = processtype.typeid
AND processiotracker.processid = process.processid
AND processiotracker.inputartifactid = artifact.artifactid
AND artifact_sample_map.artifactid = artifact.artifactid
AND artifact_sample_map.processid = sample.processid
AND processtype.displayname LIKE '%%Run%%'
AND sample.sampleid = %s
"""

PROCESSID_UDF_QUERY = """
SELECT udfname as key, udfvalue as value
FROM process_udf_view
WHERE processid = %s
"""

UDF_BY_PROCESSNAME_QUERY = """
SELECT 
    processtype.displayname,
    udf.name, 
    udf.isvisible
FROM processtype, classindex, udf
    WHERE classindex.classname = 'ConfiguredProcess'
    AND processtype.typename = 'ConfiguredProcess'
    AND udf.attachtoclassid = classindex.classindexid
    AND udf.attachtosubtypeid = processtype.typeid
    AND processtype.displayname like '%%s%'
ORDER BY processtype.displayname
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

COMPLETERUNPROCESS_BY_UDF_QUERY = """
SELECT process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate, pudf2.udfvalue
FROM process
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Finish Date')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid)
LEFT OUTER JOIN process_udf_view as pudf3 on (pudf3.processid=process.processid), processtype
WHERE process.typeid = processtype.typeid
AND processtype.displayname LIKE '%%Run%%'
AND pudf1.udfvalue is not null
AND pudf2.udfname = '%s'
AND pudf2.udfvalue = '%s'
AND pudf3.udfname = 'Status'
AND pudf3.udfvalue is not null
AND split_part(pudf3.udfvalue, ' ', 2) = split_part(pudf3.udfvalue, ' ', 4) -- should be at end of cycle
--AND process.workstatus = 'COMPLETE'
ORDER BY process.createddate
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
AND processtype.displayname = '%s'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = '%s'
AND process_udf_view.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND outputmapping.trackerid=processiotracker.trackerid 
AND outputmapping.outputartifactid=artifact.artifactid 
AND artifact.artifactid=resultfile.artifactid 
AND artifact.name like '%s Read 1 FASTQ'
AND resultfile.glsfileid IS NULL
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
AND (artifact.name like '%% FASTQ' OR artifact.name like '%% Checksums' OR artifact.name like '%% Lane Index')
AND resultfile.glsfileid IS NOT NULL
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND lab.labid=researcher.labid
AND glsfile.ispublished='t'
"""

MGA_LANE_FILES_QUERY = """
SELECT artifact.artifactid, artifact.name, resultfile.glsfileid, glsfile.luid, p1.value as scheme, p2.value as host, p3.value as port, p4.value as dir, '/' || glsfile.contenturi as contenturi
FROM process, processtype, process_udf_view, processiotracker, outputmapping, artifact, resultfile LEFT OUTER JOIN glsfile on (resultfile.glsfileid=glsfile.fileid), 
property as p1, property as p2, property as p3, property as p4
WHERE process.typeid = processtype.typeid
AND processtype.displayname = 'FASTQ Lane Pipeline'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = 'Run ID'
AND process_udf_view.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND outputmapping.trackerid=processiotracker.trackerid 
AND outputmapping.outputartifactid=artifact.artifactid 
AND artifact.artifactid=resultfile.artifactid 
AND artifact.name like '%% MGA Lane Report'
AND resultfile.glsfileid IS NOT NULL
AND p1.name LIKE glsfile.server||'.scheme'
AND p2.name LIKE glsfile.server||'.host'
AND p3.name LIKE glsfile.server||'.port'
AND p4.name LIKE glsfile.server||'.dir'
"""

MGA_FILES_QUERY = """
SELECT artifact.artifactid, artifact.name, resultfile.glsfileid, glsfile.luid, p1.value as scheme, p2.value as host, p3.value as port, p4.value as dir, '/' || glsfile.contenturi as contenturi
FROM process, processtype, process_udf_view, processiotracker, outputmapping, artifact, resultfile LEFT OUTER JOIN glsfile on (resultfile.glsfileid=glsfile.fileid), 
property as p1, property as p2, property as p3, property as p4
WHERE process.typeid = processtype.typeid
AND processtype.displayname = 'Publishing'
AND process.processid = process_udf_view.processid
AND process_udf_view.udfname = 'Run ID'
AND process_udf_view.udfvalue = '%s'
AND process.processid=processiotracker.processid 
AND outputmapping.trackerid=processiotracker.trackerid 
AND outputmapping.outputartifactid=artifact.artifactid 
AND artifact.artifactid=resultfile.artifactid 
AND artifact.name like 'MGA Report'
AND resultfile.glsfileid IS NOT NULL
AND p1.name LIKE glsfile.server||'.scheme'
AND p2.name LIKE glsfile.server||'.host'
AND p3.name LIKE glsfile.server||'.port'
AND p4.name LIKE glsfile.server||'.dir'
"""

EXTERNAL_FTPDIR_QUERY = """ 
SELECT lab.labid, lab.name, ludf2.udfvalue as ftpdir, ludf3.udfvalue as nonpfdata
FROM lab 
LEFT OUTER JOIN entity_udf_view as ludf1 on (ludf1.attachtoid=lab.labid and ludf1.udfname='External')
LEFT OUTER JOIN entity_udf_view as ludf2 on (ludf2.attachtoid=lab.labid and ludf2.udfname='FTP Directory')
LEFT OUTER JOIN entity_udf_view as ludf3 on (ludf3.attachtoid=lab.labid and ludf3.udfname='Non PF Data')
WHERE 
ludf1.udfvalue='True' 
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

BILLING_QUERY = """
SELECT distinct
researcher.firstname || ' ' || researcher.lastname as researcher, 
lab.name as lab, 
address.institution as institute,
sample_udf_view.udfvalue as slxid, 
itype.name || '_' || case when itype.name = 'Miseq' then split_part(pudf6.udfvalue, '-', 2) else case when pudf2.udfvalue is null then 'SE' else 'PE' end || pudf1.udfvalue end as runtype,
audf1.udfvalue as billable, 
to_char(to_date(pudf3.udfvalue, 'YYYY-MM'), 'YYYY-MM') as billingmonth, 
pudf4.udfvalue as flowcellid, 
'Lane' || containerplacement.wellyposition + 1 as lane, 
bpudf1.udfvalue as flowcellbillingcomments,
audf2.udfvalue as billingcomments,
pudf5.udfvalue as runfolder, 
instrument.name as instrument,

to_char(sample.datereceived, 'YYYY-MM-DD') as submissiondate,
to_char(to_date(pudf3.udfvalue, 'YYYY-MM-DD'), 'YYYY-MM-DD') as completiondate, 
audf3.udfvalue as yield_pf_r1,
audf4.udfvalue as avg_q_score_r1,
audf5.udfvalue as Percent_bases_q30_r1,
audf6.udfvalue as cluster_density_r1,
audf7.udfvalue as percent_pf_r1,
audf8.udfvalue as intensity_cycle_1_r1,
audf9.udfvalue as percent_intensity_cycle_20_r1,
audf10.udfvalue as percent_phasing_r1,
audf11.udfvalue as percent_prephasing_r1,
audf12.udfvalue as percent_aligned_r1,
audf13.udfvalue as percent_error_rate_r1,
ludf1.udfvalue as external

FROM process 
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname like 'Read 1 Cycle%%') 
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname like 'Read 2 Cycle%%') 
LEFT OUTER JOIN process_udf_view as pudf3 on (pudf3.processid=process.processid AND pudf3.udfname = 'Finish Date')
LEFT OUTER JOIN process_udf_view as pudf4 on (pudf4.processid=process.processid AND pudf4.udfname = 'Flow Cell ID')
LEFT OUTER JOIN process_udf_view as pudf5 on (pudf5.processid=process.processid AND pudf5.udfname = 'Run ID')
LEFT OUTER JOIN process_udf_view as pudf6 on (pudf6.processid=process.processid AND pudf6.udfname = 'Reagent Cartridge ID'), 
processtype, 
installation, 
instrument, 
itype, 
processiotracker, 
artifact 
LEFT OUTER JOIN artifact_udf_view as audf1 on (audf1.artifactid=artifact.artifactid AND audf1.udfname = 'Billable')
LEFT OUTER JOIN artifact_udf_view as audf2 on (audf2.artifactid=artifact.artifactid AND audf2.udfname = 'Billing Comments')
LEFT OUTER JOIN artifact_udf_view as audf3 on (audf3.artifactid=artifact.artifactid AND audf3.udfname = 'Yield PF (Gb) R1')
LEFT OUTER JOIN artifact_udf_view as audf4 on (audf4.artifactid=artifact.artifactid AND audf4.udfname = 'Avg Q Score R1')
LEFT OUTER JOIN artifact_udf_view as audf5 on (audf5.artifactid=artifact.artifactid AND audf5.udfname = '%% Bases >=Q30 R1')
LEFT OUTER JOIN artifact_udf_view as audf6 on (audf6.artifactid=artifact.artifactid AND audf6.udfname = 'Cluster Density (K/mm^2) R1')
LEFT OUTER JOIN artifact_udf_view as audf7 on (audf7.artifactid=artifact.artifactid AND audf7.udfname = '%%PF R1')
LEFT OUTER JOIN artifact_udf_view as audf8 on (audf8.artifactid=artifact.artifactid AND audf8.udfname = 'Intensity Cycle 1 R1')
LEFT OUTER JOIN artifact_udf_view as audf9 on (audf9.artifactid=artifact.artifactid AND audf9.udfname = '%% Intensity Cycle 20 R1')
LEFT OUTER JOIN artifact_udf_view as audf10 on (audf10.artifactid=artifact.artifactid AND audf10.udfname = '%% Phasing R1')
LEFT OUTER JOIN artifact_udf_view as audf11 on (audf11.artifactid=artifact.artifactid AND audf11.udfname = '%% Prephasing R1')
LEFT OUTER JOIN artifact_udf_view as audf12 on (audf12.artifactid=artifact.artifactid AND audf12.udfname = '%% Aligned R1')
LEFT OUTER JOIN artifact_udf_view as audf13 on (audf13.artifactid=artifact.artifactid AND audf13.udfname = '%% Error Rate R1'), 
containerplacement, 
container, 
artifact_sample_map, 
sample LEFT OUTER JOIN sample_udf_view on (sample_udf_view.sampleid=sample.sampleid AND sample_udf_view.udfname = 'SLX Identifier'), 
project, 
researcher, 
lab LEFT OUTER JOIN entity_udf_view as ludf1 on (lab.labid=ludf1.attachtoid AND ludf1.udfname='External')
LEFT OUTER JOIN address on (lab.billingaddressid=address.addressid), 

-- billing process
process as bprocess LEFT OUTER JOIN process_udf_view as bpudf1 on (bpudf1.processid=bprocess.processid AND bpudf1.udfname = 'Flowcell Billing Comments') ,
processtype as bprocesstype,
processiotracker as bprocessiotracker,
artifact as bartifact

WHERE process.typeid = processtype.typeid
AND processtype.displayname like '%%Run%%'
AND process.installationid=installation.id
AND installation.instrumentid=instrument.instrumentid
AND instrument.typeid=itype.typeid
AND process.processid=processiotracker.processid 
AND processiotracker.inputartifactid=artifact.artifactid
AND containerplacement.processartifactid=artifact.artifactid
AND containerplacement.containerid=container.containerid
AND artifact_sample_map.artifactid=artifact.artifactid
AND artifact_sample_map.processid=sample.processid
AND sample.projectid=project.projectid
AND project.researcherid=researcher.researcherid
AND researcher.labid=lab.labid
AND artifact.luid IN ( 
	SELECT sub_artifact.luid
	FROM processiotracker as sub_processiotracker, process as sub_process, processtype as sub_processtype, artifact as sub_artifact
	WHERE sub_processiotracker.processid=sub_process.processid 
	AND sub_process.typeid=sub_processtype.typeid 
	AND sub_processtype.displayname='Billing' 
	AND sub_processiotracker.inputartifactid=sub_artifact.artifactid 
	-- AND sub_process.daterun >= '2013-04-01' AND sub_process.daterun <= '2013-12-07'
	AND sub_process.daterun >= '%(start_date)s' AND sub_process.daterun <= '%(end_date)s'
) 
-- billing process
AND artifact.luid=bartifact.luid
AND bprocess.typeid = bprocesstype.typeid
AND bprocessiotracker.processid=bprocess.processid
AND bprocessiotracker.inputartifactid=bartifact.artifactid
AND bprocesstype.displayname='Billing'
"""

RUNPROCESS_BY_FINISHDATE_QUERY = """
SELECT 
process.luid, process.daterun, processtype.displayname, process.workstatus, process.createddate, process.lastmodifieddate,
to_char(to_date(pudf1.udfvalue, 'YYYY-MM'), 'YYYY-MM') as finishdate, pudf2.udfvalue as flowcellid

FROM process 
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Finish Date')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname like 'Flow Cell ID'),
processtype

WHERE process.typeid = processtype.typeid
AND process.workstatus = 'COMPLETE'
AND (pudf1.udfvalue >= '%(begin_date)s' and pudf1.udfvalue < '%(end_date)s' or pudf1.udfvalue is null)
AND processtype.displayname like '%%Run%%'
"""

RUNPROCESS_BY_MODIFIEDDATE_QUERY = """
SELECT 
process.luid, processtype.displayname, process.createddate, process.daterun, 
pudf1.udfvalue as finishdate, process.lastmodifieddate, pudf2.udfvalue as flowcellid, pudf3.udfvalue as status, 
pudf4.udfvalue as runfolder, pudf5.udfvalue as read1, pudf6.udfvalue as indexread1, pudf8.udfvalue as indexread2, pudf7.udfvalue as read2

FROM process 
LEFT OUTER JOIN process_udf_view as pudf1 on (pudf1.processid=process.processid AND pudf1.udfname = 'Finish Date')
LEFT OUTER JOIN process_udf_view as pudf2 on (pudf2.processid=process.processid AND pudf2.udfname like 'Flow Cell ID')
LEFT OUTER JOIN process_udf_view as pudf3 on (pudf3.processid=process.processid AND pudf3.udfname like 'Status')
LEFT OUTER JOIN process_udf_view as pudf4 on (pudf4.processid=process.processid AND pudf4.udfname like 'Run ID')
LEFT OUTER JOIN process_udf_view as pudf5 on (pudf5.processid=process.processid AND pudf5.udfname like 'Read 1 Cycles')
LEFT OUTER JOIN process_udf_view as pudf6 on (pudf6.processid=process.processid AND pudf6.udfname like 'Index 1 Read Cycles')
LEFT OUTER JOIN process_udf_view as pudf7 on (pudf7.processid=process.processid AND pudf7.udfname like 'Read 2 Cycles')
LEFT OUTER JOIN process_udf_view as pudf8 on (pudf8.processid=process.processid AND pudf8.udfname like 'Index 2 Read Cycles'),
processtype

WHERE process.typeid = processtype.typeid
AND process.workstatus = 'COMPLETE'
AND process.lastmodifieddate >= '%(begin_date)s' AND process.lastmodifieddate <= '%(end_date)s'
AND processtype.displayname like '%%Run%%'
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
sudf5.udfvalue as seqtype

FROM 
(	SELECT processid, COUNT(artifactid) AS occurences 
	FROM artifact_sample_map 
	GROUP BY processid
) AS samplewithoneartifact,
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
AND (sample.datereceived is NULL OR sample.datereceived >= '2013-08-01')
AND sample.processid=samplewithoneartifact.processid
AND sudf2.udfvalue is NULL
AND sample.projectid=project.projectid
AND artifact_sample_map.processid=sample.processid
AND artifact_sample_map.artifactid=artifact.artifactid
AND project.researcherid=researcher.researcherid
"""
