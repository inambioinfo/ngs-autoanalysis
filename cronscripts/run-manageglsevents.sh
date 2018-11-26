AUTOANALYSIS_HOME=/home/bioinformatics/software/ngs-autoanalysis/branch-2.2/
PLATFORM=$(uname -r | cut -d '.' -f 6)
source $AUTOANALYSIS_HOME/venv-$PLATFORM/bin/activate
python $AUTOANALYSIS_HOME/manageglsevents.py --logfile=/processing/Logs/manageglsevents.log
