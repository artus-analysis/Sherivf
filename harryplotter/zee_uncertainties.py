# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common
import parsertools


def uncertainties(args=None):
	""" Calculate systematic uncertainties of the Z->ee measurement."""
	# get (up) values and calculate relative difference to mean, bin y bin

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'quantities'])

	plots = []
	for quantity in common.quantities:
		for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
			for variation in common.uncertainties:
				filename = '{}_madgraph_{}_{}.root'.format(quantity, ybinsuffix, common.iterations_to_use)
				filename_up = '{}_madgraph_{}_{}.root'.format(quantity, ybinsuffix+variation+"up", common.iterations_to_use)
				filename_down = '{}_madgraph_{}_{}.root'.format(quantity, ybinsuffix+variation+"down", common.iterations_to_use)
				d = {
					#input
					'files': [common.divided_path + "/" + f for f in [filename, filename_up, filename_down]],
					'folders': [""],
					'x_expressions': ['nick0'],
					'nicks': ['central', 'up', 'down'],
					#analysis
					'analysis_modules': [
						'Ratio',
						'ShiftBinContents',
						'AbsoluteBinContents',
						'MaxHistogram'
					],
					'ratio_numerator_nicks': ['central'],
					'ratio_denominator_nicks': ['up', 'down'],
					'ratio_result_nicks': ['ratio_up', 'ratio_down'],
					"shift": -1,
					"shift_bin_contents": ['ratio_up', 'ratio_down'],
					"absolute_bin_contents": ['ratio_up', 'ratio_down'],
					'max_nick1': 'ratio_up',
					'max_nick2': 'ratio_down',
					'max_result_nick': 'ratio',

					'nicks_whitelist': ['ratio'],
					'plot_modules': ['ExportRoot'],
					'output_dir': common.systematic_path,
					'filename': filename_up.replace('.root', '').replace("up", ''),
					'export_json': False,
				}
				plots.append(d)
			#lumi
			filename = '{}_madgraph_{}_{}'.format(quantity, ybinsuffix+'_lumi', common.iterations_to_use)
			d = {
				'files': [common.divided_path + "/" + filename_up]*2,
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
	for quantity in common.quantities:
		for ybin, ybinsuffix, ybinplotlabel in zip(
				[""] + ["y{}_".format(i) for i in range(len(common.ybins))],
				["inclusive"] + common.ybin_labels,
				[""] + common.ybin_plotlabels
		):
			if (quantity is not 'zpt') and (ybin is not ""):
				continue

			files = [common.divided_path + "/" + quantity+'_madgraph_{}_1.root'.format(ybinsuffix)]
			types = common.uncertainties_with_lumi
			for unc in common.uncertainties_with_lumi:
				files += [common.systematic_path + "/" + quantity+'_madgraph_{}{}_1.root'.format(ybinsuffix, unc)]
			n_source = 4
			labels = ['Statistical'] + [common.unc_labelsdict[unc] for unc in types]
			d = {
				'files': files,
				'folders': [""],
				'x_expressions': ['nick0'] + ['ratio']*n_source,
				'filename': '_'.join(['unc', quantity])+ybinsuffix,
				'scale_factors': [100.],
				'nicks': ['nick0'] + types,
			
				'analysis_modules': ['StatisticalErrors'],
				'stat_error_nicks': ['nick0'],
				'stat_error_relative': True,
				'stat_error_relative_percent': True,
			
				'texts': [ybinplotlabel],
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
				d['x_log'] = common.zpt_xlog
				d['x_ticks'] = common.zpt_ticks
			plots.append(d)
	return [PlottingJob(plots, args)]
