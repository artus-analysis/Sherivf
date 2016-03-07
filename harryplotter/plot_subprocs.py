# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def subprocs(args=None, additional_dictionary=None):
	"""2D plot of subprocs (from fastnlo)"""
	flavs = 'duscb'
	allflavs = [r'$\\bar{{{0}}}$'.format(f) for f in flavs[::-1]] + ['$g$'] + [r"${0}$".format(f) for f in flavs]
	axlabel = "Relative Contribution"
	d = {
		# input
		"x_expressions": ["name"],
		"files": ["/usr/users/dhaitz/home/qcd/sherivf/fastnlo/MCgrid_CMS_2015_Zee/MCgrid_CMS_2015_Zee.str.root"],
		"folders": [""],
		# analysis
		"analysis_modules": ["NormalizeToUnity", "Subprocs"],
		# formatting
		"x_label": "Parton 1 Flavour",
		"y_label": "Parton 2 Flavour",
		"x_tick_labels": allflavs,
		"x_ticks": range(-5, 6),
		"y_tick_labels": allflavs,
		"y_ticks": range(-5, 6),
		"y_subplot_lims": [0, 0.5],
		"z_label": axlabel,
		"y_subplot_label": axlabel,
		"markers": ["o"],
		"z_lims": [0, 0.081],
		"subplot_grid": "horizontal",
		# output		
		"filename": "subprocs",
	}
	return [PlottingJob([d], args)]
