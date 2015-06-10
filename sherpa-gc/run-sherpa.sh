# ini
export LD_LIBRARY_PATH=$PWD:@LOCAL@/lib:@LOCAL@/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:@HOME@/sherivf/work:$RIVET_ANALYSIS_PATH
. ini.sh

echo "SHERIVFDIR: "$SHERIVFDIR
cp -r $SHERIVFDIR/sherpa-cfg/* .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee.cc $SHERIVFDIR/MCgrid_CMS_2015_Zee*.str .
cp $SHERIVFDIR/RivetMyAnalyses.so .

@WARMUP@

echo -e "\ndirectory contents:"
ls
echo "\n\n"

export SHERPACMD="@LOCAL@/bin/Sherpa -e @NEVENTS@ -R @SEED_0@"
echo -e "Start Sherpa: $SHERPACMD\n"
$SHERPACMD
