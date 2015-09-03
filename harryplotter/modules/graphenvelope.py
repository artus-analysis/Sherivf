# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger
import ROOT

log = logging.getLogger(__name__)

import ROOT
import Artus.HarryPlotter.analysisbase as analysisbase


class GraphEnvelope(analysisbase.AnalysisBase):

	def modify_argument_parser(self, parser, args):
		super(GraphEnvelope, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--envelope-nicks", nargs="+", default=None, help="")
		self.envelope_options.add_argument("--envelope-center-nick", default=None, help="")

	def run(self, plotData=None):
		super(GraphEnvelope, self).run(plotData)

		center_histo = plotData.plotdict["root_objects"][plotData.plotdict["envelope_center_nick"]]
		graph = ROOT.TGraphErrors(center_histo.GetNbinsX())

		for i in range(1, center_histo.GetNbinsX()+1):
			values = []
			for nick in plotData.plotdict['envelope_nicks']:
				values.append(plotData.plotdict["root_objects"][nick].GetBinContent(i))
			graph.SetPoint(i-1, center_histo.GetBinCenter(i), center_histo.GetBinContent(i))
			graph.SetPointError(i-1, max(values) - center_histo.GetBinContent(i), center_histo.GetBinContent(i) - min(values))

		plotData.plotdict["root_objects"]['envelope'] = graph
		plotData.plotdict['nicks'].append('envelope')
