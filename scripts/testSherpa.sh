#!/bin/bash

set -e

TESTDIR=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $SHERIVFDIR/test/$TESTDIR
cd $SHERIVFDIR/test/$TESTDIR

# copy all cfg files
cp -r $SHERIVFDIR/sherpa-cfg/* .
cp $SHERIVFDIR/fnlo-cfg/fnlo_*_warmup.tab .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee*.* .
cp $SHERIVFDIR/RivetMyAnalyses.so .

export SHERPACMD="$HOME/local/bin/Sherpa $@"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD

echo $SHERIVFDIR/test/$TESTDIR

