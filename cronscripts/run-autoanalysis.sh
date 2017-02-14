AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.0/
source source /home/mib-cri/environment.bashrc.newservers
source $AUTOANALYSIS_HOME/venv/bin/activate
python $AUTOANALYSIS_HOME/autoanalysis.py --clusterdir=/mnt/scratcha/bioinformatics/solexa/Runs/ --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/solexa/sequencingpipelines/ --cluster=clust1-headnode --logfile=/processing/Logs/autoanalysis.log
