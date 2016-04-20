# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
from Excalibur.Plotting.utility.colors import histo_colors
import common


def pdf_comparison(args=None, additional_dictionary=None):
	""" PDF comparison for different PDF sets."""
	plots = []
	text  = r"$\\mathit{{Q}}{1} = {0} \\/ GeV{1}$".format(".".join(common.pdfq.split("_")[:2]), ("^2" if "squared" in common.pdfq else ""))
	for flavour in common.pdf_unc_flavours:
		pdfs = [
			["5_pdfunc/hera2_1_9_squared_combined_exp_model_par_{0}.root".format(flavour), "HERA", "expmodelpar"],
			["5_pdfunc/hera2_zpt_bins_1_9_squared_combined_exp_model_par_{0}.root".format(flavour), "HERA+CMS", "expmodelpar"],
			["pdf_sets/CT14nlo__1_9_squared.root", "CT14", flavour],
			["pdf_sets/NNPDF30_nlo_as_0118__1_9_squared.root", "NNPDF 3.0", flavour],
			# ["pdf_sets/HERAPDF15NLO_EIG__1_9_squared.root", "HERAPDF15NLO_EIG", flavour],
			# ["pdf_sets/HERAPDF20_NLO_EIG__1_9_squared.root", "HERAPDF20NLO_EIG", flavour],
		]
		d = {
			# input
			"files": [p[0] for p in pdfs],
			"x_expressions": [p[2] for p in pdfs],
			"folders": [""],
			# formatting
			"labels": [p[1] for p in pdfs],
			"legend": "upper left",
			"line_styles": ["-"],  # "line_styles": ["-", ":", "-.", "--"],
			"colors": ['black', histo_colors['red'], histo_colors['blue'], histo_colors['green']],
			"markers": [" "],
			"x_label": "x",
			"x_log": True,
			"y_errors": [False],
			"y_label": "xfxQ",
			"line_widths": [4],
			"texts": ["\n".join([flavour.replace("_", " "), text])],
			# output
			"filename": "pdf_comparison_"+flavour,
		}
		if flavour == "gluon":
			d["y_lims"] = [0.0, 3.5]
			d["legend"] = "upper right"
		elif "valence" in flavour:
			d["legend"] = "center left"
		elif flavour == "sea_quarks":
			d["legend"] = "upper right"
			d["y_lims"] = [0, 3.2]
		plots.append(d)
	return [PlottingJob(plots, args)]
