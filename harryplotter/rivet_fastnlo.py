#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
from itertools import combinations

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
from Excalibur.Plotting.utility.colors import histo_colors


def rivet_fastnlo(args=None):
	""" compare rivet with fastnlo and MC-gen"""

	plots = []
	# normalized or not:
	for title, norm_modules, y_label_suffix, filename_norm_suffix in zip(
		['', "shape comparison"],
		[[], ["NormalizeToUnity"]],
		['', " (normalized)"],
		['', '_normalizes'],
	):
		# pT or y:
		for quantity, x, xlabel, upper_limit in zip(['pT', 'y'], ["d01-x01-y01", "d02-x01-y01"], ['zpt', 'abs(zy)'], [100, 3]):
			# all combinations of the 
			for files, labels, filename_suffixes, paths, weights in zip(
				combinations([
					"/usr/users/dhaitz/home/qcd/sherivf/rivet-results/Rivet.root",
					"/usr/users/dhaitz/home/artus/Excalibur/plots/genz{0}.root".format(quantity.lower()),
					"/usr/users/dhaitz/home/qcd/sherivf/fnlo-results/fnlo_{0}Z.root".format(quantity)], 2),
				combinations(["Sherpa+Rivet", "Madgraph+Pythia", "Sherpa+fastNLO"], 2),
				combinations(["Riv", "MG", "Fnlo"], 2),
				combinations([x, '4', '0'], 2),
				combinations(['1', '19.789', '1'], 2)
			):
				d = {
					"analysis_modules": norm_modules + ["Ratio"],
					"files": files,
					"folders": [""],
					"labels": labels,
					"markers": ["o", "fill","o"],
					"filename": quantity + "_riv-" + "_".join(filename_suffixes) + filename_norm_suffix,
					"title": title,
					"scale_factors": weights,
					"x_expressions": paths,
					"x_label": xlabel,
					"x_lims": [0.0, upper_limit],
					"y_label": "Events" + y_label_suffix,
					"y_subplot_lims": [0.5, 1.5],
				}
				plots.append(d)
	harryinterface.harry_interface(plots, args)


def genz_root(args=None):
	base_root(
		"/storage/a/dhaitz/excalibur/mc_ee_corr.root",
		"genz",
		args
	)

def z_root(args=None):
	base_root(
		"/storage/a/dhaitz/excalibur/artus/data_ee_corr_2015-02-18_10-34/out.root",
		"z",
		args
	)

def base_root(rootfile, quantityprefix, args=None):
	""" Create the root files from data for the Sherpa-Madgraph comparison."""
	plots = []
	for quantity, binning in zip(["pt", "y"], ["10,0,100", "25,0,2.5"]):
		d = {
			"files": [rootfile],
			"plot_modules": ["ExportRoot"],
			"x_bins": [binning],
			"x_expressions": [quantityprefix + quantity],
			"folders": ["all_AK5PFJetsCHSL1L2L3"],
			"weights": [],
			"nicks": [],
		}
		for njets in range(5):
			d['weights'].append("({})".format(
				" && ".join(["epluspt>25", "eminuspt>25", "abs(epluseta)<2.5",
				"abs(eminuseta)<2.5", "zmass>81", "zmass<101", "njets30<={0}".format(njets)])
			))
			d["nicks"].append(str(njets))

		plots.append(d)
	harryinterface.harry_interface(plots, args)


def rivet(args=None, additional_dictionary=None):
	"""Compare Rivet (YODA) output to (unfolded) Data and MC, different quantities, with/without normalization."""

	rootfile = '/usr/users/dhaitz/home/qcd/sherivf/unfolded/{0}_unfolded_Madgraph_inclusive.root'
	yodafile = '/storage/a/dhaitz/sherivf/sg_2015-06-23_13-42/Rivet.yoda'
	if '--yoda-files' in args:
		yodafile = args[args.index('--yoda-files')+1]
	# YODA files add when merging so we have to rescale according to the number of contributions
	n_yodacontributions = len(glob.glob(os.path.dirname(yodafile)+"/output/Rivet*.yoda"))

	plots=[]
	for mc in [True, False]:
		for norm in [False]:
			for index, (quantity, binning, label) in enumerate(zip(
					['zpt', 'abs(zy)', 'zmass', 'zphi'][:3],
					['37,30,400', '25,0,2.5', '20,81,101', 'phi'][:3],
					['zpt', 'abs(zy)', 'zmass', 'zphi'][:3]
			)):
				d = {
					'input_modules': ['InputRootZJet', 'InputYoda'],
					'analysis_modules': ['ScaleHistograms']+(['NormalizeToFirstHisto'] if norm else []) +['Ratio'],

					'yoda_files': [yodafile],  # override from command line
					'files': [rootfile.format(quantity)],
					'folders': [""],
					'nicks': 'root',
					'x_expressions': [('MC_unfolded' if mc else 'Data_unfolded')],
					'x_bins': binning,
					'scale_factors': [1./19789.],

					'ratio_numerator_nicks': ['root'],
					'ratio_denominator_nicks': ['MCgrid_CMS_2015_Zeed0{0}-x01-y01'.format(str(index+1))],

					'scale': (1./n_yodacontributions * (1 if quantity == 'abs(zy)' else 1)),
					'scale_nicks': ['MCgrid_CMS_2015_Zeed0{0}-x01-y01'.format(str(index+1))],

					'nicks_whitelist': ['root', 'd0{0}'.format(str(index+1))],
					'y_subplot_lims': [0.5, 1.5],
					'title': ("Shape comparison" if norm else ""),
					'labels': [('Madgraph' if mc else 'Data'), '_noLabel', 'Sherpa+Rivet'],
					'colors': [('red' if mc else 'black')]*2 + [histo_colors['blue']],
					'energies': [8],
					'x_label': label,
					'y_label': r'$\\sigma$ / pb' + ("" if quantity in ['abs(zy)', 'zy', 'zphi'] else " $GeV^{-1}$"),

					'filename': ('madgraph' if mc else 'data')+'-vs-sherpa_'+('shape_' if norm else '')+quantity,

				}
				if quantity == 'zpt':
					d['x_lims'] = [30, 400]
					d['y_lims'] = [0.001, 21]
					d['y_log'] = True
				elif quantity == 'zy' or quantity == 'zphi':
					d['legend'] = "lower center"
				plots.append(d)
	harryinterface.harry_interface(plots, args)


