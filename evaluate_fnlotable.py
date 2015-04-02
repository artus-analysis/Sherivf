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
		pdf_set='../NNPDF21_100.LHgrid',#'CT10nlo.LHgrid',
		lumi = 19789,  # in 1/pb
	):

	# init fnlo
	fnlo = fastNLOLHAPDF(input_filename)
	fnlo.SetLHAPDFFilename(pdf_set)
	fnlo.SetLHAPDFMember(n)
	output_filename = input_filename.replace(".txt", ".root")

	print "PDF member:", n, "  output_filename:", output_filename

	# make histo
	x_binning = sorted(list(set([item for sublist in fnlo.GetDim0BinBoundaries() for item in sublist])))
	histo = ROOT.TH1D(str(n),str(n),len(x_binning)-1, array('d', x_binning))


	# fill values
	xs = np.array(fnlo.GetCrossSection())
	print xs
	xs[xs <= 0.] = 0.  # ?
	for i in range(0, fnlo.GetNDim0Bins()):
		histo.SetBinContent(i+1, lumi*xs[i])  # multiply with lumi to get event count

	# save
	out = TFile(output_filename, "RECREATE")
	histo.Write()
	print "histogram written to file", output_filename
 
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input-filename', type=str, default=argparse.SUPPRESS)
	opt = parser.parse_args()

	main(**vars(opt))
