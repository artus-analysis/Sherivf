echo "Make fifo"
mkfifo fifo.hepmc
echo @HOME@ @LOCAL@

# ini
export LD_LIBRARY_PATH=$PWD:@LOCAL@/lib:@LOCAL@/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:@HOME@/sherivf/work:$RIVET_ANALYSIS_PATH
. ini.sh

export SHERPACMD="@LOCAL@/bin/Sherpa RESULT_DIRECTORY=$PWD EVENTS=@NEVENTS@ EVENT_OUTPUT=HepMC_Short[fifo] -R @SEED_0@"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD &

export RIVETCMD="@LOCAL@/bin/rivet --pwd --analysis MCgrid_CMS_2015_Zee fifo.hepmc"
echo "Start Rivet "$RIVETCMD
$RIVETCMD
