#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from itertools import combinations

import common
import Excalibur.Plotting.harryinterface as harryinterface


qdict = {'pT': 'zpt', 'y': 'abs(zy)', 'm': 'zmass', 'phi': 'zphi'}

def sherpa_fastnlo(args=None):
	"""Compare Sherpa directly with fastNLO"""
	plots = []
	# pT or y:
	for norm in [True, False]:
		for quantity, x in zip(['pT', 'y', 'm'], ["d01-x01-y01", "d02-x01-y01", "d03-x01-y01"]):
			# all combinations of the 
			d = {
				# input
				'input_modules': ['InputRootZJet', 'InputFastNLO'],
				"files": ['latest_sherivf_output/Rivet.root'],
				"folders": [""],
				"x_expressions": x,
				#"scale_factors": 19712.,
				'pdf_sets': ['CT10.LHgrid'],
				'fastnlo_files': ["latest_sherivf_output/output/fnlo_{0}Z_10.tab".format(quantity)],
				'members': [0],
				# analysis
				'analysis_modules': ['ScaleHistograms'] + (['NormalizeToFirstHisto'] if norm else []) + ['Ratio'],
				'scale_nicks': ['latest_sherivf_output/fnlo_{}Z.tab_CT10.LHgrid_0'.format(quantity)],
				'scale': 1./1.,
				# formatting
				'nicks_whitelist': ['fnlo', 'nick', 'ratio'],
				"markers": ["o", "fill","."],
				"x_label": qdict[quantity],
				"y_label": r"$\\mathit{\\sigma}\\ / \\ GeV$",
				"y_subplot_lims": [0, 2],
				"energies": [8],
				"y_errors": [False],
				"labels": ['Sherpa+fastNLO', 'Sherpa', 'ratio'],
				"marker_colors": ['red'],
				"title": ('Shape comparison' if norm else ''),
				# filename
				'filename': quantity.lower() + ('_norm' if norm else '')
			}
			if quantity == 'pT':
				d['y_log'] = True
				d['y_lims'] = [1e-4, 1e2]
			elif quantity == 'y' and norm:
				d['y_lims'] = [0, 100]
			plots.append(d)
	harryinterface.harry_interface(plots, args)


def fastnlo_pdfsets(args=None, additional_dictionary=None):
	""" study fastnlo tables for different PDF sets"""
	plots = []
	bindict = {
			'zmass': ['20,81,101'],
			'abs(zy)': ['25,0,2.5'],
			'zpt': ['38,20,400'],
			'zphi': ['20,-3.14159,3.14159'],
	}

	scale = True

	# configure fastNLO input
	n_members = 1
	pdf_sets = [#'NNPDF30_nlo_as_0118'
		'CT10.LHgrid', 'NNPDF21_100.LHgrid', 'abm11_3n_nlo.LHgrid',
		'cteq65.LHgrid', 'MSTW2008nnlo90cl.LHgrid'
		]
	labels = ['CT10', 'NNPDF21', 'ABM11', 'CTEQ6', 'MSTW2008']
	N = len(pdf_sets)

	for quantity, s in zip(['y', 'm', 'pT'], [2*i for i in [0.1, 1, 10]]):
		d = {
			# input
			'input_modules': ['InputFastNLO'],
			'pdf_sets': pdf_sets,
			'members': len(pdf_sets),
			'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.tab".format(quantity)],
			
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			'files': [common.divided_path + '/' + '_'.join([qdict[quantity].replace("abs(zy)", "zy"), 'madgraph', 'inclusive', '1']) + '.root'],
			'folders': '',
			'x_expressions': 'nick0',

			# analysis
			"analysis_modules": ["ScaleHistograms"],
			'scale': 1.,
			'scale_nicks':["latest_sherivf_output/fnlo_{}Z.tab_{}_{}".format(quantity, i, N) for i in pdf_sets],
			# formatting
			'labels': ['Data'] + labels,
			'legend': 'upper right',
			'markers': ['o'] + ['-',]*N,
			'line_styles': [None] + ['-']*N,
			'energies': [8],
			'y_label': r'$\\sigma \\ / \\ pb$',
			'x_label': qdict[quantity],
			# output
			'filename': ("scale_" if scale else "")+"fastnlo_"+qdict[quantity],
		}
		if quantity == 'pT':
			d['y_log'] = True
			d['y_lims'] = [1e-3, 1e2]
		plots.append(d)

	harryinterface.harry_interface(plots, args)


def fastnlo_pdfmember(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	n_members = 101

	for quantity in ['y', 'm', 'pT']:
		d = {
			# input
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			# input fastNLO
			'pdf_sets': ['NNPDF21_100.LHgrid'],
			'members': range(n_members),
			'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.tab".format(quantity)],
			# input root
			'files': [common.divided_path + '/' + '_'.join([qdict[quantity].replace("abs(zy)", "zy"), 'madgraph', 'inclusive', '1']) + '.root'],
			'folders': '',
			'x_expressions': 'nick0',
			'scale_factors': [(2. if quantity == 'y' else 1.)],
			# formatting
			'labels': ['Data', 'PDF replicas'] + [None]*(n_members-1),
			'y_label': r'$\\sigma \\ / \\ pb$',
			'x_errors': [False],
			'y_errors': [True] + [False]*n_members,
			'markers': ['o'] + ['-']*n_members,
			'line_styles': [None] + ['-']*n_members,
			'line_widths': [0.1],
			'colors': ['black'] + ['blue']*n_members,
			'energies': [8],
			'x_label': qdict[quantity],
			# output
			'filename': qdict[quantity],
		}
		if quantity == 'pT':
			d['y_log'] = True
			d['y_lims'] = [1e-3, 1e2]
		plots.append(d)

	harryinterface.harry_interface(plots, args)
