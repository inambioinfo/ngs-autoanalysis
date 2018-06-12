# NGS Auto Analysis

Automation of the processing of NextGen Sequencing data @ CRUK-CI using Genologics Clarity LiMS

This Python tool, `autoanalysis.py`, automatizes:
- the creation of the run-meta.xml needed for the pipeline to run;
- runs the different primary analysis pipeline steps;
- synchronises the data to the staging server;
- publishes external data onto the ftp server;
- and assign each run to the publishing queue in Clarity.

The list of runs is obtained from the file system; and their status are checked against our internal Clarity LiMS.

This tool replaces the old Perl `solexa_autoanalysis.pl` written by Kevin Howe and modified/maintained by Ben Davis.
All steps of the sequencing pipeline have been standardised and are using the workflow engine written by Richard Bowers.

Tools currently in used on four production servers : sol-srv001/2/3/4:
- `autoassignsamples.py`: automatically assign samples to workflow after submission
- `manageglsevents.py`: synchronise run events from sequencers to Clarity LiMS server
- `manageruns.py`: update run status in run folder by adding `Sequencing.failed` or `Sequencing.completed`
- `autoanalysis.py`: automatically runs the different primary analysis pipeline steps


## Dependencies

- Python 2.7.15

Installed on sols' servers in `/home/mib-cri/software/centos6/python2.7.15/bin/python`


- Python Clarity Client API v0.4.6: https://github.com/crukci-bioinformatics/claritypy-client/releases/tag/v0.4.6

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

On sol's servers:
```bash
virtualenv --python=/home/mib-cri/software/centos6/python2.7.15/bin/python venv
source ven/bin/activate
pip install --upgrade setuptools
pip install --upgrade urllib3
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
FILES_DB_NAME=clarityfiles
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


## Updates

After pulling new code from GitHub into a local `ngs-autoanalysis/` directory, make sure to run these commands in case the dependencies have also been updated, specially the one to the [Python Clarity Client API, claritypy-client](https://github.com/crukci-bioinformatics/claritypy-client/):

```
git pull
source venv/bin/activate
pip install -r requirements.txt
```
