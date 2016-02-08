#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Excalibur.Plotting.utility.colors as colors
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors

from plots_pdf_uncertainties import pdf_unc_flavours

def nnpdf(args=None, additional_dictionary=None):
	""" Result of NNPDF reweighting """
	plots = []
	y_lims = {
		'gluon': [0, 3],
	}
	pdfset = 'NNPDF23_nlo_as_0118'
	q = '1_4_squared'
	#q = '91_2'
	nicks = ['orig', 'reweighted']
	for flavour in pdf_unc_flavours:
		d = {
			#input
			'files': [
				'pdf_sets/{0}__{1}.root'.format(pdfset, q),
				'results/nnpdf_zpt/{0}_Zee_chi2_nRep100__{1}.root'.format(pdfset, q),
			],
			'folders': [''],
			'x_expressions': [flavour],
			'nicks': nicks,
			# analysis
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': nicks,
			'subplot_nicks': [i+'_rel' for i in nicks],
			# formatting
			'x_log': True,
			'y_subplot_lims': [-0.45, 0.45],
			'zorder': [20, 30],
			'markers': ['fill']*6,
			'grid': True,
			'subplot_grid': True,
			'line_styles': '-',
			'x_label': r'$x$',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. Uncertainty',
			'alphas': [0.4],
			'colors': [histo_colors['blue'], histo_colors['yellow']]*2,
			# output
			'filename': flavour + '_nnpdf-rew',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if 'valence' in flavour.lower():
			d['legend'] = 'center left'
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	nnpdf()
