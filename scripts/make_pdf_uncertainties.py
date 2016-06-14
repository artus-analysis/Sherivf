#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""calculate model/parametrization/total uncertainties from single job outputs"""

import math
import sherivftools

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gErrorIgnoreLevel = ROOT.kError


q_values = ['1_9_squared', '10_0_squared', '91_2']

def make_pdf_uncertainties(central, model, parametrization, output=None):
	"""main"""
	output_filename = (output or "pdf.root")
	file_created = False
	
	for flavour in ['gluon', 'd_valence_quark', 'u_valence_quark', 'sea_quarks']:

		# get root objects
		exp = get_root_histo(central, flavour)
		models = [get_root_histo(m, flavour) for m in model]
		parametrizations = [get_root_histo(p, flavour) for p in parametrization]

		# get envelops from different jobs
		mod = make_envelope(exp, models)
		par = make_envelope(exp, parametrizations)

		# add quadratically 
		exp_mod = combine_tgraphs([exp, mod])
		exp_mod_par = combine_tgraphs([exp_mod, par])

		# save
		out = ROOT.TFile(output_filename, ("UPDATE" if file_created else "RECREATE"))
		file_created = True
		for obj in ["exp", "mod", "par", "exp_mod", "exp_mod_par"]:
			eval(obj).Write(obj+"_"+flavour)
		print flavour, "PDF written to", output_filename
		out.Close()



def get_root_histo(filename, flavour):
	"""open file, return ROOT histo"""
	rfile = ROOT.TFile(filename, "READ")
	histo = rfile.Get(flavour)
	return histo



def make_envelope(central, objects):
	center_histo = central
	n_bins = center_histo.GetN()
	
	graph = ROOT.TGraphAsymmErrors(n_bins)

	for i in range(1, n_bins+1):
		values = []
		for obj in objects:
			xvalue, value = sherivftools.tgraph_get_point(obj, i-1)
			values.append(value)
		x, y = sherivftools.tgraph_get_point(center_histo, i-1)
		graph.SetPoint(i-1, x, y)
		# y errors low/high as difference to the min/max values
		graph.SetPointEYhigh(i-1, max(values) - y)
		graph.SetPointEYlow(i-1, y - min(values))
		# x errors as half the bin width
		width = center_histo.GetErrorX(i-1)
		graph.SetPointEXhigh(i-1, 0.5 * width)
		graph.SetPointEXlow(i-1, 0.5 * width)
	return graph


def combine_tgraphs(root_objects):
	graph = ROOT.TGraphAsymmErrors(root_objects[0])

	for i in range(graph.GetN()):
		error_low, error_high = 0., 0.
		for histogram in root_objects:
			error_high += histogram.GetErrorYhigh(i)**2
			error_low += histogram.GetErrorYlow(i)**2
		error_high = math.sqrt(error_high)
		error_low = math.sqrt(error_low)
		graph.SetPointEYhigh(i, error_high)
		graph.SetPointEYlow(i, error_low)
	return graph



if __name__ == "__main__":

	for q in q_values:
		base = "job_{}_hf_pdf__" + q + ".root"
		output_filename = "pdf_" + q + ".root"
		make_pdf_uncertainties(
			base.format("0"),
			[base.format(str(n)) for n in range(1, 9)],
			[base.format(str(n)) for n in range(9, 19)],
			output_filename
		)

