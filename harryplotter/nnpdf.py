#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryinterface as harryinterface
import Excalibur.Plotting.utility.colors as colors


def pdf(args=None, additional_dictionary=None, pdflabel=""):
	"""plot a PDF"""
	plots = []
	for flavour in ['gluon', 'd_quark', 'u_quark', 'strange', 'charm', 'd_antiquark', 'u_antiquark']:
		d = {
			"folders": [""],
			'x_expressions': [flavour],
			# analysis
			"analysis_modules": ["RelUncertainty"],
			"rel_nicks": ['orig', 'rew'],
			# formatting
			"nicks": ['orig', 'rew'],
			"subplot_nicks": ['orig_rel', 'rew_rel'],
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": r"$\\mathit{x}$",
			"colors": [colors.histo_colors['blue'], colors.histo_colors['yellow']],
			"x_log": True,
			"y_label": "pdf",
			"y_subplot_lims": [-0.25, 0.25],
			"y_subplot_label": "Rel. Uncert.",
			"texts": [pdflabel + r"\n$\\mathit{Q}=\\mathit{m}_Z$ (91.2 GeV)"],
			"texts_x": [0.05],
			'title': flavour.replace('_', ' '),
			# output
			'www_title': 'NNPDF Reweighting',
			'www_text': 'Result of NNPDF Reweighting: Comparison of original and reweighted PDF set. Dummy systematic errors have been used.',
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	harryinterface.harry_interface(plots, args)

def nnpdf(args=None):
	pdfset = 'NNPDF30_nlo_as_0118'
	labels = {
		'NNPDF30_nlo_as_0118': 'NNPDF 3.0',
	}
	pdf(args, {
		'files': ['pdf_sets/{}.root'.format(pdfset), 'pdf_sets/{}_HighStat_chi2_nRep100.root'.format(pdfset)],
		'labels': ['original', 'reweighted'],
		'www': 'nnpdf'
	}, pdflabel=labels[pdfset])


if __name__ == '__main__':
	nnpdf()
