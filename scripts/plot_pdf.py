#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""plot a PDF. From http://lhapdf.hepforge.org/codeexamples.html"""

import lhapdf
import numpy as np
import ROOT

import matplotlib.pyplot as plt

partondict = {
    0: 'gluon',
    21: 'gluon',
    -1: 'd antiquark',
    -2: 'u antiquark',
    #            -3 : 'sbar',
    #            -4 : 'cbar',
    #            -5 : 'bbar',
    #            -6 : 'tbar',
    1: 'd quark',
    2: 'u quark',
    #            3 : 'strange',
    #            4 : 'charm',
    #            5 : 'bottom',
    #            6 : 'top',
    7: 'd valence quark',
    8: 'u valence quark',
    9: 'sea quarks',
}


## Version info, search paths, and metadata
print "LHAPDF version", lhapdf.version()
lhapdf.pathsPrepend("/path/to/extra/pdfsets")
print "LHAPDF paths",lhapdf.paths()


pdf_set = "NNPDF23_nlo_as_0118"
#pdf_set = "NNPDF23_nlo_as_0118_HighStat_chi2_nRep100"
print "PDFset:", pdf_set
# TODO: demonstrate looping over PDF set members
pset = lhapdf.getPDFSet(pdf_set)
print "PDFset description", pset.description

flavour = 0

max_values = []
mean_values = []
min_values = []
x_values = np.logspace(-4, -0.0001, 100)

for x in x_values:
	pdf_values = []
	for i_member in range(101):
		p = pset.mkPDF(i_member)
		pdf_values.append(p.xfxQ(0, x, 91.2))
	max_values.append(max(pdf_values))
	min_values.append(min(pdf_values))
	mean_values.append(0.5*(min(pdf_values)+max(pdf_values)))


output_filename = "out.root"
out = ROOT.TFile(output_filename, "RECREATE")
tgraph = ROOT.TGraphErrors()
for i, (x, mean_value, min_value) in enumerate(zip(x_values, mean_values, min_values)):
	tgraph.SetPoint(i, x, mean_value)
	tgraph.SetPointError(i,0, mean_value-min_value)
tgraph.Write(partondict[flavour].replace(' ', '_'))
out.Close()

