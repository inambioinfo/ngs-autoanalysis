SCRATCH_DIR=/mnt/scratcha/bioinformatics/solexa/Runs/
find $SCRATCH_DIR/. -name pipeline.ended -mtime +5 | xargs -0 bash -c 'for f; do echo $(dirname $(dirname $f)) will be deleted; rm -rf $(dirname $(dirname $f)); done' bash
