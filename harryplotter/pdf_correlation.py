#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface


def pdf_correlations(args=None, additional_dictionary=None):
	""" Correlation of sigma_Z and PDF vs Z quantities and x (2D), for u/d/s/g."""
	plots = []
	lims = {
		'y': [0, 2.4],
		'm': [81, 101],
		'pT': [30, 400],
		'phi': [-3, 3],
	}
	for flavour in ['gluon', 'd quark', 'u quark', 'u antiquark', 'd antiquark', 'sea quarks']:
		for quantity in ['pT' ,'m', 'phi', 'y']:
			d = {
				# input
				"x_expressions": [flavour],
				"files": ["/usr/users/dhaitz/home/qcd/sherivf/correlations/fnlo_{}Z.root".format(quantity)],
				"folders": [""],
				# formatting
				"x_label": "x",
				"x_log": True,
				"y_label": 'z'+(quantity if quantity != 'm' else 'mass'),
				"z_label": r"Correlation coefficient $ \\rho$ ($ \\sigma_Z$, PDF)",
				"z_lims": [-1.0, 1.0],
				"colormap": "bwr",
				"texts": [r"NNPDF 2.3 NLO\n$\\mathit{Q}=\\mathit{m}_Z$ (91.2 GeV)"],
				"title": flavour,
				# output
				"filename": flavour.replace(" ", "-")+"_"+quantity,
				"www_title": "Correlations",
				"www_text": "Correlations between PDF and cross section for different flavours and Z boson quantities",

			}
			try:
				d['y_lims'] = lims[quantity]
			except KeyError:
				pass

			plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	pdf_corr()
