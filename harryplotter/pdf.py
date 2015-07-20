#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface


def pdf(args=None):
	"""plot a PDF"""
	d = {
		"analysis_modules": ["Ratio"],
		"folders": [""],
		"line_styles": ["-"],
		"markers": ["fill"],
		#"title": "gluon",
		"x_label": "$x$",
		"x_log": True,
		"y_label": "PDF",
		"y_subplot_lims": [0.9, 1.1],
		"texts": [r"NNPDF 2.3 NLO\n$\\mathit{Q}=\\mathit{m}_Z$"],
	}
	harryinterface.harry_interface([d], args)


if __name__ == '__main__':
	pdf()
