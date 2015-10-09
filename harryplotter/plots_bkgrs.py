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
						d = {
							# input
							'x_expressions': common.root_quantity(quantity),
							'x_bins': [common.bins[quantity]],
							'files': ([path+'/work/data_ee.root', path+mc] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds])[(0 if signal else 2):],
							"nicks": (['data','mc']+backgrounds_merged)[(0 if signal else 2):],
							'folders': (['zcuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['zcuts_ak5PFJetsCHSL1L2L3/ntuple']*n_mcs)[(0 if signal else 2):],
							'weights': (["(({}) && ({}))".format(ybin, njetweight)] + ["(hlt && ({}) && ({}))".format(ybin, njetweight)]*n_mcs)[(0 if signal else 2):],
							'scale_factors': [1. if signal else common.lumi],
							# formatting
							'legend': 'upper right',
							"labels": (["Data", r"DY$\\rightarrow ee$"]+[common.bkgr_labels[item] for item in backgrounds_merged_short])[(0 if signal else 2):],
							"markers": (['o'] + ['fill']*n_mcs_merged_short)[(0 if signal else 2):],
							'stacks': (['data'] + ['mc']*n_mcs_merged_short)[(0 if signal else 2):],
							"bar_colors": [colors.histo_colors[color] for color in [common.bkgr_colors[item] for item in ['mc']+backgrounds_merged_short]][(0 if signal else 1):],
							'y_log': (True if quantity == "zpt" else False),
							'texts': [ybinlabel, njetlabel],
							'texts_x':[0.03],
							'texts_y': [0.97, 0.87],
							# output
							'filename': quantity + "_" + mc_label+ybinsuffix+njetsuffix + ("" if signal else "_only_bkgrs"),
							'export_json': False,
							'www_text': "Backgrounds as a function of different quantities, with and without signal samples",
							'www_title': "Background Contributions",
						}
						if quantity == 'zpt':
							d['x_log'] = common.zpt_xlog
							if common.zpt_xlog:
								d['x_ticks'] = common.zpt_ticks
						plots.append(d)

	return [PlottingJob(plots, args)]


def subtract_backgrounds(args=None):
	"""Subtract backgrounds from data"""
	plots = []
	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities'])

	path = common.bkgr_path
	backgrounds = common.bkgr_backgrounds

	for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
		["1"] + common.ybin_weights,
		["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
		for quantity, bins in zip(*parsertools.get_list_slice([common.data_quantities, [common.bins[i] for i in common.data_quantities]], known_args.no_quantities)):
			for variation in common.variations:  # for sys uncert estimation
				datasuffix = ""
				if (("bkgr" not in variation) and (variation != "")):
					datasuffix = variation
				mc_scalefactor = -1 + (-0.5*(variation=="_bkgrdown")) + (0.5*(variation=="_bkgrup"))  # for bkgr estimation
				d = {
					#input
					'x_expressions': common.root_quantity(quantity),
					'x_bins': [bins],
					'files': [path+'/work/data_ee{}.root'.format(datasuffix)] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds],
					'nicks': ['data'],
					'weights': ["({})".format(ybin)] + ["({scalefactor}*(hlt&&({ybin})))".format(ybin=ybin, scalefactor=mc_scalefactor)]*len(backgrounds),
					'folders': ['zcuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['zcuts_ak5PFJetsCHSL1L2L3/ntuple']*len(backgrounds),
					#output
					'plot_modules': ['ExportRoot'],
					'filename': quantity + "_" + ybinsuffix + variation,
					'output_dir': common.subtract_dir,
					'export_json': False,
				}
				plots.append(d)
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
			'folders': ['zcuts_ak5PFJetsCHSL1L2L3Res/ntuple'] + ['zcuts_ak5PFJetsCHSL1L2L3/ntuple']*len(backgrounds),
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
