#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools
import Excalibur.Plotting.utility.colors as colors

import numpy as np
import common


def different_iterations(args=None):
	"""compare different unfolding iterations"""
	plots = []
	ybin = 'inclusive'
	if (common.default_unfolding_method == 'dagostini'):
		max_iteration = 4
	else:
		max_iteration = 1
	for quantity in common.data_quantities:
		basename = common.unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, '{}']) + '.root'
		d = {
			# input
			'files': [basename.format(str(1))]*2 + [basename.format(str(1+n)) for n in range(max_iteration)],
			'folders': [''],
			'nicks': ['data', 'mc'] + [str(item) for item in range(max_iteration)],
			'labels': ['Data', 'MC Gen'] + ["Unfolded ({} iter.)".format(str(item+1)) for item in range(max_iteration)],
			'x_expressions': ['data_reco', 'mc_gen']+['data_unfolded']*max_iteration,
			# formatting
			'markers': ['o', 'fill'] + ['.']*(max_iteration*2+1),
			'line_styles': ['None']*2 + ['-']*(max_iteration)+['None']*(max_iteration+1),
			'step': [True],
			'marker_colors': ['black', 'red', 'blue', 'green', 'purple']*2,
			'x_label': quantity,
			'legend': 'upper right',
			'x_lims': common.lims(quantity),
			# output
			'filename': 'iterations_' + quantity,
			'www_title': 'Unfolding: different iterations',
			'www_text': r"Different iterations for dAgostini unfolding",
		}
		if quantity == 'zpt':
			d['y_log'] = True
			d['x_log'] = True
		# ratio to MC gen
		d.update({
			'analysis_modules': ['Ratio'],
			'ratio_numerator_nicks': [str(item) for item in ([0]+range(max_iteration))],
			'ratio_denominator_nicks': ['mc'],
			'y_subplot_label': 'Ratio to MC Gen',
			'y_subplot_lims': [0, 2],
		})
		plots.append(d)
	return [PlottingJob(plots, args)]


def response_matrix(args=None):
	""" plot response matrix"""
	plots = []
	ybin = 'inclusive'
	for quantity in common.data_quantities:
		lims = common.lims(quantity)
		d = {
			# input
			'files': [common.unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, '1']) + '.root'],
			'folders': [''],
			'x_expressions': ['responsematrix'],
			'analysis_modules': ['NormalizeColumnsToUnity'],
			# formatting
			#'y_bins': common.bins[quantity],
			#'x_bins': common.bins[quantity],
			#'x_lims': lims,
			#'y_lims': lims,
			'x_label': 'gen' + quantity,
			'y_label': 'reco' + quantity,
			'energies': [8],
			'z_log': True,
			'z_lims':[1e-3, 1],
			'z_label': 'Response',
			# output
			'filename': 'responsematrix_' + quantity,
			'www_title': 'Response Matrices',
			'www_text': r"Unfolding response matrices from Unfolding for Z y,mass,pT with log and scalar z-axis",
		}
		if quantity == 'zpt' and common.zpt_xlog:
			d['y_log'] = True
			d['x_log'] = True
			d['x_ticks'] = common.zpt_ticks
			d['y_ticks'] = common.zpt_ticks
			d['x_bins'] = common.bins[quantity]
			d['y_bins'] = common.bins[quantity]
		plots.append(d)
	return [PlottingJob(plots, args)]


