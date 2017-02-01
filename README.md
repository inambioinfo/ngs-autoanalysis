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

Tools currently in used on four production servers : sol-srv001/2/3/4 with new cluster `uk-cri-lcst01` for running alignment pipeline:
- `autoassignsamples.py`: automatically assign samples to workflow after submission
- `manageglsevents.py`: run events synchronization for Clarity LiMS
- `manageruns.py`: update run status in run folder by adding `Sequencing.failed` or `Sequencing.completed`
- `autoanalysis.py`: automatically runs the different primary analysis pipeline steps

## Dependencies

- Python Clarity Client API v0.4.3: https://github.com/crukci-bioinformatics/claritypy-client/releases/tag/v0.4.3

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

v1.8 crontab usage using old cluster (LSF)

```bash
### auto assign samples (only on sol-srv001)
0 07,12,14,16 * * * source /home/mib-cri/software/ngs-autoanalysis/branch-1.8/venv/bin/activate; python /home/mib-cri/software/ngs-autoanalysis/branch-1.8/autoassignsamples.py --logfile=/processing/Logs/autoassignsamples.log --update --updatesamples --email > /dev/null 2>&1

### manage gls events
*/5 * * * * source /home/mib-cri/software/ngs-autoanalysis/branch-1.8/venv/bin/activate; python /home/mib-cri/software/ngs-autoanalysis/branch-1.8/manageglsevents.py --logfile=/processing/Logs/manageglsevents.log > /dev/null 2>&1

### manage runs
*/15 * * * * source /home/mib-cri/software/ngs-autoanalysis/branch-1.8/venv/bin/activate; python /home/mib-cri/software/ngs-autoanalysis/branch-1.8/manageruns.py --clusterdir=/lustre/mib-cri/solexa/Runs/ --processingdir=/processing/ --stagingdir=/staging/ --processeddir=/processing/ProcessedRuns/ --trashdir=/lustre/mib-cri/solexa/TrashRuns/ --logfile=/processing/Logs/manageruns.log > /dev/null 2>&1

### auto analysis
*/20 * * * * source /home/mib-cri/software/ngs-autoanalysis/branch-1.8/venv/bin/activate; python /home/mib-cri/software/ngs-autoanalysis/branch-1.8/autoanalysis.py --clusterdir=/lustre/mib-cri/solexa/Runs/ --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/mib-cri/software/core-pipelines-v2/ --cluster=uk-cri-lcst01 --logfile=/processing/Logs/autoanalysis.log > /dev/null 2>&1
```

## Updates

After pulling new code from GitHub into a local `ngs-autoanalysis/` directory, make sure to run these commands in case the dependencies have also been updated, specially the one to the [Python Clarity Client API, claritypy-client](https://github.com/crukci-bioinformatics/claritypy-client/):

```
git pull
source venv/bin/activate
pip install -r requirements.txt
```
