#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import Artus.HarryPlotter.harry as harry
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common

def z_hlt(args=None, additional_dictionary=None):
	""" HLT efficiency vs Z pT, y  """
	plots = []
	ybins = [0, 1.5, 2.5]
	ptbins = [25, 30, 35, 40, 45, 50, 200]
	ptbins_str = " ".join([str(item) for item in ptbins])

	border = "1.5"
	etabins = {
		'BB': "abs(e1eta)<{}&&abs(e2eta)<{}".format(border, border),
		'BE': "abs(e1eta)<{}&&abs(e2eta)>{}".format(border, border),
		'EB': "abs(e1eta)>{}&&abs(e2eta)<{}".format(border, border),
		'EE': "abs(e1eta)>{}&&abs(e2eta)>{}".format(border, border),
	}

	for index, etabin in enumerate(etabins.keys()):
		d = {
			"files": [common.mc],
			"folders": ["zcuts_{}/ntuple".format(common.algocorr)],
			"tree_draw_options": ["prof"],
			"x_expressions": ["e1pt"],
			"y_expressions": ["e2pt"],
			"z_expressions": ["hlt"],
			"y_bins": [ptbins_str],
			"x_bins": [ptbins_str],
			"z_label": "HLT Efficiency",
			"weights": etabins[etabin],
			
			'z_lims': [0.9, 1],
			'y_log': True,
			'x_log': True,
			'x_lims': [ptbins[0], ptbins[-1]],
			'y_lims': [ptbins[0], ptbins[-1]],
			
			"filename": "hlt_{}".format(etabin),
		}
		export = True
		if export:
			d.update({
				#'filename': 'hlt',
				'nicks': [etabin],
				'plot_modules': ['ExportRoot'],
				'file_mode': ('RECREATE' if index>-10 else 'UPDATE'),
			})
			
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)

	return [PlottingJob(plots, args)]


