#  -*- coding: utf-8 -*-

"""
replace @NDATA@

"""

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import os
import random
import sys

import Artus.HarryPlotter.plotbase as plotbase
import Artus.HarryPlotter.plotdata as plotdata


class HerafitterContainer(plotdata.PlotContainer):
	def __init__(self):
		self.values = ""

	def finish(self):
		self.header = self.header.replace('@NDATA@', str(len(self.values.splitlines())))
		self.string = self.header + self.values + "\n"

	def save(self, filename):
		textfile_name = os.path.splitext(filename)[0] + ".txt"
		with open(textfile_name, "w") as output_file:
			output_file.write(self.string)


class ExportHerafitter(plotbase.PlotBase):
	"""Create Herafitter data files."""

	def modify_argument_parser(self, parser, args):
		super(ExportHerafitter, self).modify_argument_parser(parser, args)

		self.plotting_options.add_argument("--export-nick", type=str, default='sigma',
		    help="Name of the nick to be exported [Default: %(default)s].")
		self.plotting_options.add_argument("--header-file", type=str,
		    help="Location to the txt file containing the header of the Herafitter data file.")
		self.plotting_options.add_argument("--hera-stat", type=float, default=1.,
		    help="multiplicator for stat uncertainties")
		self.plotting_options.add_argument("--hera-lumifile", type=str)
		self.plotting_options.add_argument("--hera-unffile", type=str)
		self.plotting_options.add_argument("--hera-bkgrfile", type=str)
		self.plotting_options.add_argument("--hera-effile", type=str)
		self.plotting_options.add_argument("--hera-quantity", type=str, help="quantity")
		self.plotting_options.add_argument("--hera-theoryfile", type=str, help="theory file")

	def prepare_args(self, parser, plotData):
		plotData.plotdict["formats"] = ["txt"]
		super(ExportHerafitter, self).prepare_args(parser, plotData)

	def create_canvas(self, plotData):
		plotData.plot = HerafitterContainer()
		if plotData.plotdict["header_file"] is None:
			log.fatal("No Header file given!")
			sys.exit(1)
		else:
			with open(plotData.plotdict["header_file"]) as f:
				plotData.plot.header = f.read()
				root_object = plotData.plotdict["root_objects"][plotData.plotdict["export_nick"]]
			replacedict = {
				"@THEORYFILE@": plotData.plotdict["hera_theoryfile"],
				"@NAME@": "CMS Zee jets 2012 " + plotData.plotdict["hera_theoryfile"],
				"@INDEX@": str(int(1000*random.random())),
				"@LOWERLIM@": str(root_object.GetBinLowEdge(1)),
				"@UPPERLIM@": str(root_object.GetBinLowEdge(root_object.GetNbinsX())+root_object.GetBinWidth(root_object.GetNbinsX()))
			}
			#@TITLE@
			for old, new in replacedict.iteritems():
				plotData.plot.header = plotData.plot.header.replace(old, new)


	def make_plots(self, plotData):
		root_object = plotData.plotdict["root_objects"][plotData.plotdict["export_nick"]]

		# Iterate over bins, append bin values
		lines = []
		for i in range(1, root_object.GetNbinsX()+1):
			lines.append([
				root_object.GetBinLowEdge(i),
				root_object.GetBinLowEdge(i) + root_object.GetBinWidth(i),
				root_object.GetBinContent(i),
				plotData.plotdict["hera_stat"]*(100*(root_object.GetBinError(i)/root_object.GetBinContent(i) if root_object.GetBinContent(i)>0. else 0.)),  # stat
				plotData.plotdict["root_objects"]['lumi'].GetBinContent(i),
				plotData.plotdict["root_objects"]['unf'].GetBinContent(i),
				plotData.plotdict["root_objects"]['bkgr'].GetBinContent(i),
				plotData.plotdict["root_objects"]['e'].GetBinContent(i),
				plotData.plotdict["root_objects"]['pt'].GetBinContent(i),
			])
		# now, format the values to strings with proper widths
		list_of_max_len = [0]*len(lines[0])
		for line in lines:
			for i, item in enumerate(line):
				list_of_max_len[i] = max(list_of_max_len[i], len(str(int(item))))

		# write to text
		str_lines = []
		for line in lines:
			str_lines.append("  ".join([
				"{:{width}.1f}".format(line[0], width=list_of_max_len[0]),
				"{:{width}.1f}".format(line[1], width=list_of_max_len[1]),  # 
				"{:{width}.6f}".format(line[2], width=list_of_max_len[2]+3),  # stat
				"{:{width}.6f}".format(line[3], width=list_of_max_len[3]+3),  # sys
				"{:{width}.6f}".format(line[4], width=list_of_max_len[4]+3),  # lumi
				"{:{width}.6f}".format(line[5], width=list_of_max_len[5]+3),  # unf
				"{:{width}.6f}".format(line[6], width=list_of_max_len[6]+3),  # ef
				"{:{width}.6f}".format(line[7], width=list_of_max_len[7]+3),  # bkgr
				"{:{width}.6f}".format(line[8], width=list_of_max_len[8]+3),  # pt
			]))
		plotData.plot.values = "\n".join(str_lines)
