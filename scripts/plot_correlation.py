#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plot pdf """

import ROOT
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot_pdf(input_filename, output_filename, flavour, y_label=""):
	"""main"""
	
	# get input
	print "Open", input_filename
	rootfile = ROOT.TFile(input_filename, "READ")
	roothisto = rootfile.Get(flavour)
	
	# prepare figure
	set_matplotlib_params()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xscale('log', nonposx='clip')
	ax.set_xlabel(r'$x$', position=(1., 0.), va='top', ha='right')
	ax.set_ylabel(y_label, position=(0., 1.), va='top', ha='right')
	ax.set_title(flavour, size=16)
	
	# converto from ROOT to numpy
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


def set_matplotlib_params():
	# Matplotlib settings
	matplotlib.rcParams['mathtext.fontset'] = 'stixsans'
	matplotlib.rcParams['mathtext.default'] = 'rm'
	# figure
	matplotlib.rcParams['figure.figsize'] = 7., 7.
	# axes
	matplotlib.rcParams['axes.linewidth'] = 1
	matplotlib.rcParams['axes.labelsize'] = 20
	matplotlib.rcParams['xtick.major.pad'] = 7
	matplotlib.rcParams['ytick.major.pad'] = 7
	matplotlib.rcParams['xtick.labelsize'] = 16
	matplotlib.rcParams['xtick.major.size'] = 6
	matplotlib.rcParams['xtick.major.width'] = 0.8
	matplotlib.rcParams['xtick.minor.size'] = 4
	matplotlib.rcParams['xtick.minor.width'] = 0.5
	matplotlib.rcParams['ytick.labelsize'] = 16
	matplotlib.rcParams['ytick.major.width'] = 0.8
	matplotlib.rcParams['ytick.major.size'] = 6
	matplotlib.rcParams['ytick.minor.size'] = 3.5
	matplotlib.rcParams['ytick.minor.width'] = 0.5
	matplotlib.rcParams['lines.markersize'] = 8
	# default color cycleexp
	matplotlib.rcParams["axes.formatter.limits"] = [-5, 5]
	# legend
	matplotlib.rcParams['legend.numpoints'] = 1
	matplotlib.rcParams['legend.fontsize'] = 16
	matplotlib.rcParams['legend.labelspacing'] = 0.3
	# Saving
	matplotlib.rcParams['savefig.dpi'] = 150


def get_values_from_tgraphasymmerrors(rootgraph):
	x, y, yerrlow, yerrhigh = [], [], [], []
	for i in range(rootgraph.GetN()):
			tmpX, tmpY = ROOT.Double(0), ROOT.Double(0)
			rootgraph.GetPoint(i, tmpX, tmpY)
			x += [tmpX]
			y += [tmpY]
			yerrhigh += [rootgraph.GetErrorYhigh(i)]
			yerrlow += [rootgraph.GetErrorYlow(i)]
	return x, y, yerrlow, yerrhigh


if __name__ == "__main__":
	plot_pdf(
		"/usr/users/dhaitz/home/qcd/sherivf/correlations/zpt_NNPDF23_nlo_as_0118.root",
		"pdf.png",
		"gluon",
		"$\mathit{p}_{T,Z}$ / GeV"
	)