def electron_id(args=None, additional_dictionary=None):
	"""ID efficiency for the different IDs"""
	plots = []
	ids = ["e1mvanontrig", "e1mvatrig", "e1looseid", "e1looseid95", "e1mediumid", "e1mediumid95", "e1tightid", "e1tightid95"]
	labels = ['MVA(Non-Trig)', 'MVA(Trig)', 'Loose', 'Loose(95)', 'Medium', 'Medium(95)', 'Tight', 'Tight(95)']
	d = {
		"files": [common.mc],
		#"folders": ["zcuts_{}/electrons".format(common.algocorr)],
		#"x_expressions": ["object.p4.Pt()"],
		#"y_expressions": ["object.id{}()".format(ID) for ID in ids],
		#"weights": ["genParticleMatched"],
		#"no_weight": True,
		
		"folders": ["zcuts_{}/ntuple".format(common.algocorr)],
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
	return [PlottingJob(plots, args)]


def electron_corr(args=None, additional_dictionary=None):
	"""Effects of electron momentum corrections"""
	# pT Reco/Gen for corrected/raw electrons as a function of electron |eta|
	plots = []
	etabin_list = [(0, 1), (1, 1.5), (1.5, 2.5)]
	etaweights = ["(abs(object.p4.Eta())>{}&&abs(object.p4.Eta())<{})".format(*etabins) for etabins in etabin_list]

	xdict = {
		"eta": "eabseta",
		"pt": "ept",
	}
	bindict = {
		"eta": ["12,0,2.4"],
		"pt": ["10,25,125"],
	}
	rootdict = {
		"eta": "abs(object.p4.Eta())",
		"pt": "object.p4.Pt()",
	}
	labeldict = {
		0: "",
	}
	for index, bins in enumerate(etabin_list):
		labeldict[index+1] = r"${}<|\\mathit{{\\eta}}_{{Electron}}|<{}$".format(*bins)

	for xquantity in ["eta", "pt"]:
		for index, etaweight in enumerate(['1']+etaweights):
			if xquantity == 'eta' and etaweight != '1':
				continue
			text = etaweight
			plots.append({
				# Input
				"files": [common.mc, common.mc_raw],
				"folders": ["zcuts_{}/electrons".format(common.algocorr)],
				"no_weight": True,
				"tree_draw_options": ["prof"],
				"weights": ["(genParticleMatched&&{})".format(etaweight)],
				"x_bins": bindict[xquantity],
				"x_expressions": [rootdict[xquantity]],
				"y_expressions": ["object.p4.Pt()/genParticle.p4.Pt()"],
				# Formatting
				"x_label": xdict[xquantity],
				"y_label": "erecogen",
				"labels": ["corrected","raw"],
				"y_lims": [0.985, 1.03],
				"texts": [labeldict[index]],
				"line_styles": ["-"],
				"lines": [1.],
				"colors": ['red', 'black'],
				"markers": ['o', '.'],
				"legend": ("upper left" if xquantity == 'eta' else "upper right"),
				# Output
				"filename": "electron_corr_"+xquantity+"_"+str(index),
			})
	# Z mass as a function of |y| for corrected and uncorrected
	plots.append({
		# Input
		"files": [common.mc, common.mc_raw],
		"folders": ["zcuts_{}/ntuple".format(common.algocorr)],
		"tree_draw_options": ["prof"],
		"x_expressions": ["abs(zy)"],
		"x_bins": ["10,0,2.5"],
		"y_expressions": ["zmass"],
		# Formatting
		"labels": ["corrected", "raw"],
		"y_lims": [90.4, 93.0],
		"markers": ['o', '.'],
		"line_styles": ["-"],
		"lines": [91.19],
		"colors": ['red', 'black'],
		"legend": "upper left",
		# Output
		"filename": "z_corr",
	})
	for plot in plots:
		plot.update({
			"www_title": "Electron momentum corrections",
			"www_text": "Difference between raw and corrected electrons for reconstructed electron pT and Z mass",
		})
		if additional_dictionary is not None:
			plot.update(additional_dictionary)
	return [PlottingJob(plots, args)]


def electron_trigger_sf(args=None, additional_dictionary=None):
	"""electron trigger scale factors"""
	plots = []
	for typ in ['Data', 'MC']:
		for ID in ['Tight', 'Medium', 'Loose', 'Veto']:
			d = {
				# input
				"files": [common.excaliburpath + "/data/electron_scalefactors//Electron-{}ScaleFactors.root".format(typ)],
				"folders": [""],
				# plotting
				"plot_modules": ["PlotMplZJet", "PlotMplRectangle"],
				"rectangle_color": ["red", "red"],
				"rectangle_x": [
					10.0,
					25.0,
					25.0,
					50.0
				],
				"rectangle_y": [
					0.0,
					2.5,
					1.442,
					1.566
				],
				"rectangle_hatch": [
					'\\'
					'\\'
				],
				"x_expressions": ["vbft95_"+ID.lower()],
				"x_label": "ept",
				"x_lims": [10.0, 50.0],
				"y_label": "eabseta",
				"z_label": "Trigger+ID Efficiency Scale Factors",
				"z_lims": [1, 2],
				"title": ID + " ID in " + typ,
				# output
				"filename": "_".join(['sf', typ.lower(), ID.lower()]),
				'www_text': 'Electron POG scale-factors for loose/medium/tight ID for Data and MC. Red hatched areas are excluded by event selection.',
				'www_title': 'Electron Scale Factors',
			}
			if additional_dictionary is not None:
				d.update(additional_dictionary)
			plots.append(d)
	return [PlottingJob(plots, args)]


def electron_scale_unc(args=None, additional_dictionary=None):
	"""Scale uncertainty for pT reco/pT gen of electron in bins of eta,pT"""
	d = {
		# input
		"files": [common.excaliburpath+"/data/electron_scalefactors/ElectronPtVariation.root"],
		"folders": [""],
		"x_expressions": ["mc"],
		# formatting
		"y_label": "abs(eeta)",
		"scale_factors": [100],
		"x_label": "ept",
		"x_log": True,
		"z_label": r"Electron $\\mathit{p}_T$ Scale Uncertainty / %",
		"x_ticks": [5, 10, 20, 50, 100, 200],
		# output
		"filename": "electron_pt_scalefactors",
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	return [PlottingJob([d], args)]


ids = ['Loose', 'Medium', 'Tight', 'None']

def electron_efficiencies_2d(args=None, additional_dictionary=None):
	""""2D Plots (eta, pT) for the efficiencies determined with the Egamma TnP package"""
	plots = []
	for ID in ids:
		for step, label in zip(['SCToGsfElectron', 'GsfElectronToId', "WP{}ToHLT".format(ID)],
								['Reconstruction', 'ID', 'HLT']):
			for datamc in ['data', 'mc']:
				d = {
					'files': [datamc + "_" + step + "_WP" + ID + '.root'],
					'folders': [""],
					'x_expressions': 'efficiency_2d',
					# formatting
					'x_log': True,
					'x_label': 'ept',
					'y_label': 'eabseta',
					'z_label': label + " Efficiency",
					'x_ticks': [25, 40, 60, 100, 200],
					'z_lims': [0.6, 1],
					# output
					'filename': "_".join([datamc, step, ID]),
				}
				if additional_dictionary is not None:
					d.update(additional_dictionary)
				plots.append(d)
	return [PlottingJob(plots, args)]


def electron_efficiencies_1d(args=None, additional_dictionary=None):
	"""1D Plots (pT in etabins) for the efficiencies determined with the Egamma TnP package"""
	plots = []
	
	etabins = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
	
	etalabels = [r"<|$\\eta$|<".join([str(a), str(b)]) for a, b in zip(etabins, etabins[1:])]
	for ID in ids:
		for step, label in zip(['SCToGsfElectron', 'GsfElectronToId', "WP{}ToHLT".format(ID)],
								['Reconstruction', 'ID', 'HLT']):
			for datamc in ['data', 'mc']:
				d = {
					'files': [datamc + "_" + step + "_WP" + ID + '.root'],
					'folders': [""],
					'x_expressions': ['efficiency_etabin{0}'.format(i) for i in range(len(etabins)-1)],
					# formatting
					'x_log': True,
					'x_label': 'ept',
					'y_label': label + " Efficiency",
					'y_lims': [0, 1],
					'labels': etalabels,
					'markers': ['.'],
					'y_errors': [True],
					'x_errors': [True],
					'x_ticks': [25, 40, 60, 100, 200],
					'legend': 'lower right',
					# output
					'filename': "_".join([datamc, step, ID]),
				}
				if additional_dictionary is not None:
					d.update(additional_dictionary)
				plots.append(d)
	return [PlottingJob(plots, args)]
