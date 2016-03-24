#!/bin/sh

source $MY_LANDINGZONE/gc-run.lib || exit 101

# set env
WDIR=$PWD
cd /portal/ekpcms6/home/dhaitz/artus/CMSSW
export SCRAM_ARCH=`ls bin`
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scram runtime -sh`
cd /portal/ekpcms6/home/dhaitz/qcd/sherivf
. scripts/ini.sh
cd $WDIR

echo -e "\nFit:"
xfitter

echo -e "\nafter fit: "
ls -lt

xfitter-draw --3panels --ratio-to-theory --bands --relative-errors hera/
mv hera/plots.pdf .

echo -e "\nhera: "
cd hera/
ls -lt


echo -e "\nhf_pdf:"
ls -lt hf_pdf/

echo -e "\n\nErrorType:"
grep ErrorType hf_pdf/hf_pdf.info -n
sed -i 's/replicas/hessian/g' hf_pdf/hf_pdf.info
echo -e "\n\n"

if [ @DOBANDS@ == 'False' ]; then
	echo -e "\n no errors on pdfs \n"
	ERRORS="-m 1"
else
	ERRORS=""
fi

for q in 1.9 10.0 91.2; do
	for squared in "" "--q2"; do
		pdf_2_root.py -p hf_pdf -q ${q} ${squared} $ERRORS
	done
done
mv *.root ..
mv fittedresults.txt Results.txt ..
cd ..




echo -e "\nFiles: "
ls -lt

exit 0
