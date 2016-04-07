# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger
import ROOT

log = logging.getLogger(__name__)

import ROOT
import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools

class GraphEnvelope(analysisbase.AnalysisBase):
	"""construct new tgraph from envelop of graphs"""

	def modify_argument_parser(self, parser, args):
		super(GraphEnvelope, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--envelope-nicks", nargs="+", default=None, help="")
		self.envelope_options.add_argument("--envelope-center-nick", default=None, help="")

	def run(self, plotData=None):
		super(GraphEnvelope, self).run(plotData)

		center_histo = plotData.plotdict["root_objects"][plotData.plotdict["envelope_center_nick"]]
		try:
			n_bins = center_histo.GetNbinsX()
		except AttributeError:
			n_bins = center_histo.GetN()
		
		graph = ROOT.TGraphAsymmErrors(n_bins)

		for i in range(1, n_bins+1):
			values = []
			for nick in plotData.plotdict['envelope_nicks']:
				try:
					value = plotData.plotdict["root_objects"][nick].GetBinContent(i)
				except AttributeError:
					xvalue, value = roottools.RootTools.tgraph_get_point(plotData.plotdict["root_objects"][nick], i-1)
				values.append(value)
			try:
				x = center_histo.GetBinCenter(i)
				y = center_histo.GetBinContent(i)
			except AttributeError:
				x, y = roottools.RootTools.tgraph_get_point(center_histo, i-1)
			graph.SetPoint(i-1, x, y)
			# y errors low/high as difference to the min/max values
			graph.SetPointEYhigh(i-1, max(values) - y)
			graph.SetPointEYlow(i-1, y - min(values))
			# x errors as half the bin width
			try:
				width = center_histo.GetBinWidth(i)
			except AttributeError:
				width = center_histo.GetErrorX(i-1)
			
			graph.SetPointEXhigh(i-1, 0.5 * width)
			graph.SetPointEXlow(i-1, 0.5 * width)

		plotData.plotdict["root_objects"]['envelope'] = graph
		plotData.plotdict['nicks'].append('envelope')
