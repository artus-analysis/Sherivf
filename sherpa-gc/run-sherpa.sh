echo "Make fifo"
mkfifo fifo.hepmc

# ini
export LD_LIBRARY_PATH=/usr/users/dhaitz/local/lib:/usr/users/dhaitz/local/lib64:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:/usr/users/dhaitz/home/qcd/work:$RIVET_ANALYSIS_PATH
. ini.sh

export SHERPACMD="/usr/users/dhaitz/local/bin/Sherpa RESULT_DIRECTORY=$PWD EVENTS=@NEVENTS@ EVENT_OUTPUT=HepMC_Short[fifo] -R @SEED_0@"
echo "Start Sherpa: $SHERPACMD"
$SHERPACMD &

export RIVETCMD="/usr/users/dhaitz/local/bin/rivet --pwd --analysis MCgrid_CMS_2015_Zee fifo.hepmc"
echo "Start Rivet "$RIVETCMD
$RIVETCMD

