#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob
import common

def herafile(args=None, additional_dictionary=None, pdflabel=""):
	"""make herafile"""
	plots = []
	for quantity in common.data_quantities:
		for ybin, ybinsuffix in zip(
			[""] + ["y{}_".format(i) for i in range(len(common.ybins))],
			["inclusive"] + common.ybin_labels
		):
			if (quantity is not 'zpt') and (ybin is not ""):
				continue
			uncfile = "4_systematic/{}_madgraph_{}_{}_1.root"
			d = {
				# input
				"x_expressions": ['nick0'] + ['ratio']*4,
				"folders": [""],
				'nicks': ['sigma', 'lumi', 'bkgrup', 'unfup', 'eup'],
				'scale_factors': [1] + [100]*4,
				"files": [
					'3_divided/{}_madgraph_{}_1.root'.format(quantity, ybinsuffix),
					uncfile.format(quantity, ybinsuffix, 'lumi'),
					uncfile.format(quantity, ybinsuffix, 'bkgrup'),
					uncfile.format(quantity, ybinsuffix, 'unfup'),
					uncfile.format(quantity, ybinsuffix, 'eup'),
				],
				#hera
				"hera_theoryfile": ybin+quantity,
				"hera_sys": 10,
				"hera_quantity": quantity.replace("(","").replace(")",""),
				"header_file": "herafitter/herafitter_header.txt",
				# output
				"plot_modules": ['ExportHerafitter'],
				"filename": 'CMS_Zee_HFinput_{}_{}'.format(quantity, ybinsuffix),
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
