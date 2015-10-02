#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools

import common


def zee_divide(args=None):
	"""Divide unfolded Zee data by lumi and bin width"""

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'quantities'])

	plots = []
	for quantity in common.data_quantities:
		for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
			for variation in common.variations+common.unfolding_variations:
				filename = '{}_madgraph_{}_{}'.format(quantity, ybinsuffix+variation, common.iterations_to_use)
				d = {
					'files': [common.unfold_path + '/' + filename + '.root'],
					'folders': [""],
					'x_expressions': ['data_unfolded'],
					'scale_factors': 1./(1e3*common.lumi),

					'analysis_modules': ['NormalizeByBinWidth'],

					'plot_modules': ['ExportRoot'],
					'output_dir': common.divided_path,
					'filename': filename,
					'export_json': False,
				}
				plots.append(d)
	return [PlottingJob(plots, args)]


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
