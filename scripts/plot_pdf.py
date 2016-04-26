#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""  plot pdf """

import ROOT
import matplotlib.pyplot as plt


def plot_pdf():
	"""main"""
	output_filename = "pdf.png"
	input_filename = "results/hera2/pdf_1_9_squared.root"
	rootfile = ROOT.TFile(input_filename, "READ")
	expmodelpar = rootfile.Get("expmodelpar")
	
	#TODO convert ROOT histo to mpl format
	
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.set_xlabel('x')
	ax.set_ylabel('PDF')
	ax.set_xlims(1e-4, 0.9)

	#TODO plot PDF

	fig.savefig(output_filename, bbox_inches='tight')
	plt.close()


if __name__ == "__main__":
	plot_pdf()
