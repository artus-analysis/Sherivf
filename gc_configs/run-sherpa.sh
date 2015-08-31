#!/bin/bash

echo -e "\ndirectory contents:"
ls -lt

export LD_LIBRARY_PATH=$PWD:@LOCAL@/lib:@LOCAL@/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:@HOME@/sherivf/work:$RIVET_ANALYSIS_PATH
. ini.sh

echo "SHERIVFDIR: "$SHERIVFDIR

@WARMUP@

echo -e "\n\n"

export SHERPACMD="@LOCAL@/bin/Sherpa -e @NEVENTS@ -R @SEED_0@"
echo -e "Start Sherpa: $SHERPACMD\n"
$SHERPACMD
