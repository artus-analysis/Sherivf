# -*- coding: utf-8 -*-

import common
import os

import pdf_2_root
from Excalibur.Plotting.utility.toolsZJet import PlottingJob

pdf_unc_basedir = "/storage/a/dhaitz/hera/"
pdf_unc_basefile = pdf_unc_basedir + "job_{}_herapdf__1_9_squared.root"
pdf_unc_flavours = [pdf_2_root.partondict[f].replace(' ', '_') for f in pdf_2_root.default_flavours]


def model_unc(args=None, additional_dictionary=None):
	"""get model uncertainties"""
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
			'filename': 'model_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def par_unc(args=None, additional_dictionary=None):
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
			'filename': 'par_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]



def combine_exp_model(args=None, additional_dictionary=None):
	""" combine model and experimental"""
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, 'model_'+flavour+".root"),
				pdf_unc_basefile.format(0),
			],
			'folders': [''],
			'x_expressions': ['model', flavour],
			'nicks': ['model', 'exp'],
			
			'analysis_modules': ['CombineTGraphs'],
			
			'combine_nick1': 'exp',
			'combine_nick2': 'model',
			
			'labels': ['model', 'exp', 'expmodel'],
			
			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': 'combined_exp_model_' + flavour,
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]

def combine_expmodel_par(args=None, additional_dictionary=None):
	""" combine exp/model and parameterisation uncertainty to final uncertainty"""
	plots = []
	for flavour in pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, 'par_'+flavour+".root"),
				os.path.join(common.pdf_dir, 'combined_exp_model_'+flavour+".root"),
				pdf_unc_basefile.format(0),
			],
			'folders': [''],
			'x_expressions': ['par', 'expmodel', flavour],
			'nicks': ['par', 'expmodel', 'exp'],
			
			'analysis_modules': ['CombineTGraphs'],
			
			'combine_nick1': 'par',
			'combine_nick2': 'expmodel',
		
			'labels': ['par', 'expmodel', 'exp', 'expmodelpar'],
		
			'plot_modules': ['ExportRoot'],
			'output_dir': common.pdf_dir,
			'filename': 'combined_exp_model_par_' + flavour,
			'export_json': False,
		}
	
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def plot_pdf_uncs(args=None, additional_dictionary=None):
	""" plot the pdfs with all uncertainties"""
	#TODO plot with only total unc, but comparison for HERA and HERA+CMS
	plots = []
	title = "HERA-I DIS"
	text = r"$\\mathit{Q}^2 = 1.9 \\/ GeV^2$"
	y_lims = {
		'gluon': [0, 3],
	}
	for flavour in pdf_unc_flavours:
		d = {
			'files': [os.path.join(common.pdf_dir, 'combined_exp_model_par_'+flavour+".root")],
			'folders': [''],
			'x_expressions': ["exp", "expmodel", "expmodelpar"],
			'nicks': ["exp", "expmodel", "expmodelpar"],
	
			'analysis_modules': ['RelUncertainty'],
			'rel_nicks': ["exp", "expmodel", "expmodelpar"],

			'subplot_nicks': [i+'_rel' for i in ["exp", "expmodel", "expmodelpar"]],
			
			'labels': ['Exp. Unc.', 'Model Unc.', 'Par. Unc.']*3,

			'x_log': True,
			'y_subplot_lims': [-0.45, 0.45],
			'zorder': [30, 20, 10]*3,
			'markers': ['fill']*6,
			'grid': True,
			'subplot_grid': True,
			'line_styles': '-',
			'x_label': '$x$',
			'y_label': 'xfxQ2',
			'y_subplot_label': 'Rel. Uncertainty',
			'colors': ["orangered", "yellow", "green"]*3,
			
			'title': title,
			'texts': ["\n".join([flavour.replace("_", " "), text])],
			
			'filename': flavour + '_all-uncertainties',
		}
		if flavour in y_lims:
			d['y_lims'] = y_lims[flavour]
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]

