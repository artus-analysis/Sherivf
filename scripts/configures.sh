#!/bin/bash

#####
# Rivet stuff
#####

# YODA
# dont install with CMSSW sourced - the BOOST version there is too old
alias configure_yoda=" ./configure --prefix=$HOME/local"  # --enable-root"

# LHAPDF
# dont install with CMSSW sourced - the BOOST version there is too old

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

# QDNUM

# BLACKHAT
# blackhat libraries can become quite large - install in storage space
alias configure_blackhat="./configure --prefix=/storage/a/${USER}/blackhat --with-QDpath=$HOME/local"

# SHERPA
alias configure_sherpa="./configure --prefix=$HOME/local --with-sqlite3=install --enable-hepmc2=$HOME/local/ --enable-rivet=$HOME/local/ --enable-blackhat=/storage/a/${USER}/blackhat   --enable-fastjet=$HOME/local/"


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
