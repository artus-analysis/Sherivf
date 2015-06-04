#!/bin/bash

set -e

TESTDIR=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $SHERIVFDIR/test/$TESTDIR
cd $SHERIVFDIR/test/$TESTDIR

# copy all cfg files
cp -r $SHERIVFDIR/sherpa-cfg/* .
#cp $SHERIVFDIR/fnlo-cfg/fnlo_*_warmup.txt .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee*.* .
cp $SHERIVFDIR/RivetMyAnalyses.so .

export SHERPACMD="$HOME/local/bin/Sherpa EVENTS=${1:-1000}"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD

echo $SHERIVFDIR/test/$TESTDIR

export MERLINCMD="merlin.py --live evince --input-module InputYoda -i $SHERIVFDIR/test/$TESTDIR/Rivet.yoda"

export MERLINCMD_BASE="merlin.py --live evince --input-module  InputRootZJet InputYoda --yodafiles $SHERIVFDIR/test/$TESTDIR/Rivet.yoda -i /usr/users/dhaitz/home/artus/Excalibur/old_work/data_ee_corr.root --folder all_AK5PFJetsCHSL1L2L3Res --nicks data --analys NormalizeToFirstHisto  --y-errors 0"

export MERLINCMD="${MERLINCMD_BASE} -x zpt --x-bins \"25,0,250\" --nicks-whitelist data d01"
echo $MERLINCMD

export MERLINCMD="${MERLINCMD_BASE} -x \"abs(zy)\" --x-bins \"25,0,2.5\" --nicks-whitelist data d02"
echo $MERLINCMD

$MERLINCMD
