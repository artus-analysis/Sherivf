#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, os

from Excalibur.Plotting.utility.toolsZJet import PlottingJob

import electron_plots
import fastnlo_plots
import pdf_reweighted
import pdf
import pdf_correlation
import sherpa
import zee_bkgrs
import zee_divide
import zee_uncertainties
import zee_unfolded
import pdf_uncertainties


def allplots(args=None):
	"""make allplots"""
	plotting_jobs = []

	parser = argparse.ArgumentParser()
	parser.add_argument('--www-dir', type=str, default="zee", help="www dir")
	parser.add_argument('--start', type=int, default=0, help="start")
	parser.add_argument('--end', type=int, default=999, help="end")
	known_args, args = parser.parse_known_args(**({'args':args} if args is not None else {}))

	plot_min = known_args.start
	plot_max = known_args.end

	functions = [
		pdf.pdfs_thesis,  # 0
		pdf_correlation.pdf_correlations,
		electron_plots.electron_id,
		electron_plots.electron_corr,
		electron_plots.electron_trigger_sf,
		zee_bkgrs.zee_bkgrs,  # 5
		zee_bkgrs.emu,
		zee_unfolded.different_iterations,
		zee_unfolded.response_matrix,
		zee_unfolded.unfolding_comparison,
		sherpa.sherpa,  # 10
		sherpa.sherpa_mc,
		fastnlo_plots.fastnlo_pdfsets,
		fastnlo_plots.fastnlo_pdfmember,
		fastnlo_plots.sherpa_fastnlo,
		pdf_reweighted.nnpdf,  # 15
		pdf_reweighted.herapdf_14,
		pdf_reweighted.herapdf_912,
		zee_uncertainties.plot_uncertainties,
		zee_divide.divided_ptspectrum,
		pdf_uncertainties.plot_pdf_uncs_hera,  # 20
		pdf_uncertainties.plot_pdf_uncs_heraZ,
		pdf_uncertainties.plot_pdf_unc_comparison,
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
		"herapdf_14",
		"herapdf_912",
		"uncertainties",
		"spectra_in_ybins",
		"pdf_uncertainties_hera",
		"pdf_uncertainties_heraZ",
		"pdf_uncertainties_comparison",
	][plot_min:plot_max]

	for function, wwwdir in zip(functions, wwwdirs):
		if function == zee_bkgrs.zee_bkgrs:
			plots = function(args + ["--no-njets", "--no-ybins", "--no-mcs"])
		else:
			plots = function(args)
		for plot in plots[0].plots:
			plot['www'] = os.path.join(known_args.www_dir, wwwdir)
		plotting_jobs += plots

	return plotting_jobs

