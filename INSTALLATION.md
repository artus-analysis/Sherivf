# Installation

## Needed:
For Monte Carlo event generation and fastNLO table production:

* Event generation
 * [Sherpa 2.2.0](https://sherpa.hepforge.org/trac/wiki/SherpaDownloads/Sherpa-2.2.0) [(Documentation)](https://sherpa.hepforge.org/doc/SHERPA-MC-2.2.0.html)
 * [Blackhat 0.9.9](https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation)
* Event processing and fastNLO table production
 * Rivet 2.3
 * MCgrid 2.0
 * fastNLO 2.3.1pre-2125
* for PDF fits:
 * xFitter 1.2.0

## Installation
many needed
smaller tools (without special configuration) can be directly taken from CVMFS:
QD, fastjet, LHAPDF, HepMC, YODA
source ini to get these and uptodate gcc/g++ compiler
4.7? needed for blackhat
sherpa, blackhat

bild mit software and howto


First, set up sherivf (to set environment paths and get tools from CVMFS):

    cd SheRivF
    . scripts/ini_sherivf.sh
    cd ..

### For event generation / fastNLO table production

#### BLACKHAT 0.9.9
* https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation
* GCC version 4.7.2

Blackhat libraries can become huge -> install in storage:

    wget http://www.hepforge.org/archive/blackhat/blackhat-0.9.9.tar.gz
    tar -xzf blackhat-0.9.9.tar.gz
    cd blackhat-0.9.9
    . /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/gcc/4.7.2/etc/profile.d/init.sh # blackhat has to be compiled with older gcc version
    ./configure --prefix=/storage/a/${USER}/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/$QD_CVMFS
    make -j 12
    make install
    . /cvmfs/cms.cern.ch/$ARCHITECTURE/external/gcc/4.9.1-cms/etc/profile.d/init.sh  # return to default compiler
    cd ..
#### SHERPA 2.2.0
    wget http://www.hepforge.org/archive/sherpa/SHERPA-MC-2.2.0.tar.gz
    tar -xzf SHERPA-MC-2.2.0.tar.gz
    cd SHERPA-MC-2.2.0
    ./configure --prefix=$HOME/local  --enable-hepmc2=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$HEPMC_CVMFS --enable-rivet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$RIVET_CVMFS --enable-blackhat=/storage/a/dhaitz/software/blackhat  --enable-fastjet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$FASTJET_CVMFS 
    make -j 12
    make install
    cd ..

#### fastNLO 2.3.1pre-2212
    wget http://fastnlo.hepforge.org/code/v23/fastnlo_toolkit-2.3.1pre-2212.tar.gz
    tar -xzf fastnlo_toolkit-2.3.1pre-2212.tar.gz
    cd fastnlo_toolkit-2.3.1pre-2212
    ./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION='2.6'
    make -j 8
    make install
    cd ..

#### MCgrid 2.0
    wget https://www.hepforge.org/archive/mcgrid/mcgrid-2.0.tar.gz
    tar -xzf mcgrid-2.0.tar.gz
    cd mcgrid-2.0
    ./configure --prefix=$HOME/local
    make -j 8
    make install
    cd ..





### For PDF fits

#### QCDNUM 17-00/07 
    wget http://www.nikhef.nl/user/h24/qcdnum-files/download/qcdnum170112.tar.gz
    tar -xzf qcdnum170112.tar.gz
    cd qcdnum-17-01-12
    ./configure --prefix=$HOME/local
    make -j 8
    make install
    cd ..


#### xFitter 1.2.0
    wget -U Mozilla/5.0 --no-check-certificate "https://wiki-zeuthen.desy.de/xFitter/xFitter/DownloadPage?action=AttachFile&do=get&target=xfitter-1.2.0.tgz" -O xfitter-1.2.0.tgz
    tar -xzf xfitter-1.2.0.tgz
    cd xFitter-1.2.0/
    #./configure --prefix=$HOME/local --enable-lhapdf
    #./configure --prefix=$HOME/local CFLAGS="-I/usr/users/${USER}/local/include" LDFLAGS="-L/usr/users/${USER}/local/lib/ -I/usr/users/${USER}/local/include -lblas -lyaml" --enable-process --enable-lhapdf
    autoreconf
    ./configure --prefix=$HOME/local --enable-lhapdf LDFLAGS="-L/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/lapack/3.3.1-cms/lib"
    #. /cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/lapack/3.3.1-cms/etc/profile.d/init.sh
    automake
    make -j 8
    make install
    cd ..
