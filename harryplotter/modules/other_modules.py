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


class DAgostini(analysisbase.AnalysisBase):

	def run(self, plotData=None):
		super(DAgostini, self).run(plotData)

		for index, label in enumerate(plotData.plotdict['labels']):
			plotData.plotdict['labels'][index] = label.replace('dAgostini', "d'Agostini")
		plotData.plotdict['y_subplot_label'] = plotData.plotdict['y_subplot_label'].replace('dAgostini', "d'Agostini")
