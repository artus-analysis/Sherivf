export PATH=/usr/users/dhaitz/home/qcd/Rivet-2.2.0/bin/:/usr/users/dhaitz/home/qcd/applgrid-1.4.70/bin:$PATH:/usr/users/dhaitz/local/bin
. /usr/users/dhaitz/home/qcd/Rivet-2.2.0/rivetenv.sh

export PKG_CONFIG_PATH=/usr/users/dhaitz/home/qcd/enrico/mcgrid/mcgrid/:$PKG_CONFIG_PATH

export RIVET_ANALYSIS_PATH=$PWD:$RIVET_ANALYSIS_PATH

# fastjet plugins
#-L/usr/users/dhaitz/local/include/fastjet/.libs
# install fastjet with  "./configure --prefix=$HOME/local  --enable-allcxxplugins --enable-shared"


# build plugins
# rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1

#fastnlo 
# ./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION="2.6"

#yoda
export PATH=/usr/users/dhaitz/local/bin/:$PATH
export PYTHONPATH=/usr/users/dhaitz/local/lib64/python2.6/site-packages:/usr/users/dhaitz/local/lib/python2.6/site-packages:$PYTHONPATH

#export BOOSTPATH=$(ls ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/boost/* -d | tail -n 1)
export BOOSTPATH=/cvmfs/cms.cern.ch//slc6_amd64_gcc481/external/boost/1.57.0-cflfif

#export BOOSTLIB=${BOOSTPATH}/lib/libboost_regex.so.${BOOSTPATH/*\//}
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH:$BOOSTPATH/lib:/usr/users/dhaitz/local/lib64/
# -L$(BOOSTPATH)/lib/

#LHAPDF
export PATH=/usr/users/dhaitz/qcd/lhapdf-5.9.1/bin/:$PATH

alias rivbuild="rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1"
alias riv="rivet  --analysis MCgrid_CMS_2015_Zee ../SHERPA-MC-2.1.1/Examples/V_plus_Jets/LHC_ZJets/sherpa_zjet.hepmc --pwd"

export PATH=$(dirname $(readlink -mf ${BASH_SOURCE[0]}))/scripts:$PATH
