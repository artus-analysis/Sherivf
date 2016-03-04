# -*- coding: utf-8 -*-

import argparse
import common
import os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob

pdfname = "hf_pdf"

def make_pdf_unc(args=None, additional_dictionary=None, scenario='hera'):
	""" make pdf uncertainties """
	parser = argparse.ArgumentParser()
	parser.add_argument('--scenario', default='hera2', help="scenario")
	parser.add_argument('--pdfq', default="1_9_squared")
	known_args, args = parser.parse_known_args(**({'args':args} if args is not None else {}))

	return (model_unc(args, additional_dictionary, known_args.scenario, known_args.pdfq)
		+ par_unc(args, additional_dictionary, known_args.scenario, known_args.pdfq)
		+ combine_exp_model(args, additional_dictionary, known_args.scenario, known_args.pdfq)
		+ combine_expmodel_par(args, additional_dictionary, known_args.scenario, known_args.pdfq))


def model_unc(args=None, additional_dictionary=None, pdf_scenario='hera', pdfq='1_9_squared'):
	"""get model uncertainties"""
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_"+pdfname+"__"+pdfq+".root"
	n_max = 9
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
			'filename': '_'.join([pdf_scenario, pdfq, 'model', flavour]),
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


def par_unc(args=None, additional_dictionary=None, pdf_scenario='hera', pdfq='1_9_squared'):
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_"+pdfname+"__"+pdfq+".root"
	"""get parametrisation uncertainties"""
	variations = [0] + range(9, 19)
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
			'filename': '_'.join([pdf_scenario, pdfq, 'par', flavour]),
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]



def combine_exp_model(args=None, additional_dictionary=None, pdf_scenario='hera', pdfq='1_9_squared'):
	""" combine model and experimental"""
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_"+pdfname+"__"+pdfq+".root"
	plots = []
	for flavour in common.pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, "_".join([pdf_scenario, pdfq, 'model',flavour])+".root"),
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
			'filename': "_".join([pdf_scenario, pdfq, 'combined', 'exp', 'model', flavour]),
			'export_json': False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]

def combine_expmodel_par(args=None, additional_dictionary=None, pdf_scenario='hera', pdfq='1_9_squared'):
	""" combine exp/model and parameterisation uncertainty to final uncertainty"""
	pdf_unc_basefile = common.results_dir+pdf_scenario+ "/job_{}_"+pdfname+"__"+pdfq+".root"
	plots = []
	for flavour in common.pdf_unc_flavours:
		d = {
			'files': [
				os.path.join(common.pdf_dir, "_".join([pdf_scenario, pdfq, 'par', flavour])+".root"),
				os.path.join(common.pdf_dir, "_".join([pdf_scenario, pdfq, 'combined', 'exp', 'model', flavour])+".root"),
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
			'filename': "_".join([pdf_scenario, pdfq, 'combined', 'exp', 'model', 'par', flavour]),
			'export_json': False,
		}
	
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]
