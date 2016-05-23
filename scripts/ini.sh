#!/bin/bash

# source ROOT if not sourced

export ROOTSYS=/cvmfs/sft.cern.ch/lcg/app/releases/ROOT/5.34.13/x86_64-slc6-gcc48-opt/root/
export GCCLIBS=/cvmfs/sft.cern.ch/lcg/external/gcc/4.7.2/x86_64-slc5/lib64/
export LD_LIBRARY_PATH=$GCCLIBS:$LD_LIBRARY_PATH
. $ROOTSYS/bin/thisroot.sh


export SHERIVFDIR=$(dirname $(dirname $(readlink -mf ${BASH_SOURCE[0]})))

if [ -f $SHERIVFDIR/scripts/configures.sh ]; then
	. $SHERIVFDIR/scripts/configures.sh
fi

export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD


export SHERIVF_STORAGE_PATH=/storage/a/${USER}/sherivf/
export HERA_STORAGE_PATH=/storage/a/${USER}/hera/
export PKG_CONFIG_PATH=$SHERIVFDIR/../enrico/mcgrid/mcgrid/:$PKG_CONFIG_PATH
export LOCALHOME=/usr/users/${USER}/

# Rivet
export PATH=$SHERIVFDIR/../Rivet-2.2.0/bin/:$SHERIVFDIR/scripts:$PATH:/usr/users/${USER}/local/bin
export PATH=$HOME/local/bin:$PATH
export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH
if [ -e $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh ]
then
	. $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh
fi


#Sherpa
export SHERPA_INCLUDE_PATH=$LOCALHOME/local/include/SHERPA-MC
export SHERPA_SHARE_PATH=$LOCALHOME/local/share/SHERPA-MC
export SHERPA_LIBRARY_PATH=$LOCALHOME/local/lib/SHERPA-MC
export LD_LIBRARY_PATH=$SHERPA_LIBRARY_PATH:$LOCALHOME/local/lib:$LD_LIBRARY_PATH


#other stuff
export QCDNUM_ROOT=/portal/ekpcms6/home/${USER}/qcd/qcdnum-17-00-06

export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH

export BOOSTPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/boost/1.57.0-cflfif
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH:$BOOSTPATH/lib:$HOME/local/lib64/:/usr/users/${USER}/local/lib/SHERPA-MC/

# aliases
export RIVET_COMPILER_FLAGS="-std=c++0x -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA -DUSE_FNLO=1"

