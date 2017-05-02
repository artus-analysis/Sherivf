# Installation

A bunch of software tools is needed for the generation of events, the creation of fastNLO tables and PDF fits.
Some of the small tools with can be directly taken from the CernVM File System (CVMFS).
The main programs like Sherpa need to be locally installed with special configuration as is detailed in the installation instructions below.


![Software](docs/software.png?raw=true)

The installation procedure has been tested on an SLC6 machine, namely the EKPCMS6 and the NAF.
On the BMS machines, there are currently errors with this installation procedure, probably due to missing libraries in /cvmfs. 
Make sure you have enough free disk space.
If possible, install in the `/home/$USER` directory:

    mkdir /home/$USER/PDFstudies
    cd $_  # '$_' is a bash variable for the argument to the previous command, here the created directory

Now, set up SheRivf: Clone the repository and source the ini script to set the environment paths and get tools from CVMFS:

    git clone git@github.com:artus-analysis/Sherivf.git  # or with https: git clone https://github.com/artus-analysis/Sherivf.git
    
Make sure to set the compilation and storage paths in ini_sherivf.sh according to your environment. Afterwards, check it out:

    cd Sherivf
    . scripts/ini_sherivf.sh


Then, install the needed programs by following the command-line instructions below.
Please install the programs in the same folder next to the Sherivf toolkit.

For batch submission of jobs necessary for PDF fits and large-scale MC production, [grid-control](https://ekptrac.physik.uni-karlsruhe.de/trac/grid-control) is used.
It has to be installed and the `go.py` executable inside the grid-control directory has to be in the bash PATH variable:
    
    svn co https://ekptrac.physik.uni-karlsruhe.de/svn/grid-control/tags/stable/grid-control
    cd ..
   

For general bash usage, the [bashrc](https://github.com/artus-analysis/bashrc) repository provides some useful commands and default settings.

## For event generation / fastNLO table production

### [Blackhat 0.9.9](https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation)
Blackhat libraries can become quite large and are therefore installed on a storage server.
Also, make sure you have sufficient disk space available in your home directory.

    wget http://www.hepforge.org/archive/blackhat/blackhat-0.9.9.tar.gz
    tar -xzf blackhat-0.9.9.tar.gz
    cd blackhat-0.9.9
    . /cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/gcc/4.7.2/etc/profile.d/init.sh # blackhat has to be compiled with older gcc version
    ./configure $STORAGE_PATH/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/$ARCHITECTURE_47/external/$QD_CVMFS  # blackhat libraries can become huge -> install on storage server:
    make -j 12
    make install
    . /cvmfs/cms.cern.ch/$ARCHITECTURE/external/gcc/4.9.1-cms/etc/profile.d/init.sh  # return to default compiler
    cd ..

### [Sherpa 2.2.0](https://sherpa.hepforge.org/trac/wiki/SherpaDownloads/Sherpa-2.2.0) [(Documentation)](https://sherpa.hepforge.org/doc/SHERPA-MC-2.2.0.html)
    wget http://www.hepforge.org/archive/sherpa/SHERPA-MC-2.2.0.tar.gz
    tar -xzf SHERPA-MC-2.2.0.tar.gz
    cd SHERPA-MC-2.2.0
    ./configure --prefix=$COMPILE  --enable-hepmc2=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$HEPMC_CVMFS --enable-rivet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$RIVET_CVMFS --enable-blackhat=$STORAGE_PATH/software/blackhat  --enable-fastjet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$FASTJET_CVMFS 
    make -j 12
    make install
    cd ..

### [fastNLO 2.3.1pre-2212](http://fastnlo.hepforge.org/)
    wget http://fastnlo.hepforge.org/code/v23/fastnlo_toolkit-2.3.1pre-2212.tar.gz
    tar -xzf fastnlo_toolkit-2.3.1pre-2212.tar.gz
    cd fastnlo_toolkit-2.3.1pre-2212
    ./configure --prefix=$COMPILE --enable-pyext  PYTHON_VERSION='2.6'
    make -j 8
    make install
    cd ..

### [MCgrid 2.0](http://mcgrid.hepforge.org/)
    wget https://www.hepforge.org/archive/mcgrid/mcgrid-2.0.tar.gz
    tar -xzf mcgrid-2.0.tar.gz
    cd mcgrid-2.0
    ./configure --prefix=$COMPILE
    make -j 8
    make install
    cd ..
## For Scale uncertainty calculation
## Caution: The calculation of scale uncertainties with this framework is not working as intended
### Workaround: Use HOPPET for this purpose (needs a later fastNLO version):
    svn checkout http://hoppet.hepforge.org/svn/trunk hoppet
    cd hoppet/
    ./configure --prefix=$COMPILE
    make
    make install
    cd ..

    svn checkout https://ekptrac.physik.uni-karlsruhe.de/svn/fastNLO/trunk/v2.0/toolkit@2301 #fastNLO version tested for use with HOPPET
    cd toolkit/
    cp ../fastnlo_toolkit-2.3.1pre-2212/AUTHORS .
    autoreconf -i
    ./configure --prefix=$COMPILE --enable-pyext PYTHON_VERSION=2.6 --with-hoppet
    make -j 12
    make install
    
    

    



## For PDF fits

### [QCDNUM 17-00/07](http://www.nikhef.nl/~h24/qcdnum/)
    wget http://www.nikhef.nl/user/h24/qcdnum-files/download/qcdnum170112.tar.gz
    tar -xzf qcdnum170112.tar.gz
    cd qcdnum-17-01-12
    ./configure --prefix=$COMPILE
    make -j 8
    make install
    cd ..


### [xFitter 1.2.0](https://wiki-zeuthen.desy.de/xFitter/)
    wget -U Mozilla/5.0 --no-check-certificate "https://wiki-zeuthen.desy.de/xFitter/xFitter/DownloadPage?action=AttachFile&do=get&target=xfitter-1.2.0.tgz" -O xfitter-1.2.0.tgz
    tar -xzf xfitter-1.2.0.tgz
    cd xFitter-1.2.0/
    autoreconf
    ./configure --prefix=$COMPILE --enable-lhapdf LDFLAGS="-L/cvmfs/cms.cern.ch/$ARCHITECTURE/external/lapack/3.3.1-cms/lib"
    automake
    make -j 8
    make install
    cd ..
