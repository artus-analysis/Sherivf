# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger

log = logging.getLogger(__name__)

import ROOT
import math
import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class MaxHistogram(analysisbase.AnalysisBase):
	""" new histo from two histo with bin content being the max content for each of the inputs"""

	def modify_argument_parser(self, parser, args):
		super(MaxHistogram, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--max-nick1", type=str)
		self.envelope_options.add_argument("--max-nick2", type=str)
		self.envelope_options.add_argument("--max-result-nick", type=str, default='max')

	def run(self, plotData=None):
		super(MaxHistogram, self).run(plotData)

		histo_1 = plotData.plotdict["root_objects"][plotData.plotdict["max_nick1"]]
		histo_2 = plotData.plotdict["root_objects"][plotData.plotdict["max_nick2"]]
		result_histo = histo_1.Clone()
		result_nick = plotData.plotdict["max_result_nick"]

		for i in range(1, result_histo.GetNbinsX()+1):
			# y errors low/high as difference to the min/max values
			result_histo.SetBinContent(i, max([histo_1.GetBinContent(i), histo_2.GetBinContent(i)]))
			result_histo.SetBinError(i, 0)

		plotData.plotdict["root_objects"][result_nick] = result_histo
		plotData.plotdict['nicks'].append(result_nick)
