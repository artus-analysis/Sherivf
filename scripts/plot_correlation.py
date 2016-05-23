#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plot pdf """

import ROOT
import numpy as np
import matplotlib.pyplot as plt

import plot_pdf


def plot_pdf(input_filename, output_filename, flavour, y_label=""):
	"""main"""
	
	# get input
	print "Open", input_filename
	rootfile = ROOT.TFile(input_filename, "READ")
	roothisto = rootfile.Get(flavour)
	
	# prepare figure
	plot_pdf.set_matplotlib_params()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xscale('log', nonposx='clip')
	ax.set_xlabel(r'$x$', position=(1., 0.), va='top', ha='right')
	ax.set_ylabel(y_label, position=(0., 1.), va='top', ha='right')
	ax.set_title(flavour, size=16)
	
	# convert from ROOT to numpy
	#x = np.array([roothisto.GetXaxis().GetBinCenter(i) for i in xrange(1, roothisto.GetNbinsX() +1)])
	xl = np.array([roothisto.GetXaxis().GetBinLowEdge(i) for i in xrange(1, roothisto.GetNbinsX() +1)])
	xu = np.array([roothisto.GetXaxis().GetBinUpEdge(i) for i in xrange(1, roothisto.GetNbinsX() +1)])
	#y = np.array([roothisto.GetYaxis().GetBinCenter(i) for i in xrange(1, roothisto.GetNbinsY() +1)])
	yl = np.array([roothisto.GetYaxis().GetBinLowEdge(i) for i in xrange(1, roothisto.GetNbinsY() +1)])
	yu = np.array([roothisto.GetYaxis().GetBinUpEdge(i) for i in xrange(1, roothisto.GetNbinsY() +1)])
	bincontents = np.zeros((roothisto.GetNbinsY(), roothisto.GetNbinsX()))
	for y in xrange(1, roothisto.GetNbinsY() + 1):
		for x in xrange(1, roothisto.GetNbinsX() + 1):
			bincontents[y - 1, x - 1] = roothisto.GetBinContent(x, y)
	
	# draw
	ax.pcolormesh(np.concatenate((xl, xu[-1:])), np.concatenate((yl, yu[-1:])), bincontents, cmap='coolwarm', rasterized=True)
	
	# finish
	print "Writing to", output_filename
	fig.savefig(output_filename, bbox_inches='tight')
	plt.close()


if __name__ == "__main__":
	plot_pdf(
		"/usr/users/dhaitz/home/qcd/sherivf/correlations/zpt_NNPDF23_nlo_as_0118.root",
		"pdf.png",
		"gluon",
		"$\mathit{p}_{T,Z}$ / GeV"
	)

