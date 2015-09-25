#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""plot a PDF. From http://lhapdf.hepforge.org/codeexamples.html"""

import argparse
import lhapdf
import numpy as np
import os
import ROOT

import tools

partondict = {
	0: 'gluon',
	21: 'gluon',
	-1: 'd antiquark',
	-2: 'u antiquark',
	-3 : 'sbar',
	-4 : 'cbar',
	-5 : 'bbar',
	-6 : 'tbar',
	1: 'd quark',
	2: 'u quark',
	3 : 'strange',
	4 : 'charm',
	5 : 'bottom',
	6 : 'top',
	7: 'd valence quark',
	8: 'u valence quark',
	9: 'sea quarks',
}


def main(
		pdfset,
		flavours,
		output_filename,
		n_points,
		q,
		folder):
	"""evaluate a PDF set and write the resuling TGraph to disk"""

	out = ROOT.TFile((folder+"/" if folder is not None else "") + output_filename, "RECREATE")
	x_values = np.logspace(-4, -0.01, n_points)  # TODO get min, max x from PDF set

	## Version info, search paths, and metadata
	print "LHAPDF version", lhapdf.version()
	lhapdf.pathsPrepend(os.getcwd())
	lhapdf.setVerbosity(0)
	print "LHAPDF paths",lhapdf.paths()
	print "PDFset:", pdfset
	pset = lhapdf.getPDFSet(pdfset)
	n_members = pset.size
	print n_members, "members in PDF set"

	# iterate over flavours, get pdfgraph, write
	for flavour in flavours:
		tgraph = get_pdf_tgraph(pset, flavour, x_values, n_points, n_members, q)
		tgraph.Write(partondict[flavour].replace(' ', '_'))

	print "Written to", output_filename
	out.Close()

def getopt():
	parser = argparse.ArgumentParser(description='evaluate PDF set')
	parser.add_argument('-p', '--pdfset', help='LHAPDF PDF Filename', default='NNPDF30_nlo_as_0118')
	parser.add_argument('-o', '--output-filename', default=None)
	parser.add_argument('-f', '--flavours', type=int, nargs="*", default=[21, 1, 2, 3, 4, -1, -2, 7, 8, 9])
	parser.add_argument('-n', '--n-points', default=100, type=int, help="points in x")
	parser.add_argument('-q', '--q', default=91.2, type=float, help="Q")
	parser.add_argument('--folder', type=str, default=None)

	opt = parser.parse_args()
	if opt.output_filename is None:
		opt.output_filename = "{}__{}.root".format(opt.pdfset, str(opt.q).replace('.', '_'))
	else:
		opt.output_filename += ".root"
	return opt

def get_pdf_tgraph(pset, flavour, x_values, n_points, n_members, Q): 
	all_values = []
	# load each member only once
	for i_member in range(n_members):
		p = pset.mkPDF(i_member)
		pdf_values = []
		for x in x_values:
			if flavour == 7:
				pdf = p.xfxQ(1, x, Q) - p.xfxQ(-1, x, Q)
			elif flavour == 8:
				pdf = p.xfxQ(2, x, Q) - p.xfxQ(-2, x, Q)
			elif flavour == 9:
				pdf = 2*(p.xfxQ(-1, x, Q) + p.xfxQ(-2, x, Q) + p.xfxQ(-3, x, Q))
			else:
				pdf = p.xfxQ(flavour, x, Q)
			pdf_values.append(pdf)
		all_values.append(pdf_values)

	# construct tgraph from central value and uncertainties
	tgraph = ROOT.TGraphAsymmErrors()
	for index, x_value in enumerate(x_values):
		values = [pdf_values[index] for pdf_values in all_values]
		central_value = values[0]
		lower_error, upper_error = tools.get_pdf_uncertainty_for_bin(central_value, values[1:])
		tgraph.SetPoint(index, x_value, central_value)
		tgraph.SetPointEYlow(index, lower_error)
		tgraph.SetPointEYhigh(index, upper_error)

	return tgraph

if __name__ == '__main__':
	opt = getopt()
	main(**vars(opt))
