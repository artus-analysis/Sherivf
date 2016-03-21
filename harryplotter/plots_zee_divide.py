#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools

import common


def divided_ptspectrum(args=None):
	""" pT spectrum in y bins"""
	plots = []

	cut_bins = 0  # n outer bins to be cut away
	pdfset = 'CT14nlo'

	nbins = len(common.ybin_plotlabels[:(-cut_bins if cut_bins>0 else 99)])

	for quantity in ['zpt']:#common.data_quantities:
		filenames = []
		x_expressions = []
		nicks = []
		for index, ybin in enumerate(common.ybin_labels[:(-cut_bins if cut_bins>0 else 99)]):
			filenames.append('{}/{}_{}_{}_{}.root'.format(common.divided_path, quantity, common.default_mc, ybin, common.iterations_to_use))
			x_expressions.append('nick0')
			nicks.append(str(index))

		ntotal = 2*len(filenames)
		nmc = ntotal - nbins
		colors = ['black', 'red', 'blue', 'green', 'purple', 'orange', 'cyan'][:nbins]*(ntotal/nbins)
		factors = [10**x for x in range(nbins)][::-1]
		labels = []
		for ybin, factor in zip(common.ybin_plotlabels_space[:(-cut_bins if cut_bins>0 else 99)], factors):
			if factor > 1:
				exp = int(math.log10(factor))
				exp = ("" if exp == 1 else "^{"+str(exp)+"}")
				labels += [r"{0} ($\\times10{1}$)".format(ybin, exp)]
			else:
				labels += [ybin]
		invert_binwidth = 1./0.4
		labels += [None]*nmc
		d = {
			'files': filenames,
			'folders': [""],
			'x_expressions': x_expressions,
			'nicks': nicks,
			# formatting
			'scale_factors': [invert_binwidth * f for f in factors],
			'x_label': quantity,
			'y_errors': [True]*nbins+[False]*nmc,
			'lumis': [common.lumi],
			'colors': colors,
			'y_label': common.xseclabels_bin[quantity],
			'energies': [8],
			'markers': ['o', 'D', 'x', '*', 'd', 's'][:nbins]+["."]*nmc,
			'line_styles': [None]*nbins + ['-']*nmc,
			'step': True,
			'filename': quantity,
			'zorder': [30]*nmc+[20]*nmc,
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['x_log'] = common.zpt_xlog
			d['x_ticks'] = common.zpt_ticks
			d['y_lims'] = [invert_binwidth*1e-5, invert_binwidth*1e5]
			d['legend'] = None
			fastnlo_files = []
			fastnlo_nicks = []
			for index, ybin in enumerate(common.ybin_labels[:(-cut_bins if cut_bins>0 else 99)]):
				fastnlo_files.append(common.sherpa_results+"/y{0}_{1}.tab".format(index, quantity))
				fastnlo_nicks.append('mc'+str(index))
			nicks = nicks + fastnlo_nicks
			d.update({
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				'pdf_sets': [pdfset],
				'members': [0],
				'fastnlo_files': fastnlo_files,
				'fastnlo_nicks': fastnlo_nicks,
				#analysis
				'analysis_modules': ['ScaleErrors', 'ScaleHistograms', 'Ratio'],
				'scale_nicks': fastnlo_nicks,
				'scales': [invert_binwidth * f for f in factors],
				'scale_error_nicks': nicks[nbins:],
				'scale_error_factors': [0],
				'ratio_numerator_nicks': [n for n in nicks if 'mc' not in n],
				'ratio_denominator_nicks': [n for n in nicks if 'mc' in n],
				'y_subplot_lims': [0.5, 1.5],
				'y_subplot_label': 'Data/Sim. Ratio\n',
			})
		if True:
			d['plot_modules'] = ['PlotMplZJet', 'PlotMplLegendTable']
			d["legend_table_column_headers"] = ['Data', 'Sim.']
			d["legend_table_row_headers"] = labels[:nmc]
			d["legend_table_filename"] = quantity + '_legend'
			d['legend_table_phantomtext'] = r"$1^5$"
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	zee_divide()
