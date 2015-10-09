#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common

def pdfs_thesis(args=None, additional_dictionary=None):
	"""PDF plots for thesis"""
	plots = []
	pdfset = "NNPDF30_nlo_as_0118"
	flavours = ['gluon', 'd_valence_quark', 'u_valence_quark', 'strange', 'd_antiquark', 'u_antiquark']
	labels = ["gluon/10", r"$d_v$", r"$u_v$", r"$s$", r"$\\bar{d}$", r"$\\bar{u}$"]
	for q in [1.9, 3, 10, 14, 91.2, 200]:
		d = {
			# input
			"files": ["pdf_sets/{}/Q_{}.root".format(pdfset, str(q).replace(".", "_"))],
			"folders": [""],
			'x_expressions': flavours,
			"nicks": flavours,
			# analysis
			"analysis_modules": ["ScaleHistograms", "ConvertToTGraphErrors"],
			"scale_nicks": ["gluon"],
			"scale": 0.1,
			# formatting
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": r"$\\mathit{x}$",
			"x_log": True,
			"labels": labels,
			"y_label": "pdf",
			"x_lims": [1e-4, 1],
			"y_lims": [0, 1],
			"title": common.pdfsetdict[pdfset],
			"texts": [r"$\\mathit{Q}=$" + " {} GeV".format(q)],
			"alphas": [0.75],
			"texts_x": [0.05],
			# output
			"www_title": "PDFs at different Q values",
			"www_text": " ",
			"filename": "pdf_{}".format(("%03d" % q).replace(".", "_")),
		}

		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	pdfs_thesis()
