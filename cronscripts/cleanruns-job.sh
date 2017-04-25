#!/bin/sh
#SBATCH --no-requeue
#SBATCH -p general
#SBATCH -J clean_scratch_space
#SBATCH --mem 4096
#SBATCH --mincpus 1
#SBATCH --open-mode truncate
#SBATCH -o /mnt/scratcha/bioinformatics/solexa/Runs/clean_scratch_space/run-cleanruns.%j.out

/home/solexa/ngs-autoanalysis/branch-2.0/run-cleanruns.sh
