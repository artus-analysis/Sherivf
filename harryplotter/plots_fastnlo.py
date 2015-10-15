#!/usr/bin/env python
# -*- coding: utf-8 -*-

import common
from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def sherpa_fastnlo(args=None):
	"""Compare Sherpa directly with fastNLO"""
	plots = []
	pdfset = 'CT10'
	member = 0
	for quantity in common.quantities:
		for ybin, ybinsuffix in zip(
				[""] + ["y{}_".format(i) for i in range(len(common.ybins))],
				["inclusive"] + common.ybin_labels
		):
			if (quantity is not 'zpt') and (ybin is not ""):
				continue
			replaced_quantity = common.qdict.get(quantity, quantity)
			d = {
				# input
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				"files": ['latest_sherivf_output/Rivet.root'],
				"folders": [""],
				"x_expressions": ybin+replaced_quantity,
				'pdf_sets': [pdfset],
				'fastnlo_files': ["latest_sherivf_output/{}.tab".format(ybin+replaced_quantity)],
				'members': [0],
				# analysis
				'analysis_modules': ['Ratio'],
				# formatting
				"markers": ["o", "fill","."],
				"x_label": quantity,
				"y_label": common.xseclabels[quantity],
				"y_subplot_lims": [0.999, 1.001],
				"energies": [8],
				"y_errors": [False],
				"labels": ['Sherpa+fastNLO', 'Sherpa', 'ratio'],
				"marker_colors": ['red'],
				"y_subplot_label": "Sherpa/fastNLO",
				"texts": [pdfset],
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
		'CT10nlo', 'NNPDF30_nlo_as_0118', 'abm11_3n_nlo',
		#'cteq66', 'MSTW2008nlo68cl',
		'HERAPDF15NLO_EIG',
		'MMHT2014nlo68clas118'
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
				'fastnlo_files': ["latest_sherivf_output/{0}.tab".format(ybin+replaced_quantity)],
					#root
				'files': [common.divided_path + '/' + '_'.join([quantity, 'madgraph', ybinsuffix, '1']) + '.root'],
				'folders': '',
				'x_expressions': 'nick0',
				# analysis
				"analysis_modules": ["Ratio"],
				'ratio_denominator_nicks': ['nick0'],
				'ratio_numerator_nicks':["latest_sherivf_output/{}.tab_{}_{}".format(ybin+replaced_quantity, i, member) for i in pdf_sets],
				# formatting
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
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				if common.zpt_xlog:
					d['x_ticks'] = common.zpt_ticks
				d['y_lims'] = [common.zpt_miny, 1e1]
			plots.append(d)

	return [PlottingJob(plots, args)]


def fastnlo_pdfmember(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	pdfset = 'NNPDF30_nlo_as_0118'
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
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				# input fastNLO
				'pdf_sets': [pdfset],
				'members': [0],
				'fastnlo_files': ["latest_sherivf_output/{0}.tab".format(ybin+replaced_quantity)],
				'uncertainty_style': style,
				'uncertainty_type': 'PDF',
				# input root
				'files': [common.divided_path + '/' + '_'.join([quantity, 'madgraph', ybinsuffix, '1']) + '.root'],
				'folders': '',
				'x_expressions': 'nick0',
				# analysis
				'analysis_modules': ['Ratio'],
				# formatting
				'labels': ['Data', common.pdfsetdict.get(pdfset, pdfset), 'ratio'],
				'y_label': common.xseclabels[quantity],
				'line_styles': [None, '-', None],
				'markers': ['.', 'fill', '.'],
				'energies': [8],
				'step': True,
				'alphas': [0.5],
				'lumis': [common.lumi],
				'x_label': quantity,
				'y_subplot_lims': [0.75, 1.25],
				'y_subplot_label': 'Data/Sim.',
				'texts': [ybinplotlabel],
				# output
				'filename': ybin+quantity,
				'www_title': 'Data and fastNLO with PDFUncertainties',
				'www_text': ('Unfolded data compared to fastNLO table evaluated with {}.'.format(common.pdfsetdict.get(pdfset))
					+ r" \'{}\' uncertainty style is used.".format(style)),
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
