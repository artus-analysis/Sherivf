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
		'hera2_abszy': common.hera_cms_title,
		'hera2_zy': common.hera_cms_title,
		'hera2_zpt': common.hera_cms_title,
		'hera2_zpt_bins': common.hera_cms_title,
	}
	title = titles.get(pdf_scenario, "")
	text = r"$\\mathit{{Q}}{1} = {0} \\/ GeV{1}$".format(".".join(common.pdfq.split("_")[:2]), ("^2" if "squared" in common.pdfq else ""))
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["exp", "exp_mod", "exp_mod_par"]
	for flavour in common.pdf_unc_flavours:
		d = {
			# input
			'files': [os.path.join("results/"+pdf_scenario+"/pdf_" +common.pdfq+ ".root")],
			'folders': [''],
			'x_expressions': [nick+"_"+flavour for nick in nicks],
			'nicks': nicks,
			# analysis
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': nicks,
			'subplot_nicks': [i+'_rel' for i in nicks],
			# labels
			'labels': ['Exp. Unc.', 'Model Unc.', 'Par. Unc.']*len(nicks),
			'x_log': True,
			'y_subplot_lims': [-0.45, 0.45],
			'zorder': [1.30, 1.20, 1.10]*3,
			'markers': ['fill']*2*len(nicks),
			'alphas': [0.7, 0.9, 0.7]*len(nicks),
			'line_styles': '-',
			'x_label': 'x',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. uncertainty',
			'colors': [histo_colors[c] for c in ["red", "yellow", "green"]]*len(nicks),
			'title': title,
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			'x_lims': [1e-4, 0.9],
			# output
			'filename': flavour + '_all-uncertainties',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if 'valence' in flavour:
			d['legend'] = 'center left'
		elif flavour in ['d_quark', 'u_quark']:
			d['legend'] = 'lower left'
			d['y_lims'] = [0, 0.9]
		elif 'sea' in flavour:
			d['y_lims'] = [0, 3.5]
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def plot_pdf_unc_comparison(args=None, additional_dictionary=None, scenario='hera2_abszy'):
	""" comparison between hera and hera+CMS with total uncertainties"""
	plots = []
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["hera", "heracms"]
	scenarios = ['hera2', scenario]
	labels = [common.hera_title, common.hera_cms_title_short]
	for pdfq in common.pdfqs:
		text = r"$\\mathit{{Q}}{1} = {0} \\/ GeV{1}$".format(".".join(pdfq.split("_")[:2]), ("^2" if "squared" in pdfq else ""))
		for only_exp in [True, False]:
			for flavour in common.pdf_unc_flavours:
				for _print in [True, False]:
					d = {
						#input
						'files': [os.path.join("results/"+scenario+"/pdf_" +common.pdfq+ ".root") for scenario in scenarios],
						'folders': [''],
						'x_expressions': [("exp" if only_exp else "exp_mod_par")+"_"+flavour],
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
						'zorder': [1.2, 1.3],
						'markers': ['fill']*4,
						'x_errors': [True]*4,
						'y_errors': [True]*4,
						'line_styles': '-',
						'x_label': 'x',
						'y_label': 'xfxQ2',
						'y_subplot_label': 'Rel. uncertainty',
						'alphas': [(0.5 if _print else 0.7)],
						'colors': [histo_colors['blue'], histo_colors['red']]*2,
						'subplot_legend': 'upper center',
						'texts': ["\n".join([flavour.replace("_", " "), text])],
						'x_lims': [1e-4, 0.9],
						'title': ("Only experimental uncertainties" if only_exp else ""),
						# output
						'filename': '_'.join([flavour, ("exp" if only_exp else "expmodelpar"), pdfq])+('_print' if _print else ''),
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



def plot_pdf_unc_comparison_all(args=None, additional_dictionary=None, scenario='hera2_zpt_bins'):
	""" ALL flavours: comparison between hera and hera+CMS with total uncertainties"""
	plots = []
	text = r"$\\mathit{{Q}}{1} = {0} \\/ GeV{1}$".format(".".join(common.pdfq.split("_")[:2]), ("^2" if "squared" in common.pdfq else ""))

	scenarios = ['hera2', scenario]
	scaledict = {
		'gluon': 0.25,
		'sea_quarks': 0.25,
	}
	flavours = ['gluon', 'd_valence_quark', 'u_valence_quark', 'sea_quarks']
	texts = [r'$g$ $(\\!\\times {})$'.format(scaledict['gluon']), '$d_v$', '$u_v$', r'$sea$ $(\\!\\times {})$'.format(scaledict['sea_quarks'])]
	labels = [common.hera_title, common.hera_cms_title_short]
	for only_exp in [True, False]:
		x_expressions = []
		scales = []
		nicks = []
		files = []
		for flavour in flavours:
			for scenario in scenarios:
				x_expressions += [("exp" if only_exp else "exp_mod_par") + "_" + flavour]
				nicks += [flavour + '_' + scenario]
				if flavour in scaledict.keys():
					scales += [scaledict[flavour]]
				else:
					scales += [1]
		for scenario in scenarios:
			files += [os.path.join("results/"+scenario+"/pdf_" +common.pdfq+ ".root")],
		for _print in [True, False]:
			d = {
				#input
				'files': files*len(flavours),
				'folders': [''],
				'x_expressions': x_expressions,
				'nicks': nicks,
				'analysis_modules': ['ScaleHistograms'],
				'scale_nicks': nicks,
				'scales': scales,
				# formatting
				'labels': labels + [None]*2*len(flavours),
				'x_log': True,
				'zorder': [1.1, 1.2]*len(flavours),
				'markers': ['fill']*2*len(flavours),
				'x_errors': [True]*2*len(flavours),
				'y_errors': [True]*2*len(flavours),
				'line_styles': '-',
				'x_label': 'x',
				'y_label': 'xfxQ2',
				'y_subplot_label': 'Rel. uncertainty',
				'alphas': [(0.5 if _print else 0.7)],
				'colors': [histo_colors['blue'], histo_colors['red']]*len(flavours),
				#'facecolors': [histo_colors['blue'], 'none'],
				'texts': [text]+texts,
				'texts_x':[0.03, 0.5, 0.8, 0.85, 0.02],
				'texts_y':[0.97, 0.78, 0.48, 0.8, 0.80],
				'x_lims': [1e-4, 0.9],
				'y_lims': [0, 1],
				#'hatches': [None, '////']*4,
				'title': ("Only experimental uncertainties" if only_exp else ""),
				# output
				'filename': ("exp" if only_exp else "expmodelpar")+('_print' if _print else ''),
			}
			if False:  # add line with diff of uncertainties
				d['analysis_modules'] += ['UncDiff']
				d['subplot_nicks'] += ['unc_diff']
				d['labels'] += ['Uncertainty diff.']
				d['x_errors'] += [None]
				d['y_errors'] += [None]
				d['y_errors'] += [' ']
				d['colors'] += ['black']
			if additional_dictionary is not None:
				d.update(additional_dictionary)
			plots.append(d)
	return [PlottingJob(plots, args)]

