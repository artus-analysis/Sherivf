# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common
import parsertools


def uncertainties(args=None):
	""" Calculate systematic uncertainties of the Z->ee measurement."""
	# get (up) values and calculate relative difference to mean, bin y bin

	#for quantities
	#for ybins
	#for unc sources
	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'quantities'])

	plots = []
	for quantity in common.data_quantities:
		for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
			for variation in ['_eup', '_bkgrup']:
				filename1 = '{}_madgraph_{}_{}.root'.format(quantity, ybinsuffix, common.iterations_to_use)
				filename2 = '{}_madgraph_{}_{}.root'.format(quantity, ybinsuffix+variation, common.iterations_to_use)
				d = {
					#input
					'files': [common.divided_path + "/" + f for f in [filename1, filename2]],
					'folders': [""],
					'x_expressions': ['nick0'],
					#analysis
					'analysis_modules': [
						'Ratio',
						'ShiftBinContents',
						'AbsoluteBinContents',
					],
					"shift": -1,
					"shift_bin_contents": ["ratio"],
					"absolute_bin_contents": ["ratio"],

					'nicks_whitelist': ['ratio'],
					'plot_modules': ['ExportRoot'],
					'output_dir': common.systematic_path,
					'filename': filename2,
					'export_json': False,
				}
				plots.append(d)
	return [PlottingJob(plots, args)]


def plot_uncertainties(args=None):
	""" Plot all systematic uncertainties."""
	plots = []
	for quantity in common.data_quantities:
		pass  # TODO
	return [PlottingJob(plots, args)]
