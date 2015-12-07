#!/bin/bash

export SHERIVFDIR=$(dirname $(dirname $(readlink -mf ${BASH_SOURCE[0]})))
export HERADIR=$SHERIVFDIR/../herafitter-1.1.1

# additional excalibur cfgs: vary electron scale etc. etc.
export EXCALIBURCONFIGS=$(dirname $(readlink -mf ${BASH_SOURCE[0]})):$EXCALIBURCONFIGS

if [ -f $SHERIVFDIR/scripts/functions.sh ]; then
	. $SHERIVFDIR/scripts/functions.sh
fi
if [ -f $SHERIVFDIR/scripts/configures.sh ]; then
	. $SHERIVFDIR/scripts/configures.sh
fi

export MCGRID_OUTPUT_PATH=$PWD
export MCGRID_PHASESPACE_PATH=$PWD

if ( [[ $HOSTNAME == *"naf"* ]] || [[ $HOSTNAME == *"bird"* ]] ); then
	export SHERIVFDIR=/afs/desy.de/user/d/dhaitz/qcd/sherivf
	export SHERIVF_STORAGE_PATH=/nfs/dust/cms/user/dhaitz/sherivf/
else
	export SHERIVFDIR=/portal/ekpcms6/home/dhaitz/qcd/sherivf
	export SHERIVF_STORAGE_PATH=/storage/a/dhaitz/sherivf/
fi

# Rivet
export PATH=$SHERIVFDIR/../Rivet-2.2.0/bin/:$SHERIVFDIR/scripts:$PATH:/usr/users/dhaitz/local/bin
export PATH=$SHERIVFDIR/../herafitter-1.1.1/bin:$PATH
export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH
if [ -e $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh ]
then
	. $SHERIVFDIR/../Rivet-2.2.0/rivetenv.sh
fi

#harry plotter
export PLOTCONFIGS=$SHERIVFDIR/harryplotter:$PYTHONCONFIGS
export PYTHONPATH=$SHERIVFDIR/harryplotter:$SHERIVFDIR/scripts:$PYTHONPATH
export MODULES_SEARCH_PATH=$SHERIVFDIR/harryplotter/modules:$MODULES_SEARCH_PATH

export PKG_CONFIG_PATH=$SHERIVFDIR/../enrico/mcgrid/mcgrid/:$PKG_CONFIG_PATH

export EKPHOME=/usr/users/dhaitz/

#Sherpa
export SHERPA_INCLUDE_PATH=$EKPHOME/local/include/SHERPA-MC
export SHERPA_SHARE_PATH=$EKPHOME/local/share/SHERPA-MC
export SHERPA_LIBRARY_PATH=$EKPHOME/local/lib/SHERPA-MC
export LD_LIBRARY_PATH=$SHERPA_LIBRARY_PATH:$LD_LIBRARY_PATH

export QCDNUM_ROOT=/portal/ekpcms6/home/dhaitz/qcd/qcdnum-17-00-06


export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH

#export BOOSTPATH=$(ls ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/boost/* -d | tail -n 1)
export BOOSTPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/boost/1.57.0-cflfif

#export BOOSTLIB=${BOOSTPATH}/lib/libboost_regex.so.${BOOSTPATH/*\//}
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH:$BOOSTPATH/lib:$HOME/local/lib64/:/usr/users/dhaitz/local/lib/SHERPA-MC/
# -L$(BOOSTPATH)/lib/

#LHAPDF
if [[ `lhapdf-config  --version` == 5.* ]]; then
	export LHAPATH=/cvmfs/cms.cern.ch/lhapdf/pdfsets/5.9.1
elif [[ `lhapdf-config  --version` == 6.* ]]; then
	export LHAPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/share/LHAPDF/
fi

# aliases
rivbuild_nofastnlo(){
	rivet-buildplugin RivetMyAnalyses.so $1.cc -std=c++0x -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA $2
}
rivbuild(){
	rivbuild_nofastnlo $1 -DUSE_FNLO=1
}
