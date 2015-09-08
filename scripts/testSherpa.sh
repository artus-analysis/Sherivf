#!/bin/bash

set -e


TESTDIR=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $SHERIVFDIR/test/$TESTDIR
cd $SHERIVFDIR/test/$TESTDIR


export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD

# copy all cfg files
cp -r $SHERIVFDIR/sherpa-cfg/fo/* .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee*.* .
cp $SHERIVFDIR/RivetMyAnalyses.so .
cp $SHERIVFDIR/fnlo-cfg/*.evtcount .

#warmup files
cp $SHERIVFDIR/fnlo-cfg/*.txt .
mkdir -p MCgrid_CMS_2015_Zee/phasespace/
cp *.txt MCgrid_CMS_2015_Zee/phasespace/


export SHERPACMD="$HOME/local/bin/Sherpa $@"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD

cp MCgrid_CMS_2015_Zee/*.tab .

echo $SHERIVFDIR/test/$TESTDIR

yoda_2_root.py Rivet.yoda
