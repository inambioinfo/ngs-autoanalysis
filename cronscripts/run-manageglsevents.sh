AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.2/
source $AUTOANALYSIS_HOME/venv-$(uname -r | cut -d '.' -f 6)/bin/activate
python $AUTOANALYSIS_HOME/manageglsevents.py --logfile=/processing/Logs/manageglsevents.log
