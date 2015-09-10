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

data_quantities = ['zpt', 'abs(zy)', 'zmass']

bins = {
	'zpt': "38,20,400",
	'zy': "50,-2.5,2.5",
	'abs(zy)': "24,0,2.4",
	'zmass': "20,81,101",
	'zphi': '32,-3.2,3.2',
	'njets30': "7,-0.5,6.5",
	'eminuspt': "20,20,120",
	'eminuseta': "48,-2.4,2.4",
}

pdfsetdict = {
	'NNPDF23_nlo_as_0118': 'NNPDF 2.3',
	'NNPDF21_100': 'NNPDF 2.1',
	'abm11_3n_nlo': 'ABM11',
	'cteq65': 'CTEQ 6.5',
	'MSTW2008nlo68cl': 'MSTW 2008',
	'CT10nlo': 'CT10 NLO',
}


nmembersdict = {
	'CT10.LHgrid': 51,
	'NNPDF23_nlo_as_0118.LHgrid': 101,
}

qdict = {
	'abs(zy)': 'abszy',
	'eminuspt': 'ept',
	'eminuseta': 'eeta',
}

excaliburpath = os.environ['EXCALIBURPATH']
bkgr_path = excaliburpath

unfold_path = "2_unfolded"
divided_path = "3_divided"

iterations_to_use = 1

mc = excaliburpath + "/work/mc_ee.root"
mc_raw = excaliburpath + "/work/mc_ee_raw.root"
data = excaliburpath + "/work/mc_ee.root"

bkgr_backgrounds = ['zz', 'wz', 'tt', 'tw', 'ww', 'wjets', 'dytautau', 'qcd']

lumi = 19.712