def fastnlo_pdfsets(args=None, additional_dictionary=None):
	""" study fastnlo tables for different PDF sets"""
	plots = []
	bindict = {
			'zmass': ['20,81,101'],
			'abs(zy)': ['25,0,2.5'],
			'zpt': ['37,30,400'],
			'zphi': ['20,-3.14159,3.14159'],
	}
	qdict = {'pT': 'zpt', 'y': 'abs(zy)', 'm': 'zmass', 'phi': 'zphi'}

	scale = True

	# configure fastNLO input
	n_members = 1
	pdf_sets = ['CT10nlo.LHgrid', 'NNPDF21_100.LHgrid', 'abm11_3n_nlo.LHgrid',
		'cteq65.LHgrid', 'MSTW2008nnlo90cl.LHgrid']
	labels = ['CT10', 'NNPDF', 'ABM11', 'CTEQ6', 'MSTW']
	colors = ['blue', 'red', 'green', 'purple', 'orange']
	N = len(pdf_sets)

	for quantity, sf in zip(['y', 'm', 'pT', 'phi'], [2*i for i in [0.1, 1, 10, 0.314159]]):
		d = {
			'input_modules': 'InputFastNLO',
			'pdf_sets': pdf_sets,
			'members': len(pdf_sets),
			#'labels': ['Different PDF Sets'.format(N-1)] + [None]*(N-1),
			'labels': labels,
			'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.txt".format(quantity)],
			'legend': 'upper right',
			'markers': ['-',]*N,
			'line_styles': ['-']*N,
			'colors': colors,
			'energies': [8],
			'filename': ("scale_" if scale else "")+"fastnlo_"+qdict[quantity],
		}
		if quantity == 'pT':
			d['y_log'] = True
	
		# add comparison with unfolded data / MC
		rootfile = '/usr/users/dhaitz/home/qcd/sherivf/unfolded/{0}_unfolded_Madgraph_inclusive.root'
		mc = False

		# nicks (for scaling)
		nicks = []
		for pdf_set in pdf_sets:
			nicks.append("_".join([d['fastnlo_files'][0], pdf_set, str(n)]))

		d.update({
			'input_modules': ['InputRootZJet', 'InputFastNLO'],
			'files': [rootfile.format(qdict[quantity])],
			'x_bins': bindict[qdict[quantity]],
			'folders': [""],
			'x_expressions': [('MC_unfolded' if mc else 'Data_unfolded')],
			'labels': ['Data'] + d['labels'],
			'colors': ['black'] + d['colors'],
			'line_styles': [None] + d['line_styles'],
			'markers': ['o'] + d['markers'],
			'x_label': qdict[quantity],
			'analysis_modules':['ScaleHistograms'],
			'scale_factors': [1./19789.],
			'scale_nicks': nicks,
			'scale': (sf if scale else 1.)/1000.,
			'y_label': r'$\\sigma$ / pb' + ("" if quantity == 'y' else " $GeV^{-1}$"),
			'texts': [("fastNLO scaled by factor {0}".format(str(sf)) if scale else "")],
		})
		if quantity == 'pT':
			d['y_lims'] = [0.001, 30]
			d['legend'] = 'lower left'
		elif quantity == 'y':
			d['legend'] = 'lower left'

		# ratio
		if scale:
			d['analysis_modules'].append('Ratio')
			d['markers'] += ['-']*N
			d['line_styles'] += ['-']*N
			d['colors'] += colors
			d.update({
				'ratio_numerator_nicks': nicks,
				'ratio_denominator_nicks': ['nick0'],
				'y_subplot_lims': [0, 2],
				'y_subplot_label': 'Ratio MC/Data',
				
			})
			
		plots.append(d)

	harryinterface.harry_interface(plots, args)


