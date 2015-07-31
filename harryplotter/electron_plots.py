#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface


def z_hlt(args=None, additional_dictionary=None):
	""" HLT efficiency vs Z pT, y  """
	plots = []
	ybins = [30, 40, 50, 70, 100, 200, 400]
	d = {
		"files": ["work/mc_ee.root"],
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"tree_draw_options": ["prof"],
		"x_bins": ["12,0,2.4"],
		"x_expressions": ["abs(zy)"],
		"y_bins": [" ".join([str(item) for item in ybins])],

		"y_ticks": ybins,
		"y_expressions": ["zpt"],
		"y_lims": [ybins[0], ybins[-1]],
		"y_log": True,
		"z_expressions": ["hlt"],
		"z_label": "HLT Efficiency",
	}
	plots.append(d)

	d2 = {
		#"files": ["work/mc_ee.root"],
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"line_styles": ["-"],
		"tree_draw_options": ["prof"],
		"weights": ["abs(zy)<0.5",
			"(abs(zy)>0.5&&abs(zy)<1)",
			"(abs(zy)>1&&abs(zy)<1.5)",
			"(abs(zy)>1.5&&abs(zy)<2)",
			"(abs(zy)>2&&abs(zy)<2.5)"
		],
		"x_bins": ["30 40 50 70 100"],
		"x_expressions": ["zpt"],
		"y_expressions": ["hlt"]
	}
	plots.append(d2)

	if additional_dictionary is not None:
		for d in plots:
			d.update(additional_dictionary)
	harryinterface.harry_interface(plots, args)


def electron_id(args=None, additional_dictionary=None):
	"""   """
	plots = []
	ids = ["e1mvanontrig", "e1mvatrig", "e1looseid", "e1looseid95", "e1mediumid", "e1mediumid95", "e1tightid", "e1tightid95"]
	labels = ['MVA(Non-Trig)', 'MVA(Trig)', 'Loose', 'Loose(95)', 'Medium', 'Medium(95)', 'Tight', 'Tight(95)']
	d = {
		"files": ["work/mc_ee.root"],
		#"folders": ["zcuts_ak5PFJetsCHSL1L2L3/electrons"],
		#"x_expressions": ["object.p4.Pt()"],
		#"y_expressions": ["object.id{}()".format(ID) for ID in ids],
		#"weights": ["genParticleMatched"],
		#"no_weight": True,
		
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"y_expressions": ids,
		"x_expressions": ["e1pt"],
		"tree_draw_options": ["prof"],
		"x_bins": ["20,25,125"],

		"y_label": "ID Efficiency",
		"x_label": "e1pt",
		"y_lims": [0, 1],
		#"plot_modules": ['PlotMplZJet', 'PlotMplRectangle'],
		#"rectangle_x": [0, 25],
		"legend": "lower right",
		"labels": labels,
		
		"filename": "electron_IDs",
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	plots.append(d)
	d = dict(d)
	d.update({
		"x_expressions": ["abs(e1eta)"],
		"x_label": "e1abseta",
		"y_expressions": ["e1pt"],
		"y_bins": ["20,25,125"],
		"x_bins": ["24,0,2.4"],
		"y_lims": [25, 125],
		"z_lims": [0, 1],
	})
	for ID, label in zip(ids, labels):
		d = dict(d)
		d["z_expressions"] = [ID]
		d["filename"] = ID
		d['z_label'] = label + " ID Efficiency"
		d['y_label'] = "e1pt"
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	harryinterface.harry_interface(plots, args)


def electron_corr(args=None, additional_dictionary=None):
	"""pT Reco/Gen for corrected/raw electrons as a function of electron |eta|"""
	d = {
		# Input
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/electrons"],
		"no_weight": True,
		"tree_draw_options": ["prof"],
		"weights": ["(genParticleMatched)"],
		"x_bins": ["12,0,2.4"],
		"x_expressions": ["abs(object.p4.Eta())"],
		"y_expressions": ["object.p4.Pt()/genParticle.p4.Pt()"],
		# Formatting
		"x_label": "eabseta",
		"y_label": "erecogen",
		"labels": ["corrected","raw"],
		"y_lims": [0.97, 1.03],
		"line_styles": ["-"],
		"lines": [1.],
		"colors": ['red', 'black'],
		"markers": ['o', '.'],
		"legend": "upper left",
		# Output
		"filename": "electron_corr",
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	harryinterface.harry_interface([d], args)


def z_corr(args=None, additional_dictionary=None):
	"""Z mass as a function of |y| for corrected and uncorrected"""
	d = {
		# Input
		"folders": ["zcuts_ak5PFJetsCHSL1L2L3/ntuple"],
		"tree_draw_options": ["prof"],
		"x_expressions": ["abs(zy)"],
		"x_bins": ["10,0,2.5"],
		"y_expressions": ["zmass"],
		# Formatting
		"labels": ["corrected", "raw"],
		"y_lims": [90.0, 94.0],
		"markers": ['o', '.'],
		"line_styles": ["-"],
		"colors": ['red', 'black'],
		# Output
		"filename": "z_corr",
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	harryinterface.harry_interface([d], args)


def electron_all(args=None):

	d = {'files': ['work/mc_ee.root', 'work/mc_ee_raw.root']}

	electron_corr(args, d)
	electron_id(args, d)
	z_corr(args, d)
	z_hlt(args, d)

