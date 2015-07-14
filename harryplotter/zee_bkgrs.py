#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface


def zee_bkgrs(args=None):
	"""Plot data, signal and backgounds, for all combinations of njet categories, 
	rapidity bins, mc samples, log/linear scale, ZpT/y/mass/ Njets as x-quantity."""

	path = '/portal/ekpcms5/home/dhaitz/git/excalibur/'
	plots = []
	ybins = np.arange(0, 2.4, 0.4)
	bkgr_signal_ratio = False

	for njetweight, njetlabel, njetsuffix in zip(
		["1", "njets30<2", "njets30>1"],
		["", "$ n_{jets(p_T>30GeV)}<=1$", "$ n_{jets(p_T>30GeV)}>1$"],
		["", "_njets0-1", "_njets2"]
	):
		# iterate over rapidity bins
		for ybin, ybinlabel, ybinsuffix in zip(
					["1"] + ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])],
					["", "|y|<0.4"] + ["{0}<|y|<{1}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])][1:],
					["_inclusive"] + ["_{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
		):
		# iterate over MC samples
			for mc, mc_label in zip(['/store/mc_ee_corr.root', '/store/mc_ee_powheg_corr.root'],
				['Madgraph', 'Powheg']):
				# log / linear scale
				for log, suffix in zip([False, True], ['', '_log']):
					# different quantities
					for quantity, bins in zip(['zpt', 'zy', 'zmass', 'njets30'],
						[[30, 40, 60, 80, 100, 120, 140, 170, 200, 1000],
						"14,-2.8, 2.8",
						"20,81,101",
						"7,-0.5,6.5"]):
						d = {
							'x_expressions': quantity,
							'files': [
								path + 'work/data_ee_corr.root',

								path + mc,

								path + '/store/background_ee_zz.root',
								path + '/store/background_ee_wz.root',
								path + '/store/background_ee_tt.root',
								path + '/store/background_ee_tw.root',
								path + '/store/background_ee_ww.root',
								path + '/store/background_ee_wjets.root',
								path + '/store/background_ee_dytautau.root',
							],
							'legend': None,
							"labels": [
								"data", 
								r"DY->ee ", 
								"ZZ,WZ", 
								"tt",
								"tW, WW, W+jets, DY->tautau"
							],
							"nicks": [
								'data',
								'mc',
								'wwwzzz',
								'wwwzzz',
								'tt',
								'min',
								'min',
								'min',
								'min'
							],
							'title': "own work",
							"markers": [
								"o", 
								"fill", 
								"fill", 
								"fill", 
								"fill", 
							],
							'stacks': ['data'] + ['mc']*4,
							'folders': ['zcuts_AK5PFJetsCHSL1L2L3'],
							'weights': "(({}) && ({}))".format(ybin, njetweight),


							'lumi': 19.8,
							'energy': '8',
						
							'texts': [ybinlabel, njetlabel],
							'texts_x':[0.03],
							'texts_y': [0.97, 0.87],

							'x_bins': bins,
							'y_log': log,

							#'ratio': True,
							'y_ratio_lims': [0.5, 1.5],

							'save_legend': "legend" + "_" + mc_label,
							#'export_json': False,

							'filename': quantity + suffix + "_" + mc_label+ybinsuffix+njetsuffix,
						}
						if quantity == 'zpt':
							d['x_log'] = True
							d['x_lims'] = [30, 650]
							d['x_ticks'] = [30, 50, 70, 100, 200, 400, 1000]
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


if __name__ == '__main__':
	zee_bkgrs()
