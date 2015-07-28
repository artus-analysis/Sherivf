#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface


def electron_hlt(args=None):
	"""   """
	plots = []
	harryinterface.harry_interface(plots, args)


def electron_id(args=None):
	"""   """
	plots = []
	harryinterface.harry_interface(plots, args)


def electron_corr(args=None):
	"""   """
	d = {
		"folders": ["nocuts_ak5PFJetsCHSL1L2L3/electrons"],
		"x_label": "eabseta",
		"y_label": "erecogen",
		"labels": ["corrected","raw"],
		"no_weight": True,
		"tree_draw_options": ["prof"],
		"weights": ["(genParticle.p4.Pt()>5&&genParticleMatched)"],
		"x_bins": ["12,0,2.4"],
		"x_expressions": ["abs(object.p4.Eta())"],
		"y_expressions": ["object.p4.Pt()/genParticle.p4.Pt()"],
		"y_lims": [0.5, 1.5],
		"lines": [1.],
		"filename": "electron_corr",
	}
	harryinterface.harry_interface([d], args)


def electron_corr_2(args=None):
	"""   from default ntuple"""
	d = {
		"folders": ["nocuts_ak5PFJetsCHSL1L2L3/ntuple"],
		#"x_label": "eabseta",
		#"y_label": "erecogen",
		"labels": ["corrected","raw"],
		#"no_weight": True,
		"tree_draw_options": ["prof"],
		"weights": ["(matchedgenelectron1pt>5)"],
		"x_bins": ["12,0,2.4"],
		"x_expressions": ["abs(e1eta)"],
		"y_expressions": ["e1pt/matchedgenelectron1pt"],
		"y_lims": [1.0, 1.2],
		"lines": [1.],
		"filename": "electron_corr_2",
	}
	harryinterface.harry_interface([d], args)



def z_corr(args=None):
	""" z mass vs y for corrected and uncorrected  """
	d = {
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"labels": ["corrected", "raw"],
		"tree_draw_options": ["prof"],
		"x_bins": ["5,0,2.5"],
		"x_expressions": ["abs(zy)"],
		"y_expressions": ["zmass"],
		"y_lims": [90.0, 94.0],
		"markers": ['.', 'o'],
		"filename": "z_corr",
	}
	harryinterface.harry_interface([d], args)



