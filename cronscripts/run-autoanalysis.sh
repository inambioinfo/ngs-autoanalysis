AUTOANALYSIS_HOME=/home/bioinformatics/software/ngs-autoanalysis/branch-2.2/
PLATFORM=$(uname -r | cut -d '.' -f 6)
source /home/bioinformatics/environment.bashrc.newservers
source $AUTOANALYSIS_HOME/venv-$PLATFORM/bin/activate
python $AUTOANALYSIS_HOME/autoanalysis.py --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/solexa/sequencingpipelines/ --logfile=/processing/Logs/autoanalysis.log
