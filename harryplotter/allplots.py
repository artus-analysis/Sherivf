#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, os, matplotlib

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


import plots_electron
import plots_fastnlo
import plots_pdf_reweighted
import plots_pdf
import plots_pdf_correlation
import plots_sherpa
import plots_bkgrs
import plots_zee_divide
import plots_uncertainties
import plots_unfolded
import plots_pdf_uncertainties
import branching
import plot_subprocs


def allplots(args=None):
	"""make allplots"""
	
	matplotlib.rcParams['lines.markersize'] = 10
	
	plotting_jobs = []

	parser = argparse.ArgumentParser()
	parser.add_argument('--www-dir', type=str, default="zee", help="www dir")
	parser.add_argument('--start', type=int, default=0, help="start")
	parser.add_argument('--end', type=int, default=999, help="end")
	parser.add_argument('--numbers', type=int, default=None, nargs='+', help="number")
	known_args, args = parser.parse_known_args(**({'args':args} if args is not None else {}))

	plot_min = known_args.start
	plot_max = known_args.end
	numbers = known_args.numbers

	functions = [
		plots_pdf.pdfs_thesis,  # 0
		plots_pdf_correlation.pdf_correlations,
		plots_electron.electron_id,
		plots_electron.electron_corr,
		plots_electron.electron_trigger_sf,
		plots_bkgrs.zee_bkgrs,  # 5
		plots_bkgrs.emu,
		plots_unfolded.different_iterations,
		plots_unfolded.response_matrix,
		plots_unfolded.unfolding_comparison,
		plots_sherpa.sherpa,  # 10
		plots_sherpa.sherpa_mc,
		plots_fastnlo.fastnlo_pdfsets,
		plots_pdf_uncertainties.plot_pdf_unc_comparison_all,
		plots_fastnlo.sherpa_fastnlo,
		plots_pdf_reweighted.nnpdf_zpt_10,  # 15
		plots_uncertainties.scale_pdf_uncertainties,
		plots_fastnlo.k_factors,
		plots_uncertainties.plot_uncertainties,
		plots_zee_divide.divided_ptspectrum,
		plots_pdf_uncertainties.plot_pdf_uncs_hera2,  # 20
		plots_pdf_uncertainties.plot_pdf_uncs_hera2_abszy,
		plots_pdf_uncertainties.plot_pdf_uncs_hera2_zpt,
		plots_pdf_uncertainties.plot_pdf_uncs_hera2_zpt_bins,
		plots_pdf_uncertainties.plot_pdf_unc_comparison_zpt,
		plots_bkgrs.signal_background_ratio,  # 25
		plots_electron.electron_scale_unc,
		plots_electron.z_hlt,
		plots_electron.electron_efficiencies_2d,
		plots_electron.electron_efficiencies_1d,
		plots_fastnlo.fastnlo_pdfmembers,  # 30
		plots_unfolded.unfolded_mc_comparison,
		plots_pdf_reweighted.nnpdf_zpt_91,
		plots_pdf_reweighted.nnpdf_zpt_2,
		plots_pdf_reweighted.nnpdf_abszy_2,
		plots_pdf_reweighted.nnpdf_abszy_10,  # 35
		plots_pdf_reweighted.nnpdf_abszy_91,
		branching.branching_ratio,
		plots_pdf_uncertainties.plot_pdf_unc_comparison_abszy,
		plots_pdf_uncertainties.plot_pdf_unc_comparison_zpt_bins,
		plots_pdf_reweighted.nnpdf_zpt_bins_2,  # 40
		plots_pdf_reweighted.nnpdf_zpt_bins_10,
		plots_pdf_reweighted.nnpdf_zpt_bins_91,
		plots_pdf_uncertainties.plot_pdf_unc_comparison_zy,
		plots_pdf_uncertainties.plot_pdf_uncs_hera2_zy,
		plot_subprocs.subprocs,  # 45
		plot_subprocs.production_channels,
		plots_unfolded.correlation_matrix,
		plots_pdf_reweighted.weights,
		plots_pdf_reweighted.alphas,
		plots_unfolded.stat_unf_contribution  # 50
	][plot_min:plot_max]

	wwwdirs = [
		"pdfs",
		"correlations",
		"electron_id",
		"electron_momentum_corrections",
		"electron_sf",
		"backgrounds",
		"emu",
		"unfolding_iteration",
		"unfolding_reponsematrices",
		"unfolding_comparisons",
		"sherpa",
		"sherpa_mc",
		"fastnlo_pdfsets",
		"pdf_all",
		"fastnlo_sherpa",
		"nnpdf_zpt_10",
		"scale_pdf_uncertainty",
		"k_factors",
		"uncertainties",
		"spectra_in_ybins",
		"pdf_uncertainties_hera2",
		"pdf_uncertainties_hera2_abszy",
		"pdf_uncertainties_hera2_zpt",
		"pdf_uncertainties_hera2_zpt_bins",
		"pdf_uncertainties_comparison_zpt",
		"backgrounds_signal_ratio",
		"electron_scale_uncertainty",
		"hlt",
		"electron_efficiencies_2d",
		"electron_efficiencies_1d",
		"fastnlo_pdfmembers",
		"unfolding_crosschecks",
		"nnpdf_zpt_91",
		"nnpdf_zpt_2",
		"nnpdf_abszy_2",
		"nnpdf_abszy_10",
		"nnpdf_abszy_91",
		"branching_ratio",
		"pdf_uncertainties_comparison_abszy",
		"pdf_uncertainties_comparison_zpt_bins",
		"nnpdf_zpt_bins_2",
		"nnpdf_zpt_bins_10",
		"nnpdf_zpt_bins_91",
		"pdf_uncertainties_comparison_zy",
		"pdf_uncertainties_hera2_zy",
		"subprocs",
		"subprocs",
		"correlation_matrix",
		"weights",
		"alphas",
		"stat_unf_contribution",
	][plot_min:plot_max]

	if numbers is not None:
		new_functions, new_wwwdirs = [], []
		for number in numbers:
			new_functions.append(functions[number])
			new_wwwdirs.append(wwwdirs[number])
		functions, wwwdirs = new_functions, new_wwwdirs
		#	wwwdirs = functions[number:number+1], wwwdirs[number:number+1]

	for function, wwwdir in zip(functions, wwwdirs):
		if function == plots_bkgrs.zee_bkgrs:
			plots = function(args + ["--no-njets", "--no-mcs"])
		elif function == plots_bkgrs.signal_background_ratio:
			plots = function(args + ["--no-njets"])
		else:
			plots = function(args)
		for plot in plots[0].plots:
			plot['www'] = os.path.join(known_args.www_dir, wwwdir)
		plotting_jobs += plots

	return plotting_jobs

