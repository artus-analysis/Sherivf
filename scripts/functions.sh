#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds
	merlin.py --py unfold --no-mcs
	merlin.py --py zee_divide
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
nnpdf_fit(){
	PDFSET=NNPDF30_nlo_as_0118
	copy_herafitter_steering.py -m nnpdf
	cd $HERADIR
	rm $HERADIR/output/NNPDF*_HighStat_chi2/* $HERADIR/NNPDF/data/* -rf
	mkdir -p output/${PDFSET}_HighStat_chi2
	FitPDF
	cd output/${PDFSET}_HighStat_chi2
	pdf_2_root.py -p ${PDFSET}_HighStat_chi2_nRep100 -f 0 1 2 3 4 -1 -2
	cp ${PDFSET}_HighStat_chi2_nRep100*.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}

hera_fit(){
	cd $HERADIR
	FitPDF
	NAME=herapdf
	OUTPUTNAME=hera
	cd output/
	for q in 1.3 91.2;
		do pdf_2_root.py -p $NAME -f 0 1 2 3 4 -1 -2 -q ${q}
	done
	rename $NAME $OUTPUTNAME *.root
	mv ${OUTPUTNAME}__*.root $SHERIVFDIR/pdf_sets
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
