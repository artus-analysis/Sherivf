#!/bin/bash

# source ROOT if not set
if [ -z $ROOT_INCLUDE_PATH ]; then
	export ROOTSYS=/cvmfs/sft.cern.ch/lcg/app/releases/ROOT/5.34.13/x86_64-slc6-gcc48-opt/root/
	#export GCCLIBS=/cvmfs/sft.cern.ch/lcg/external/gcc/4.7.2/x86_64-slc5/lib64/
	#export LD_LIBRARY_PATH=$GCCLIBS:$LD_LIBRARY_PATH
	. $ROOTSYS/bin/thisroot.sh
fi

# use GCC version from CVMFS
export ARCHITECTURE_47=slc6_amd64_gcc472
export ARCHITECTURE=slc6_amd64_gcc491
alias set_gcc_472=". /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/gcc/4.7.2/etc/profile.d/init.sh"
alias set_gcc_491=". /cvmfs/cms.cern.ch/$ARCHITECTURE/external/gcc/4.9.1-cms/etc/profile.d/init.sh"
set_gcc_491

# take software from CVMFS
export YODA_CVMFS=yoda/1.3.1
export HEPMC_CVMFS=hepmc/2.06.07-cms
export RIVET_CVMFS=rivet/2.2.1-kpegke
export FASTJET_CVMFS=fastjet/3.1.0
for SOFTWARE in lhapdf/6.1.5 $YODA_CVMFS $HEPMC_CVMFS $FASTJET_CVMFS $RIVET_CVMFS; do
	. /cvmfs/cms.cern.ch/$ARCHITECTURE/external/$SOFTWARE/etc/profile.d/init.sh
done
export QD_CVMFS=qd/2.3.13
. /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/$QD_CVMFS/etc/profile.d/init.sh


# some environment paths
export SHERIVFDIR=$(dirname $(dirname $(readlink -mf ${BASH_SOURCE[0]})))
export PATH=$SHERIVFDIR/scripts:$HOME/local/bin:$PATH
export LD_LIBRARY_PATH=$HOME/local/lib:$LD_LIBRARY_PATH
#export LD_LIBRARY_PATH=$HOME/local/lib:$HOME/local/lib/SHERPA-MC:$LD_LIBRARY_PATH

# output paths for batch mode
export STORAGE_PATH=/storage/a/${USER}
export SHERIVF_STORAGE_PATH=$STORAGE_PATH/sherivf/
export HERA_STORAGE_PATH=$STORAGE_PATH/hera/




export MC_GRID_DIR=$SHERIVFDIR/../mcgrid-2.0
if [ -d "$MC_GRID_DIR" ]; then
	export PKG_CONFIG_PATH=/storage/a/dhaitz/software/mcgrid-2.0:$PKG_CONFIG_PATH  #TODO
	export RIVET_COMPILER_FLAGS="-std=c++0x -Wl,--export-dynamic,-z,defs $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lYODA"
fi

#export MCGRID_OUTPUT_PATH=$PWD
#export MCGRID_PHASESPACE_PATH=$PWD

# Rivet
#export PATH=$SHERIVFDIR/../Rivet-2.2.0/bin/:/usr/users/${USER}/local/bin:$PATH
#export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH
#if [ -e $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh ]
#then
#	. $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh
#fi


#Sherpa
#export SHERPA_INCLUDE_PATH=$LOCALHOME/local/include/SHERPA-MC
#export SHERPA_SHARE_PATH=$LOCALHOME/local/share/SHERPA-MC
#export SHERPA_LIBRARY_PATH=$LOCALHOME/local/lib/SHERPA-MC
#export LD_LIBRARY_PATH=$SHERPA_LIBRARY_PATH:$LOCALHOME/local/lib:$LD_LIBRARY_PATH


#other stuff
#export QCDNUM_ROOT=/portal/ekpcms6/home/${USER}/qcd/qcdnum-17-00-06
#export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH
#export BOOSTPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/boost/1.57.0-cflfif
#export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH:$BOOSTPATH/lib:$HOME/local/lib64/:/usr/users/${USER}/local/lib/SHERPA-MC/

# aliases
#    -lHepMC -DUSE_FNLO=1"

