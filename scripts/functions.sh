#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds
	merlin.py --py unfold --no-mcs
	merlin.py --py zee_divide
	merlin.py --py herafile
}

calculate_all_correlations(){
	for i in pT m y; do
		calculate_correlation.py -t latest_sherivf_output/fnlo_${i}Z.tab -o  correlations/fnlo_${i}Z.root
	done
}


# plotting
alias make_allplots="merlin.py --py allplots"

## Final PDF fitting

hera_fit(){
	PDFSET=NNPDF30_nlo_as_0118
	cd $SHERIVFDIR/../herafitter-1.1.1
	rm $SHERIVFDIR/../herafitter-1.1.1/output/NNPDF*_HighStat_chi2/* $SHERIVFDIR/../herafitter-1.1.1/NNPDF/data/* -rf
	mkdir -p output/${PDFSET}_HighStat_chi2
	FitPDF
	cd output/${PDFSET}_HighStat_chi2
	pdf_2_root.py -p ${PDFSET}_HighStat_chi2_nRep100 -f 0 1 2 3 4 -1 -2
	cp ${PDFSET}_HighStat_chi2_nRep100.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}
