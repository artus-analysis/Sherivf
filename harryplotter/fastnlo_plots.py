#!/usr/bin/env python
# -*- coding: utf-8 -*-

import common
from Excalibur.Plotting.utility.toolsZJet import PlottingJob


xseclabels = {'zpt': 'xsecpt', 'abs(zy)': 'xsecabsy', 'zmass': 'xsecm', 'zphi': 'xsecphi'}

def sherpa_fastnlo(args=None):
	"""Compare Sherpa directly with fastNLO"""
	plots = []
	pdfset = 'CT10'
	member = 0
	# pT or y:
	for quantity in ['zpt', 'abs(zy)', 'zmass']:
		replaced_quantity = common.qdict.get(quantity, quantity)
		d = {
			# input
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			"files": ['latest_sherivf_output/Rivet.root'],
			"folders": [""],
			"x_expressions": replaced_quantity,
			#"scale_factors": 19712.,
			'pdf_sets': [pdfset],
			'fastnlo_files': ["latest_sherivf_output/{}.tab".format(replaced_quantity)],
			'members': [0],
			# analysis
			'analysis_modules': ['Ratio'],
			# formatting
			"markers": ["o", "fill","."],
			"x_label": quantity,
			"y_label": xseclabels[quantity],
			"y_subplot_lims": [0.999, 1.001],
			"energies": [8],
			"y_errors": [False],
			"labels": ['Sherpa+fastNLO', 'Sherpa', 'ratio'],
			"marker_colors": ['red'],
			"y_subplot_label": "Sherpa/fastNLO",
			"texts": [pdfset],
			# filename
			'filename': quantity.lower(),
			'www_title': 'Sherpa vs fastNLO',
			'www_text': 'fastNLO ({} used) compared to Sherpa for Z y,mass,pT'.format(pdfset),
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['y_lims'] = [1e-4, 1e2]
		elif quantity == 'abs(zy)':
			d['y_lims'] = [0, 80]
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
		'cteq66', 'MSTW2008nlo68cl'
		]
	labels = [common.pdfsetdict.get(i, i) for i in pdf_sets]
	N = len(pdf_sets)
	member = 0
	colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan'][:N]

	for quantity in ['abs(zy)', 'zmass', 'zpt']:
		replaced_quantity = common.qdict.get(quantity, quantity)
		d = {
			# input
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
				#fnlo
			'pdf_sets': pdf_sets,
			'members': [member],#len(pdf_sets),
			'fastnlo_files': ["latest_sherivf_output/{0}.tab".format(replaced_quantity)],
				#root
			'files': [common.divided_path + '/' + '_'.join([quantity, 'madgraph', 'inclusive', '1']) + '.root'],
			'folders': '',
			'x_expressions': 'nick0',
			# analysis
			"analysis_modules": ["Ratio"],
			'ratio_denominator_nicks': ['nick0'],
			'ratio_numerator_nicks':["latest_sherivf_output/{}.tab_{}_{}".format(replaced_quantity, i, member) for i in pdf_sets],
			# formatting
			'labels': ['Data'] + labels,
			'legend': 'upper right',
			'markers': ['o'] + ['-',]*N*2,
			'colors': ['black'] + colors*2,
			'line_styles': [None] + ['-']*N*2,
			'energies': [8],
			'y_label': xseclabels[quantity],
			'step': [True],
			'x_label': quantity,
			'y_subplot_label': 'MC/Data',
			'y_subplot_lims': [0.75, 1.25],
			# output
			'filename': "fastnlo_"+quantity,
			'www_title': 'Data and fastNLO for different PDF sets',
			'www_text': 'Unfolded data compared to fastNLO table evaluated with different PDF sets for Z y,mass,pT.',
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['y_lims'] = [1e-4, 1e1]
		plots.append(d)

	return [PlottingJob(plots, args)]


def fastnlo_pdfmember(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	pdfset = 'NNPDF30_nlo_as_0118'
	style = 'kMCSampling'

	for quantity in ['abs(zy)', 'zmass', 'zpt']:
		replaced_quantity = common.qdict.get(quantity, quantity)
		d = {
			# input
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			# input fastNLO
			'pdf_sets': [pdfset],
			'members': [0],
			'fastnlo_files': ["latest_sherivf_output/{0}.tab".format(replaced_quantity)],
			'pdf_uncertainty_style': style,
			# input root
			'files': [common.divided_path + '/' + '_'.join([quantity, 'madgraph', 'inclusive', '1']) + '.root'],
			'folders': '',
			'x_expressions': 'nick0',
			# analysis
			'analysis_modules': ['Ratio'],
			# formatting
			'labels': ['Data', common.pdfsetdict.get(pdfset, pdfset), 'ratio'],
			'y_label': xseclabels[quantity],
			'line_styles': [None, '-', None],
			'markers': ['.', 'fill', '.'],
			'energies': [8],
			'step': True,
			'x_label': quantity,
			'y_subplot_lims': [0.75, 1.25],
			# output
			'filename': quantity,
			'www_title': 'Data and fastNLO with PDFUncertainties',
			'www_text': ('Unfolded data compared to fastNLO table evaluated with {}.'.format(common.pdfsetdict.get(pdfset))
				+ r" \'{}\' uncertainty style is used.".format(style)),
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['y_lims'] = [1e-4, 1e1]
		plots.append(d)

	return [PlottingJob(plots, args)]
