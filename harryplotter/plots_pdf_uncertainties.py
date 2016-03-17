# -*- coding: utf-8 -*-

import common
import os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors


def plot_pdf_uncs_hera2(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera2')
def plot_pdf_uncs_hera2_abszy(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera2_abszy')
def plot_pdf_uncs_hera2_zy(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera2_zy')
def plot_pdf_uncs_hera2_zpt(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera2_zpt')
def plot_pdf_uncs_hera2_zpt_bins(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera2_zpt_bins')


def plot_pdf_uncs(args=None, additional_dictionary=None, pdf_scenario='hera'):
	""" plot the pdfs with all uncertainties"""
	plots = []
	titles = {
		'hera2': common.hera_title,
		'hera2_abszy': common.hera_cms_title + r" |$y$|",
		'hera2_zy': common.hera_cms_title + r" $y$",
		'hera2_zpt': common.hera_cms_title + r" $p_\\mathrm{T}$",
		'hera2_zpt_bins': common.hera_cms_title + r" ($p_\\mathrm{T}$ in bins of |y|)",
	}
	title = titles.get(pdf_scenario, "")
	text = r"$\\mathit{{Q}}^2 = {} \\/ GeV{}$".format(".".join(common.pdfq.split("_")[:2]), ("^2" if "squared" in common.pdfq else ""))
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["exp", "expmodel", "expmodelpar"]
	for flavour in common.pdf_unc_flavours:
		d = {
			# input
			'files': [os.path.join(common.pdf_dir, pdf_scenario+"_"+common.pdfq+'_combined_exp_model_par_'+flavour+".root")],
			'folders': [''],
			'x_expressions': nicks,
			'nicks': nicks,
			# analysis
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': nicks,
			'subplot_nicks': [i+'_rel' for i in nicks],
			# labels
			'labels': ['Exp. Unc.', 'Model Unc.', 'Par. Unc.']*len(nicks),
			'x_log': True,
			'y_subplot_lims': [-0.45, 0.45],
			'zorder': [30, 20, 10]*3,
			'markers': ['fill']*2*len(nicks),
			'alphas': [0.7, 0.9, 0.7]*len(nicks),
			'line_styles': '-',
			'x_label': 'x',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. Uncertainty',
			'colors': [histo_colors[c] for c in ["red", "yellow", "green"]]*len(nicks),
			'title': title,
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			'x_lims': [1e-4, 0.9],
			# output
			'filename': flavour + '_all-uncertainties',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def plot_pdf_unc_comparison(args=None, additional_dictionary=None, scenario='hera2_abszy'):
	""" comparison between hera and hera+CMS with total uncertainties"""
	plots = []
	text = r"$\\mathit{{Q}}^2 = {} \\/ GeV{}$".format(".".join(common.pdfq.split("_")[:2]), ("^2" if "squared" in common.pdfq else ""))
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["hera", "heracms"]
	scenarios = ['hera2', scenario]
	labels = [common.hera_title, common.hera_cms_title]
	for only_exp in [True, False]:
		for flavour in common.pdf_unc_flavours:
			d = {
				#input
				'files': [os.path.join(common.pdf_dir, scenario+"_"+common.pdfq+'_combined_exp_model_par_'+flavour+".root") for scenario in scenarios],
				'folders': [''],
				'x_expressions': [("exp" if only_exp else "expmodelpar")],
				'nicks': nicks,
				# analysis
				'analysis_modules': ['RelUncertainty'],
				'rel_nicks': nicks,
				'subplot_nicks': [i+'_rel' for i in nicks],
				'unc_diff_nicks': [i+'_rel' for i in nicks],
				# formatting
				'labels': labels + [None]*2,
				'x_log': True,
				'y_subplot_lims': [-0.45, 0.45],
				'zorder': [20, 30],
				'markers': ['fill']*4,
				'x_errors': [True]*4,
				'y_errors': [True]*4,
				'line_styles': '-',
				'x_label': 'x',
				'y_label': 'xfxQ2',
				'y_subplot_label': 'Rel. Uncertainty',
				'alphas': [0.7],
				'colors': [histo_colors['blue'], histo_colors['red']]*2,
				'subplot_legend': 'upper center',
				'texts': ["\n".join([flavour.replace("_", " "), text])],
				'x_lims': [1e-4, 0.9],
				'title': ("Only experimental uncertainties" if only_exp else ""),
				# output
				'filename': '_'.join([flavour, ("exp" if only_exp else "expmodelpar")]),
			}
			if False:  # add line with diff of uncertainties
				d['analysis_modules'] += ['UncDiff']
				d['subplot_nicks'] += ['unc_diff']
				d['labels'] += ['Uncertainty diff.']
				d['x_errors'] += [None]
				d['y_errors'] += [None]
				d['y_errors'] += [' ']
				d['colors'] += ['black']
			if flavour in y_lims:
				d['y_lims'] = y_lims[flavour]
			if 'valence' in flavour.lower():
				d['legend'] = 'center left'
			if additional_dictionary is not None:
				d.update(additional_dictionary)
			plots.append(d)
	return [PlottingJob(plots, args)]

def plot_pdf_unc_comparison_zpt(args=None, additional_dictionary=None):
	return plot_pdf_unc_comparison(args, additional_dictionary, scenario='hera2_zpt')
def plot_pdf_unc_comparison_abszy(args=None, additional_dictionary=None):
	return plot_pdf_unc_comparison(args, additional_dictionary, scenario='hera2_abszy')
def plot_pdf_unc_comparison_zy(args=None, additional_dictionary=None):
	return plot_pdf_unc_comparison(args, additional_dictionary, scenario='hera2_zy')
def plot_pdf_unc_comparison_zpt_bins(args=None, additional_dictionary=None):
	return plot_pdf_unc_comparison(args, additional_dictionary, scenario='hera2_zpt_bins')
