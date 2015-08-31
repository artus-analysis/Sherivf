#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
import Excalibur.Plotting.utility.colors as colors
import parsertools

import numpy as np
import common


def unfold(args=None):
	"""Unfold Z(->ee) distributions and save as root. All combinations of n jet categories, rapidity bins, MC samples and quantities (y, mass, pT) are plotted."""

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])

	# some variables
	ybins = np.arange(0, 2.8, 0.4)
	lumi = 19.712
	path = common.bkgr_path
	max_iterations = 4

	plots = []
	for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])],
				["inclusive"] + ["{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
	], known_args.no_ybins)):
		for mc_label, mc in zip(*parsertools.get_list_slice([
			['Madgraph', 'Powheg'],
			['mc_ee.root', 'mc_ee_powheg.root']
		], known_args.no_mcs)):
			for quantity in parsertools.get_list_slice(['zpt', 'zmass', 'zy'], known_args.no_quantities):
				for iteration in parsertools.get_list_slice([range(1, 1+max_iterations)], known_args.no_iterations)[0]:
					d = {
						'x_expressions': ['data']+[quantity.replace("z", "genz"), quantity, quantity.replace("z", "genz")],
						'y_expressions': [None, quantity, None, None],
						'files': ["1_background-subtracted/" + quantity + "_" + ybinsuffix + ".root"]+[path + "/work/" + mc]*3,
						'nicks': [
							'data_reco',
							'responsematrix',
							'mc_reco',
							'mc_gen',
						],
						'lumis': [lumi],
						'folders': ['']+['leptoncuts_ak5PFJetsCHSL1L2L3/ntuple']*3,
						'weights': "({}&&hlt)".format(ybin),
						'x_bins': [common.bins[quantity]],
						'y_bins': [common.bins[quantity]],
						# analysis
						'analysis_modules': ['Unfolding'],
						'unfolding': ['data_reco', 'mc_reco'],
						'unfolding_responsematrix': 'responsematrix',
						'unfolding_mc_gen': 'mc_gen',
						'unfolding_mc_reco': 'mc_reco',
						'unfolding_new_nicks': ['data_unfolded', 'mc_unfolded'],
						'unfolding_iterations': iteration,
						'libRooUnfold': '~/home/RooUnfold-1.1.1/libRooUnfold.so',
						#output
						'plot_modules': ['ExportRoot'],
						'filename': "_".join([quantity, mc_label.lower(), ybinsuffix, str(iteration)]),
						'output_dir': common.unfold_path,
						'export_json': False,
					}
					plots.append(d)
	harryinterface.harry_interface(plots, args)


def different_iterations(args=None):
	"""compare different unfolding iterations"""
	plots = []
	ybin = 'inclusive'
	max_iteration = 3
	for quantity in ['zmass', 'zpt', 'zy']:
		basename = common.unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, '{}']) + '.root'
		d = {
			# input
			'files': [basename.format(str(1))]*2 + [basename.format(str(1+n)) for n in range(max_iteration)],
			'folders': [''],
			'nicks': [str(item) for item in range(max_iteration+2)],
			'labels': ['Data', 'MC Gen'] + ["Unfolded ({} iter.)".format(str(item+1)) for item in range(max_iteration)],
			'x_expressions': ['data_reco', 'mc_gen']+['data_unfolded']*max_iteration,
			# formatting
			'markers': ['o', 'fill'] + ['.']*(max_iteration*2+1),
			'line_styles': ['None']*2 + ['-']*(max_iteration)+['None']*(max_iteration+1),
			'step': [True],
			'marker_colors': ['black', 'red', 'blue', 'green'],
			'x_label': quantity,
			# output
			'filename': 'iterations_' + quantity,
		}
		if quantity == 'zpt':
			d['y_log'] = True
		else:
			d['legend'] = 'upper left'
		# ratio to MC gen
		d.update({
			'analysis_modules': ['Ratio'],
			'ratio_numerator_nicks': [str(item) for item in ([0]+range(2,max_iteration+2))],
			'ratio_denominator_nicks': ['1'],
			'y_subplot_label': 'Ratio to MC Gen',
			'y_subplot_lims': [0, 2],
		})
		plots.append(d)
	harryinterface.harry_interface(plots, args)

def response_matrix(args=None):
	""" plot response matrix"""
	plots = []
	ybin = 'inclusive'
	for log in [True, False]:
		for quantity, y_lims in zip(['zmass', 'zpt', 'zy'], [[81, 101], [0, 400], [-2.5, 2.5]]):
			d = {
				# input
				'files': [common.unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, '1']) + '.root'],
				'folders': [''],
				'x_expressions': ['responsematrix'],
				# formatting
				'y_lims': y_lims,
				'x_label': 'gen' + quantity,
				'y_label': 'reco' + quantity,
				'energies': [8],
				'z_log': log,
				# output
				'filename': 'responsematrix_' + quantity + ("_log" if log else ""),
			}
			plots.append(d)
	harryinterface.harry_interface(plots, args)


def unfolding_comparison(args=None):
	"""Comparison between reco,gen,unfolded for Data and MC"""
	plots = []

	ybin = 'inclusive'
	labels = ['Data Reco', 'MC Reco', 'MC Gen', 'Data Unfolded', 'MC Unfolded']
	expressions = [label.lower().replace(" ", "_") for label in labels]

	for iterations in range(1, 4):
		for quantity in ['zmass', 'zpt', 'zy']:
			filename = unfold_path + '/' + '_'.join([quantity, 'madgraph', ybin, str(iterations)]) + '.root'
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
				'lumis': [19.712],
				'x_label': quantity,
				'title': str(iterations) + " iteration" + ("s" if iterations != 1 else ""),
				# output
				'filename': "_".join(['unfolded', quantity, str(iterations)]),
			}
			if quantity == 'zpt':
				d['y_log'] = True
			else:
				d['legend'] = 'upper left'
			# ratio to MC gen
			d.update({
				'analysis_modules': ['Ratio'],
				'ratio_numerator_nicks': [expression for expression in expressions if expression != 'mc_gen'],
				'ratio_denominator_nicks': ['mc_gen'],
				'y_subplot_label': 'Ratio to MC Gen',
				'y_subplot_lims': [0, 2],
			})
			plots.append(d)
	harryinterface.harry_interface(plots, args)


def unfolded_to_hera(args=None):
	""" take unfolded data and convert it into herafitter format"""
	plots = []
	d = {
		'files': ['2_unfolded/zpt_madgraph_inclusive_3.root'],
		'folders': [''],
		'x_expressions': ['data_unfolded'],
		# output
		'plot_modules': 'ExportHerafitter',
		'header_file': '/usr/users/dhaitz/home/qcd/sherivf/herafitter/herafitter_header.txt',
		'filename': 'CMS_Zee_HFinput',
		'output_dir': 'herafitter/',
	}
	plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	zee_unfolded()
