#  -*- coding: utf-8 -*-

"""
replace @NDATA@

"""

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import os
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

		self.plotting_options.add_argument("--export-nick", type=str, default='nick0',
		    help="Name of the nick to be exported [Default: %(default)s].")
		self.plotting_options.add_argument("--header-file", type=str,
		    help="Location to the txt file containing the header of the Herafitter data file.")

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


	def make_plots(self, plotData):
		root_object = plotData.plotdict["root_objects"][plotData.plotdict["export_nick"]]

		# Iterate over bins, append bin values
		lines = []
		for i in range(1, root_object.GetNbinsX()+1):
			lines.append([
				root_object.GetBinLowEdge(i),
				root_object.GetBinLowEdge(i) + root_object.GetBinWidth(i),
				root_object.GetBinContent(i),
				root_object.GetBinError(i),  # stat
				2*root_object.GetBinError(i)  # sys
			])
		# now, format the values to strings with proper widths
		list_of_max_len = [0]*len(lines[0])
		for line in lines:
			for i, item in enumerate(line):
				list_of_max_len[i] = max(list_of_max_len[i], len(str(int(item))))

		str_lines = []
		for line in lines:
			str_lines.append("  ".join([
				"{:{width}.0f}".format(line[0], width=list_of_max_len[0]),
				"{:{width}.0f}".format(line[1], width=list_of_max_len[1]),
				"{:{width}.2f}".format(line[2], width=list_of_max_len[2]+3),
				"{:{width}.5f}".format(line[3], width=list_of_max_len[3]+3),
				"{:{width}.5f}".format(line[4], width=list_of_max_len[4]+3),
			]))
		plotData.plot.values = "\n".join(str_lines)
