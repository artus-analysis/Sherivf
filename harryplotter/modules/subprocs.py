# -*- coding: utf-8 -*-
import logging
import Artus.Utility.logger as logger

log = logging.getLogger(__name__)

import Artus.HarryPlotter.analysisbase as analysisbase


class Subprocs(analysisbase.AnalysisBase):

	def run(self, plotData=None):
		super(Subprocs, self).run(plotData)

		plotData.plotdict['root_objects']["ratio"] = plotData.plotdict['root_objects']["nick0"].ProjectionY()
		plotData.plotdict['nicks'] += ["ratio"]

		th2 = plotData.plotdict['root_objects']["nick0"]
		gg = th2.GetBinContent(6, 6)  # center
		gq = 0
		for i in range(1,6) + range(7, 12):
			gq += (th2.GetBinContent(i, 6) + th2.GetBinContent(6, i)) # cross
		qqbar = 0
		for i in range(1,6) + range(7, 12):
			qqbar += th2.GetBinContent(i, 12-i)  # diagonal downwards
		qq = 0
		for i in range(1,6) + range(7, 12):
			qq += th2.GetBinContent(i, i)  # diagonal upwards
		qqprime = 1 - gg - gq - qq - qqbar
		for channel in ['gq', 'qqbar', 'qqprime', 'gg', 'qq']:
			print channel, "{:.2f} % ". format(100 * eval(channel))
