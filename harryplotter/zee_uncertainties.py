# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common
import parsertools


def uncertainties(args=None):
	""" Calculate systematic uncertainties of the Z->ee measurement."""
	# get (up) values and calculate relative difference to mean, bin y bin

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'quantities'])

	plots = []
	for quantity in common.data_quantities:
		for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
			for variation in ['_eup', '_bkgrup', '_unfup']:
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
					'filename': filename2.replace('.root', ''),
					'export_json': False,
				}
				plots.append(d)
			#lumi
			filename = '{}_madgraph_{}_{}'.format(quantity, ybinsuffix+'_lumi', common.iterations_to_use)
			d = {
				'files': [common.divided_path + "/" + filename1]*2,
				'folders': [""],
				'x_expressions': ['nick0'],
				'scale_factors': [common.lumi_uncertainty, 1],

				'analysis_modules': ['Ratio'],

				'nicks_whitelist': ['ratio'],
				'plot_modules': ['ExportRoot'],
				'output_dir': common.systematic_path,
				'filename': filename,
				'export_json': False,
			}
			plots.append(d)
	return [PlottingJob(plots, args)]


def plot_uncertainties(args=None):
	""" Plot all systematic uncertainties."""
	plots = []
	for quantity in common.data_quantities:
		files = [common.divided_path + "/" + quantity+'_madgraph_inclusive_1.root']
		types = ['_eup', '_bkgrup', '_unfup', '_lumi']
		for unc in ['_eup', '_bkgrup', '_unfup', '_lumi']:
			files += [common.systematic_path + "/" + quantity+'_madgraph_inclusive{}_1.root'.format(unc)]
		n_source = 4
		labels = ['Statistical', 'Electron ID/Trigger Efficiency', 'Background', 'Unfolding', 'Luminosity']
		d = {
			'files': files,
			'folders': [""],
			'x_expressions': ['nick0'] + ['ratio']*n_source,
			'filename': '_'.join(['unc', quantity]),
			'scale_factors': [100.],
			'nicks': ['nick0'] + types,
			
			'analysis_modules': ['StatisticalErrors'],
			'stat_error_nicks': ['nick0'],
			'stat_error_relative': True,
			'stat_error_relative_percent': True,
			
			'y_label': 'Uncertainty / %',
			'x_label': quantity,
			'labels': labels,
			'markers': ['o', 'd', '*', '.', 'D'],
			'line_styles': ['-'],
			'step': [True],
			'y_errors': [False],
		}
		if quantity == 'zpt':
			d['y_lims'] = [0, 10]
		plots.append(d)
	return [PlottingJob(plots, args)]
