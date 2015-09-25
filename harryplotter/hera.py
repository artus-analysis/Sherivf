#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def herafile(args=None, additional_dictionary=None, pdflabel=""):
	"""make herafile"""
	quantity = "abs(zy)"
	uncfile = "4_systematic/{}_madgraph_inclusive_{}_1.root"

	d = {
		# input
		"x_expressions": ['nick0'] + ['ratio']*4,
		"folders": [""],
		'nicks': ['sigma', 'lumi', 'bkgrup', 'unfup', 'eup'],
		'scale_factors': [1] + [100]*4,
		"files": [
			'3_divided/{}_madgraph_inclusive_1.root'.format(quantity),
			uncfile.format(quantity, 'lumi'),
			uncfile.format(quantity, 'bkgrup'),
			uncfile.format(quantity, 'unfup'),
			uncfile.format(quantity, 'eup'),
		],
		# output
		"plot_modules": ['ExportHerafitter'],
		"header_file": "herafitter/herafitter_header.txt",
		"hera_sys": 10,
		"hera_quantity": quantity.replace("(","").replace(")",""),
		"filename": 'CMS_Zee_HFinput',
		"output_dir": "/usr/users/dhaitz/home/qcd/sherivf/herafitter",


		# output
		"export_json": False,
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	return [PlottingJob([d], args)]


if __name__ == '__main__':
	herafile()
