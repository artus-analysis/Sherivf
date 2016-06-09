#!/bin/bash

# set environment
export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH
export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD
. @SHERIVFDIR@/scripts/ini_sherivf.sh


@WARMUP@

# copy warmup files, create folders
mkdir -p @ANALYSIS@/phasespace/
mv *.txt @ANALYSIS@/phasespace/

# run Sherpa
export SHERPACMD="@SHERPAPATH@/Sherpa -e @NEVENTS@ -R @SEED_0@"
echo -e "Start Sherpa: $SHERPACMD\n"
$SHERPACMD

mv @ANALYSIS@/*.tab .
mv @ANALYSIS@/phasespace/*.txt .
