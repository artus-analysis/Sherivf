#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds
	merlin.py --py unfold --no-mcs
	merlin.py --py zee_divide
	merlin.py --py uncertainties
	merlin.py --py herafile
}

clear_analysis(){
for i in 1_background-subtracted 2_unfolded 3_divided 4_systematic; do
	rm -f $SHERIVFDIR/${i}/*.root
done
rm -f $SHERIVFDIR/herafitter/CMS_Zee_HFinput_*.txt
}

calculate_all_correlations(){
	for set in NNPDF30_nlo_as_0118 NNPDF23_nlo_as_0118; do
		for i in zpt abszy zmass; do
			calculate_correlation.py -t output_for_correlation_plots/${i}.tab -o  correlations/${i}_${set}.root -p ${set} & 
		done
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



## PDF uncertainties
make_pdfuncs()
{
	for i in hera heraZ heraZ_pt heraZ_bins; do
		merlin.py --py pdf_unc_${i}
	done
}
clear_pdfuncs()
{
	rm $SHERIVFDIR/5_pdfunc/*.root
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
