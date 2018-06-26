AUTOANALYSIS_HOME=/home/mib-cri/software/ngs-autoanalysis/branch-2.2/
PLATFORM=$(uname -r | cut -d '.' -f 6)
source $AUTOANALYSIS_HOME/venv-$PLATFORM/bin/activate
if [ "$PLATFORM" == "el7" ]; then limsdev='--limsdev'; else limsdev=''; fi
python $AUTOANALYSIS_HOME/autoassignsamples.py --logfile=/processing/Logs/autoassignsamples.log --update --updatesamples --email $limsdev
