#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Excalibur.Plotting.utility.toolsZJet import PlottingJob


def herafile(args=None, additional_dictionary=None, pdflabel=""):
	"""make herafile"""
	quantity = "abs(zy)"
	d = {
		"x_expressions": ['nick0'],
		"files": ['3_divided/{}_madgraph_inclusive_1.root'.format(quantity)],
		"folders": [""],
		#"x_bins": ['37,30,400'],
		# 
		"plot_modules": ['ExportHerafitter'],
		"header_file": "herafitter/herafitter_header.txt",
		"hera_sys": 3,
		"hera_stat": 1,
		"hera_quantity": quantity.replace("(","").replace(")",""),
		"filename": 'CMS_Zee_HFinput',
		"output_dir": "/usr/users/dhaitz/home/qcd/sherivf/herafitter",
	}
	if additional_dictionary is not None:
		d.update(additional_dictionary)
	return [PlottingJob([d], args)]


if __name__ == '__main__':
	herafile()
