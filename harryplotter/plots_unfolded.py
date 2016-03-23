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
		basename = common.unfold_path + '/' + '_'.join([quantity, common.default_mc, ybin, '{}']) + '.root'
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
	for quantity in common.data_quantities:
		for ybin, ybinplotlabel in zip(["inclusive"] + common.ybin_labels, [""] + common.ybin_plotlabels):
			if (quantity is not 'zpt') and (ybin is not "inclusive"):
				continue
			lims = common.lims(quantity)
			d = {
				# input
				'files': [common.unfold_path + '/' + '_'.join([quantity, common.default_mc, ybin, '1']) + '.root'],
				'folders': [''],
				'x_expressions': ['responsematrix'],
				'analysis_modules': ['NormalizeRowsToUnity'],
				# formatting
				'y_label': 'gen' + quantity,
				'x_label': 'reco' + quantity,
				'z_log': True,
				'z_lims':[1e-3, 1],
				'z_label': 'Response',
				'rasterized': True,
				'texts': [ybinplotlabel],
				# output
				'filename': 'responsematrix_' + quantity + ("" if ybin=='inclusive' else "_"+ybin),
				'www_title': 'Response Matrices',
				'www_text': "",
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
	"""Comparison between reco,unfolded for"""
	plots = []

	ybin = 'inclusive'
	labels = ['Data Unfolded', 'Data Reco']
	expressions = [label.lower().replace(" ", "_") for label in labels]
	labels = [l.replace(' Reco', '') for l in labels]

	for iterations in range(1, 5):
		for quantity in common.data_quantities:
			for ybin, ybinplotlabel in zip(["inclusive"] + common.ybin_labels, [""] + common.ybin_plotlabels):
				if (quantity is not 'zpt') and (ybin is not "inclusive"):
					continue
				filename = common.unfold_path + '/' + '_'.join([quantity, common.default_mc, ybin, str(iterations)]) + '.root'
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
					'lumis': [common.lumi],
					'energies': [8],
					'markers': ['o', '-'],
					'line_styles': [None, '-'],
					'step': True,
					'legend': 'upper right',
					'x_lims': common.lims(quantity),
					'y_subplot_lims': [0.95, 1.05],
					'x_bins': common.bins[quantity],
					'x_label': quantity,
					'texts': [ybinplotlabel],
					# output
					'filename': "_".join(['unfolded', quantity, str(iterations)])+("" if ybin=='inclusive' else "_"+ybin),
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
					'y_subplot_label': 'Unfolded/Reco',
				})
				plots.append(d)
	return [PlottingJob(plots, args)]


def unfolded_mc_comparison(args=None):
	""" compare the result of the unfolding procedure for diff MCs or diff algos """
	plots = []
	for quantity in ['zpt', 'abszy']:
		for ybin, ybinplotlabel in zip(["inclusive"] + common.ybin_labels, [""] + common.ybin_plotlabels):
			if (quantity is not 'zpt') and (ybin is not "inclusive"):
				continue

			# MC comparison
			iterations = 1
			dic1 = {
				'files': ['2_unfolded/{0}_{1}_{3}_{2}.root'.format(quantity, mc, iterations, ybin) for mc in common.mcs],
				'filename': 'unfolding_samples_'+quantity+("" if ybin=='inclusive' else "_"+ybin),
				'analysis_modules': ['Ratio'],
				'y_subplot_label': '{}/{}'.format(common.mcs[0].capitalize(), common.mcs[1].capitalize()),
				'labels': ['Response matrix from {} sample'.format(mc) for mc in  [s.capitalize() for s in common.mcs]],
				'markers': ['o', '-'],
				'line_styles': [None, '-'],
				'step': True,
			}
			# method comparison
			methods = [''] + ['_'+m for m in common.other_methods]
			# ['', '_dagostini', '_binbybin']
		
			iterations = [1, 4, 1]
			dic2 = {
				'files': ['2_unfolded/{0}_{3}_{4}_{2}{1}.root'.format(quantity, method, iteration, common.default_mc, ybin) for method, iteration in zip(methods, iterations)],
				'nicks': ['inv', 'dago', 'bbb'],
				'analysis_modules': ['Ratio'],
				'ratio_numerator_nicks': ['dago', 'bbb'],
				'ratio_denominator_nicks': ['inv'],
				# formatting
				'y_rel_lims': [0, 1.4],
				'y_subplot_label': 'Ratio to matrix inv.',
				'labels': ['Matrix inversion',r"Iterative d$\\prime$Agostini ({0} iterations)".format(iterations[1]), 'Bin-by-bin'] + ['dago/inv', 'bbb/inv'],
				'filename': 'unfolding_methods_'+quantity+("" if ybin=='inclusive' else "_"+ybin),
				'step': True,
				'colors': [colors.histo_colors['blue'], 'black', 'red', 'black', 'red'],
				'markers': ['fill', 'o',  '-',  '-', '-'],
				'line_styles': [None, None, '-', '-', '-'],
				'zorder': [10,30,20],
			}
			for dic in [dic1, dic2]:
				dic.update({
					'lumis': [19.71],
					'energies': [8],
					'x_lims': common.lims(quantity),
					'x_bins': common.bins[quantity],
					'x_expressions': 'data_unfolded',
					'folders': [''],
					'x_label': quantity,
					'y_subplot_lims': [0.95, 1.05],
					'title': ybinplotlabel,
				})
				if quantity == 'zpt':
					dic['y_log'] = True
					dic['x_log'] = common.zpt_xlog
					dic['x_ticks'] = common.zpt_ticks
					dic['y_lims'] = [1, 10e7]
				plots.append(dic)
	return [PlottingJob(plots, args)]


def correlation_matrix(args=None):
	""" plot correlation matrix"""
	plots = []
	ybin = 'inclusive'
	for quantity in common.data_quantities:
		lims = common.lims(quantity)
		d = {
			# input
			'files': [common.unfold_path + '/' + '_'.join([quantity, common.default_mc, ybin, '1']) + '.root'],
			'folders': [''],
			'x_expressions': ['data_unfolded_corr'],
			'x_bins': common.bins[quantity],
			'y_bins': common.bins[quantity],
			# formatting
			'x_label': quantity,
			'y_label': quantity,
			'z_lims':[-1, 1],
			'z_label': 'Correlation Coefficient',
			'colormap': 'bwr',
			'rasterized': True,
			# output
			'filename': 'correlationmatrix_' + quantity,
			'www_title': 'Correlation Matrices',
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
