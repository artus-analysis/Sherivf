#!/bin/bash

TESTDIR=test_$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir $TESTDIR
cd $TESTDIR
cp -r $SHERIVFDIR/sherpa-cfg/* .

echo "Make fifo"
#mkfifo fifo.hepmc

export SHERPACMD="Sherpa RESULT_DIRECTORY=$PWD EVENTS=1 EVENT_OUTPUT=HepMC_Short[fifo]"
echo "Start Sherpa: $SHERPACMD"
#$SHERPACMD &
$SHERPACMD

export RIVETCMD="rivet --pwd --analysis MCgrid_CMS_2015_Zee fifo.hepmc"
echo "Start Rivet "$RIVETCMD
#$RIVETCMD

#rm fifo.hepmc
