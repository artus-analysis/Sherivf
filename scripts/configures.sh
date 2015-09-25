#!/bin/bash

# fastjet plugins
#-L$HOME/local/include/fastjet/.libs
alias configure_fastjet="./configure --prefix=$HOME/local  --enable-allcxxplugins --enable-shared"

#MCgrid
alias configure_mcgrid="./configure --prefix=$HOME/local CXXFLAGS='-DFASTNLO_ENABLED=1'"

#SHERPA
alias configure_sherpa="./configure --prefix=$HOME/local --with-sqlite3=install --enable-hepmc2=$HOME/local/ --enable-rivet=$HOME/local/ --enable-blackhat=/storage/a/dhaitz/blackhat   --enable-fastjet=$HOME/local/"

#fastnlo
alias configure_fastnlo="./configure --prefix=$HOME/local --enable-pyext  PYTHON_VERSION='2.6'"

#blackhat
alias configure_blackhat="./configure --prefix=/storage/a/dhaitz/blackhat --with-QDpath=$HOME/local"

# HERAfitter
alias configure_herafitter="./configure --enable-lhapdf  LDFLAGS=\"-L/usr/users/dhaitz/local/lib/ -lblas -llapack -ltmglib\"  --enable-nnpdfWeight"

#yoda
alias configure_yoda=" ./configure --prefix=$HOME/local --with-boost=$BOOSTPATH --enable-root"
