#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
import array
import os

def main():
	"""http://arxiv.org/pdf/1502.02701v1.pdf, Fig 14a"""
	xbins = [5, 15, 22, 28, 34, 40, 46, 52, 58, 64, 300]
	ybins = [0, 0.8, 1.5, 2.5]
	histo = ROOT.TH2D("name", "title", len(xbins)-1, array.array('d', xbins), len(ybins)-1, array.array('d', ybins))
	outfile = ROOT.TFile(os.environ["EXCALIBURPATH"] + "/data/electron_scalefactors/ElectronPtVariation.root", "RECREATE")

	values = [
		[9,  5, 1, 4,4,5,5,9,7,9],
		[16, 8, 7, 1,4,5,4,8,9,9],
		[30,21,16,10,2,1,2,4,6,10],
	]

	for iy in range(1, len(ybins)):
		for ix in range(1, len(xbins)):
			histo.SetBinContent(ix, iy, 1e-4*values[iy-1][ix-1])

	histo.Write("mc")
	outfile.Close()

if __name__ == "__main__":
	main()
