# -*- coding: utf-8 -*-

import os

bkgr_labels = {
	'zz': "ZZ",
	'wz': "WZ",
	'tt': r"$t\\bar{t}$",
	'tw': "tW",
	'ww': "WW",
	'wjets': "W+jets",
	'dytautau': r"DY$\\rightarrow \\tau\\tau$",
	'qcd': "QCD",
	'others': "tW, WW, QCD,\nW+jets, "+r"DY$\\rightarrow \\tau\\tau$",
	'diboson': 'ZZ, WZ',
}

bkgr_colors = {
	'mc': 'blue',
	'zz': 'yellow',
	'wz': 'green',
	'tt': 'green',
	'tw': 'violet',
	'ww': 'grey',
	'wjets': 'red',
	'dytautau': 'teal',
	'qcd': 'salmon',
	'others': 'brown',
	'diboson': 'yellow',
}

bkgr_path = os.environ['EXCALIBURPATH']
bkgr_backgrounds = ['zz', 'wz', 'tt', 'tw', 'ww', 'wjets', 'dytautau', 'qcd']

bins = {
	'zpt': "40,0,400",
	'zy': "14,-2.8,2.8",
	'zmass': "20,81,101",
	'njets30': "7,-0.5,6.5",
}
