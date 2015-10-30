#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import parsertools
import common

def sherpa(args=None, additional_dictionary=None):
	"""Comparisons for Sherpa and Data,Madgraph(Powheg)"""
	plots = []

	known_args, args = parsertools.parser_list_tool(args, ['norm', 'quantities'])

	for normalize in parsertools.get_list_slice([[True, False]], known_args.no_norm)[0]:
		for quantity in parsertools.get_list_slice([["zpt", "abszy",
			"zmass", "zphi",
			"eminuspt", "eminuseta"]], known_args.no_quantities)[0]:
			try:
				factor = (float(common.bins[quantity].split(',')[2])-float(common.bins[quantity].split(',')[1])) / float(common.bins[quantity].split(',')[0])
			except IndexError:
				factor = 1.
			d = {
				# input
				"files": [
					"latest_sherivf_output/Rivet.root",
					os.environ['EXCALIBURPATH'] + '/work/mc_ee.root',
					os.environ['EXCALIBURPATH'] + '/work/data_ee.root',
				],
				"nicks": ["sherpa", "madg", "data"],
				"folders": [
					"",
					"zcuts_ak5PFJetsCHSL1L2L3/ntuple",
					"zcuts_ak5PFJetsCHSL1L2L3Res/ntuple",
				],
				'weights': ['1', 'weight', 'weight'],
				'scale_factors': [factor] +[1e-3/common.lumi]*2,  # fb->pb
				"x_expressions": [quantity] + [common.root_quantity(quantity)]*2,
				"x_bins": [None]+[common.bins[quantity]]*2,
				# analysis
				"analysis_modules": (["NormalizeToFirstHisto"] if normalize else [])+["Ratio"],
				#"scale_factors":[1.] + ,
				"ratio_numerator_nicks": ["sherpa", "madg"],
				"ratio_denominator_nicks": ["data"],
				"ratio_result_nicks": ['ratio0', 'ratio1'],
				# plotting
				"nicks_whitelist": ['data', 'mad', 'sherpa', 'ratio'],
				"x_label": quantity,
				"y_label": "xsec",
				"labels": ["Data", "Madgraph+Pythia", "Sherpa",  "ratio0", "ratio1"],
				#"legend": "lower center",
				"marker_colors": ["black", "red", "red", "cornflowerblue"],
				"line_styles": [None, "-", None, None, None],
				"step": [True],
				"markers": [".", ".", "fill", ".", "."],
				"title": ("Shape comparison" if normalize else ""),
				"y_subplot_lims": [0.5, 1.5],
				"energies": [8],
				"y_errors": [False, False, False, False, False],
				# output
				"filename": ("norm_" if normalize else "") + quantity,
				'www_title': 'Data / Sherpa /Madgraph',
				'www_text': 'Comparison of Data, CMS-Madgraph(reco-level) and self-produced Sherpa. \
					Efficiency scale factors have been applied, but no unfolding has been performed.'
			}
			if quantity == 'zpt':
				d['y_log'] = True
				d['legend'] = 'upper right'
				d['y_lims'] = [0.001, 90]
			elif quantity == 'zmass' or quantity == 'eminuseta':
				d['legend'] = None
			elif quantity == 'eminuspt':
				d['legend'] = 'upper right'
			elif quantity == 'abszy':
				d['legend'] = 'upper right'
			limdict = {
				"abszy": 4.5,
				"zmass": 30,
				"zphi": 4,
				"eminuspt": 10,
				"eminuseta": 2.5,
			}
			if quantity in limdict:
				d['y_lims'] = [0, limdict[quantity]]

			plots.append(d)
	return [PlottingJob(plots, args)]


def sherpa_mc(args=None, additional_dictionary=None):
	"""Comparisons for Sherpa and Madgraph Gen"""
	known_args, args = parsertools.parser_list_tool(args, ['quantities'])
	plots = []

	for quantity in parsertools.get_list_slice(["zpt", "abs(genzy)",
		"genzmass", "genzphi", "geneminuspt", "geneminuseta"], known_args.no_quantities):
		minzpt = common.lims('zpt')[0]
		d = {
			# input
			#"yoda_files": ["latest_sherivf_output/Rivet.yoda"],
			"weights": ["1", "({})".format("&&".join([
				"(ngenelectrons>1)",
				"(geneminuspt>25&&genepluspt>25)",
				"(abs(geneminuseta)<2.4&&abs(genepluseta)<2.4)",
				"(abs(geneminuseta)<1.442||abs(geneminuseta)>1.566)",
				"(abs(genepluseta)<1.442||abs(genepluseta)>1.566)",
				"(genzpt>{})".format(minzpt),
				"(genzmass>81&&genzmass<101)",
			]))],
			"files": [
				os.environ['SHERIVFDIR'] + "/latest_sherivf_output/Rivet.root",
				os.environ['EXCALIBURPATH'] + '/work/mc_ee_gen.root',
			],
			"folders": [
				"",
				"nocuts_ak5PFJetsCHSL1L2L3/ntuple",
			],
			#"input_modules": ["InputRootZJet", "InputYoda"],
			'scale_factors': [1, 1./1000.],
			"x_expressions": [quantity.replace('gen', '').replace('(', '').replace(')', ''), common.root_quantity(quantity)],
			"x_bins": [None, common.bins[quantity.replace('gen', '')]],
			# analysis
			"analysis_modules": ["Ratio"],
			#"ratio_numerator_nicks": [quantity.replace('gen', '')],
			#"ratio_denominator_nicks": ["nick0"],
			# plotting
			#"nicks_whitelist": ["nick", quantity.replace('gen', ''), "madg", "ratio"],
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
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	rivet_fastnlo()
