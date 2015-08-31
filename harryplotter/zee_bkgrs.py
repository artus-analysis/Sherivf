#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import parsertools
import common

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
import Excalibur.Plotting.utility.colors as colors


def zee_bkgrs(args=None):
	"""Plot data, signal and backgrounds, for all combinations of njet categories,
	rapidity bins, mc samples, log/linear scale, ZpT/y/mass/ Njets as x-quantity."""

	plots = []
	ybins = np.arange(0, 2.4, 0.4)
	bkgr_signal_ratio = False
	path = common.bkgr_path
	backgrounds = common.bkgr_backgrounds

	known_args, args = parsertools.parser_list_tool(args, ['njets', 'ybins', 'mcs', 'logs', 'quantities', 'signal'])

	n_mcs = 1 + len(backgrounds)
	backgrounds_merged = ['diboson', 'diboson', 'tt', 'others', 'others', 'others', 'others', 'others']
	n_mcs_merged = 1 + len(backgrounds_merged)
	backgrounds_merged_short = ['diboson', 'tt', 'others']
	n_mcs_merged_short = 1 + len(backgrounds_merged_short)

	# add signal data+mc or plot only backgrounds
	for signal in parsertools.get_list_slice([[False, True]], known_args.no_signal)[0]:
		for njetweight, njetlabel, njetsuffix in zip(*parsertools.get_list_slice([
			["1", "njets30<2", "njets30>1"],
			["", "$n_{jets}<=1$", "$n_{jets}}>1$"],
			["", "_njets0-1", "_njets2"]
		], known_args.no_njets)):
			# iterate over rapidity bins
			for ybin, ybinlabel, ybinsuffix in zip(*parsertools.get_list_slice([
						["1"] + ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])],
						["", "$|y|<0.4$"] + ["${0}<|y|<{1}$".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])][1:],
						["_inclusive"] + ["_{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
			], known_args.no_ybins)):
			# iterate over MC samples
				for mc, mc_label in zip(*parsertools.get_list_slice([
					['/work/mc_ee.root', '/work/mc_ee_powheg.root'],
					['Madgraph', 'Powheg']
				], known_args.no_mcs)):
					# log / linear scale
					for log, suffix in zip(*parsertools.get_list_slice([
						[False, True], ['', '_log']
					], known_args.no_logs)):
						# different quantities
						for quantity in parsertools.get_list_slice(['zpt', 'zy', 'zmass', 'njets30'], known_args.no_quantities):
							d = {
								# input
								'x_expressions': quantity,
								'x_bins': [common.bins[quantity]],
								'files': ([path+'/work/data_ee.root', path+mc] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds])[(0 if signal else 2):],
								"nicks": (['data','mc']+backgrounds_merged)[(0 if signal else 2):],
								'folders': (['leptoncuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['leptoncuts_ak5PFJetsCHSL1L2L3/ntuple']*n_mcs)[(0 if signal else 2):],
								'weights': (["(e1mvatrig && e2mvatrig && ({}) && ({}))".format(ybin, njetweight)] + ["(hlt && e1mvatrig && e2mvatrig && ({}) && ({}))".format(ybin, njetweight)]*n_mcs)[(0 if signal else 2):],
								'scale_factors': [1. if signal else 19.712],
								# formatting
								'legend': None,
								"labels": (["Data", r"DY$\\rightarrow ee$"]+[common.bkgr_labels[item] for item in backgrounds_merged_short])[(0 if signal else 2):],
								"markers": (['o'] + ['fill']*n_mcs_merged_short)[(0 if signal else 2):],
								'stacks': (['data'] + ['mc']*n_mcs_merged_short)[(0 if signal else 2):],
								"bar_colors": [colors.histo_colors[color] for color in [common.bkgr_colors[item] for item in ['mc']+backgrounds_merged_short]][(0 if signal else 1):],
								'y_log': log,
								'texts': [ybinlabel, njetlabel],
								'texts_x':[0.03],
								'texts_y': [0.97, 0.87],
								# output
								'save_legend': "legend" + "_" + mc_label + ("" if signal else "_only-bkgrs"),
								'filename': quantity + suffix + "_" + mc_label+ybinsuffix+njetsuffix + ("" if signal else "_only_bkgrs"),
								'export_json': False,
							}
							plots.append(d)
	"""
							if bkgr_signal_ratio:
								d.update({
									"nicks": ['data','signal','bkgr','bkgr','bkgr','bkgr','bkgr','bkgr','bkgr'],
									"labels": ["data", "signal", "back"],
									'stacks': ["data", "mc", "mc"],
									'markers': 	d['markers'][:3],
									'y_ratio_label': "bkgr/signal",
									'ratio_num': ['bkgr'],
									'ratio_denom': ['signal'],
									'y_ratio_lims': [0.0, 0.1],
									'filename': d['filename'] + '_sig-bkgr',
									'save_legend': d['save_legend'] + "_sig-bkgr",
								})
								plots.append(d)
						"""
	harryinterface.harry_interface(plots, args)


def subtract_backgrounds(args=None):
	"""Subtract backgrounds from data"""
	plots = []
	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities'])

	path = common.bkgr_path
	ybins = np.arange(0, 2.4, 0.4)
	backgrounds = common.bkgr_backgrounds
	mc_scalefactor = -1
	quantities = ['zpt', 'zy', 'zmass']
	binnings = [common.bins[i] for i in quantities]

	for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
		["1"] + ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])],
		["inclusive"] + ["{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
	], known_args.no_ybins)):
		for quantity, bins in zip(*parsertools.get_list_slice([quantities, binnings], known_args.no_quantities)):
			d = {
				#input
				'x_expressions': quantity,
				'x_bins': [bins],
				'files': [path+'/work/data_ee.root'] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds],
				'nicks': ['data'],
				'weights': [ybin] + ["({scalefactor}*(hlt && ({ybin})))".format(ybin=ybin, scalefactor=mc_scalefactor)]*len(backgrounds),
				'folders': ['zcuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['zcuts_ak5PFJetsCHSL1L2L3/ntuple']*len(backgrounds),
				#output
				'plot_modules': ['ExportRoot'],
				'filename': "_".join([quantity, ybinsuffix]),
				'output_dir': "1_background-subtracted",
				'export_json': False,
			}
			plots.append(d)
	harryinterface.harry_interface(plots, args)


def emu(args=None):
	"""plot emu Data and backgrounds"""
	plots = []
	backgrounds = ['tt', 'tw', 'ww','dytautau']
	known_args, args = parsertools.parser_list_tool(args, ['quantities'])
	path = common.bkgr_path

	for quantity in parsertools.get_list_slice(['zpt', 'zy', 'zmass', 'njets30'], known_args.no_quantities):
		d = {
			# input
			'x_expressions': quantity,
			'x_bins': [common.bins[quantity]],
			'files': [path+'/work/data_em.root']+[path+'/work/background_ee_{}.root'.format(item) for item in backgrounds],
			'folders': ['zcuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['zcuts_ak5PFJetsCHSL1L2L3/ntuple']*len(backgrounds),
			#'weights': ['1']+['(hlt&&e1mvatrig&&e2mvatrig)']*4,
			# formatting
			'stacks': ['data'] + ['mc']*len(backgrounds),
			"bar_colors": [colors.histo_colors[color] for color in ['blue', 'yellow', 'green', 'brown']],
			"labels": [r"Data $e\\mu$"]+[common.bkgr_labels[item] for item in backgrounds],
		}
		if quantity == 'zpt':
			d['x_lims'] = [0, 200]
		plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	zee_bkgrs()
