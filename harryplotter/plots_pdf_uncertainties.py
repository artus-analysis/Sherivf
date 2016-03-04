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
		'hera2': "HERA DIS",
		'hera2_abszy': r"HERA DIS + CMS Z($\\rightarrow$ee)+jet |$y$|",
		'hera2_zy': r"HERA DIS + CMS Z($\\rightarrow$ee)+jet $y$",
		'hera2_zpt': r"HERA DIS + CMS Z($\\rightarrow$ee)+jet $p_\\mathrm{T}$",
		'hera2_zpt_bins': r"HERA DIS + CMS Z($\\rightarrow$ee)+jet ($p_\\mathrm{T}$ in bins of |y|)",
	}
	title = titles.get(pdf_scenario, "")
	text = r"$\\mathit{{Q}}^2 = {} \\/ GeV{}$".format(".".join(common.pdfq.split("_")[:-1]), ("^2" if "squared" in common.pdfq else ""))
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["exp", "expmodel", "expmodelpar"]
	for flavour in common.pdf_unc_flavours:
		d = {
			# input
			'files': [os.path.join(common.pdf_dir, pdf_scenario+'_combined_exp_model_par_'+flavour+".root")],
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
			'x_label': r'$x$',
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
	text = r"$\\mathit{{Q}}^2 = {} \\/ GeV{}$".format(".".join(common.pdfq.split("_")[:-1]), ("^2" if "squared" in common.pdfq else ""))
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["hera", "heracms"]
	scenarios = ['hera2', scenario]
	labels = ['HERA', r'HERA + CMS Z($\\rightarrow$ee)']*len(nicks),
	for flavour in common.pdf_unc_flavours:
		d = {
			#input
			'files': [os.path.join(common.pdf_dir, scenario+'_combined_exp_model_par_'+flavour+".root") for scenario in scenarios],
			'folders': [''],
			'x_expressions': ["expmodelpar"],
			'nicks': nicks,
			# analysis
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': nicks,
			'subplot_nicks': [i+'_rel' for i in nicks],
			# formatting
			'labels': labels,
			'x_log': True,
			'y_subplot_lims': [-0.45, 0.45],
			'zorder': [20, 30],
			'markers': ['fill']*6,
			'line_styles': '-',
			'x_label': r'$x$',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. Uncertainty',
			'alphas': [0.4],
			'colors': [histo_colors['blue'], histo_colors['yellow']]*2,
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			'x_lims': [1e-4, 0.9],
			# output
			'filename': '_'.join([flavour, scenario, 'cms']),
		}
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
