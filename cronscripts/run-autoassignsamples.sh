AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.1/
source $AUTOANALYSIS_HOME/venv/bin/activate
python $AUTOANALYSIS_HOME/autoassignsamples.py --logfile=/processing/Logs/autoassignsamples.log --update --updatesamples --email
