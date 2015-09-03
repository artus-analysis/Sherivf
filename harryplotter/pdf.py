#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface


def pdfs_thesis(args=None, additional_dictionary=None):
	"""PDF plots for thesis"""
	plots = []
	flavours = ['gluon', 'd_valence_quark', 'u_valence_quark', 'strange', 'd_antiquark', 'u_antiquark']
	labels = ["gluon/10", r"$d_v$", r"$u_v$", r"$s$", r"$\\bar{d}$", r"$\\bar{u}$"]
	for q in [1.9, 3, 10, 14, 91.2, 200]:
		d = {
			"files": ["pdf_sets/pdfs_for_plotting_{}.root".format(str(q).replace(".", "_"))],
			"folders": [""],
			'x_expressions': flavours,
			"nicks": flavours,
			
			"analysis_modules": ["ScaleHistograms", "ConvertToTGraphErrors"],
			"scale_nicks": ["gluon"],
			"scale": 0.1,
			
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": r"$\\mathit{x}$",
			"x_log": True,
			"labels": labels,
			"y_label": "pdf",
			"x_lims": [1e-3, 1],
			"y_lims": [0, 1],
			"title": "NNPDF 3.0 NLO",
			"texts": [r"$\\mathit{Q}=$" + " {} GeV".format(q)],
			"texts_x": [0.05],
			
			"filename": "pdf_{}".format(("%03d" % q).replace(".", "_")),
		}

		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	pdfs_thesis()
