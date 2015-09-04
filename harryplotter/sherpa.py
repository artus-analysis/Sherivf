#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import Excalibur.Plotting.harryinterface as harryinterface
import parsertools
import common

def sherpa(args=None, additional_dictionary=None):
	"""Comparisons for Sherpa and Data,Madgraph(Powheg)"""
	plots = []

	known_args, args = parsertools.parser_list_tool(args, ['norm', 'quantities'])

	for normalize in parsertools.get_list_slice([[False, True]], known_args.no_norm)[0]:
		for index, quantity, binning in zip(*parsertools.get_list_slice([
			[0,1,2,3,6,7],
			["genzpt", "abs(genzy)", "genzmass", "genzphi", "geneminuspt", "geneminuseta"],
			["38,20,400", "25,0,2.5", "20,81,101", "32,-3.2,3.2", "20,20,120", "48,-2.4,2.4"],
		], known_args.no_quantities)):
			d = {
				# input
				"yoda_files": ["latest_sherivf_output/Rivet.yoda"],
				"files": [
					os.environ['EXCALIBURPATH'] + '/work/mc_ee.root',
					os.environ['EXCALIBURPATH'] + '/work/data_ee.root',
				],
				"nicks": ["madg", "data"],
				"folders": [
					"zcuts_ak5PFJetsCHSL1L2L3/ntuple",
					"zcuts_ak5PFJetsCHSL1L2L3Res/ntuple",
				],
				"input_modules": ["InputRootZJet", "InputYoda"],
				'scale_factors': [1./19712.], # MC: fb->pb
				"x_expressions": [quantity.replace("gen", "")],
				"x_bins": [binning],
				# analysis
				"analysis_modules": ["ScaleHistograms"]
					+(["NormalizeToFirstHisto"] if normalize else [])
					+["Ratio"],
					'scale_nicks': ["MCgrid_CMS_2015_Zeed0{}-x01-y01".format(index+1)],
					'scale': 1., # for test scaling
				"ratio_numerator_nicks": ["MCgrid_CMS_2015_Zeed{:02d}-x01-y01".format(index+1), "madg"],
				"ratio_denominator_nicks": ["data"],
				"ratio_result_nicks": ["ratio0", "ratio1"],
				# plotting
				"nicks_whitelist": ["data", "d0"+str(index+1), "madg","powh", "ratio"],
				"x_label": quantity.replace("gen", ""),
				"y_label": "xsec",
				"labels": [r"Data", "Sherpa", "Madgraph+Pythia", "ratio0", "ratio1"],
				"legend": "lower center",
				"marker_colors": ["black", "red", "red", "cornflowerblue"],
				"line_styles": [None, "-", None, None, None],
				"step": [True],
				"markers": [".", ".", "fill", ".", "."],
				"title": ("Shape comparison" if normalize else ""),
				"y_subplot_lims": [0.5, 1.5],
				"energies": [8],
				"y_errors": [True, False, True, False, False],
				# output
				"filename": quantity + ("_norm" if normalize else ""),
				'www_title': 'Data / Sherpa /Madgraph',
				'www_text': 'Comparison of Data, CMS-Madgraph(reco-level) and self-produced Sherpa. \
					Efficiency scale factors have been applied, but no unfolding has been performed.'
			}
			if quantity == 'genzpt':
				d['y_log'] = True
				d['legend'] = 'upper right'
				d['y_lims'] = [0.001, 900]
			elif quantity == 'genzmass' or quantity == 'geneminuseta':
				d['legend'] = None
			elif quantity == 'geneminuspt':
				d['legend'] = 'upper right'
			elif quantity == 'genzy':
				d['legend'] = 'upper right'

			plots.append(d)
	harryinterface.harry_interface(plots, args)


def sherpa_mc(args=None, additional_dictionary=None):
	"""Comparisons for Sherpa and Madgraph Gen"""
	known_args, args = parsertools.parser_list_tool(args, ['quantities'])
	plots = []

	for index, quantity in zip(*parsertools.get_list_slice([
		[0,1,2,3,6,7],
		["genzpt", "abs(genzy)", "genzmass", "genzphi", "geneminuspt", "geneminuseta"],
	], known_args.no_quantities)):
			d = {
				# input
				"yoda_files": ["latest_sherivf_output/Rivet.yoda"],
				"weights": ["({})".format("&&".join([
					"(ngenelectrons>1)",
					"(geneminuspt>25&&genepluspt>25)",
					"(abs(geneminuseta)<2.4&&abs(genepluseta)<2.4)",
					"(abs(geneminuseta)<1.442||abs(geneminuseta)>1.566)",
					"(abs(genepluseta)<1.442||abs(genepluseta)>1.566)",
					"(genzpt>20)",
					"(genzmass>81&&genzmass<101)",
				]))],
				"files": [
					os.environ['EXCALIBURPATH'] + '/work/mc_ee_gen.root',
				],
				"folders": [
					"nocuts_ak5PFJetsCHSL1L2L3/ntuple",
				],
				"input_modules": ["InputRootZJet", "InputYoda"],
				'scale_factors': [1./1000.],
				"x_expressions": [quantity],
				"x_bins": [common.bins[quantity.replace('gen', '')]],
				# analysis
				"analysis_modules": ["Ratio"],
				"ratio_numerator_nicks": ["MCgrid_CMS_2015_Zeed{:02d}-x01-y01".format(index+1)],
				"ratio_denominator_nicks": ["nick0"],
				# plotting
				"nicks_whitelist": ["nick", "d0"+str(index+1), "madg", "ratio"],
				"y_label": "xsec",
				"y_subplot_lims": [0.9, 1.1],
				"y_errors": [True, False, False],
				"labels": ['Madgraph', 'ratio', 'Sherpa'],
			}
			if quantity == 'genzpt':
				d['y_log'] = True
				d['legend'] = 'upper right'
				d['y_lims'] = [0.001, 900]
			elif quantity == 'genzmass' or quantity == 'geneminuseta':
				d['legend'] = None
			elif quantity == 'geneminuspt':
				d['legend'] = 'upper right'
			elif quantity == 'genzy':
				d['legend'] = 'upper right'
			plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	rivet_fastnlo()
