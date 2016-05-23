#!/bin/sh

source $MY_LANDINGZONE/gc-run.lib || exit 101

# set environment
WDIR=$PWD
cd /portal/ekpcms6/home/dhaitz/artus/CMSSW
export SCRAM_ARCH=`ls bin`
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scram runtime -sh`
cd /portal/ekpcms6/home/dhaitz/qcd/sherivf
. scripts/ini.sh
cd $WDIR

# run xfitter
echo -e "\nFit:"
xfitter
xfitter-draw --3panels --ratio-to-theory --bands --relative-errors hera/
mv hera/plots.pdf .

cd hera/
echo -e "\n\nErrorType:"
grep ErrorType hf_pdf/hf_pdf.info -n
sed -i 's/replicas/hessian/g' hf_pdf/hf_pdf.info

# evaluate PDFs
for q in 1.9 10.0 91.2; do
	for squared in "" "--q2"; do
		pdf_2_root.py -p hf_pdf -q ${q} ${squared}
	done
done
mv *.root fittedresults.txt Results.txt minuit.out.txt ..
cd ..

exit 0
