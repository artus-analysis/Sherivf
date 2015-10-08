# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger

log = logging.getLogger(__name__)

import ROOT
import math
import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class CombineTGraphs(analysisbase.AnalysisBase):
	""" combine 2 tgraphs by adding their errors in quadrature"""

	def modify_argument_parser(self, parser, args):
		super(CombineTGraphs, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--combine-nick1", type=str)
		self.envelope_options.add_argument("--combine-nick2", type=str)

	def run(self, plotData=None):
		super(CombineTGraphs, self).run(plotData)

		graph_1 = plotData.plotdict["root_objects"][plotData.plotdict["combine_nick1"]]
		graph_2 = plotData.plotdict["root_objects"][plotData.plotdict["combine_nick2"]]
		graph = ROOT.TGraphAsymmErrors(graph_1)

		for i in range(graph.GetN()):
			# y errors low/high as difference to the min/max values
			graph.SetPointEYhigh(i, math.sqrt(graph_1.GetErrorYhigh(i)**2 + graph_2.GetErrorYhigh(i)**2))
			graph.SetPointEYlow(i, math.sqrt(graph_1.GetErrorYlow(i)**2 + graph_2.GetErrorYlow(i)**2))
			#print roottools.RootTools.scale_tgraph(graph, i)
			#print roottools.RootTools.scale_tgraph(graph_1, i)
			# x errors as half the bin width
			#graph.SetPointEXhigh(i-1, 0.5 * center_histo.GetBinWidth(i))
			#graph.SetPointEXlow(i-1, 0.5 * center_histo.GetBinWidth(i))

		plotData.plotdict["root_objects"]['combined'] = graph
		plotData.plotdict['nicks'].append('combined')
