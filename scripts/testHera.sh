#!/bin/bash

TESTDIR=$SHERIVFDIR/heratest/$(date +"%Y-%m-%d_%H-%M-%S")
echo "Make directory $TESTDIR"
mkdir -p $TESTDIR
cd $TESTDIR

for i in ewparam.txt minuit.in.txt unpolarised.wgt  zmstf.wgt; do
	cp $HERADIR/$i $TESTDIR
done

copy_herafitter_steering.py -m $1 -d $TESTDIR

FitPDF

echo $TESTDIR
