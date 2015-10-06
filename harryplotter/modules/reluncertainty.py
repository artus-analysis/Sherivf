# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger
import ROOT

log = logging.getLogger(__name__)

import ROOT
import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class RelUncertainty(analysisbase.AnalysisBase):

	def modify_argument_parser(self, parser, args):
		super(RelUncertainty, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--rel-nicks", nargs="+", default=None, help="")

	def run(self, plotData=None):
		super(RelUncertainty, self).run(plotData)

		for nick in plotData.plotdict['rel_nicks']:
			orig = plotData.plotdict["root_objects"][nick]
			graph = ROOT.TGraphAsymmErrors()
			try:  # TH
				n_bins = orig.GetNbinsX()
			except AttributeError:  # TGraph
				n_bins = orig.GetN()

			for i in range(1, n_bins+1):
				try:  # TH
					graph.SetPoint(i-1, orig.GetBinCenter(i), 0)
				except AttributeError:  # TGraph
					x, y = roottools.RootTools.tgraph_get_point(orig, i-1)
					graph.SetPoint(i-1, x, 0)
				try:  # TH
					graph.SetPointError(i-1, 0, orig.GetBinError(i)/orig.GetBinContent(i))
				except AttributeError:  # TGraph
					x, y = roottools.RootTools.tgraph_get_point(orig, i-1)
					try:
						graph.SetPointEYhigh(i-1, orig.GetErrorYhigh(i-1)/y)
						graph.SetPointEYlow(i-1, orig.GetErrorYlow(i-1)/y)
					except ZeroDivisionError:
						graph.SetPointEYhigh(i-1, 0)
						graph.SetPointEYlow(i-1, 0)
				except ZeroDivisionError:
					graph.SetPointError(i-1, 0, 0)


			new_nick = nick+"_rel"
			plotData.plotdict["root_objects"][new_nick] = graph
			plotData.plotdict['nicks'].append(new_nick)
