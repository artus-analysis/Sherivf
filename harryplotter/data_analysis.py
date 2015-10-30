# -*- coding: utf-8 -*-

import numpy as np
import parsertools
import common

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import Excalibur.Plotting.utility.colors as colors
import parsertools


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
		for quantity, bins in zip(*parsertools.get_list_slice([common.data_quantities, [common.unfbins[i] for i in common.data_quantities]], known_args.no_quantities)):
			for variation in common.variations:  # for sys uncert estimation
				datasuffix = ""
				if (("bkgr" not in variation) and (variation != "")):
					datasuffix = variation
				mc_scalefactor = -1 + (-0.5*(variation=="_bkgrdown")) + (0.5*(variation=="_bkgrup"))  # for bkgr estimation
				folder = "leptoncuts" if (quantity == 'zpt') else "zcuts"
				d = {
					#input
					'x_expressions': common.root_quantity(quantity),
					'x_bins': [bins],
					'files': [path+'/work/data_ee{}.root'.format(datasuffix)] + [path+'/work/background_ee_{}.root'.format(item) for item in backgrounds],
					'nicks': ['data'],
					'weights': ["({})".format(ybin)] + ["{scalefactor}*(hlt&&({ybin}))".format(ybin=ybin, scalefactor=mc_scalefactor)]*len(backgrounds),
					'folders': ['{}_ak5PFJetsCHSL1L2L3Res/ntuple'.format(folder)] + ['{}_ak5PFJetsCHSL1L2L3/ntuple'.format(folder)]*len(backgrounds),
					#output
					'plot_modules': ['ExportRoot'],
					'filename': quantity + "_" + ybinsuffix + variation,
					'output_dir': common.subtract_dir,
					'export_json': False,
				}
				plots.append(d)
	return [PlottingJob(plots, args)]


def unfold(args=None):
	"""Unfold Z(->ee) distributions and save as root. All combinations of n jet categories, rapidity bins, MC samples and quantities (y, mass, pT) are plotted."""

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])

	# some variables
	path = common.bkgr_path
	max_iterations = 4

	plots = []
	for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels,
	], known_args.no_ybins)):
		for mc_label, mc in zip(*parsertools.get_list_slice([
			['Madgraph', 'Powheg'],
			['mc_ee.root', 'mc_ee_powheg.root']
		], known_args.no_mcs)):
			for quantity in parsertools.get_list_slice([common.data_quantities], known_args.no_quantities)[0]:
				for iteration in parsertools.get_list_slice([range(1, 1+max_iterations)], known_args.no_iterations)[0]:
					for variation in common.variations + common.unfolding_variations:
						if variation == '_unfdown':
							unfolding_variation = -1
							input_var = ""
						elif variation == '_unfup':
							unfolding_variation = 1
							input_var = ""
						else:
							unfolding_variation = 0
							input_var = variation
						if quantity == 'zpt':
							folder = 'leptoncuts'
						else:
							folder = 'zcuts'
						bins = common.unfbins[quantity]
						d = {
							'x_expressions': ['data']+[common.root_quantity(quantity).replace("z", "genz"), common.root_quantity(quantity), common.root_quantity(quantity).replace("z", "genz")],
							'y_expressions': [None, common.root_quantity(quantity), None, None],
							'files': ["1_background-subtracted/" + quantity + "_" + ybinsuffix + input_var + ".root"]+[path + "/work/" + mc]*3,
							'nicks': [
								'data_reco',
								'responsematrix',
								'mc_reco',
								'mc_gen',
							],
							'lumis': [common.lumi],
							'folders': ['']+['{}_ak5PFJetsCHSL1L2L3/ntuple'.format(folder)]*3,
							'weights': "weight*({0}&&hlt)".format(ybin),
							'x_bins': [bins],
							'y_bins': [None, bins, None, None],
							# analysis
							'analysis_modules': ['Unfolding'],
							'unfolding': ['data_reco', 'mc_reco'],
							'unfolding_responsematrix': 'responsematrix',
							'unfolding_mc_gen': 'mc_gen',
							'unfolding_mc_reco': 'mc_reco',
							'unfolding_new_nicks': ['data_unfolded', 'mc_unfolded'],
							'unfolding_iterations': iteration,
							'unfolding_variation': unfolding_variation,
							'libRooUnfold': '~/home/RooUnfold/libRooUnfold.so',
							#output
							'plot_modules': ['ExportRoot'],
							'filename': "_".join([quantity, mc_label.lower(), ybinsuffix]) + variation + "_" + str(iteration),
							'output_dir': common.unfold_path,
							'export_json': False,
						}
						plots.append(d)
	return [PlottingJob(plots, args)]


def zee_divide(args=None):
	"""Divide unfolded Zee data by lumi and bin width"""

	known_args, args = parsertools.parser_list_tool(args, ['ybins', 'quantities'])

	plots = []
	for quantity in common.data_quantities:
		for ybin, ybinsuffix in zip(*parsertools.get_list_slice([
				["1"] + common.ybin_weights,
				["inclusive"] + common.ybin_labels
	], known_args.no_ybins)):
			for variation in common.variations+common.unfolding_variations:
				filename = '{}_madgraph_{}_{}'.format(quantity, ybinsuffix+variation, common.iterations_to_use)
				d = {
					'files': [common.unfold_path + '/' + filename + '.root'],
					'folders': [""],
					'x_expressions': ['data_unfolded'],
					'scale_factors': 1./(1e3*common.lumi),

					'analysis_modules': ['NormalizeByBinWidth'],

					'plot_modules': ['ExportRoot'],
					'output_dir': common.divided_path,
					'filename': filename,
					'export_json': False,
				}
				plots.append(d)
	return [PlottingJob(plots, args)]
