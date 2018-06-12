AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.1/
source /home/mib-cri/environment.bashrc.newservers
source $AUTOANALYSIS_HOME/venv/bin/activate
python $AUTOANALYSIS_HOME/autoanalysis.py --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/solexa/sequencingpipelines/ --logfile=/processing/Logs/autoanalysis.log
