#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.colors import histo_colors
from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def branching_ratio(args=None, additional_dictionary=None):
	""" Z boson decay channels branching ratio"""
	d = {
		"input_modules": ["InputInteractive"],
		"x_expressions": ["0.5 2"] + ["3.5"]*3,
		"y_expressions": ["69.91 20", "10.09", "6.73", "3.37"],
		"y_errors": ["0.06 0.06"]+["0.01"]*3,
		#formatting
		"markers": ["fill"],
		"colors": [histo_colors[color] for color in ['blue', 'yellow', 'green', 'brown']],
		"labels": [None] + ['$e^+e^-$', r'$\\mu^+\\mu^-$', r'$\\tau^+\\tau^-$'],
		"legend": "center right",
		"x_bins": ["0 1 1.5 2.5 3 4"],
		"x_label": "Decay channel",
		"x_lims": [-0.5, 4.5],
		"x_ticks": [0.5, 2, 3.5],
		"x_tick_labels": ["Hadrons", r"Neutrinos", "Charged leptons"],
		"y_label": "Branching ratio / %",
		"y_lims": [0, 100],
		"filename": "branching",
	}
	return [PlottingJob([d], args)]
