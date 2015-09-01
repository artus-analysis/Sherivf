#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
import parsertools

import common


def zee_divide(args=None):
	"""Divide unfolded Zee data by lumi and bin width"""

	#known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])
	plots = []
	for quantity, name in zip(['pT', 'y', 'm'], ['pt', 'y', 'mass']):
		filename = 'z{}_madgraph_inclusive_1'.format(name)
		d = {
			'files': ['2_unfolded/' + filename + '.root'],
			'folders': [""],
			'x_expressions': ['data_unfolded'],
			'scale_factors': 1./19712.,

			'analysis_modules': ['NormalizeByBinWidth'],

			'plot_modules': ['ExportRoot'],
			'output_dir': common.divided_path,
			'filename': filename,
			
		}

		plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	zee_divide()
