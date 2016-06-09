#!/bin/bash

export LD_LIBRARY_PATH=/usr/users/$USER/local/lib:/usr/users/$USER/local/lib/SHERPA-MC/:$LD_LIBRARY_PATH
export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH
export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD



#. ini.sh
################################################################################

export ARCHITECTURE_47=slc6_amd64_gcc472
export ARCHITECTURE=slc6_amd64_gcc491
alias set_gcc_472=". /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/gcc/4.7.2/etc/profile.d/init.sh"
alias set_gcc_491=". /cvmfs/cms.cern.ch/$ARCHITECTURE/external/gcc/4.9.1-cms/etc/profile.d/init.sh"
. /cvmfs/cms.cern.ch/$ARCHITECTURE/external/gcc/4.9.1-cms/etc/profile.d/init.sh

# take software from CVMFS
export YODA_CVMFS=yoda/1.3.1
export HEPMC_CVMFS=hepmc/2.06.07-cms
export RIVET_CVMFS=rivet/2.2.1-kpegke
export FASTJET_CVMFS=fastjet/3.1.0
export GSL_CVMFS=gsl/1.10-cms
for SOFTWARE in lhapdf/6.1.5 $YODA_CVMFS $HEPMC_CVMFS $FASTJET_CVMFS $RIVET_CVMFS $GSL_CVMFS; do
	. /cvmfs/cms.cern.ch/$ARCHITECTURE/external/$SOFTWARE/etc/profile.d/init.sh
done
export QD_CVMFS=qd/2.3.13
. /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/$QD_CVMFS/etc/profile.d/init.sh

################################################################################




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
