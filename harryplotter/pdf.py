#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface
import Excalibur.Plotting.utility.colors as colors


def pdf(args=None, additional_dictionary=None):
	"""plot a PDF"""
	plots = []
	for flavour in ['gluon', 'd_quark', 'u_quark']:#, 'sea_quarks', 'd_valence_quark', 'u_valence_quark']:
		d = {
			"analysis_modules": ["Divide", "ConvertToTGraphErrors"],
			"convert_nicks": ['3', '4'],
			"divide_denominator_nicks": ['1'],
			"divide_numerator_nicks": ['1', '2'],
			"divide_result_nicks": ['3', '4'],
			"subplot_nicks": ['3', '4'],
			"nicks": ['1', '2', '3', '4'],
			"folders": [""],
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": r"$\\mathit{x}$",
			"colors": [colors.histo_colors['blue'], colors.histo_colors['yellow']],
			"x_log": True,
			"y_label": "PDF xfx",
			"y_subplot_lims": [0.8, 1.2],
			"y_subplot_label": "Ratio to NNPDF",
			"texts": [r"NNPDF 2.3 NLO\n$\\mathit{Q}=\\mathit{m}_Z$ (91.2 GeV)"],
		}
		d.update({
			'x_expressions': [flavour],
			'title': flavour.replace('_', ' ')
		})
	
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	harryinterface.harry_interface(plots, args)

def nnpdf(args=None):
	pdf(args, {
		'files': ['pdf_sets/NNPDF23_nlo_as_0118.root', 'pdf_sets/NNPDF23_nlo_as_0118_HighStat_chi2_nRep100.root'],
		'labels': ['original', 'reweighted'],
		'www': 'nnpdf'
	})


if __name__ == '__main__':
	nnpdf()
