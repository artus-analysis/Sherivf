#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds
	merlin.py --py unfold --no-mcs
	merlin.py --py zee_divide
	merlin.py --py uncertainties
	merlin.py --py herafile
}

calculate_all_correlations(){
	for i in zpt abszy zmass; do
		calculate_correlation.py -t latest_sherivf_output/${i}.tab -o  correlations/${i}.root &
	done
}


# plotting
alias make_allplots="merlin.py --py allplots"


## Final PDF fitting
fit_nnpdf(){
	PDFSET=NNPDF30_nlo_as_0118
	copy_herafitter_steering.py -m nnpdf
	cd $HERADIR
	rm $HERADIR/output/NNPDF*_HighStat_chi2/* $HERADIR/NNPDF/data/* -rf
	mkdir -p output/${PDFSET}_HighStat_chi2
	FitPDF
	cd output/${PDFSET}_HighStat_chi2
	pdf_2_root.py -p ${PDFSET}_HighStat_chi2_nRep100
	cp ${PDFSET}_HighStat_chi2_nRep100*.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}


fit_hera(){
	_hera_fit hera
}
fit_heraZ(){
	_hera_fit heraZ
}

#base function:
_hera_fit(){
	cd $HERADIR
	copy_herafitter_steering.py -m $1
	rm -rf $HERADIR/$1/*
	FitPDF
	NAME=herapdf
	cd $1/
	for q in 1.4 91.2;
		do pdf_2_root.py -p $NAME -q ${q}
	done
	rename $NAME $1 *.root
	mv ${1}__*.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}



## for switching LHAPDF versions
install_lhapdf(){
	rm /usr/users/dhaitz/local/lib64/python2.6/site-packages/lhapdf.*
	cd $SHERIVFDIR/../$1
	make install
	cd -
}
install_lhapdf6(){
	install_lhapdf LHAPDF-6.1.5
}
install_lhapdf5(){
	install_lhapdf lhapdf-5.9.1
}
