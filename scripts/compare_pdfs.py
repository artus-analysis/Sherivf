#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plot pdf """

import argparse
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gErrorIgnoreLevel = ROOT.kError


def plot_pdf(input_filename, output_filename, flavour):
	"""main"""
	
	# add argparse for command line configuration
	parser = argparse.ArgumentParser(description='Plots PDFs')
	parser.add_argument('-i', '--input-filename', help='Input root file. [Default: %(default)s]', default=input_filename)
	parser.add_argument('-c', '--compare-filename', help='Input root file. [Default: %(default)s]', default=input_filename)
	parser.add_argument('-o', '--output-filename', help='Output root file. [Default: %(default)s]', default=output_filename)
	parser.add_argument('-f', '--flavour', help='Parton flavour. [Default: %(default)s]', default=flavour)
	args = parser.parse_args()
	
	# get input
	print "Open", args.input_filename, 'and', args.compare_filename
	rootfile1 = ROOT.TFile(args.input_filename, "READ")
	rootfile2 = ROOT.TFile(args.compare_filename, "READ")
	histo1 = rootfile1.Get("exp_mod_par_"+args.flavour)
	histo2 = rootfile2.Get("exp_mod_par_"+args.flavour)
	colors = ['red', 'blue']  # green, yellow, red
	
	# prepare figure
	set_matplotlib_params()
	fig = plt.figure()
	ax1, ax2 = [plt.subplot2grid((4,1), (0, 0), rowspan=3), plt.subplot2grid((4,1), (3, 0))]
	for ax in [ax1, ax2]:
		ax.set_xlim(1e-4, 1)
		ax.set_xscale('log', nonposx='clip')
	ax2.set_xlabel(r'$x$', position=(1., 0.), va='top', ha='right')
	ax1.set_ylabel('$x$f($x,Q^2$)', position=(0., 1.), va='top', ha='right')
	ax2.set_ylabel('Rel. uncertainty', position=(0., 1.), va='top', ha='right')
	ax1.set_xticklabels([])
	ax2.set_ylim(-0.45, 0.45)
	if (args.flavour == 'd_valence_quark'):
	  ax1.set_ylim(0, 0.6)
	ax1.text(0.05, 0.95, args.flavour.replace('_',' ')+' PDF', size=16, transform=ax1.transAxes, ha="left", va="top")
	ax1.text(0.05, 0.85, r'$Q^2 = 1.9 \ GeV^2$', size=16, transform=ax1.transAxes, ha="left", va="top")
	
	# iterate over ROOT objects
	for color, histo, alpha in zip(colors, [histo1,histo2], [0.7, 0.5]):
		# convert ROOT histo to mpl format
		x, y, yerrlow, yerrhigh = get_values_from_tgraphasymmerrors(histo)

		# draw PDF
		ax1.plot(x, y, color=color)
		ax1.fill_between(x,
					[(y_val-error) for y_val, error in zip(y, yerrlow)],
					[(y_val+error) for y_val, error in zip(y, yerrhigh)],
					color=color,
					alpha=alpha,
				)
		patch1 = mpatches.Patch(color='red')
		patch2 = mpatches.Patch(color='blue')
		if(args.flavour == 'gluon'):
		  location = "lower center"
		elif(args.flavour == 'sea_quarks'):
		  location = "upper right"
		else: 
		  location = "center left"
		ax1.legend((patch1,patch2),(r'$\phi^*_\eta$', r'$\mathit{p}_{T}^{Z}$'),loc=location)
		ax2.fill_between(x,
					[(-error/y_val) for y_val, error in zip(y, yerrlow)],
					[(error/y_val) for y_val, error in zip(y, yerrhigh)],
					color=color,
					alpha=alpha,
				)
		if(args.flavour == 'd_valence_quark'):
		  ax1.set_ylim(0,0.55)
		else:  
		  ax1.set_ylim(0, max(ax.get_xlim()[1], max(y)*1.4))
	
	# finish
	
	print "Writing to", args.output_filename
	fig.savefig(args.output_filename, bbox_inches='tight')
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
		"results/hera2/pdf_1_9_squared.root",
		"pdf.png",
		"gluon"
	)

