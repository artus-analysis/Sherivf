#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plot pdf """

import argparse
import matplotlib.pyplot as plt
import numpy as np

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gErrorIgnoreLevel = ROOT.kError

import plot_pdf


def plot_correlation(input_filename, output_filename, flavour, y_label=""):
	"""Script to make PDF correlation plots"""
	
	# get command line arguments
	parser = argparse.ArgumentParser(description='Plots the correlation coefficient between PDFs and xs')
	parser.add_argument('-i', '--input-filename', help='Input root file. [Default: %(default)s]', default=input_filename)
	parser.add_argument('-o', '--output-filename', help='Output root file. [Default: %(default)s]', default=output_filename)
	parser.add_argument('-f', '--flavour', help='Parton flavour. [Default: %(default)s]', default=flavour)
	parser.add_argument('-y', '--y-label', help='y-axis label. [Default: %(default)s]', default=y_label)
	args = parser.parse_args()
	
	# get input
	print "Open", args.input_filename
	rootfile = ROOT.TFile(args.input_filename, "READ")
	roothisto = rootfile.Get(args.flavour)
	
	# prepare figure
	plot_pdf.set_matplotlib_params()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xscale('log', nonposx='clip')
	ax.set_xlabel(r'$x$', position=(1., 0.), va='top', ha='right')
	ax.set_ylabel(r'$|y^Z|$', position=(0., 1.), va='top', ha='right')
	ax.set_title(args.flavour+' 13 TeV NNPDF30', size=16)
	
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
	cax = ax.pcolormesh(np.concatenate((xl, xu[-1:])), np.concatenate((yl, yu[-1:])), bincontents, cmap='coolwarm', rasterized=True)
	cbar = fig.colorbar(cax, ticks=[-1,-0.5,0,0.5,1])
	plt.ylim(ymax = 2.3, ymin = 0)
	#plt.zlim(zmax = 1, zmin = -1)
	cbar.set_label('Correlation Coefficient')
	#cbar.ax.set_yticklabels(['-1','-0.5','0','0.5','1'])
	cax.set_clim(-1,1)
	# finish
	print "Writing to", args.output_filename
	fig.savefig(args.output_filename, bbox_inches='tight')
	plt.close()


if __name__ == "__main__":
	plot_correlation(
		"/usr/users/dhaitz/home/qcd/sherivf/correlations/zpt_NNPDF23_nlo_as_0118.root",
		"pdf.png",
		"gluon",
		"$\mathit{\phi}_{\eta}^{*}$"
	)
