#  -*- coding: utf-8 -*-

"""
create xFitter correlation files from TH2 correlation matrix

"""

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import os

import Artus.HarryPlotter.plotbase as plotbase
import Artus.HarryPlotter.plotdata as plotdata


class CorrelationContainer(plotdata.PlotContainer):
	def __init__(self):
		self.string = ""

	def save(self, filename):
		with open(filename, "w") as output_file:
			output_file.write(self.string)


class ExportCorrelation(plotbase.PlotBase):
	"""Create Correlation data files."""

	def modify_argument_parser(self, parser, args):
		super(ExportCorrelation, self).modify_argument_parser(parser, args)
		self.plotting_options.add_argument("--export-corr-quantity", type=str,
		    help="quantity [Default: %(default)s].")

	def prepare_args(self, parser, plotData):
		plotData.plotdict["formats"] = ["corr"]
		super(ExportCorrelation, self).prepare_args(parser, plotData)

	def create_canvas(self, plotData):
		plotData.plot = CorrelationContainer()
		plotData.plot.string = """&StatCorr
   Name1 = 'CMS Zee'
   Name2 = 'CMS Zee'

   NIdColumns1 = 2
   NIdColumns2 = 2

   IdColumns1 = '@QUANTITY@low', '@QUANTITY@high'
   IdColumns2 = '@QUANTITY@low', '@QUANTITY@high'

   NCorr = @NCORR@

   MatrixType = 'Statistical correlations'
&End
"""

	def make_plots(self, plotData):
		histo = plotData.plotdict["root_objects"].values()[0]

		NCorr = histo.GetNbinsX() * histo.GetNbinsY()
		plotData.plot.string = plotData.plot.string.replace('@NCORR@', str(NCorr))
		if plotData.plotdict["export_corr_quantity"]:
			plotData.plot.string = plotData.plot.string.replace('@QUANTITY@', plotData.plotdict["export_corr_quantity"])

		# add bin border and correlation values
		for xbin in range(1, histo.GetNbinsX()+1):
			for ybin in range(1, histo.GetNbinsY()+1):
				xcenter = histo.GetXaxis().GetBinCenter(xbin)
				xerr = histo.GetXaxis().GetBinWidth(xbin) / 2.
				ycenter = histo.GetYaxis().GetBinCenter(ybin)
				yerr = histo.GetYaxis().GetBinWidth(ybin) / 2.
				plotData.plot.string += " ".join([str(x) for x in [xcenter-xerr, xcenter+xerr, ycenter-yerr, ycenter+yerr, histo.GetBinContent(xbin, ybin)]]) + "\n"

