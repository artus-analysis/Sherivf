#!/bin/bash

TESTDIR=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $SHERIVFDIR/test/$TESTDIR
cd $SHERIVFDIR/test/$TESTDIR
cp -r $SHERIVFDIR/sherpa-cfg/* .
cp $SHERIVFDIR/fnlo_pTZ_warmup.txt $SHERIVFDIR/fnlo_yZ_warmup.txt $SHERIVFDIR/MCgrid_CMS_2015_Zee.cc $SHERIVFDIR/MCgrid_CMS_2015_Zee.str $SHERIVFDIR/MCgrid_CMS_2015_Zee_2.str .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee.cc $SHERIVFDIR/MCgrid_CMS_2015_Zee.str $SHERIVFDIR/MCgrid_CMS_2015_Zee_2.str .
cp $SHERIVFDIR/RivetMyAnalyses.so .


export SHERPACMD="/usr/users/dhaitz/local/bin/Sherpa EVENTS=99" # EVENT_OUTPUT=HepMC_Short[fifo]"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD

