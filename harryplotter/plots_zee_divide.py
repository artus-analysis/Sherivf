#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools

import common


def divided_ptspectrum(args=None):
	""" pT spectrum in y bins"""
	plots = []

	nbins = len(common.ybin_plotlabels)

	for quantity in common.data_quantities:
		filenames = []
		x_expressions = []
		nicks = []
		for index, ybin in enumerate(common.ybin_labels):
			filenames.append('{}/{}_madgraph_{}_{}.root'.format(common.divided_path, quantity, ybin, common.iterations_to_use))
			x_expressions.append('nick0')
			nicks.append(str(index))
		if quantity == 'zpt':
			for index, ybin in enumerate(common.ybin_labels):
				filenames.append(common.sherivf_output_dir + "/Rivet.root")
				x_expressions.append("y{}_{}".format(index, quantity))
				nicks.append(quantity+str(index))
		ntotal = len(filenames)
		nmc = ntotal - nbins
		colors = ['black', 'red', 'blue', 'green', 'purple', 'orange', 'cyan'][:nbins]*(ntotal/nbins)
		d = {
			'files': filenames,
			'folders': [""],
			'x_expressions': x_expressions,
			'nicks': nicks,
			# formatting
			'x_label': quantity,
			'y_errors': [False],
			'lumis': [common.lumi],
			'colors': colors,
			'y_label': common.xseclabels[quantity],
			'energies': [8],
			'labels': common.ybin_plotlabels+[None]*nmc,
			'markers': ['o', 'D', 'x', '*', 'd', 's'][:nbins]+["."]*nmc,
			'line_styles': [None]*nbins + ['-']*nmc,
			'step': True,
			'filename': quantity,
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['x_log'] = common.zpt_xlog
			d['x_ticks'] = common.zpt_ticks
			d['y_lims'] = [1e-5, 1]
			#ratio
			d.update({
				'analysis_modules': ['Ratio'],
				'ratio_numerator_nicks': [n for n in nicks if quantity not in n],
				'ratio_denominator_nicks': [n for n in nicks if quantity in n],
				'y_subplot_lims': [0.65, 1.35],
				'y_subplot_label': 'Data/Sim. Ratio\n',
			})
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	zee_divide()
