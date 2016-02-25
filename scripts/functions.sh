#!/bin/bash

####### CMS data analysis steps

# execute the different steps for data analysis
make_analysis(){
	merlin.py --py subtract_backgrounds $@
	merlin.py --py unfold $@
	merlin.py --py zee_divide $@
	merlin.py --py uncertainties $@
	merlin.py --py herafile $@
}

clear_analysis(){
for i in 1_background-subtracted 2_unfolded 3_divided 4_systematic; do
	rm -f $SHERIVFDIR/${i}/*.root
done
rm -f $SHERIVFDIR/herafitter/CMS_Zee_HFinput_*.txt
}

# calculate the root files for the correlation plots
calculate_all_correlations(){
	SETS=${1:-/storage/a/dhaitz/sherivf/ekpcloud_2015-09-26_09-57/}
	for set in NNPDF30_nlo_as_0118 NNPDF23_nlo_as_0118 NNPDF30_nlo_as_0118_nolhc; do
		for i in zpt abszy zmass; do
			calculate_correlation.py -t $SETS/${i}.tab -o  correlations/${i}_${set}.root -p ${set} & 
		done
	done
}


# plotting
alias make_allplots="merlin.py --py allplots"


## PDF uncertainties
make_pdfuncs()
{
	for i in hera2 hera2_abszy hera2_zpt hera2_zpt_bins; do
		merlin.py --py make_pdf_unc --scenario ${i}
	done
}
clear_pdfuncs()
{
	rm -f $SHERIVFDIR/5_pdfunc/*.root
}

# SHERPA
sherpa_integrate()
{
	cd $SHERIVFDIR/sherpa/$1
	Sherpa EVENTS=1000
}

