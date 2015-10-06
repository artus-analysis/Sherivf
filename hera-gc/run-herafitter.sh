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

echo -e "\nParameter values:"
#echo $MEMBER $DATASET $ORDER $HF_SCHEME $MCHARM $Q02 $Q2MIN $FS $FC $DG_S $EG_S $DUV_S $DDV_S $EDV_S $DUBAR_S $EUBAR_S $DDBAR_S $EDBAR_S $ALPHAS $ALPHAS_S $BANDS $CHI2EXTRAPARAM[$DATASET] $BPRIG_S $PDFStyle
echo @MCHARM@ @MBOTTOM@

echo -e "\nFit:"
FitPDF

echo -e "\nafter fit: "
ls -lt

echo -e "\nhera: "
cd hera/
ls -lt


echo -e "\nherapdf:"
ls -lt herapdf/

if [ @DOBANDS@ == 'False' ]; then
	echo -e "\n no errors on pdfs \n"
	ERRORS="-m 1"
else
	ERRORS=""
fi

for q in 1.4 1.9 91.2; do
	for squared in "" "--q2"; do
		pdf_2_root.py -p herapdf -q ${q} ${squared} $ERRORS
	done
done
mv *.root ..
mv fittedresults.txt ..
cd ..




echo -e "\nFiles: "
ls -lt

exit 0
