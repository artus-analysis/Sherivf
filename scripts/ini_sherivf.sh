#!/bin/bash

# source ROOT if not set
if [ -z $ROOT_INCLUDE_PATH ]; then
	export ROOTSYS=/cvmfs/sft.cern.ch/lcg/app/releases/ROOT/5.34.13/x86_64-slc6-gcc48-opt/root/
	cd $ROOTSYS
	. bin/thisroot.sh
	cd -
fi

# use GCC version from CVMFS
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
export NUMPY_CVMFS=py2-numpy/1.9.2
export LHAPDF_CVMFS=lhapdf/6.1.5-cms
export LHAPDF_DATA_PATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc493/external/lhapdf/6.1.6/share/LHAPDF/
export PYTHON_CVMFS=python/2.7.6-kpegke
export MATPLOTLIB_CVMFS=py2-matplotlib/1.2.1-cms3
export LIBPNG_CVMFS=libpng/1.6.16
export DATEUTIL_CVMFS=py2-python-dateutil/1.5-kpegke
for SOFTWARE in $LIBPNG_CVMFS $MATPLOTLIB_CVMFS $PYTHON_CVMFS $NUMPY_CVMFS lapack/3.3.1-cms $LHAPDF_CVMFS $YODA_CVMFS $HEPMC_CVMFS $FASTJET_CVMFS $RIVET_CVMFS $GSL_CVMFS; do
	. /cvmfs/cms.cern.ch/$ARCHITECTURE/external/$SOFTWARE/etc/profile.d/init.sh
done
export QD_CVMFS=qd/2.3.13
. /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/$QD_CVMFS/etc/profile.d/init.sh

# some environment paths
export SHERIVFDIR=$(dirname $(dirname $(readlink -mf ${BASH_SOURCE[0]})))
export PATH=$SHERIVFDIR/scripts:$HOME/local/bin:$PATH
export LD_LIBRARY_PATH=$HOME/local/lib:$HOME/local/lib/SHERPA-MC:/cvmfs/cms.cern.ch/$ARCHITECTURE/external/python/2.7.6-kpegke/lib/:$LD_LIBRARY_PATH
export PYTHONPATH="\
$HOME/local/lib64/python2.6/site-packages/\
:/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$NUMPY_CVMFS/lib/python2.7/site-packages/\
:/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$LHAPDF_CVMFS/lib/python2.7/site-packages/\
:/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$MATPLOTLIB_CVMFS/lib/python2.7/site-packages/\
:/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$DATEUTIL_CVMFS/lib/python2.7/site-packages/\
:$PYTHONPATH"
export LHAPATH=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$LHAPDF_CVMFS/share/LHAPDF


# output paths for batch mode
if [ $USER = "tberger" ]; then
	export STORAGE_PATH=/storage/jbod/${USER}
elif [ $USER = "afriedel" ]; then
	export STORAGE_PATH=/nfs/dust/cms/user/afriedel
	export COMPILE=/afs/desy.de/user/a/afriedel/local/
fi
export SHERIVF_STORAGE_PATH=$STORAGE_PATH/sherivf/
export XFITTER_STORAGE_PATH=$STORAGE_PATH/xfitter/
export PATH=$SHERIVFDIR/grid-control:$PATH
