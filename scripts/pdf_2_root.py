#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""plot a PDF. From http://lhapdf.hepforge.org/codeexamples.html"""

import argparse
import lhapdf
import numpy as np
import ROOT


partondict = {
	0: 'gluon',
	21: 'gluon',
	-1: 'd antiquark',
	-2: 'u antiquark',
	#            -3 : 'sbar',
	#            -4 : 'cbar',
	#            -5 : 'bbar',
	#            -6 : 'tbar',
	1: 'd quark',
	2: 'u quark',
	#            3 : 'strange',
	#            4 : 'charm',
	#            5 : 'bottom',
	#            6 : 'top',
	7: 'd valence quark',
	8: 'u valence quark',
	9: 'sea quarks',
}


def main():
	"""evaluate a PDF set and write the resuling TGraph to disk"""

	opt = getopt()
	opt.output_filename = opt.output_filename + ".root"
	out = ROOT.TFile(opt.output_filename, "RECREATE")
	n_members = 101
	x_values = np.logspace(-4, -0.0001, opt.n_points)

	## Version info, search paths, and metadata
	print "LHAPDF version", lhapdf.version()
	lhapdf.pathsPrepend("/storage/a/dhaitz/PDFsets")
	lhapdf.pathsPrepend("/usr/users/dhaitz/home/qcd/herafitter-1.1.1/output/NNPDF23_nlo_as_0118_HighStat_chi2")
	lhapdf.setVerbosity(0)
	print "LHAPDF paths",lhapdf.paths()
	print "PDFset:", opt.pdfset
	pset = lhapdf.getPDFSet(opt.pdfset)

	# iterate over flavours, get pdfgraph, write
	for flavour in opt.flavours:
		tgraph = get_pdf_tgraph(pset, flavour, x_values, opt.n_points, n_members, opt.q)
		tgraph.Write(partondict[flavour].replace(' ', '_'))

	print "Written to", opt.output_filename
	out.Close()

def getopt():
	parser = argparse.ArgumentParser(description='evaluate PDF set')
	parser.add_argument('-p', '--pdfset', help='LHAPDF PDF Filename', 
		default='NNPDF23_nlo_as_0118_HighStat_chi2_nRep100')
	#	default='NNPDF23_nlo_as_0118')
	parser.add_argument('-o', '--output-filename', default='out')
	parser.add_argument('-f', '--flavours', nargs="*", default=[0, 1, 2])#, 7, 8, 9])
	parser.add_argument('-n', '--n-points', default=100, type=int, help="points in x")
	parser.add_argument('-q', '--q', default=91.2, type=float, help="Q")
	opt = parser.parse_args()
	return opt

def get_pdf_tgraph(pset, flavour, x_values, n_points, n_members, Q): 
	all_values = []
	for i_member in range(n_members):
		p = pset.mkPDF(i_member)
		pdf_values = []
		for x in x_values:
			pdf_values.append(p.xfxQ(flavour, x, Q))
		all_values.append(pdf_values)

	# get min, max and mean for each point in x from all members
	max_values, mean_values, min_values = [], [], []
	for i in range(n_points):
		max_values.append(max([pdf_values[i] for pdf_values in all_values]))
		min_values.append(min([pdf_values[i] for pdf_values in all_values]))
		mean_values.append(0.5*(max_values[-1] + min_values[-1]))

	# put the python lists into a TGraph
	tgraph = ROOT.TGraphErrors()
	for i, (x, mean_value, min_value) in enumerate(zip(x_values, mean_values, min_values)):
		tgraph.SetPoint(i, x, mean_value)
		tgraph.SetPointError(i,0, mean_value-min_value)
	return tgraph

if __name__ == '__main__':
	main()
