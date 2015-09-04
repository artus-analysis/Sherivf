#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds --no-ybins
	merlin.py --py unfold --no-ybins --no-mcs
	merlin.py --py zee_divide
	make_herafile
}

make_herafile(){
	merlin.py --hera-sys 3 --hera-stat 1 -i 3_divided/zpt_madgraph_inclusive_1.root -f "''" -x nick0  --plot-m ExportHerafitter --x-bins '38,20,400' --header-file ../../qcd/sherivf/herafitter/herafitter_header.txt --filename CMS_Zee_HFinput -o ~/home/qcd/sherivf/herafitter/
}

calculate_all_correlations(){
	for i in pT m y; do
		calculate_correlation.py -t latest_sherivf_output/fnlo_${i}Z.tab -o  correlations/fnlo_${i}Z.root
	done
}



# plotting
export WWWSUBDIR="zee/"
make_allplots(){
	merlin.py --py pdfs_thesis --www ${WWWSUBDIR}pdfs
	merlin.py --py pdf_correlations --www ${WWWSUBDIR}correlations

	#merlin.py --py z_hlt --www ${WWWSUBDIR}z_trigger
	merlin.py --py electron_id --www ${WWWSUBDIR}electron_id
	merlin.py --py electron_corr --www ${WWWSUBDIR}momentum_corrections
	merlin.py --py electron_trigger_sf --www ${WWWSUBDIR}electron_sf

	merlin.py --py zee_bkgrs --no-njets --no-ybins --no-mcs --www ${WWWSUBDIR}backgrounds
	merlin.py --py emu --www ${WWWSUBDIR}emu

	merlin.py --py different_iterations --www ${WWWSUBDIR}unfolding_iteration
	merlin.py --py response_matrix --www ${WWWSUBDIR}unfolding_reponsematrices
	merlin.py --py unfolding_comparison --www ${WWWSUBDIR}unfolding_comparisons

	merlin.py --py sherpa --www ${WWWSUBDIR}sherpa
	merlin.py --py sherpa_mc --www ${WWWSUBDIR}sherpa_mc

	merlin.py --py fastnlo_pdfsets --www ${WWWSUBDIR}fastnlo_pdfsets
	merlin.py --py fastnlo_pdfmember --www ${WWWSUBDIR}fastnlo_pdfmember
	merlin.py --py sherpa_fastnlo --www ${WWWSUBDIR}fastnlo_sherpa

	merlin.py --py nnpdf --www ${WWWSUBDIR}nnpdf
}



## Final PDF fitting

hera_fit(){
	PDFSET=NNPDF30_nlo_as_0118
	export LHAPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/share/LHAPDF/
	cd $SHERIVFDIR/../herafitter-1.1.1
	rm $SHERIVFDIR/../herafitter-1.1.1/output/NNPDF*_HighStat_chi2/* $SHERIVFDIR/../herafitter-1.1.1/NNPDF/data/* -rf
	mkdir -p output/${PDFSET}_HighStat_chi2
	FitPDF
	cd output/${PDFSET}_HighStat_chi2
	pdf_2_root.py -p ${PDFSET}_HighStat_chi2_nRep100 -f 0 1 2 3 4 -1 -2
	cp ${PDFSET}_HighStat_chi2_nRep100.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}


switch_lhapdf5(){
	switch_lhapdf lhapdf-5.9.1
}

switch_lhapdf6(){
	switch_lhapdf LHAPDF-6.1.5
}

switch_lhapdf(){
	cd /usr/users/dhaitz/home/qcd/$1
	make install -j 10
}
