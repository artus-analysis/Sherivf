echo "Make fifo"
#mkfifo fifo.hepmc

echo "SHERIVFDIR: "

# ini
export LD_LIBRARY_PATH=$PWD:@LOCAL@/lib:@LOCAL@/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:@HOME@/sherivf/work:$RIVET_ANALYSIS_PATH
. ini.sh
cp -r $SHERIVFDIR/sherpa-cfg/* .
#cp $SHERIVFDIR/fnlo_pTZ_warmup.txt $SHERIVFDIR/fnlo_yZ_warmup.txt $SHERIVFDIR/MCgrid_CMS_2015_Zee.cc $SHERIVFDIR/MCgrid_CMS_2015_Zee.str $SHERIVFDIR/MCgrid_CMS_2015_Zee_2.str .
cp $SHERIVFDIR/MCgrid_CMS_2015_Zee.cc $SHERIVFDIR/MCgrid_CMS_2015_Zee.str $SHERIVFDIR/MCgrid_CMS_2015_Zee_2.str .
cp $SHERIVFDIR/RivetMyAnalyses.so .


ls
echo ""
echo ""
echo ""
ls Process/*

export SHERPACMD="@LOCAL@/bin/Sherpa EVENTS=@NEVENTS@"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD # &

#export RIVETCMD="@LOCAL@/bin/rivet --pwd --analysis MCgrid_CMS_2015_Zee fifo.hepmc"
#echo "Start Rivet "$RIVETCMD
#$RIVETCMD
