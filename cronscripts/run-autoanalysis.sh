AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.2/
source /home/mib-cri/environment.bashrc.newservers
source $AUTOANALYSIS_HOME/venv-$(uname -r | cut -d '.' -f 6)/bin/activate
python $AUTOANALYSIS_HOME/autoanalysis.py --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/solexa/sequencingpipelines/ --logfile=/processing/Logs/autoanalysis.log
