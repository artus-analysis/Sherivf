# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import ROOT
import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class UncDiff(analysisbase.AnalysisBase):
	"""Diff of uncertainties"""

	def modify_argument_parser(self, parser, args):
		super(UncDiff, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--unc-diff-nicks", nargs="+", default=None, help="")

	def run(self, plotData=None):
		super(UncDiff, self).run(plotData)

		ng = ROOT.TGraph()
		tg1, tg2 = [plotData.plotdict["root_objects"][nick] for nick in plotData.plotdict["unc_diff_nicks"]]
		for i in range(1, tg1.GetN()+1):
			diff = (tg2.GetErrorYhigh(i) + tg2.GetErrorYlow(i)) -  (tg1.GetErrorYhigh(i) + tg1.GetErrorYlow(i))
			x, y = roottools.RootTools.tgraph_get_point(tg1, i)
			ng.SetPoint(i, x, diff)

		new_nick = 'unc_diff'
		plotData.plotdict["root_objects"][new_nick] = ng
		plotData.plotdict['nicks'].append(new_nick)
