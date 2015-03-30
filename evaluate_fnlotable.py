#!/usr/bin/env python

"""
	Script to evalute fastNLO tables.
	Written by gsieber, modified by dhaitz 
	2015
"""

from array import array
import numpy as np
import math
 
import fastnlo
from fastnlo import fastNLOLHAPDF
 
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from ROOT import TFile


def main(
		n=0,
		input_filename='fnlo_yZ.txt',
		pdf_set='../NNPDF21_100.LHgrid',#'CT10nlo.LHgrid',
	):

	# init fnlo
	fnlo = fastNLOLHAPDF(input_filename)
	fnlo.SetLHAPDFFilename(pdf_set)
	fnlo.SetLHAPDFMember(n)
	output_filename = "histo_{}.root".format(n)
	output_filename = "histo.root"

	print "PDF member:", n, "  output_filename:", output_filename

	# make histo
	x_binning = sorted(list(set([item for sublist in fnlo.GetDim0BinBoundaries() for item in sublist])))
	histo = ROOT.TH1D(str(n),str(n),len(x_binning)-1, array('d', x_binning))

	lumi = 19879

	# fill values
	xs = np.array(fnlo.GetCrossSection())
	print xs
	xs[xs <= 0.] = 0.  # ?
	for i in range(0, fnlo.GetNDim0Bins()):
		histo.SetBinContent(i+1, lumi*xs[i])
		#histo.SetBinError(i+1, math.sqrt(xs[i]))

	# save
	out = TFile(output_filename, "RECREATE")
	histo.Write()
 
if __name__ == '__main__':
	main()
