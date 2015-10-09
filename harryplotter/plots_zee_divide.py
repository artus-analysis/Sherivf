#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools

import common


def divided_ptspectrum(args=None):
	""" pT spectrum in y bins"""
	plots = []

	#TODO add MC

	for quantity in common.data_quantities:
		filenames = []
		for ybin in common.ybin_labels:
			filenames.append('{}/{}_madgraph_{}_{}.root'.format(common.divided_path, quantity, ybin, common.iterations_to_use))
		d = {
			'files': filenames,
			'folders': [""],
			'x_expressions': ['nick0'],
			
			'x_label': quantity,
			#'line_styles': ['-'],
			#'step': True,
			'lumis': [common.lumi],
			'energies': [8],
			'labels': common.ybin_plotlabels,
			'markers': ['o', 'D', '.', '*', 'd', 's'],
			'filename': quantity,
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['x_log'] = common.zpt_xlog
			d['x_ticks'] = common.zpt_ticks
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	zee_divide()
