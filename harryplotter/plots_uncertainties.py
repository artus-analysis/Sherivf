# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common
import parsertools
from Excalibur.Plotting.utility.colors import histo_colors


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
				filename = '{}_{}_{}_{}.root'.format(quantity, common.default_mc, ybinsuffix, common.iterations_to_use)
				filename_up =   '{}_{}_{}_{}.root'.format(quantity, common.default_mc, ybinsuffix+variation+"up", common.iterations_to_use)
				filename_down = '{}_{}_{}_{}.root'.format(quantity, common.default_mc, ybinsuffix+variation+"down", common.iterations_to_use)
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

					'x_bins': common.bins[quantity],
					'nicks_whitelist': ['ratio'],
					'plot_modules': ['ExportRoot'],
					'output_dir': common.systematic_path,
					'filename': filename_up.replace('.root', '').replace("up", ''),
					'export_json': False,
				}
				plots.append(d)
			#lumi
			filename = '{}_{}_{}_{}'.format(quantity, common.default_mc, ybinsuffix+'_lumi', common.iterations_to_use)
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

			files = [common.divided_path + "/" + quantity+'_{}_{}_1.root'.format(common.default_mc, ybinsuffix)]
			types = common.uncertainties_with_lumi
			for unc in common.uncertainties_with_lumi:
				files += [common.systematic_path + "/" + quantity+'_{}_{}{}_1.root'.format(common.default_mc, ybinsuffix, unc)]
			n_source = len(common.uncertainties_with_lumi)
			labels = ['Statistical'] + [common.unc_labelsdict[unc] for unc in types] + ['Total']
			d = {
				# input
				'files': files,
				'folders': [""],
				'x_expressions': ['nick0'] + ['ratio']*n_source,
				'filename': '_'.join(['unc', quantity])+ybinsuffix,
				'scale_factors': [100.],
				'nicks': ['nick0'] + types,
				# analysis
				'analysis_modules': ['StatisticalErrors', "AddHistogramsSquared"],
				'stat_error_nicks': ['nick0'],
				'stat_error_relative': True,
				'stat_error_relative_percent': True,
				'square_add_nicks': ['nick0'] + types,
				# formatting
				'title': ybinplotlabel,
				'y_label': 'Relative uncertainty / %',
				'x_label': quantity,
				'labels': labels,
				'markers': ['o', 'd', '*', '.', 'D'],
				'line_styles': ['-'],
				'step': [True],
				'y_errors': [False],
				'legend_order': [4,2,3,5,1,0],
			}
			if quantity == 'zpt':
				d['y_lims'] = [0, 5]
				#d['x_lims'] = common.lims[quantity]
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['legend'] = 'upper left'
			elif quantity == 'abszy':
				d['legend'] = 'upper left'
				d['y_lims'] = [0, 5]
			if ybin != '':
				d['y_lims'] = [0, 15]
			plots.append(d)
	return [PlottingJob(plots, args)]


def scale_pdf_uncertainties(args=None, additional_dictionary=None):
	"""fastNLO prediction with scale uncertainty"""
	plots = []

	pdfset = 'CT14nlo'
	scalestyle = 'kAsymmetricSixPoint'
	pdfstyle = 'kHessianAsymmetric'

	for quantity in common.quantities:
		for ybin, ybinsuffix, ybinplotlabel in zip(
				[""] + ["y{}_".format(i) for i in range(len(common.ybins))],
				["inclusive"] + common.ybin_labels,
				[""] + common.ybin_plotlabels
		):
			if (quantity is not 'zpt') and (ybin is not ""):
				continue
			replaced_quantity = common.qdict.get(quantity, quantity)
			d = {
				# input
				'input_modules': ['InputFastNLO'],
				# input fastNLO
				'pdf_sets': [pdfset],
				'fastnlo_nicks': ['nick0', 'nick1'],
				'members': [0],
				'fastnlo_files': [common.sherivf_output_dir+"/{0}.tab".format(ybin+replaced_quantity)],
				'uncertainty_styles': [scalestyle, pdfstyle],
				'uncertainty_types': ['Scale', 'PDF'],
				# analysis
				'analysis_modules': ['RelUncertainty'],
				'rel_nicks': ['nick0', 'nick1'],
				'subplot_nicks': ['rel'],
				'y_subplot_lims': [-0.5, 0.5],
				# formatting
				'y_label': common.xseclabels[quantity],
				'line_styles': [None, '-', None],
				'markers': ['fill'],
				'energies': [8],
				'colors': [histo_colors['blue'], histo_colors['red']],
				'step': True,
				'alphas': [0.5],
				'zorder': [30, 40],
				'hatches': [None, '//'],
				#'title': '6p Scale Uncertainty',
				'x_lims': common.lims(quantity),
				'y_subplot_label': 'Rel. uncertainty',
				'x_label': quantity,
				'labels': ['Scale uncertainty', 'PDF uncertainty'],
				'texts': ['\n'.join(['6p scale variation', common.pdfsetdict[pdfset], ybinplotlabel])],
				# output
				'filename': 'scale-pdf-unc_'+ybin+quantity,
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 5e1]
			elif quantity == 'abszy':
				d['y_lims'] = [0, 60]
			plots.append(d)

	return [PlottingJob(plots, args)]