def unfolding_comparison(args=None):
	"""Comparison between reco,gen,unfolded for Data and MC"""
	plots = []

	ybin = 'inclusive'
	labels = ['Data Reco', 'MC Reco', 'MC Gen', 'Data Unfolded', 'MC Unfolded']
	expressions = [label.lower().replace(" ", "_") for label in labels]

	for iterations in range(1, 5):
		for quantity in common.data_quantities:
			filename = common.unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, str(iterations)]) + '.root'
			if (common.default_unfolding_method != 'dagostini') and (iterations > 1):
				continue
			d = {
				# input
				'files': [filename],
				'folders': [''],
				'x_expressions': expressions,
				'nicks': expressions,
				# formatting
				'labels': labels,
				'markers': ['o']*2+['fill']+['.']*2+['o']*2+['.']*2,
				'line_styles': [None]*3 + ['-']*2+[None]*2+['-']*2,
				'step': [True],
				'marker_colors': ['black', 'red'],
				'zorder': [10,10,2,10,10],
				'energies': [8],
				'legend': 'upper right',
				'x_lims': common.lims(quantity),
				'y_subplot_lims': [0.9, 1.1],
				#'lumis': [common.lumi],
				'x_label': quantity,
				#'title': str(iterations) + " iteration" + ("s" if iterations != 1 else ""),
				# output
				'filename': "_".join(['unfolded', quantity, str(iterations)]),
				'www_title': 'Unfolding',
				'www_text': 'Comparison of Data and MC at reco-, gen- and unfolded-level for different unfolding iterations',
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['x_log'] = common.zpt_xlog
				d['y_lims'] = [1, 1e7]
				d['x_ticks'] = common.zpt_ticks
			# ratio to MC gen
			d.update({
				'analysis_modules': ['Ratio'],
				'ratio_numerator_nicks': [e for e in expressions if "unfolded" in e],
				'ratio_denominator_nicks': [e for e in expressions if "reco" in e],
				'y_subplot_label': 'Unfolded/Reco',
			})
			plots.append(d)
	return [PlottingJob(plots, args)]


def unfolded_to_hera(args=None):
	""" take unfolded data and convert it into herafitter format"""
	plots = []
	d = {
		'files': ['2_unfolded/zpt_madgraph_inclusive_{}.root'.format(iterations_to_use)],
		'folders': [''],
		'x_expressions': ['data_unfolded'],
		# output
		'plot_modules': 'ExportHerafitter',
		'header_file': '/usr/users/dhaitz/home/qcd/sherivf/herafitter/herafitter_header.txt',
		'filename': 'CMS_Zee_HFinput',
		'output_dir': 'herafitter/',
	}
	plots.append(d)
	return [PlottingJob(plots, args)]


def unfolded_mc_comparison(args=None):
	""" compare the result of the unfolding procedure for diff MCs or diff algos """
	plots = []
	for quantity in ['zpt', 'abszy']:
		# MC comparison
		iterations = 1
		dic1 = {
			'files': ['2_unfolded/{0}_{1}_inclusive_{2}.root'.format(quantity, mc, iterations) for mc in ['madgraph', 'powheg']],
			'filename': 'unfolding_samples_'+quantity,
			'analysis_modules': ['Ratio'],
			'labels': ['Response matrix from {} sample'.format(mc) for mc in  ['Madgraph', 'Powheg']],
		}
		# method comparison
		methods = [''] + ['_'+m for m in common.other_methods]
		# ['', '_dagostini', '_binbybin']
		
		iterations = [1, 4, 1]
		dic2 = {
			'files': ['2_unfolded/{0}_madgraph_inclusive_{2}{1}.root'.format(quantity, method, iteration) for method, iteration in zip(methods, iterations)],
			'x_bins': common.bins[quantity],
			'nicks': ['inv', 'dago', 'bbb'],
			'analysis_modules': ['Ratio', 'DAgostini'],
			'ratio_numerator_nicks': ['inv', 'dago'],
			'ratio_denominator_nicks': ['bbb'],
			# formatting
			'y_subplot_label': 'Ratio to bin-by-bin',
			'labels': ['Matrix inversion',"Iterative dAgostini ({0} iterations)".format(iterations[1]), 'Bin-by-bin'] + ['inv/bbb', 'dago/bbb'],
			'filename': 'unfolding_methods_'+quantity,
			'step': True,
			'colors': ['black', 'red', colors.histo_colors['blue'], 'black', 'red'],
			'markers': ['o', '-',  'fill',  '-', '-'],
			'line_styles': [None, '-', None, '--', '-'],
		}
		for dic in [dic1, dic2]:
			dic.update({
				'x_lims': common.lims(quantity),
				'x_expressions': 'data_unfolded',
				'folders': [''],
				'x_label': quantity,
				'y_subplot_lims': [0.95, 1.05],
			})
			if quantity == 'zpt':
				dic['y_log'] = True
				dic['x_log'] = common.zpt_xlog
				dic['x_ticks'] = common.zpt_ticks
				dic['y_lims'] = [1, 10e6]
			plots.append(dic)
	return [PlottingJob(plots, args)]
