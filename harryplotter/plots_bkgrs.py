#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import parsertools
import common

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import Excalibur.Plotting.utility.colors as colors


def zee_bkgrs(args=None):
	"""Plot data, signal and backgrounds, for all combinations of njet categories,
	rapidity bins, mc samples, log/linear scale, ZpT/y/mass/ Njets as x-quantity."""

	known_args, args = parsertools.parser_list_tool(args, ['njets', 'ybins', 'mcs', 'quantities', 'signal'])

	plots = []
	ybins = common.ybins
	bkgr_signal_ratio = False
	path = common.bkgr_path

	backgrounds = common.bkgr_backgrounds
	backgrounds_merged = common.backgrounds_merged
	backgrounds_merged_short = common.backgrounds_merged_short

	n_mcs = 1 + len(backgrounds)
	n_mcs_merged = 1 + len(backgrounds_merged)
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
						["1"] + common.ybin_weights,
						[""] + common.ybin_plotlabels,
						["_inclusive"] + common.ybin_labels
			], known_args.no_ybins)):
			# iterate over MC samples
				for mc, mc_label in zip(*parsertools.get_list_slice([
					['/work/mc_ee.root', '/work/mc_ee_powheg.root'],
					['Madgraph', 'Powheg']
				], known_args.no_mcs)):
					# different quantities
					for quantity in parsertools.get_list_slice(common.data_quantities + ['njets30'], known_args.no_quantities):
						for normalized in [True, False]:
							if normalized and signal:
								continue
							d = {
								# input
								'x_expressions': common.root_quantity(quantity),
								'x_bins': [common.bins[quantity]],
								'files': ([path+'/work/data_ee.root', path+mc] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds])[(0 if signal else 2):],
								"nicks": (['data','mc']+backgrounds_merged)[(0 if signal else 2):],
								'folders': (['zcuts_{}Res/ntuple'.format(common.algocorr)] + ['zcuts_{}/ntuple'.format(common.algocorr)]*n_mcs)[(0 if signal else 2):],
								'weights': (["(({}) && ({}))".format(ybin, njetweight)] + ["(hlt && ({}) && ({}))".format(ybin, njetweight)]*n_mcs)[(0 if signal else 2):],
								'scale_factors': [1. if signal else common.lumi],
								# formatting
								"analysis_modules": (['NormalizeSumOfBinsToUnity'] if normalized else []),
								'legend': 'upper right',
								"labels": (["Data", r"DY$\\rightarrow ee$"]+[common.bkgr_labels[item] for item in backgrounds_merged_short])[(0 if signal else 2):],
								"markers": (['o'] + ['fill']*n_mcs_merged_short)[(0 if signal else 2):],
								'stacks': (['data'] + ['mc']*n_mcs_merged_short)[(0 if signal else 2):],
								"bar_colors": [colors.histo_colors[color] for color in [common.bkgr_colors[item] for item in ['mc']+backgrounds_merged_short]][(0 if signal else 1):],
								'y_log': (True if (quantity == "zpt" and not normalized) else False),
								'texts': [ybinlabel, njetlabel],
								'texts_x':[0.03],
								'texts_y': [0.97, 0.87],
								# output
								'filename': quantity + "_" + mc_label+ybinsuffix+njetsuffix + ("" if signal else "_only_bkgrs") + ("_norm" if normalized else ""),
								'www_text': "Backgrounds as a function of different quantities, with and without signal samples",
								'www_title': "Background Contributions",
							}
							if quantity == 'zpt':
								d['x_log'] = common.zpt_xlog
								if common.zpt_xlog:
									d['x_ticks'] = common.zpt_ticks
							if quantity == 'zmass' and not signal:
								d['x_label'] = 'eemass'
							if normalized:
								d['y_lims'] = [0, 1]
								d['y_label'] = 'Relative contribution to total background'
								d['legend'] = 'upper center'
							plots.append(d)

	return [PlottingJob(plots, args)]


def signal_background_ratio(args=None):
	""" Signal and background + ratio"""
	plots = []
	known_args, args = parsertools.parser_list_tool(args, ['njets', 'ybins', 'quantities'])

	for njetweight, njetlabel, njetsuffix in zip(*parsertools.get_list_slice([
			["1", "njets30<2", "njets30>1"],
			["", "$n_{jets}<=1$", "$n_{jets}}>1$"],
			["", "_njets0-1", "_njets2"]
	], known_args.no_njets)):
		# iterate over rapidity bins
		for ybin, ybinlabel, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				[""] + common.ybin_plotlabels,
				["_inclusive"] + common.ybin_labels
		], known_args.no_ybins)):
			for quantity in parsertools.get_list_slice(common.data_quantities + ['njets30'], known_args.no_quantities):
				for log in [True, False]:
					d = {
						'x_expressions': common.root_quantity(quantity),
						'x_bins': [common.bins[quantity]],
						'files': [common.bkgr_path+'/work/mc_ee.root'] + [common.bkgr_path+'/work/background_ee_{}.root'.format(item) for item in common.bkgr_backgrounds],
						"nicks": ['signal']+['background']*len(common.bkgr_backgrounds),
						"stacks": ['stack'],
						'folders': ['zcuts_{}/ntuple'.format(common.algocorr)],
						'weights': (["(hlt && ({}) && ({}))".format(ybin, njetweight)]),
						'scale_factors': [common.lumi],
						#
						'analysis_modules': ['Ratio'],
						'ratio_numerator_nicks': ['background'],
						'ratio_denominator_nicks': ['signal'],
						#
						'markers': ['fill']*2+['.'],
						'labels': ['Signal', 'Background', 'Ratio'],
						'y_subplot_label': 'Background/Signal',
						'x_errors': [False, False, True],
						'y_subplot_lims': [0, 0.1],
						'y_log': log,
						#
						'filename': quantity + "_" + ybinsuffix+njetsuffix + ('_log' if log else ''),
						'www_text': " ",
						'www_title': "Background /Signal Ratio",
					}
					plots.append(d)
					if quantity == 'zpt':
						d['x_log'] = common.zpt_xlog
						if common.zpt_xlog:
							d['x_ticks'] = common.zpt_ticks
	return [PlottingJob(plots, args)]


def emu(args=None):
	"""plot emu Data and backgrounds"""
	plots = []
	backgrounds = ['tt', 'tw', 'ww','dytautau']
	known_args, args = parsertools.parser_list_tool(args, ['quantities'])
	path = common.bkgr_path

	for quantity in parsertools.get_list_slice(common.data_quantities + ['njets30'], known_args.no_quantities):
		d = {
			# input
			'x_expressions': common.root_quantity(quantity),
			'x_bins': [common.bins[quantity]],
			'files': [path+'/work/data_em.root']+[path+'/work/background_ee_{}.root'.format(item) for item in backgrounds],
			'folders': ['zcuts_{}Res/ntuple'.format(common.algocorr)] + ['zcuts_{}/ntuple'.format(common.algocorr)]*len(backgrounds),
			#'weights': ['1']+['(hlt&&e1mvatrig&&e2mvatrig)']*4,
			# formatting
			'stacks': ['data'] + ['mc']*len(backgrounds),
			"bar_colors": [colors.histo_colors[color] for color in ['blue', 'yellow', 'green', 'brown']],
			"labels": [r"Data $e\\mu$"]+[common.bkgr_labels[item] for item in backgrounds],
			# output
			'www_title': "Background estimation with the e&mu; method",
			'www_text': " ",
		}
		if quantity == 'zpt':
			d['x_lims'] = [0, 200]
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	zee_bkgrs()
