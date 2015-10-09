#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Artus.HarryPlotter.harry as harry
import Excalibur.Plotting.harryinterface as harryinterface


def zee_unfolding_crosscheck(args=None):
	"""Cross-check unfolding procedure derived from one mc and applied to the other (Powheg/Madgraph)."""

	# some variables
	path = '/portal/ekpcms5/home/dhaitz/git/excalibur'
	data = '/work/data_ee_corr.root'

	plots = []
	mc_samples = ['/store/mc_ee_corr.root', '/store/mc_ee_powheg_corr.root']
	for mc_label, mc, data in zip( ['Madgraph', 'Powheg'], mc_samples, reversed(mc_samples)):
		for quantity, bins in zip(['zpt', 'zmass', 'zy'], ["10,30,430", "10,81,101","10,-3,3"]):
			d = {
				'x_expressions': [
					quantity,
					quantity,
					"gen"+quantity,
					"gen"+quantity,
					],
				'y_expressions': [
					None,
					None,
					quantity,
					None,
					],
				'files': [
					path + data,

					path + mc,
					path + mc,
					path + mc,

				],
				'scale_factors': [
					1,

					1,
					1,
					1,

				],
				'nicks': [
					'data',

					'mc',
					'responsematrix',
					'gen',

				],
				'folders': ['zcuts_AK5PFJetsCHSL1L2L3'],
				'analysis_modules': [
					'Unfolding',
				],
				#module options
	
				'unfolding': 'data',
				'unfolding_responsematrix': 'responsematrix',
				'unfolding_mc_gen': 'gen',
				'unfolding_mc_reco': 'mc',
				'unfolding_new_nicks': 'Data',
				'libRooUnfold': '~/home/RooUnfold-1.1.1/libRooUnfold.so',
				
		
				'nicks_blacklist': ['responsematrix',
				 'mc', 'data'],

				'lumi': 19.8,
				'energy': '8',
				'y_ratio_lims': [0.5, 1.5],
		
				'x_bins': bins,
				'y_bins': bins,
				'x_label': quantity,
				'y_label': 'Events',

				'ratio': True,
				'filename': quantity + "_" + mc_label,

			}
			if quantity == 'zpt':
				d['x_log'] = True
				d['y_log'] = True
				d['x_ticks'] = [30, 50, 70, 100, 230]

			plots.append(d)
	harryinterface.harry_interface(plots, args)

if __name__ == '__main__':
	zee_unfolding_crosscheck()
