#!/bin/bash

TESTDIR=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $SHERIVFDIR/test/$TESTDIR
cd $SHERIVFDIR/test/$TESTDIR
cp -r $SHERIVFDIR/sherpa-cfg/* .

echo "Make fifo"
#mkfifo fifo.hepmc

export SHERPACMD="/usr/users/dhaitz/local/bin/Sherpa RESULT_DIRECTORY=$PWD EVENTS=1 EVENT_OUTPUT=HepMC_Short[fifo]"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD #&

export RIVETCMD="/usr/users/dhaitz/local/bin/rivet --pwd --analysis MCgrid_CMS_2015_Zee fifo.hepmc"
echo "Start Rivet "$RIVETCMD
#$RIVETCMD

#rm fifo.hepmc
