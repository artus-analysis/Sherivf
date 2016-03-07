#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convert fastNLO subproc file to root 6x6 TH2"""

import ROOT
import numpy


def main():

	# get subproc values
	filename = "/usr/users/dhaitz/home/qcd/sherivf/fastnlo/MCgrid_CMS_2015_Zee/MCgrid_CMS_2015_Zee.str.evtcount"
	f = open(filename, 'r')
	values = []
	for line in f.readlines():
		if ("Subproc" in line):
			values.append(int(line.replace("  ", " ").split(" ")[2]))

	# create TH2
	rf = ROOT.TFile(filename.replace('.evtcount', '.root'), 'RECREATE')
	th2 = ROOT.TH2F("name", "title", 11, -5.5, 5.5, 11, -5.5, 5.5)
	for i, value in enumerate(values):
		th2.SetBinContent(1+(i%11), 1+(i/11), value)

	# symmetrize
	for xbin in range(1, th2.GetNbinsX()+1):
		for ybin in range(1, th2.GetNbinsY()+1):
			if xbin > ybin:
				avg = 0.5 * (th2.GetBinContent(xbin, ybin) + th2.GetBinContent(ybin, xbin))
				th2.SetBinContent(xbin, ybin, avg)
				th2.SetBinContent(ybin, xbin, avg)

	rf.Write()
	rf.Close()
	print "Written to", filename.replace('.evtcount', '.root')


if __name__ == "__main__":
	main()
