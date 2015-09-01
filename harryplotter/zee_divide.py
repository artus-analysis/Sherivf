#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface
import parsertools

import common


def zee_divide(args=None):
	"""Divide unfolded Zee data by lumi and bin width"""

	#known_args, args = parsertools.parser_list_tool(args, ['ybins', 'mcs', 'quantities', 'iterations'])

	# TODO: divide unfolded data by lumi and bin width and write root output to folder '3_divided/'

	plots = []
	
	plots.append(d)
	harryinterface.harry_interface(plots, args)


if __name__ == '__main__':
	zee_divide()
