#!/bin/bash

echo -e "\ndirectory contents:"
ls -lt

export LD_LIBRARY_PATH=$PWD:@LOCAL@/lib:@LOCAL@/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:@HOME@/sherivf/work:$RIVET_ANALYSIS_PATH
#. ini.sh
export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD


@WARMUP@

# copy warmup files, create folders
mkdir -p @ANALYSIS@/phasespace/
mv *.txt @ANALYSIS@/phasespace/

echo "SHERIVFDIR: "$SHERIVFDIR

echo -e "\n\n"

export SHERPACMD="@SHERPAPATH@/Sherpa -e @NEVENTS@ -R @SEED_0@"
echo -e "Start Sherpa: $SHERPACMD\n"
$SHERPACMD

mv @ANALYSIS@/*.tab .
mv @ANALYSIS@/phasespace/*.txt .


echo -e "\nafter sherpa:"
ls -tl
