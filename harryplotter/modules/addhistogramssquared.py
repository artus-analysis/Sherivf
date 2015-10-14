# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import math

import Artus.HarryPlotter.analysisbase as analysisbase
import Artus.HarryPlotter.utility.roottools as roottools


class AddHistogramsSquared(analysisbase.AnalysisBase):
	"""Add histograms by summing up their bin contents quadratically.
	
		This module creates a new histogram with nickname 'added' whose contents 
		are the quadratically added contents of the histograms specified with --add-squared-nicks
		Bin errors are set to zero.
	"""

	def modify_argument_parser(self, parser, args):
		super(AddHistogramsSquared, self).modify_argument_parser(parser, args)
		self.envelope_options = parser.add_argument_group("{} options".format(self.name()))
		self.envelope_options.add_argument("--square-add-nicks", type=str, nargs="+")

	def run(self, plotData=None):
		super(AddHistogramsSquared, self).run(plotData)

		root_objects = [plotData.plotdict["root_objects"][nick] for nick in plotData.plotdict["square_add_nicks"]]
		result_histo = root_objects[0].Clone("square_added")

		#TODO add checks that all histos have same binning?

		# loop over bins, add contents quadratically, then extract square root:
		for i in range(1, result_histo.GetNbinsX()+1):
			content = 0.
			for histogram in root_objects:
					content += histogram.GetBinContent(i)**2
			content = math.sqrt(content)

			result_histo.SetBinContent(i, content)
			result_histo.SetBinError(i, 0) #TODO also add errors ?

		plotData.plotdict["root_objects"]['square_added'] = result_histo
		plotData.plotdict['nicks'].append('square_added')
