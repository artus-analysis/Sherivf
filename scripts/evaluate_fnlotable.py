#!/usr/bin/env python

"""
	Script to evalute fastNLO tables.
	Written by gsieber, modified by dhaitz 
	2015
"""

from array import array
import numpy as np
import math
import argparse
 
import fastnlo
from fastnlo import fastNLOLHAPDF
 
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from ROOT import TFile


def main(
		n=0,
		input_filename='fnlo_yZ.txt',
		pdf_set=(
			#'../NNPDF21_100.LHgrid'
			'CT10nlo.LHgrid'
		),
		lumi = 19789,  # in 1/pb
	):

	# init fnlo
	fnlo = fastNLOLHAPDF(input_filename)
	fnlo.SetLHAPDFFilename(pdf_set)
	fnlo.SetLHAPDFMember(n)
	fnlo.CalcCrossSection()
	output_filename = input_filename.replace(".txt", ".root")
	out = TFile(output_filename, "RECREATE")


	print "PDF member:", n, "  output_filename:", output_filename

	# make histo
	x_binning = sorted(list(set([item for sublist in fnlo.GetDim0BinBounds() for item in sublist])))
	histo = ROOT.TH1D(str(n),str(n),len(x_binning)-1, array('d', x_binning))


	# fill values for central xsec
	xs = np.array(fnlo.GetCrossSection())
	xs[xs <= 0.] = 0.  # ?
	for i in range(0, fnlo.GetNDim0Bins()):
		histo.SetBinContent(i+1, lumi*xs[i])  # multiply with lumi to get event count
	histo.Write()


	# errors for PDF variations
	print "Calulating errors for {} PDF variations".format(fnlo.GetNPDFMembers() - 1)
	errors = [0.] * len(x_binning)
	for i in range(1, fnlo.GetNPDFMembers()):
		fnlo.SetLHAPDFMember(i)
		fnlo.CalcCrossSection()
		xsec = fnlo.GetCrossSection()
		for j in range(len(xsec)):
			errors[j] += ((xsec[j]-xs[j])/xs[j])**2 # sum up errors in QUADRATURE
	for i, quad_error in enumerate(errors):
		errors[i] = math.sqrt(quad_error) # root of squared errors

	# put PDF errors in graph
	pdf_uncertainty = ROOT.TGraph()
	pdf_uncertainty.SetName("pdf_uncertainty")
	for i, error in enumerate(errors):
		pdf_uncertainty.SetPoint(i, x_binning[i], error)

	pdf_uncertainty.Write()


	if False:  # dont use for now
		# scale uncertainties
		variations = [0.5, 1, 2]
		errors = [0.] * len(x_binning)
		for mur in variations:
			for muf in variations:
				fnlo.SetScaleFactorsMuRMuF(mur, muf)
				fnlo.CalcCrossSection()
				xsec = fnlo.GetCrossSection()
				for i, xsec_bin in xsec:
					errors[i] = max(errors[i], abs(xsec_bin -xs[i])/xs[i])

		# put scale errors in graph
		scale_uncertainty = ROOT.TGraph()
		scale_uncertainty.SetName("scale_uncertainty")
		for i, error in enumerate(errors):
			scale_uncertainty.SetPoint(i, x_binning[i], error)

		scale_uncertainty.Write()


	# finish
	print "histogram written to file", output_filename
	out.Close()
 
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input-filename', type=str, default=argparse.SUPPRESS)
	parser.add_argument('-p', '--pdf-set', type=str, default=argparse.SUPPRESS)
	opt = parser.parse_args()
	main(**vars(opt))
