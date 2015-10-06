# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def electron_scale_sigma(args=None, additional_dictionary=None):
	"""Sigma for pT reco/pT gen of electron in bins of eta,pT"""
	d = {
		# input
		"files": ["work/mc_ee.root"],
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"x_bins": ["20 30 40 50 200"],  # binning same as scale factors
		"x_expressions": ["eminuspt"],
		"y_bins": ["0 0.8 1.4442 1.566 2 2.5"],  # binning same as scale factors
		"y_expressions": ["abs(eminuseta)"],
		"z_expressions": ["(eminuspt/geneminuspt)"],
		"tree_draw_options": ["profs"],  # profS to get sigma, not sigma/sqrt(N)
		"nicks": ["mc"],
		# analysis
		"analysis_modules": ["StatisticalErrors"],
		"stat_error_nicks": ["mc"],
		"stat_error_relative": True,
		# output
		"filename": "sigma_pt",
		"plot_modules": ["ExportRoot"],
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	return [PlottingJob([d], args)]
