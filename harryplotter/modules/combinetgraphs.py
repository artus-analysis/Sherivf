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
		self.envelope_options.add_argument("--combine-nicks", type=str, nargs="+")
		#self.envelope_options.add_argument("--combine-nick2", type=str)

	def run(self, plotData=None):
		super(CombineTGraphs, self).run(plotData)

		root_objects = [plotData.plotdict["root_objects"][nick] for nick in plotData.plotdict["combine_nicks"]]
		graph = False
		for root_object in root_objects:
			if isinstance(root_object, ROOT.TGraphAsymmErrors):
				graph = ROOT.TGraphAsymmErrors(root_object)
		if not graph:
			if isinstance(root_objects[0], ROOT.TH1):
				histo = root_objects[0]
				graph = ROOT.TGraphAsymmErrors(histo.GetNbinsX())
				for i in range(histo.GetNbinsX()):
					graph.SetPoint(i, histo.GetBinCenter(i+1), 0)
					graph.SetPointEXlow(i, histo.GetBinWidth(i+1)/2.)
					graph.SetPointEXhigh(i, histo.GetBinWidth(i+1)/2.)
			else:
				pass #TODO warn
				
				
		for i in range(graph.GetN()):
			error_low, error_high = 0., 0.
			for histogram in root_objects:
				if isinstance(histogram, ROOT.TGraphAsymmErrors):
					error_high += histogram.GetErrorYhigh(i)**2
					error_low += histogram.GetErrorYlow(i)**2
				elif isinstance(histogram, ROOT.TGraph):
					error_high += histogram.GetErrorY(i)**2
					error_low += histogram.GetErrorY(i)**2
				elif isinstance(histogram, ROOT.TH1):
					error_high += histogram.GetBinError(i+1)**2
					error_low += histogram.GetBinError(i+1)**2
					
			error_high = math.sqrt(error_high)
			error_low = math.sqrt(error_low)
			
			graph.SetPointEYhigh(i, error_high)
			graph.SetPointEYlow(i, error_low)

		plotData.plotdict["root_objects"]['combined'] = graph
		plotData.plotdict['nicks'].append('combined')
