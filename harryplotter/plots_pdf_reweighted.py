#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.utility.colors as colors
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors

from plots_pdf_uncertainties import pdf_unc_flavours
import common

def nnpdf(args=None, additional_dictionary=None, plot_errors = True):
	""" Result of NNPDF reweighting 

	plot PDFs with rel uncertainties
	OR
	plot_errors == True: rel uncertainty with ratio
	"""
	plots = []
	q = additional_dictionary.get('q', '91_2')
	mode = additional_dictionary.get('mode', 'zpt')
	y_lims = {
		'gluon': [0.01, 10],
	}
	pdfset = 'NNPDF30_nlo_as_0118_nolhc_1000'
	nicks = ['original', 'reweighted']
	for flavour in pdf_unc_flavours:
		d = {
			#input
			'files': [
				'pdf_sets/{0}__{1}.root'.format(pdfset, q),
				'results/nnpdf_{2}/{0}_Zee_chi2_nRep100__{1}.root'.format(pdfset, q, mode),
			],
			'folders': [''],
			'x_expressions': [flavour],
			'nicks': nicks,
			# formatting
			'x_log': True,
			'zorder': [20, 30],
			'markers': ['fill']*6,
			'grid': True,
			'subplot_grid': True,
			'title': common.pdfsetdict.get(pdfset, pdfset),
			'x_label': r'$x$',
			'texts': mode + '\n' + str(q),
			# output
			'filename': flavour + '_nnpdf-rew',
		}
		if plot_errors:
			d.update({
				#analysis
				'analysis_modules': [
					'ConvertToHistogram',
					'StatisticalErrors',
					'Ratio',
				],
				'ratio_numerator_nicks': ['reweighted'],
				'ratio_denominator_nicks': ['original'],
				'stat_error_relative': True,
				# formatting
				'colors': [histo_colors['blue'], histo_colors['yellow'], 'black'],
				'y_label': 'PDF relative uncertainty',
				'y_subplot_label': 'Ratio rew./orig.',
				'markers': ['-'],
				'y_subplot_lims': [0.5, 1.5],
				'line_widths': [2.],
				'step': True,
				'line_styles': ['-'],
				'y_log': True,
				'y_lims': [0.01, 10]
			})
		else:
			d.update({
				#analysis
				'analysis_modules': ['RelUncertainty'],
				'rel_nicks': nicks,
				'subplot_nicks': [i+'_rel' for i in nicks],
				# formatting
				'y_subplot_lims': [-0.45, 0.45],
				'alphas': [0.4],
				'colors': [histo_colors['blue'], histo_colors['yellow']]*2,
				'y_label': 'xfxQ2',
				'y_subplot_label': 'Rel. Uncertainty',
			})
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if 'valence' in flavour.lower():
			d['legend'] = 'center left'
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
