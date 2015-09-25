#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.utility.colors as colors
from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def pdf(args=None, additional_dictionary=None, pdflabel=""):
	"""plot a PDF"""
	plots = []
	# determine q from file name:
	q_value = "91.2"
	try:
		q_values = [f.split('.')[0].split('__')[-1].replace('_', '.') for f in additional_dictionary['files']]
		if len(list(set(q_values))) == 1:
			q_value = q_values[0]
	except:
		pass

	for flavour in ['gluon', 'd_quark', 'u_quark', 'strange', 'charm', 'd_antiquark', 'u_antiquark']:
		d = {
			"folders": [""],
			'x_expressions': [flavour],
			# analysis
			"analysis_modules": ["RelUncertainty"],
			"rel_nicks": ['orig', 'new'],
			# formatting
			"nicks": ['orig', 'new'],
			"subplot_nicks": ['orig_rel', 'new_rel'],
			"line_styles": ["-"],
			"markers": ["fill"],
			"x_label": r"$\\mathit{x}$",
			"colors": [colors.histo_colors['blue'], colors.histo_colors['yellow']]*2,
			"x_log": True,
			"y_label": "pdf",
			"y_subplot_lims": [-0.25, 0.25],
			"y_subplot_label": "Rel. Uncert.",
			"texts": [pdflabel + r"\n$\\mathit{{Q}}={} \\ GeV$".format(q_value)],
			"texts_x": [0.05],
			'title': flavour.replace('_', ' '),
			'subplot_fraction': 50,
			# output
			'www_title': 'NNPDF Reweighting',
			'www_text': 'Result of NNPDF Reweighting: Comparison of original and reweighted PDF set. Dummy systematic errors have been used.',
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def nnpdf(args=None):
	pdfset = 'NNPDF30_nlo_as_0118'
	labels = {
		'NNPDF30_nlo_as_0118': 'NNPDF 3.0',
	}
	return pdf(args, {
		'files': ['pdf_sets/{}.root'.format(pdfset), 'pdf_sets/{}_HighStat_chi2_nRep100__91_2.root'.format(pdfset)],
		'labels': ['original', 'reweighted']*2,
	}, pdflabel=labels[pdfset])


def herapdf(args=None, q_value='91_2'):
	"""plot hera pdf reweighted pdf"""
	return pdf(args, {
		'files':  ['pdf_sets/hera{}__{}.root'.format(a, q_value) for a in ['', 'Z']],
		'labels': ['HERA', r'HERA+CMS']*2,
		'www_title': 'PDF Fit',
		'www_text': 'No model or parametrisation uncertainties',
	})

def herapdf_13(args=None):
	return herapdf(args, '1_3')

def herapdf_912(args=None):
	return herapdf(args, '91_2')


if __name__ == '__main__':
	nnpdf()
