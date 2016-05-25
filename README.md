# SheRivF
Sherpa,Rivet &amp; FastNLO configs


## Needed:
* Sherpa 2.2.0
* Rivet 2.3
* MCgrid 2.0
* fastNLO 2.3.1pre-2125

## Installation
Wiki page?
many needed
smaller tools (without special configuration) can be directly taken from CVMFS:
QD, fastjet, LHAPDF, HepMC, YODA
source ini to get these and uptodate gcc/g++ compiler
4.7? needed for blackhat
sherpa, blackhat

bild mit software and howto

#### BLACKHAT 0.9.9
https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation
GCC version 4.7.2
Install in storage
    wget http://www.hepforge.org/archive/blackhat/blackhat-0.9.9.tar.gz && tar -xzf
    ./configure --prefix=/storage/a/${USER}/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/external/$QD_CVMFS

#### SHERPA 2.2.0
https://sherpa.hepforge.org/trac/wiki
    wget http://www.hepforge.org/archive/sherpa/SHERPA-MC-2.2.0.tar.gz  && tar -xvf 
    ./configure --prefix=$HOME/local  --enable-hepmc2=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$HEPMC_CVMFS --enable-rivet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$RIVET_CVMFS --enable-blackhat=/storage/a/dhaitz/software/blackhat  --enable-fastjet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/$FASTJET_CVMFS 

#### fastNLO 2.3.1pre-2212
    wget http://fastnlo.hepforge.org/code/v23/fastnlo_toolkit-2.3.1pre-2212.tar.gz
    ./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION='2.6'

#### MCgrid 2.0
    wget https://www.hepforge.org/archive/mcgrid/mcgrid-2.0.tar.gz
    tar -xvf mcgrid-2.0.tar.gz
    ./configure --prefix=$HOME/local



#### xFitter
    ./configure --prefix=$HOME/local CFLAGS=\"-I/usr/users/${USER}/local/include\" LDFLAGS=\"-L/usr/users/${USER}/local/lib/ -I/usr/users/${USER}/local/include -lblas -lyaml\" --enable-process --enable-lhapdf

## Usage
 bild mit komplettem workflow


### Monte Carlo simulation and fastNLO table production
fastNLO tables allow
they are necessary for 
needed for PDF fits

are created from Monte Carlo events
Rivet, which implements phase space cuts and e.g. Z boson reconstruction 
MCgrid, rivet plugin, generates fastNLO tables


 
 

sherivf
Different modes:
Rivet analysis compilation
Integration run of sherpa
warmup
local for testing  
* sherivf.py -s zjet --rivet MCgrid_CMS_2015_Zee -n 1000
batch mode for large-scale production for enough events in distant phase space


* convert fastNLO table to root: `evaluate_fnlotable.py -i fnlo.tab`

* correlation plots


`sherivf.py`
3000000 events correspond to 1h runtime


other scripts
* fnlostatana
* pdf to root
	`pdf_2_root.py --folder pdf_sets -p NNPDF23_nlo_as_0118`
* yoda2root

Build Rivet plugin:
* `rivet-buildplugin RivetMyAnalyses.so MCgrid_CMS_2015_Zee.cc -Wl,--export-dynamic,-z,defs  $(pkg-config mcgrid --cflags) $(pkg-config mcgrid --libs)  -lHepMC -lYODA  -DUSE_FNLO=1`




### PDF fits
* send to batch with `hera.py`
 


![My image](docs/test.png?raw=true)
