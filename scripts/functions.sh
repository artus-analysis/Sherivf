#!/bin/bash

# CMS data analysis steps
make_analysis(){
	merlin.py --py subtract_backgrounds --no-ybins
	merlin.py --py unfold --no-ybins --no-mcs
	merlin.py --py zee_divide
	make_herafile
}

make_herafile(){
	merlin.py -i 3_divided/zpt_madgraph_inclusive_1.root -f "''" -x nick0  --plot-m ExportHerafitter --x-bins '38,20,400' --header-file ../../qcd/sherivf/herafitter/herafitter_header.txt --filename CMS_Zee_HFinput -o ~/home/qcd/sherivf/herafitter/
}


# plotting
export WWWSUBDIR="zee/"
make_allplots(){
	merlin.py --py pdfs_thesis --www ${WWWSUBDIR}pdfs
	merlin.py --py pdf_correlations --www ${WWWSUBDIR}correlations

	merlin.py --py z_hlt --www ${WWWSUBDIR}z_trigger
	merlin.py --py electron_id --www ${WWWSUBDIR}electron_id
	merlin.py --py electron_corr --www ${WWWSUBDIR}momentum_corrections
	merlin.py --py z_corr --www ${WWWSUBDIR}momentum_corrections
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





calculate_all_correlations(){
	for i in pT m y; do
		calculate_correlation.py -t latest_sherivf_output/fnlo_${i}Z.tab -o  correlations/fnlo_${i}Z.root
	done
}



## Final PDF fitting

nnpdf_analysis(){
	hera_fit
}
hera_fit(){
	export LHAPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/share/LHAPDF/
	cd $SHERIVFDIR/../herafitter-1.1.1
	rm $SHERIVFDIR/../herafitter-1.1.1/output/NNPDF23_nlo_as_0118_HighStat_chi2/* $SHERIVFDIR/../herafitter-1.1.1/NNPDF/data/* -rf
	FitPDF
	cd output/NNPDF23_nlo_as_0118_HighStat_chi2
	pdf_2_root.py -p NNPDF23_nlo_as_0118_HighStat_chi2_nRep100
	cp NNPDF23_nlo_as_0118_HighStat_chi2_nRep100.root $SHERIVFDIR/pdf_sets
	cd $SHERIVFDIR
}

