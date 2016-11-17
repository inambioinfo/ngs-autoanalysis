# NGS Auto Analysis

Automation of the processing of NextGen Sequencing data @ CRUK-CI using Genologics Clarity LiMS

This Python tool, `autoanalysis.py`, automatizes:
- the creation of the run-meta.xml needed for the pipeline to run;
- runs the different primary analysis pipeline steps;
- synchronizes the data to the staging server;
- publishes external data onto the ftp server;
- and assign each run to the publishing queue in Clarity.

The list of runs is obtained from the file system; and their status are checked against our internal Clarity LiMS.

This tool replaces the old Perl `solexa_autoanalysis.pl` written by Kevin Howe and modified/maintained by Ben Davis
because all steps of the sequencing pipeline have been standardized and are now using the workflow engine written by Richard Bowers.

Tools currently in used on four production servers : sol-srv001/2/3/4 with /lustre/ mounted for running alignment pipeline:
- `autoassignsamples.py`: automatically assign samples to workflow after submission
- `manageglsevents.py`: run events synchronization for Clarity LiMS
- `manageruns.py`: update run status in run folder by adding `Sequencing.failed` or `Sequencing.completed`
- `autoanalysis.py`: automatically runs the different primary analysis pipeline steps

## Dependencies

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Your specific Genologics configurations and credentials should be written in this file:

```bash
venv/src/claritypy-glsclient/gls.conf
```

```
[gls]
SERVER=genomicsequencing.cruk.cam.ac.uk
TEST_SERVER=limsdev.cruk.cam.ac.uk
USERNAME=your_api_user
PASSWORD=your_api_password
DB_NAME=clarityDB
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password
[logging]
LOGFILE=glsclient.log
```

## Testing

```bash
python -m unittest --verbose autoanalysis.data
python -m unittest --verbose autoanalysis.pipelines
python -m unittest --verbose autoanalysis.glslims
```

## Usage
