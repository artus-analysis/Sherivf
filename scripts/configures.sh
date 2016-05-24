#!/bin/bash

#####
# Rivet stuff
#####

# YODA 1.6.1
# dont install with CMSSW sourced - the BOOST version there is too old
# https://yoda.hepforge.org/
# wget http://www.hepforge.org/archive/yoda/YODA-1.6.1.tar.gz && tar -xvf YODA-1.6.1.tar.gz
alias configure_yoda="./configure --prefix=$HOME/local"

# LHAPDF
# wget http://www.hepforge.org/archive/lhapdf/LHAPDF-6.1.6.tar.gz && tar -xvf LHAPDF-6.1.6.tar.gz
# dont install with CMSSW sourced - the BOOST version there is too old
alias configure_lhapdf="./configure --prefix=$HOME/local"

# HEPMC
alias configure_hepmc="./configure --prefix=$HOME/local --with-momentum=GEV --with-length=MM"

# FASTJET
#-L$HOME/local/include/fastjet/.libs
# also make plugins in fastjet subfolders? esp SIScone?
alias configure_fastjet="./configure --prefix=$HOME/local  --enable-allcxxplugins --enable-shared"

# RIVET




#####
# Sherpa stuff
#####


# BLACKHAT
# blackhat libraries can become quite large -> install in storage space
# https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation
# wget http://www.hepforge.org/archive/blackhat/blackhat-0.9.9.tar.gz && tar -xzf blackhat-0.9.9.tar.gz
alias configure_blackhat="./configure --prefix=/storage/a/${USER}/blackhat"
#./configure --prefix=/storage/a/${USER}/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/qd/2.3.13/


# SHERPA 2.2.0
# https://sherpa.hepforge.org/trac/wiki
# wget http://www.hepforge.org/archive/sherpa/SHERPA-MC-2.2.0.tar.gz  && tar -xvf SHERPA-MC-2.2.0.tar.gz
alias configure_sherpa="./configure --prefix=$HOME/local --with-sqlite3=install --enable-hepmc2=$HOME/local/ --enable-rivet=$HOME/local/ --enable-blackhat=/storage/a/${USER}/blackhat   --enable-fastjet=$HOME/local/"
#./configure --prefix=$HOME/local  --enable-hepmc2=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/hepmc/2.06.07/ --enable-rivet=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/rivet/2.4.0-giojec --enable-blackhat=/storage/a/dhaitz/software/blackhat  --enable-fastjet=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/fastjet/3.1.0 





#####
# fastNLO and fitting stuff
#####

#fastnlo
alias configure_fastnlo="./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION='2.6'"

#MCgrid
alias configure_mcgrid="./configure --prefix=$HOME/local CXXFLAGS='-DFASTNLO_ENABLED=1'"

#YAML
#TODO

# xFitter
alias configure_xfitter="./configure --prefix=$HOME/local CFLAGS=\"-I/usr/users/${USER}/local/include\" LDFLAGS=\"-L/usr/users/${USER}/local/lib/ -I/usr/users/${USER}/local/include -lblas -lyaml\" --enable-process --enable-lhapdf"