def fastnlo_pdfmember(args=None, additional_dictionary=None):
	"""Evaluate fastNLO table for n members of a PDF set."""
	plots = []

	n_members = 100

	for quantity in ['y', 'm', 'pT', 'phi']:
		d = {
			'input_modules': 'InputFastNLO',
			'pdf_sets': ['NNPDF21_100.LHgrid'],
			'members': range(n_members),
			'fastnlo_files': ["latest_sherivf_output/fnlo_{0}Z.txt".format(quantity)],

			'legend': None,
			'markers': ['-',],
			'line_styles': ['-'],
			'line_widths': [0.1],
			'colors': ['blue'],
			'energies': [8],

			'filename': quantity,
		}
		if quantity == 'pT':
			d['y_log'] = True
		plots.append(d)

	harryinterface.harry_interface(plots, args)


def sherpa_gens(args=None, additional_dictionary=None):
	"""Comparisons for Sherpa and Madgraph,Powheg Gen."""
	plots = []

	normalize = False
	for normalize in [True, False]:
		for index, quantity, binning, label in zip(
			[0,1,2,3,6,7],
			["genzpt", "abs(genzy)", "genzmass", "genzphi", "geneminuspt", "geneminuseta"],
			["37,30,400", "25,0,2.5", "20,81,101", "12,-3,3", "40,0,200", "60,-3,3"],
			["xsecpt", "xsecabsy", "xsecm", "xsecphi", "xsecpt", "xseceta"],
		):
			d = {
				#"yoda_files": ["/storage/a/dhaitz/sherivf/sg_2015-08-03_11-40/Rivet.yoda"],
				"yoda_files": ["/storage/a/dhaitz/sherivf/sg_2015-08-03_15-25/output/Rivet_1.yoda"],

				#"weights": ["(genepluspt>25&&geneminuspt>25&&((geneminuseta>-2.4&&geneminuseta<-1.566)||(geneminuseta>-1.442&&geneminuseta<1.442)||(geneminuseta>1.566&&geneminuseta<2.4))&&((genepluseta>-2.4&&genepluseta<-1.566)||(genepluseta>-1.442&&genepluseta<1.442)||(genepluseta>1.566&&genepluseta<2.4))&&genzmass>81&&genzmass<101&&genzpt>30)"],
				"weights": ["(genepluspt>0&&geneminuspt>0&&genzmass>81&&genzmass<101&&genzpt>0&&((geneminuseta>-2.4&&geneminuseta<-1.566)||(geneminuseta>-1.442&&geneminuseta<1.442)||(geneminuseta>1.566&&geneminuseta<2.4))&&((genepluseta>-2.4&&genepluseta<-1.566)||(genepluseta>-1.442&&genepluseta<1.442)||(genepluseta>1.566&&genepluseta<2.4)))"],
				"files": [
					os.environ['EXCALIBURPATH'] + '/work/mc_ee.root',
					os.environ['EXCALIBURPATH'] + '/work/mc_ee_powheg.root',
				],
				"nicks": ["madg", "powh"],
				"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
				"input_modules": ["InputRootZJet", "InputYoda"],
				'scale_factors': [1e-3], # MC: fb->pb
				"x_expressions": [quantity],
				"x_bins": [binning],

				"analysis_modules": ["ScaleHistograms"]
					+(["NormalizeToFirstHisto"] if normalize else [])
					+["Ratio"],
				'scale_nicks': ["MCgrid_CMS_2015_Zeed0{}-x01-y01".format(index+1)],
				'scale': 1./50., # contributions
				"ratio_numerator_nicks": ["MCgrid_CMS_2015_Zeed{:02d}-x01-y01".format(index+1)],
				"ratio_denominator_nicks": ["madg", "powh"],
				"ratio_result_nicks": ["ratio0", "ratio1"],

				"nicks_whitelist": ["d0"+str(index+1), "madg","powh", "ratio"],

				"y_label": label,
				"labels": ["Sherpa+Rivet", "Madgraph DYJets", "Powheg DY", "ratio", "ratio2"],
				"legend": "lower center",
				"marker_colors": ["black", "red", "black", "red"],
				"line_styles": [None, "-", "-", None, None],
				"step": [False, True, True, False, False],
				"markers": ["fill", ".", ".", ".", "."],
				"title": ("Shape comparison" if normalize else ""),
				"y_subplot_lims": [0.75, 1.25],
				"energies": [8],

				"filename": quantity + ("_norm" if normalize else ""),

			}
			if quantity == 'genzpt':
				d['y_log'] = True
				d['legend'] = 'upper right'
			elif quantity == 'genzmass' or quantity == 'geneminuseta':
				d['legend'] = None
			elif quantity == 'geneminuspt':
				d['legend'] = 'upper right'

			plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	rivet_fastnlo()
