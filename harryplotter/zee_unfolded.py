#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
import parsertools

import numpy as np
import zee_bkgrs as bkgrs

def unfold(args=None):
	"""Unfold Z(->ee) distributions and save as root. All combinations of n jet categories, rapidity bins, MC samples and quantities (y, mass, pT) are plotted."""

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])

	# some variables
	ybins = np.arange(0, 2.8, 0.4)
	lumi = 19.712
	path = bkgrs.bkgr_path

	plots = []
	for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])],
				["inclusive"] + ["{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
	], known_args.no_ybins)):
		for mc_label, mc in zip(*parsertools.get_list_slice([
			['Madgraph', 'Powheg'],
			['mc_ee.root', 'mc_ee_powheg.root']
		], known_args.no_mcs)):
			for quantity, bins in zip(*parsertools.get_list_slice([
				['zpt', 'zmass', 'zy'],
				["40,0,400", "20,81,101", "25,-2.5,2.5"]
			], known_args.no_quantities)):
				for iteration in parsertools.get_list_slice([range(5)], known_args.no_iterations)[0]:
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
						'weights': ybin,
						'x_bins': [bins],
						'y_bins': [bins],
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
						'output_dir': "2_unfolded",
						'export_json': False,
					}
					plots.append(d)
	harryinterface.harry_interface(plots, args)


def unfold(args=None):
	"""Unfolded Z(->ee) distributions. All combinations of n jet categories, rapidity bins, MC samples and quantities (y, mass, pT) are plotted."""



if __name__ == '__main__':
	zee_unfolded()
