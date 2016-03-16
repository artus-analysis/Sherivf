#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import common
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors

def sherpa_fastnlo(args=None):
	"""Compare Sherpa directly with fastNLO"""
	plots = []
	pdfset = 'CT10'
	member = 0
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
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				"files": [common.sherpa_results + '/Rivet.root'],
				"folders": [""],
				"x_expressions": ybin+replaced_quantity,
				'pdf_sets': [pdfset],
				'fastnlo_files': [common.sherpa_results+"/{}.tab".format(ybin+replaced_quantity)],
				'members': [0],
				# analysis
				'analysis_modules': ['Ratio'],
				# formatting
				"markers": ["fill", "o", "o"],
				"x_label": quantity,
				"y_label": common.xseclabels[quantity],
				"y_subplot_lims": [0.99, 1.01],
				"energies": [8],
				"y_errors": [False],
				"labels": ['Sherpa', 'Sherpa+fastNLO', 'ratio'],
				"marker_colors": ['red'],
				"y_subplot_label": "Sherpa/fastNLO",
				"texts": [ybinplotlabel],
				# filename
				'filename': ybin+quantity.lower(),
				'www_title': 'Sherpa vs fastNLO',
				'www_text': 'fastNLO ({} used) compared to Sherpa for Z y,mass,pT'.format(pdfset),
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e2]
			elif quantity == 'abszy':
				d['y_lims'] = [0, 50]
			elif quantity == 'zmass':
				d['y_lims'] = [0, 40]
			plots.append(d)
	return [PlottingJob(plots, args)]


def fastnlo_pdfsets(args=None, additional_dictionary=None):
	""" study fastnlo tables for different PDF sets"""
	plots = []
	# configure fastNLO input
	n_members = 1
	pdf_sets = [
		'CT14nlo', 'NNPDF30_nlo_as_0118', 'abm11_3n_nlo',
		#'cteq66', 'MSTW2008nlo68cl',
		'HERAPDF20_NLO_EIG',
		'MMHT2014nlo68clas118',
		#'PDF4LHC15_nlo_100'
		]
	labels = [common.pdfsetdict.get(i, i) for i in pdf_sets]
	N = len(pdf_sets)
	member = 0
	colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan'][:N]

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
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
					#fnlo
				'pdf_sets': pdf_sets,
				'members': [member],
				'fastnlo_files': [common.sherpa_results+"/{0}.tab".format(ybin+replaced_quantity)],
					#root
				'files': [common.divided_path + '/' + '_'.join([quantity, common.default_mc, ybinsuffix, '1']) + '.root'],
				'folders': '',
				'x_expressions': 'nick0',
				# analysis
				"analysis_modules": ["Ratio"],
				'ratio_denominator_nicks': ['nick0'],
				'ratio_numerator_nicks':[common.sherpa_results+"/{}.tab_{}_{}".format(ybin+replaced_quantity, i, member) for i in pdf_sets],
				# formatting
				'legend_order': [0, 3, 4, 5, 1, 2],
				'labels': ['Data'] + labels,
				'legend': 'upper right',
				'markers': ['o'] + ['-',]*N*2,
				'colors': ['black'] + colors*2,
				'line_styles': [None] + ['-']*N*2,
				'energies': [8],
				'y_label': common.xseclabels[quantity],
				'step': [True],
				'lumis': [common.lumi],
				'x_label': quantity,
				'y_subplot_label': 'Sim./Data',
				'y_subplot_lims': [0.75, 1.25],
				'texts': [ybinplotlabel],
				# output
				'filename': ybin + "fastnlo_"+quantity,
				'www_title': 'Data and fastNLO for different PDF sets',
				'www_text': 'Unfolded data compared to fastNLO table evaluated with different PDF sets for Z y,mass,pT.',
			}
			if quantity == 'zpt':
				d.update({
				'x_bins': common.bins[quantity],
				'x_lims': common.lims(quantity),
				})
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)

	return [PlottingJob(plots, args)]


def fastnlo_tables(args=None, additional_dictionary=None):
	"""Compare fastnlo tables with data and central prediction."""
	plots = []
	member = 0
	pdf_set = 'HERAPDF15NLO_EIG'
	basedir = '/storage/ekpcloud_local/dhaitz/sherivf/ekpcloud_2015-12-01_14-51/'
	#basedir = print os.readlink(os.environ['SHERIVFDIR'] + '/results/MCgrid_CMS_2015_Zee_zjet')
	N = 40
	for subplot in [True, False]:
		for quantity in ['abszy', 'zpt']:  # common.quantities:
			replaced_quantity = common.qdict.get(quantity, quantity)
			tables = [
				basedir+'{}.tab'.format(quantity), # central
			] + [basedir+'output/{}_{}.tab'.format(quantity, i) for i in range(N)]
			nicks = ['central'] + map(str, range(N))
			d = {
				# input
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				'nicks': ['data'],
				'files': [common.divided_path + '/' + '_'.join([quantity, common.default_mc, 'inclusive', '1']) + '.root'],
				'folders': '',
				'x_expressions': 'nick0',
				#fnlo
				'pdf_sets': [pdf_set],
				'members': [member],
				'fastnlo_files': tables,
				'fastnlo_nicks': nicks,
				# analysis
				"analysis_modules": ["Ratio"],
				'ratio_numerator_nicks': nicks,
				'ratio_denominator_nicks': ['data'],
				# formatting
				'labels': ['data', 'merged', 'individual tables']+[None]*2*(N-1),
				'zorder': [40] + ([30] + [20]*N)*2,
				'markers': ['o'] + ['-']*(N+1)*2,
				'y_errors': [True] + [False]*2*(N+1),
				'colors': ['black'] + (['red'] + ['blue']*N)*2,
				'line_styles': [None] + ['-']*(N+1)*2,
				'line_widths': [1] + ([2] + [0.7]*N)*2,
				'energies': [8],
				'y_label': common.xseclabels[quantity],
				'step': [True],
				'subplot_fraction': (90 if subplot else 10),
				'x_label': quantity,
				'y_subplot_label': 'Ratio sim./data',
				'y_subplot_lims': [0.4, 1.5],
				# output
				'filename': "fastnlo_tables_"+('subplot_' if subplot else '')+quantity,
			}
			if quantity == 'zpt':
		
				d['y_subplot_lims'] =  [0.65, 1.2]
				d.update({
				'x_bins': common.bins[quantity],
				'x_lims': common.lims(quantity),
				})
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)
	return [PlottingJob(plots, args)]


