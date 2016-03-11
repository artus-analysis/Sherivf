# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import ROOT
import copy

import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class RelUncertainty(analysisbase.AnalysisBase):
	"""Relative Uncertainty (bin content -> 0; error -> error/content)"""

	def modify_argument_parser(self, parser, args):
		super(RelUncertainty, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--rel-nicks", nargs="+", default=None, help="")

	def prepare_args(self, parser, plotData):
		if plotData.plotdict['rel_nicks'] is None:
			plotData.plotdict['rel_nicks'] = copy.deepcopy(plotData.plotdict['nicks'])

	def run(self, plotData=None):
		super(RelUncertainty, self).run(plotData)

		for nick in plotData.plotdict['rel_nicks']:
			log.debug("Rel uncertainty for nick "+nick)
			orig = plotData.plotdict["root_objects"][nick]
			graph = ROOT.TGraphAsymmErrors()
			if isinstance(orig, ROOT.TH1):
				for i in range(1, orig.GetNbinsX()+1):
					graph.SetPoint(i-1, orig.GetBinCenter(i), 0)
					try:
						graph.SetPointError(i-1, 0, orig.GetBinError(i)/orig.GetBinContent(i))
					except ZeroDivisionError:
						graph.SetPointError(i-1, 0, 0)
			elif isinstance(orig, ROOT.TGraph):
				for i in range(orig.GetN()):
					x, y = roottools.RootTools.tgraph_get_point(orig, i)
					graph.SetPoint(i, x, 0)
					try:
						graph.SetPointEYhigh(i, orig.GetErrorYhigh(i)/y)
						graph.SetPointEYlow(i, orig.GetErrorYlow(i)/y)
					except ZeroDivisionError:
						graph.SetPointEYhigh(i, 0)
						graph.SetPointEYlow(i, 0)
					graph.SetPointEXhigh(i, orig.GetErrorXhigh(i))
					graph.SetPointEXlow(i, orig.GetErrorXlow(i))
			else:
				pass # TODO TProfiles?
			new_nick = nick+"_rel"
			plotData.plotdict["root_objects"][new_nick] = graph
			plotData.plotdict['nicks'].append(new_nick)
