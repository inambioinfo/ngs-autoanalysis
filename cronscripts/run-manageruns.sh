AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.0/
source $AUTOANALYSIS_HOME/venv/bin/activate
python $AUTOANALYSIS_HOME/manageruns.py --clusterdir=/lustre/mib-cri/solexa/Runs/ --processingdir=/processing/ --stagingdir=/staging/ --processeddir=/processing/ProcessedRuns/ --trashdir=/lustre/mib-cri/solexa/TrashRuns/ --logfile=/processing/Logs/manageruns.log
