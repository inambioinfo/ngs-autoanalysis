AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.2/
PLATFORM=$(uname -r | cut -d '.' -f 6)
source /home/mib-cri/environment.bashrc.newservers
source $AUTOANALYSIS_HOME/venv-$PLATFORM/bin/activate
if ["$PLATFORM" == "el7"]; then
  limsdev='--limsdev'
else
  limsdev=''
fi
python $AUTOANALYSIS_HOME/autoanalysis.py --processingdir=/processing/ --stagingdir=/staging/ --softdir=/home/solexa/sequencingpipelines/ --logfile=/processing/Logs/autoanalysis.log $limsdev
