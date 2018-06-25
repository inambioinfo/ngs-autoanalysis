#!/bin/bash
set -v

scp /home/mib-cri/software/ngs-autoanalysis/branch-2.2/cleanruns.sh clust1-headnode:/mnt/scratcha/bioinformatics/solexa/Runs/clean_scratch_space/.
scp /home/mib-cri/software/ngs-autoanalysis/branch-2.2/cronscripts/cleanruns-job.sh clust1-headnode:/mnt/scratcha/bioinformatics/solexa/Runs/clean_scratch_space/.

ssh clust1-headnode "sbatch /mnt/scratcha/bioinformatics/solexa/Runs/clean_scratch_space/cleanruns-job.sh"
