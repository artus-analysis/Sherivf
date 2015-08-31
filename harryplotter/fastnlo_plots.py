#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from itertools import combinations

import common
import Excalibur.Plotting.harryinterface as harryinterface


qdict = {'pT': 'zpt', 'y': 'abs(zy)', 'm': 'zmass', 'phi': 'zphi'}

def rivet_fastnlo(args=None):
	""" compare rivet with fastnlo and MC-gen"""
	plots = []
	# normalized or not:
	for title, norm_modules, y_label_suffix, filename_norm_suffix in zip(
		['', "shape comparison"],
		[[], ["NormalizeToUnity"]],
		['', " (normalized)"],
		['', '_normalizes'],
	):
		# pT or y:
		for quantity, x, xlabel, upper_limit in zip(['pT', 'y'], ["d01-x01-y01", "d02-x01-y01"], ['zpt', 'abs(zy)'], [100, 3]):
			# all combinations of the 
			for files, labels, filename_suffixes, paths, weights in zip(
				combinations([
					"/usr/users/dhaitz/home/qcd/sherivf/rivet-results/Rivet.root",
					"/usr/users/dhaitz/home/artus/Excalibur/plots/genz{0}.root".format(quantity.lower()),
					"/usr/users/dhaitz/home/qcd/sherivf/fnlo-results/fnlo_{0}Z.root".format(quantity)], 2),
				combinations(["Sherpa+Rivet", "Madgraph+Pythia", "Sherpa+fastNLO"], 2),
				combinations(["Riv", "MG", "Fnlo"], 2),
				combinations([x, '4', '0'], 2),
				combinations(['1', '19.789', '1'], 2)
			):
				d = {
					"analysis_modules": norm_modules + ["Ratio"],
					"files": files,
					"folders": [""],
					"labels": labels,
					"markers": ["o", "fill","o"],
					"filename": quantity + "_riv-" + "_".join(filename_suffixes) + filename_norm_suffix,
					"title": title,
					"scale_factors": weights,
					"x_expressions": paths,
					"x_label": xlabel,
					"x_lims": [0.0, upper_limit],
					"y_label": "Events" + y_label_suffix,
					"y_subplot_lims": [0.5, 1.5],
				}
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
	pdf_sets = [#'NNPDF30_nlo_as_0118'cal
		'CT10nlo.LHgrid', 'NNPDF21_100.LHgrid', 'abm11_3n_nlo.LHgrid',
		'cteq65.LHgrid', 'MSTW2008nnlo90cl.LHgrid'
		]
	labels = ['CT10', 'NNPDF', 'ABM11', 'CTEQ6', 'MSTW']
	colors = ['blue', 'red', 'green', 'purple', 'orange']
	N = len(pdf_sets)

	for quantity, sf in zip(['y', 'm', 'pT'#, 'phi'
								], [2*i for i in [0.1, 1, 10, 0.314159]]):
		d = {
			'input_modules': ['InputFastNLO'],
			'pdf_sets': pdf_sets,
			'members': len(pdf_sets),
			#'labels': ['Different PDF Sets'.format(N-1)] + [None]*(N-1),
			'labels': labels,
			'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.tab".format(quantity)],
			'legend': 'upper right',
			'markers': ['-',]*N,
			'line_styles': ['-']*N,
			'colors': colors,
			'energies': [8],
			'filename': ("scale_" if scale else "")+"fastnlo_"+qdict[quantity],
		}
		if quantity == 'pT':
			d['y_log'] = True
		"""
		# add comparison with unfolded data / MC
		rootfile = '/usr/users/dhaitz/home/qcd/sherivf/unfolded/{0}_unfolded_Madgraph_inclusive.root'
		mc = False

		# nicks (for scaling)
		nicks = []
		for pdf_set in pdf_sets:
			nicks.append("_".join([d['fastnlo_files'][0], pdf_set, str(n)]))

		d.update({
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			'files': [rootfile.format(qdict[quantity])],
			'x_bins': bindict[qdict[quantity]],
			'folders': [""],
			'x_expressions': [('MC_unfolded' if mc else 'Data_unfolded')],
			'labels': ['Data'] + d['labels'],
			'colors': ['black'] + d['colors'],
			'line_styles': [None] + d['line_styles'],
			'markers': ['o'] + d['markers'],
			'x_label': qdict[quantity],
			'analysis_modules':['ScaleHistograms'],
			'scale_factors': [1./19789.],
			'scale_nicks': nicks,
			'scale': (sf if scale else 1.)/1000.,
			'y_label': r'$\\sigma$ / pb' + ("" if quantity == 'y' else " $GeV^{-1}$"),
			'texts': [("fastNLO scaled by factor {0}".format(str(sf)) if scale else "")],
		})
		if quantity == 'pT':
			d['y_lims'] = [0.001, 30]
			d['legend'] = 'lower left'
		elif quantity == 'y':
			d['legend'] = 'lower left'

		# ratio
		if scale:
			d['analysis_modules'].append('Ratio')
			d['markers'] += ['-']*N
			d['line_styles'] += ['-']*N
			d['colors'] += colors
			d.update({
				'ratio_numerator_nicks': nicks,
				'ratio_denominator_nicks': ['nick0'],
				'y_subplot_lims': [0, 2],
				'y_subplot_label': 'Ratio MC/Data',
				
			})
		"""
		plots.append(d)

	harryinterface.harry_interface(plots, args)


def fastnlo_pdfmember(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	n_members = 101

	for quantity, sf in zip(['y', 'm', 'pT'], [0.1, 1, 10]):
		d = {
			# input
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			# input fastNLO
			'pdf_sets': ['NNPDF21_100.LHgrid'],
			'members': range(n_members),
			#'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.tab".format(quantity)],
			'fastnlo_files': ["latest_sherivf_output/output/fnlo_{0}Z_0.tab".format(quantity)],
			# input root
			'files': [os.environ['EXCALIBURPATH'] + '/work/data_ee.root'],#[common.unfold_path + '/' + '_'.join([qdict[quantity].replace("abs(zy)", "zy"), 'madgraph', 'inclusive', '1']) + '.root'],
				#'folders': '',
			'x_bins': common.bins[qdict[quantity]],
			'zjetfolders': ['zcuts'],
			'algorithms': ['ak5PFJetsCHS'],
			'x_expressions': qdict[quantity], #'data_unfolded',
			'scale_factors': [1./19712.],
			# analysis
			"analysis_modules": ["ScaleHistograms"],
			'scale': sf*(0.2),
			#'scale_nicks':["latest_sherivf_output/fnlo_{}Z.tab_NNPDF21_100.LHgrid_{}".format(quantity, i) for i in range(n_members)],
			'scale_nicks':["latest_sherivf_output/output/fnlo_{}Z_0.tab_NNPDF21_100.LHgrid_{}".format(quantity, i) for i in range(n_members)],
			# formatting
			'legend': None,
			'markers': ['o'] + ['-']*n_members,
			'line_styles': [None] + ['-']*n_members,
			'line_widths': [0.1],
			'colors': ['black'] + ['blue']*n_members,
			'energies': [8],
			# output
			'filename': qdict[quantity],
		}
		if quantity == 'pT':
			d['y_log'] = True
			d['y_lims'] = [1e-3, 1e2]
		plots.append(d)

	harryinterface.harry_interface(plots, args)
