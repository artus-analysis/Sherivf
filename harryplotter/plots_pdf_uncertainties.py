# -*- coding: utf-8 -*-

import common
import os

import pdf_2_root
from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors

pdf_unc_flavours = [pdf_2_root.partondict[f].replace(' ', '_') for f in pdf_2_root.default_flavours]


def pdf_unc_base(args=None, additional_dictionary=None, scenario='hera'):
	""" make pdf uncertainties """
	jobs = []
	jobs += model_unc(args, additional_dictionary, scenario)
	jobs += par_unc(args, additional_dictionary, scenario)
	jobs += combine_exp_model(args, additional_dictionary, scenario)
	jobs += combine_expmodel_par(args, additional_dictionary, scenario)
	return jobs

def pdf_unc_hera(args=None, additional_dictionary=None):
	""" make pdf uncertainties for hera """
	return pdf_unc_base(args, additional_dictionary, 'hera')

def pdf_unc_heraZ(args=None, additional_dictionary=None):
	""" make pdf uncertainties for heraZ """
	return pdf_unc_base(args, additional_dictionary, 'heraZ')

def pdf_unc_heraZ_pt(args=None, additional_dictionary=None):
	""" make pdf uncertainties for heraZ """
	return pdf_unc_base(args, additional_dictionary, 'heraZ_pt')

def pdf_unc_heraZ_bins(args=None, additional_dictionary=None):
	""" make pdf uncertainties for heraZ """
	return pdf_unc_base(args, additional_dictionary, 'heraZ_bins')



def model_unc(args=None, additional_dictionary=None, pdf_scenario='hera'):
	"""get model uncertainties"""
	pdf_unc_basedir = os.environ['SHERIVFDIR']+"/latest_herafitter_"+pdf_scenario+"/"
	pdf_unc_basefile = pdf_unc_basedir + "job_{}_herapdf__1_9_squared.root"
	n_max = 9
	q_squared = 1.9
	exp_unc = 'exp_unc'
	nicks = ["nick"+str(i) for i in range(n_max)]
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			 # input
			'files': [pdf_unc_basefile.format(i) for i in range(n_max)],
			'folders': [''],
			'x_expressions': [flavour],
			'nicks': nicks,
			# 
			'analysis_modules': ['GraphEnvelope'],
			'envelope_center_nick': nicks[0],
			'envelope_nicks': nicks[1:],
			
			'nicks_whitelist': ['envelope', exp_unc],
			'labels': ['model', 'exp'],

			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': pdf_scenario+'_model_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def par_unc(args=None, additional_dictionary=None, pdf_scenario='hera'):
	pdf_unc_basedir = os.environ['SHERIVFDIR']+"/latest_herafitter_"+pdf_scenario+"/"
	pdf_unc_basefile = pdf_unc_basedir + "job_{}_herapdf__1_9_squared.root"
	"""get parametrisation uncertainties"""
	variations = [0] + range(9, 20)
	q_squared = 1.9
	exp_unc = 'exp_unc'
	nicks = ["nick"+str(i) for i in variations]
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			 # input
			'files': [pdf_unc_basefile.format(i) for i in variations],
			'folders': [''],
			'x_expressions': [flavour],
			'nicks': nicks,
			# 
			'analysis_modules': ['GraphEnvelope'],
			'envelope_center_nick': nicks[0],
			'envelope_nicks': nicks[1:],
			
			'nicks_whitelist': ['envelope', exp_unc],
			'labels': ['par', 'exp'],

			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': pdf_scenario+'_par_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]



def combine_exp_model(args=None, additional_dictionary=None, pdf_scenario='hera'):
	""" combine model and experimental"""
	pdf_unc_basedir = os.environ['SHERIVFDIR']+"/latest_herafitter_"+pdf_scenario+"/"
	pdf_unc_basefile = pdf_unc_basedir + "job_{}_herapdf__1_9_squared.root"
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, pdf_scenario+'_model_'+flavour+".root"),
				pdf_unc_basefile.format(0),
			],
			'folders': [''],
			'x_expressions': ['model', flavour],
			'nicks': ['model', 'exp'],
			
			'analysis_modules': ['CombineTGraphs'],
			
			'combine_nicks': ['exp', 'model'],
			
			'labels': ['model', 'exp', 'expmodel'],
			
			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': pdf_scenario+'_combined_exp_model_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]

def combine_expmodel_par(args=None, additional_dictionary=None, pdf_scenario='hera'):
	""" combine exp/model and parameterisation uncertainty to final uncertainty"""
	pdf_unc_basedir = os.environ['SHERIVFDIR']+"/latest_herafitter_"+pdf_scenario+"/"
	pdf_unc_basefile = pdf_unc_basedir + "job_{}_herapdf__1_9_squared.root"
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, pdf_scenario+'_par_'+flavour+".root"),
				os.path.join(common.pdf_dir, pdf_scenario+'_combined_exp_model_'+flavour+".root"),
				pdf_unc_basefile.format(0),
			],
			'folders': [''],
			'x_expressions': ['par', 'expmodel', flavour],
			'nicks': ['par', 'expmodel', 'exp'],
			
			'analysis_modules': ['CombineTGraphs'],
			'combine_nicks': ['par', 'expmodel'],
		
			'labels': ['par', 'expmodel', 'exp', 'expmodelpar'],
		
			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': pdf_scenario+'_combined_exp_model_par_' + flavour,
			'export_json': False,
		}
	
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


###
### Now the actual plots ...
###

def plot_pdf_uncs_hera(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'hera')
def plot_pdf_uncs_heraZ(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'heraZ')
def plot_pdf_uncs_heraZ_pt(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'heraZ_pt')
def plot_pdf_uncs_heraZ_bins(args=None, additional_dictionary=None):
	return plot_pdf_uncs(args, additional_dictionary, 'heraZ_bins')


def plot_pdf_uncs(args=None, additional_dictionary=None, pdf_scenario='hera'):
	""" plot the pdfs with all uncertainties"""
	plots = []
	titles = {
		'hera': "HERA-I DIS",
		'heraZ': "HERA-I DIS + CMS",
		'heraZ_pt': "HERA-I DIS + CMS (pT-spectrum)",
		'heraZ_bins': "HERA-I DIS + CMS (pT in y-bins)",
	}
	title = titles.get(pdf_scenario, "")
	text = r"$\\mathit{Q}^2 = 1.9 \\/ GeV^2$"
	y_lims = {
		'gluon': [0, 4],
	}
	nicks = ["exp", "expmodel", "expmodelpar"]
	for flavour in pdf_unc_flavours:
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
			'grid': True,
			'alphas': [0.7, 0.9, 0.7]*len(nicks),
			'subplot_grid': True,
			'line_styles': '-',
			'x_label': r'$x$',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. Uncertainty',
			'colors': [histo_colors[c] for c in ["red", "yellow", "green"]]*len(nicks),
			'title': title,
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			# output
			'filename': flavour + '_all-uncertainties',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def plot_pdf_unc_comparison(args=None, additional_dictionary=None):
	""" comparison between hera and hera+CMS with total uncertainties"""
	plots = []
	text = r"$\\mathit{Q}^2 = 1.9 \\/ GeV^2$"
	y_lims = {
		'gluon': [0, 3],
	}
	nicks = ["hera", "heracms"]
	scenarios = ['hera', 'heraZ']
	for flavour in pdf_unc_flavours:
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
			'labels': ['HERA', 'HERA+CMS']*len(nicks),
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
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			# output
			'filename': flavour + '_hera_cms',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if 'valence' in flavour.lower():
			d['legend'] = 'center left'
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]

