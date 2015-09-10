#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob

import electron_plots
import fastnlo_plots
import nnpdf
import pdf
import pdf_correlation
import sherpa
import zee_bkgrs
import zee_divide
import zee_uncertainties
import zee_unfolded


def allplots(args=None):
	"""make allplots"""
	plotting_jobs = []
	wwwbase = 'zee'
	plot_min = 0
	plot_max = 99

	functions = [
		pdf.pdfs_thesis,
		pdf_correlation.pdf_correlations,
		electron_plots.electron_id,
		electron_plots.electron_corr,
		electron_plots.electron_trigger_sf,
		zee_bkgrs.zee_bkgrs,
		zee_bkgrs.emu,
		zee_unfolded.different_iterations,
		zee_unfolded.response_matrix,
		zee_unfolded.unfolding_comparison,
		sherpa.sherpa,
		sherpa.sherpa_mc,
		fastnlo_plots.fastnlo_pdfsets,
		fastnlo_plots.fastnlo_pdfmember,
		fastnlo_plots.sherpa_fastnlo,
		nnpdf.nnpdf,
	][plot_min:plot_max]
	
	wwwdirs = [
		"pdfs",
		"correlations",
		"electron_id",
		"momentum_corrections",
		"electron_sf",
		"backgrounds",
		"emu",
		"unfolding_iteration",
		"unfolding_reponsematrices",
		"unfolding_comparisons",
		"sherpa",
		"sherpa_mc",
		"fastnlo_pdfsets",
		"fastnlo_pdfmember",
		"fastnlo_sherpa",
		"nnpdf",
	][plot_min:plot_max]

	for function, wwwdir in zip(functions, wwwdirs):
		plots = function(args)
		for plot in plots[0].plots:
			plot['www'] = os.path.join(wwwbase, wwwdir)
		plotting_jobs += plots

	return plotting_jobs

