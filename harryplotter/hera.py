#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common

def herafile(args=None, additional_dictionary=None, pdflabel=""):
	"""make herafile"""
	plots = []
	#TODO in y bins
	for quantity in common.data_quantities:
		ybin = "inclusive"
		uncfile = "4_systematic/{}_madgraph_{}_{}_1.root"
		d = {
			# input
			"x_expressions": ['nick0'] + ['ratio']*4,
			"folders": [""],
			'nicks': ['sigma', 'lumi', 'bkgrup', 'unfup', 'eup'],
			'scale_factors': [1] + [100]*4,
			"files": [
				'3_divided/{}_madgraph_{}_1.root'.format(quantity, ybin),
				uncfile.format(quantity, ybin, 'lumi'),
				uncfile.format(quantity, ybin, 'bkgrup'),
				uncfile.format(quantity, ybin, 'unfup'),
				uncfile.format(quantity, ybin, 'eup'),
			],
			# output
			"plot_modules": ['ExportHerafitter'],
			"header_file": "herafitter/herafitter_header.txt",
			"hera_sys": 5,
			"hera_quantity": quantity.replace("(","").replace(")",""),
			"filename": 'CMS_Zee_HFinput_{}_{}'.format(quantity, ybin),
			"output_dir": "/usr/users/dhaitz/home/qcd/sherivf/herafitter",

			# output
			"export_json": False,
		}
		if additional_dictionary is not None:
			d.update(additional_dictionary)
		plots.append(d)
	return [PlottingJob(plots, args)]


if __name__ == '__main__':
	herafile()
