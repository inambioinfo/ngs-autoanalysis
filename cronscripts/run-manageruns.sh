AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.2/
source $AUTOANALYSIS_HOME/venv/bin/activate
python $AUTOANALYSIS_HOME/manageruns.py --processingdir=/processing/ --stagingdir=/staging/ --processeddir=/processing/ProcessedRuns/ --logfile=/processing/Logs/manageruns.log
