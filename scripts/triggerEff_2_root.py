#!/usr/bin/env python

"""
	Script to convert the txt files from [1] into root files.
	[1] http://lovedeep.web.cern.ch/lovedeep/WORK13/TnPRun2012ReReco_2013Oct28/intro.html
"""

import argparse
import array

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True


def main(
		input_filename='effiGsfIdTightData.txt',
		output_filename=None,
	):
	if output_filename is None:
		output_filename = input_filename.replace('.txt', '.root')
	txtfile = open(input_filename , "r" )
	content = txtfile.readlines()
	
	# get binning
	xbins, ybins = [], []
	for line in content[7:]:
		values = [float(item) for item in line.split()]
		xbins += values[:2]
		ybins += values[2:4]
	xbins = sorted(list(set(xbins)))
	ybins = sorted(list(set(ybins)))

	#create histo
	histo = ROOT.TH2D('name', 'title',
		len(xbins)-1, array.array('d', xbins),
		len(ybins)-1, array.array('d', ybins),
	)

	# get values and fill
	# TODO: errors
	for line in content[7:]:
		values = [float(item) for item in line.split()]
		x = 0.5 * (values[1] + values[0])
		y = 0.5 * (values[3] + values[2])
		eff = values[4]
		histo.Fill(x, y, eff)

	# write
	out_file = ROOT.TFile(output_filename, "RECREATE")
	histo.Write()
	out_file.Close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input-filename', type=str, default=argparse.SUPPRESS)
	opt = parser.parse_args()
	main(**vars(opt))
