#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface


def pdf_corr(args=None):
	"""Correlation of sigma_Z and PDF vs |y| and x (2D), for u/d/s/g."""
	dicts = []
	partons = ["Gluon", "Up", "Down", "Strange"]
	for parton, title in zip(partons, [p.lower() for p in partons]):
		d = {
			"colormap": "seismic", 
			"filename": parton, 
			"files": [
				"/usr/users/dhaitz/home/artus/Excalibur/test_{}.root".format(parton)
			], 
			"folders": [
				"result"
			], 
			"texts": [
				"NNPDF 2.3 NNLO",
				"Q = 91.1 GeV",
				r"$ Z \\rightarrow \\mu \\mu$ "
			], 
			"texts_y": [
				0.97,
				0.92,
				0.97
			], 
			"texts_x": [
				0.03,
				0.03,
				0.8
			],
			"title": title, 
			"x_expressions": [
				"corr"
			], 
			"x_label": "x", 
			"x_lims": [
				0.0001, 
				1.0
			], 
			"x_log": True, 
			"y_label": "|$ y_Z $|", 
			"y_lims": [
				0.0, 
				2.8
			], 
			"z_label": r"Correlation coefficient $ \\rho$ ($ \\sigma_Z$, PDF)", 
			"z_lims": [
				-1.0, 
				1.0
			]
		}
		dicts.append(d)
	harryinterface.harry_interface(dicts, args)


def correlations(args=None, additional_dictionary=None):
	"""   """
	plots = []
	for flavour in ['gluon']:
		for quantity in ['pT' ,'m', 'phi', 'y']:
			d = {
				"colormap": "bwr",
				"filename": quantity,
				"files": ["/usr/users/dhaitz/home/qcd/sherivf/correlations/fnlo_{}Z.root".format(quantity)],
				"folders": [""],
				"texts": ["NNPDF2.2 NLO"],
				"x_expressions": [flavour],
				"x_label": "x",
				"x_log": True,
				"y_label": 'z'+(quantity if quantity != 'm' else 'mass'),
				"z_label": "Correlation Coefficient",
				"z_lims": [-1.0, 1.0]
			}

			plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	pdf_corr()
