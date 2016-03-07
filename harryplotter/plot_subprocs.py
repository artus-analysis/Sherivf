# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.colors import histo_colors
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


def production_channels(args=None, additional_dictionary=None):
	""" Z+jet production channels"""
	n = 5
	d = {
		"input_modules": ["InputInteractive"],
		"x_expressions": [" ".join([str(0.5 + 1.5*i) for i in range(n)])],
		"y_expressions": ["60.54 20.25 8.15 7.58 3.47"],
		"y_errors": [None],
		"x_errors": [None],
		"legend": None,
		"grid": 'horizontal',
		#
		#'analysis_modules': ['Prime'],
		#formatting
		"markers": ["fill"],
		"colors": histo_colors['blue'],
		"x_bins": [" ".join([str(1.5*i) + " " + str(1 + 1.5*i) for i in range(n)])],
		"x_label": "\nProduction Channel",
		"x_lims": [-0.5, n + 2.5],
		"x_ticks": [0.5 + 1.5*i for i in range(n)],
		"x_tick_labels": ["$gq$", r"$q\\bar{q}$", r"$qq\\prime$", "$gg$", "$qq$"],
		"y_label": "Relative Contribution / %",
		"y_lims": [0, 100],
		"filename": "zjet_production-channels",
	}
	return [PlottingJob([d], args)]
