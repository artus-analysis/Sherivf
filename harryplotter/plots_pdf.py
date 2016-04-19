#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common

def pdfs_thesis(args=None, additional_dictionary=None):
	"""PDF plots for thesis"""
	plots = []
	pdfset = "NNPDF30_nlo_as_0118"
	flavours = ['gluon', 'd_valence_quark', 'u_valence_quark', 'sea_quarks']
	scale = 0.25
	labels = [r"gluon $(\\!\\times {})$".format(scale), r"$d_v$", r"$u_v$", r"sea quarks $(\\!\\times {})$".format(scale)]
	for q in [1.4, 3, 10, 14, 91.2, 200]:
		d = {
			# input
			"files": ["pdf_sets/{}/pdfs_for_plotting_{}.root".format(pdfset, str(q).replace(".", "_"))],
			"folders": [""],
			'x_expressions': flavours,
			"nicks": flavours,
			# analysis
			"analysis_modules": ["ScaleHistograms"],
			"scale_nicks": ["gluon", "sea_quarks"],
			"scales": [scale],
			# formatting
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": "x",
			"x_log": True,
			"labels": labels,
			"y_label": "pdf",
			"x_lims": [1e-4, 0.9],
			"y_lims": [0, 1],
			"title": common.pdfsetdict[pdfset],
			"texts": [r"$\\mathit{Q} =$" + " {} GeV".format(q)],
			"alphas": [0.75],
			# output
			"www_title": "PDFs at different Q values",
			"www_text": " ",
			"filename": "pdf_{}".format(("%03d" % q).replace(".", "_")),
		}
		if q == 91.2:
			d['legend'] = "center left"
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	pdfs_thesis()
