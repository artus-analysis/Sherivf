#!/bin/bash

make_analysis(){
	merlin.py --py subtract_backgrounds --no-ybins
	merlin.py --py unfold --no-ybins --no-mcs
	merlin.py --py zee_divide
	make_herafile
}

make_herafile(){
	merlin.py -i 3_divided/zpt_madgraph_inclusive_1.root -f "''" -x nick0  --plot-m ExportHerafitter --x-bins '38,20,400' --header-file ../../qcd/sherivf/herafitter/herafitter_header.txt --filename CMS_Zee_HFinput -o ~/home/qcd/sherivf/herafitter/
}

make_allplots(){
	merlin.py --py 
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

nnpdf_analysis(){
	qcd
	make_herafile
	hera_fit
	merlin.py --py nnpdf --www nnpdf
}


calculate_all_correlations(){
	for i in pT m y; do
		calculate_correlation.py -t latest_sherivf_output/fnlo_${i}Z.tab -o  correlations/fnlo_${i}Z.root
	done
}
