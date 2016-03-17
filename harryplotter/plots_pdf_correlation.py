#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import calculate_correlation
import common

def pdf_correlations(args=None, additional_dictionary=None):
	""" Correlation of sigma_Z and PDF vs Z quantities and x (2D), for u/d/s/g."""
	plots = []
	for pdfset in ['NNPDF30_nlo_as_0118', 'NNPDF23_nlo_as_0118', 'NNPDF30_nlo_as_0118_nolhc']:
		for flavour in calculate_correlation.partons.values():
			for quantity in ['zpt' ,'zmass', 'abszy']:
				d = {
					# input
					"x_expressions": [flavour],
					"files": ["/usr/users/dhaitz/home/qcd/sherivf/correlations/{}_{}.root".format(quantity, pdfset)],
					"folders": [""],
					# formatting
					"x_label": "x",
					"x_log": True,
					"y_label": quantity,
					"z_label": r"Correlation coefficient $ \\rho$ ($ \\sigma_Z$, PDF)",
					"z_lims": [-1.0, 1.0],
					"colormap": "coolwarm",
					"rasterized": True,
					"texts": [common.pdfsetdict.get(pdfset, pdfset)+r"\n$\\mathit{Q}=\\mathit{m}_Z$ (91.2 GeV)"],
					"title": flavour,
					'rasterized': True,
					# output
					"filename": "_".join([flavour.replace(" ", "-"), quantity, pdfset]),
					"www_title": "Correlations",
					"www_text": "Correlations between PDF and cross section for different flavours and Z boson quantities",
				}
				try:
					if ',' in common.bins[quantity]:
						d['y_lims'] = [float(i) for i in common.bins[quantity].split(",")[1:]]
					else:  # non-equidistant bins:
						bins = [float(i) for i in common.bins[quantity].split(" ")]
						d['y_lims'] = [bins[0], bins[-1]]
					if quantity == 'zpt':
						d['y_lims'] = [30, 400]
				except KeyError:
					pass
				plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	pdf_corr()
