# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
#import calculate_correlation
import common

def pdf_comparison(args=None, additional_dictionary=None):
	""" PDF comparison for different PDF sets."""
	plots = []
	
	for flavour in common.pdf_unc_flavours:
		pdfs = [
			["5_pdfunc/hera2_1_9_squared_combined_exp_model_par_{0}.root".format(flavour), "HERA", "expmodelpar"],
			["5_pdfunc/hera2_zpt_bins_1_9_squared_combined_exp_model_par_{0}.root".format(flavour), "HERA+CMS", "expmodelpar"],
			["pdf_sets/CT14nlo__1_9_squared.root", "CT14", flavour],
			["pdf_sets/NNPDF30_nlo_as_0118__1_9_squared.root", "NNPDF3.0", flavour],
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
			"markers": [" "],
			"x_label": "x",
			"x_log": True,
			"y_errors": [False],
			"y_label": "xfx",
			"line_widths": [4],
			"title": flavour.replace("_", " "),
			# output
			"filename": "pdf_comparison_"+flavour,
		}
		if flavour == "gluon":
			d["y_lims"] = [0.0, 3.0]
		elif flavour == "sea_quarks":
			d["legend"] = "upper right"
		plots.append(d)
	return [PlottingJob(plots, args)]
