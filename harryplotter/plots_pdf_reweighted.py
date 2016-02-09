#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

import Excalibur.Plotting.utility.colors as colors
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors

from plots_pdf_uncertainties import pdf_unc_flavours
import common

def nnpdf(args=None, additional_dictionary=None):
	""" Result of NNPDF reweighting 

	plot PDFs with rel uncertainties
	OR
	plot_errors == True: rel uncertainty with ratio
	"""
	plots = []
	q = additional_dictionary.get('q', '91_2')
	mode = additional_dictionary.get('mode', 'zpt')
	additional_dictionary.pop('q')
	additional_dictionary.pop('mode')
	y_lims = {
		#'gluon': [0.01, 10],
	}
	n_replicas= 1000
	pdfset = 'NNPDF30_nlo_as_0118_nolhc_1000'
	labels = ['Original', 'Reweighted']
	nicks = [label.lower() for label in labels]
	for flavour in pdf_unc_flavours:
		files = [
			'pdf_sets/{0}__{1}.root'.format(pdfset, q),
			'results/nnpdf_{2}/{0}_Zee_chi2_nRep{3}__{1}.root'.format(pdfset, q, mode, n_replicas),
		]
		qlabel = r'$Q{0}$ = {1}'.format(('^2' if 'squared' in q else ''), q.replace('_squared', '').replace('_', '.'))
		filename = '_'.join(['nnpdf_{}', flavour, q])
		d = {
			#input
			'folders': [''],
			'x_expressions': [flavour],
			# formatting
			'x_log': True,
			'zorder': [20, 30],
			'markers': ['fill']*6,
			'title': common.pdfsetdict.get(pdfset, pdfset),
			'x_label': r'$x$',
			'labels': labels,
			'texts': (r"Reweighted: {0}".format(common.labels.get_nice_label(mode).split('/')[0].replace('\\', '\\\\')) + '\n' + qlabel),
		}
		# errors with ratio
		d1 = copy.deepcopy(d)
		d1.update({
			'files': files*2,
			'nicks': nicks + [i+'_tgraph' for i in nicks],
			#analysis
			'analysis_modules': [
				'ConvertToHistogram',
				'StatisticalErrors',
				'Ratio',
			],
			'convert_nicks': nicks,
			'ratio_numerator_nicks': ['reweighted'],
			'ratio_denominator_nicks': ['original'],
			'stat_error_relative': True,
			'nicks_whitelist': ['tgraph', 'ratio'],
			# formatting
			'colors': [histo_colors['blue'], histo_colors['yellow'], 'black'],
			'y_label': 'PDF relative uncertainty',
			'y_subplot_label': 'Ratio rew./orig.\n',
			'markers': ['fill']*2+['-'],
			'y_subplot_lims': [0.5, 1.5],
			'alphas': [0.6],
			'line_styles': ['-'],
			'y_lims': [0, 0.45],
			# output
			'filename': filename.format('errors'),
		})
		# full PDF
		d2 = copy.deepcopy(d)
		d2.update({
			'files': files,
			'nicks': nicks,
			#analysis
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': nicks,
			'subplot_nicks': [i+'_rel' for i in nicks],
			# formatting
			'y_subplot_lims': [-0.45, 0.45],
			'alphas': [0.4],
			'colors': [histo_colors['blue'], histo_colors['yellow']]*2,
			'y_label': 'xfxQ2',
			'line_styles': ['-'],
			'y_subplot_label': 'Rel. Uncertainty',
			# output
			'filename': filename.format('pdf'),
		})
		if flavour in y_lims:
			d2['y_lims'] = y_lims[flavour]
		if 'valence' in flavour.lower():
			d2['legend'] = 'center left'
		for d in [d1, d2]:
			if additional_dictionary is not None:
				d.update(additional_dictionary)
			plots.append(d)
	return [PlottingJob(plots, args)]


def nnpdf_zpt_91(args=None):
	return nnpdf(args, {'q': '91_2', 'mode': 'zpt'})

def nnpdf_zpt_2(args=None):
	return nnpdf(args, {'q': '1_9_squared', 'mode': 'zpt'})

def nnpdf_zpt_10(args=None):
	return nnpdf(args, {'q': '10_0_squared', 'mode': 'zpt'})

def nnpdf_abszy_91(args=None):
	return nnpdf(args, {'q': '91_2', 'mode': 'abszy'})

def nnpdf_abszy_2(args=None):
	return nnpdf(args, {'q': '1_9_squared', 'mode': 'abszy'})

def nnpdf_abszy_10(args=None):
	return nnpdf(args, {'q': '10_0_squared', 'mode': 'abszy'})

if __name__ == '__main__':
	nnpdf()
