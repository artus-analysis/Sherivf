#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""plot a PDF. From http://lhapdf.hepforge.org/codeexamples.html"""

import argparse
import lhapdf
import numpy as np
import os
import ROOT

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
default_flavours = [21, 1, 2, 3, -1, -2, 7, 8, 9]

def main(
		pdfset,
		flavours,
		output_filename,
		n_points,
		q,
		q2,  # q2 instead of q
		members,
		folder):
	"""evaluate a PDF set and write the resuling TGraph to disk"""

	if folder is not None and not os.path.exists(folder):
		os.makedirs(folder)
	out = ROOT.TFile((folder+"/" if folder is not None else "") + output_filename, "RECREATE")
	x_values = np.logspace(-4, -0.01, n_points)  # TODO get min, max x from PDF set

	## Version info, search paths, and metadata
	print "LHAPDF version", lhapdf.version()
	lhapdf.pathsPrepend(os.getcwd())
	lhapdf.setVerbosity(0)
	print "LHAPDF paths",lhapdf.paths()
	pset = lhapdf.getPDFSet(pdfset)
	print pset.description
	n_members = pset.size
	if members is not None:
		n_members=members

	# iterate over flavours, get pdfgraph, write
	for flavour in flavours:
		tgraph = get_pdf_tgraph(pset, flavour, x_values, n_points, n_members, q, q2)
		tgraph.Write(partondict[flavour].replace(' ', '_'))

	print "Written to", output_filename
	out.Close()

def getopt():
	parser = argparse.ArgumentParser(description='evaluate PDF set')
	parser.add_argument('-p', '--pdfset', help='LHAPDF PDF Filename. [Default: %(default)s]', default='NNPDF30_nlo_as_0118')
	parser.add_argument('-o', '--output-filename', default=None)
	parser.add_argument('-f', '--flavours', type=int, nargs="*", default=default_flavours)
	parser.add_argument('-n', '--n-points', default=100, type=int, help="points in x. [Default: %(default)s]")
	parser.add_argument('-m', '--members', default=None, type=int, help="n members. [Default: %(default)s]")
	parser.add_argument('-q', '--q', default=91.2, type=float, help="Q value. [Default: %(default)s]")
	parser.add_argument('--q2', action='store_true', help="Q2 instead of Q")
	parser.add_argument('--folder', type=str, default=None)

	opt = parser.parse_args()
	if opt.output_filename is None:
		opt.output_filename = get_default_filename(opt.pdfset, opt.q, opt.q2)
	opt.output_filename += ".root"
	return opt


def get_default_filename(pdfset, q, q2):
	output_filename = "{}__{}".format(pdfset, str(q).replace('.', '_'))
	if q2:
		output_filename += "_squared"
	return output_filename


def get_pdf_tgraph(pset, flavour, x_values, n_points, n_members, Q, Q2):
	all_values = []
	# load each member only once
	for i_member in range(n_members):
		p = pset.mkPDF(i_member)
		method = p.xfxQ2 if Q2 else p.xfxQ
		pdf_values = []
		for x in x_values:
			if flavour == 7:
				pdf = method(1, x, Q) - method(-1, x, Q)
			elif flavour == 8:
				pdf = method(2, x, Q) - method(-2, x, Q)
			elif flavour == 9:
				pdf = 2*(method(-1, x, Q) + method(-2, x, Q) + method(-3, x, Q))
			else:
				pdf = method(flavour, x, Q)
			pdf_values.append(pdf)
		all_values.append(pdf_values)

	# construct tgraph from central value and uncertainties
	tgraph = ROOT.TGraphAsymmErrors()
	do_uncertainty = True
	for index, x_value in enumerate(x_values):
		values = [pdf_values[index] for pdf_values in all_values]
		central_value = values[0]
		tgraph.SetPoint(index, x_value, central_value)
		if do_uncertainty:
			try:
				unc = pset.uncertainty(values)
				#unc.errminus = 0
				tgraph.SetPointEYlow(index, unc.errminus)
				tgraph.SetPointEYhigh(index, unc.errplus)
			except RuntimeError:
				print "Could not compute uncertainties!"
				do_uncertainty = False

	return tgraph

if __name__ == '__main__':
	opt = getopt()
	main(**vars(opt))
