# -*- coding: utf-8 -*-

import argparse
import common
import os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def make_pdf_unc(args=None, additional_dictionary=None, scenario='hera'):
	""" make pdf uncertainties """
	parser = argparse.ArgumentParser()
	parser.add_argument('--scenario', default='hera2', help="scenario")
	known_args, args = parser.parse_known_args(**({'args':args} if args is not None else {}))

	return (model_unc(args, additional_dictionary, known_args.scenario)
		+ par_unc(args, additional_dictionary, known_args.scenario)
		+ combine_exp_model(args, additional_dictionary, known_args.scenario)
		+ combine_expmodel_par(args, additional_dictionary, known_args.scenario))


def model_unc(args=None, additional_dictionary=None, pdf_scenario='hera'):
	"""get model uncertainties"""
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_herapdf__1_9_squared.root"
	n_max = 9
	q_squared = 1.9
	exp_unc = 'exp_unc'
	nicks = ["nick"+str(i) for i in range(n_max)]
	plots = []
	for flavour in common.pdf_unc_flavours:
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
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_herapdf__1_9_squared.root"
	"""get parametrisation uncertainties"""
	variations = [0] + range(9, 20)
	q_squared = 1.9
	exp_unc = 'exp_unc'
	nicks = ["nick"+str(i) for i in variations]
	plots = []
	for flavour in common.pdf_unc_flavours:
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
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_herapdf__1_9_squared.root"
	plots = []
	for flavour in common.pdf_unc_flavours:
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
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_herapdf__1_9_squared.root"
	plots = []
	for flavour in common.pdf_unc_flavours:
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
