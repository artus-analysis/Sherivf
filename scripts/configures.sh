#!/bin/bash

#####
# MC production
#####


# BLACKHAT
# blackhat libraries can become quite large -> install in storage space
# https://blackhat.hepforge.org/trac/wiki/BlackHatInstallation
# wget http://www.hepforge.org/archive/blackhat/blackhat-0.9.9.tar.gz && tar -xzf blackhat-0.9.9.tar.gz
alias configure_blackhat="./configure --prefix=/storage/a/${USER}/blackhat"
#./configure --prefix=/storage/a/${USER}/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/qd/2.3.13/
# GCC version 4.7.2
# ./configure --prefix=/storage/a/${USER}/software/blackhat --with-QDpath=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/external/qd/2.3.13/ && make -j 12

# SHERPA 2.2.0
# https://sherpa.hepforge.org/trac/wiki
# wget http://www.hepforge.org/archive/sherpa/SHERPA-MC-2.2.0.tar.gz  && tar -xvf SHERPA-MC-2.2.0.tar.gz
alias configure_sherpa="./configure --prefix=$HOME/local --with-sqlite3=install --enable-hepmc2=$HOME/local/ --enable-rivet=$HOME/local/ --enable-blackhat=/storage/a/${USER}/blackhat   --enable-fastjet=$HOME/local/"
#./configure --prefix=$HOME/local  --enable-hepmc2=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/hepmc/2.06.07-cms/ --enable-rivet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/rivet/2.2.1 --enable-blackhat=/storage/a/dhaitz/software/blackhat  --enable-fastjet=/cvmfs/cms.cern.ch/$ARCHITECTURE/external/fastjet/3.1.0 


# RIVET



#fastnlo
# wget http://fastnlo.hepforge.org/code/v23/fastnlo_toolkit-2.3.1pre-2212.tar.gz
alias configure_fastnlo="./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION='2.6'"




#MCgrid
alias configure_mcgrid="./configure --prefix=$HOME/local CXXFLAGS='-DFASTNLO_ENABLED=1'"
#./configure --prefix=/storage/a/${USER}/software/mcgrid

# wget https://www.hepforge.org/archive/mcgrid/mcgrid-2.0.tar.gz
# tar -xvf mcgrid-2.0.tar.gz



#####
# fastNLO and fitting stuff
#####
#YAML
#TODO

# xFitter
alias configure_xfitter="./configure --prefix=$HOME/local CFLAGS=\"-I/usr/users/${USER}/local/include\" LDFLAGS=\"-L/usr/users/${USER}/local/lib/ -I/usr/users/${USER}/local/include -lblas -lyaml\" --enable-process --enable-lhapdf"
