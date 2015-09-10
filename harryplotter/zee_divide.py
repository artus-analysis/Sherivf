#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools

import common


def zee_divide(args=None):
	"""Divide unfolded Zee data by lumi and bin width"""

	#known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])
	plots = []
	for quantity in common.data_quantities:
		filename = '{}_madgraph_inclusive_{}'.format(quantity, common.iterations_to_use)
		d = {
			'files': ['2_unfolded/' + filename + '.root'],
			'folders': [""],
			'x_expressions': ['data_unfolded'],
			'scale_factors': 1./19712.,

			'analysis_modules': ['NormalizeByBinWidth'],

			'plot_modules': ['ExportRoot'],
			'output_dir': common.divided_path,
			'filename': filename,
			'export_json': False,
			
		}

		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	zee_divide()