def fastnlo_pdfunc(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	pdfset = 'NNPDF30_nlo_as_0118_nolhc'
	style = 'kMCSampling'

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
				'input_modules': [ 'InputFastNLO'],
				# input fastNLO
				'pdf_sets': [pdfset],
				'members': [0],
				'fastnlo_files': [common.sherpa_results+"/{0}.tab".format(ybin+replaced_quantity)],
				'uncertainty_style': style,
				'uncertainty_type': 'PDF',
				# analysis
				'analysis_modules': ['RelUncertainty'],
				# formatting
				'subplot_nicks': ['rel'],
				'y_label': common.xseclabels[quantity],
				'line_styles': [None, '-', None],
				'markers': ['fill'],
				'energies': [8],
				'step': True,
				'alphas': [0.8],
				'colors': histo_colors['blue'],
				'x_label': quantity,
				'y_subplot_lims': [-0.05, 0.05],
				'y_subplot_label': 'PDF Uncertainty',
				'texts': [ybinplotlabel],
				# output
				'filename': 'pdfunc_' + ybin + quantity,
				#'www_title': 'Data and fastNLO with PDFUncertainties',
				#'www_text': ('Unfolded data compared to fastNLO table evaluated with {}.'.format(common.pdfsetdict.get(pdfset))
				#	+ r" \'{}\' uncertainty style is used.".format(style)),
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)

	return [PlottingJob(plots, args)]


def fastnlo_pdfmembers(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	pdfset = 'NNPDF30_nlo_as_0118_nolhc'
	n_members = common.nmembersdict[pdfset]

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
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				# input fastNLO
				'pdf_sets': [pdfset],
				'members': range(n_members),
				'fastnlo_files': [common.sherpa_results+"/{0}.tab".format(ybin+replaced_quantity)],
				'fastnlo_nicks': map(str, range(n_members)),
				# input root
				'files': [common.divided_path + '/' + '_'.join([quantity, common.default_mc, ybinsuffix, '1']) + '.root'],
				'folders': '',
				'x_expressions': 'nick0',
				# analysis
				'analysis_modules': ['Ratio'],
				'ratio_numerator_nicks': ['nick0'],
				'ratio_denominator_nicks': map(str, range(n_members)),
				# formatting
				'labels': ['Data', 'PDF set members'] + [None]*(2*n_members-1),
				'markers': ['o'] +[' ']*n_members*2,
				'line_styles': [None] + ['-']*n_members*2,
				'line_widths': [0.5],
				'y_errors': [True]+ [False]*n_members*2,
				#'x_errors': [False]+ [True]*n_members*2,
				'colors': ['black'] + ['blue']*n_members*2,
				'step': True,
				'energies': [8],
				'texts': [ybinplotlabel],
				'lumis': [common.lumi],
				'x_label': quantity,
				'y_label': common.xseclabels[quantity],
				'title': common.pdfsetdict[pdfset],
				
				'y_subplot_lims': [0.75, 1.25],
				'y_subplot_label': 'Data/Sim.',

				# output
				'filename': ybin+quantity,
				'www_title': 'Data and fastNLO with PDF set members',
				#'www_text': ('Unfolded data compared to fastNLO table evaluated with {}.'.format(common.pdfsetdict.get(pdfset))
				#	+ r" \'{}\' uncertainty style is used.".format(style)),
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)

	return [PlottingJob(plots, args)]


def k_factors(args=None, additional_dictionary=None):
	"""fastNLO LO and NLO cross section"""
	plots = []

	pdfset = 'CT10nlo'

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
				'k_factors': [False, True],
				'fastnlo_nicks': ['nlo', 'ratio'],
				'fastnlo_files': [common.sherivf_output_dir+"/{0}.tab".format(ybin+replaced_quantity)],
				# analysis
				'analysis_modules': ['Ratio'],
				'ratio_result_nicks': ['lo'],
				# formatting
				'y_label': common.xseclabels[quantity],
				'markers': ['fill', '.', '.'],
				'line_styles': [None, None, '-'],
				'energies': [8],
				'step': True,
				'labels': ['NLO', 'ratio', 'LO'],
				'y_subplot_label': 'k Factor',
				'y_subplot_lims': [0, 2],
				'x_label': quantity,
				'texts': [ybinplotlabel],
				'x_errors': [True],
				# output
				'filename': 'kfactor_'+ybin+quantity,
				'www_title': 'NLO-LO comparison',
				'www_text': ' ',
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)

	return [PlottingJob(plots, args)]
