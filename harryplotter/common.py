# -*- coding: utf-8 -*-

import numpy as np
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
	'tt': 'violet',
	'tw': 'violet',
	'ww': 'grey',
	'wjets': 'red',
	'dytautau': 'teal',
	'qcd': 'salmon',
	'others': 'brown',
	'diboson': 'yellow',
}

data_quantities = ['zpt', 'abszy', 'zmass']
quantities = data_quantities 
def root_quantity(quantity):
	return {'abszy': 'abs(zy)'}.get(quantity, quantity)

bins = {
	'zpt': "30 40 60 80 100 120 140 170 200 1000",#"37,30,400",
	'zy': "50,-2.5,2.5",
	'abs(zy)': "24,0,2.4",
	'zmass': "20,81,101",
	'zphi': '32,-3.2,3.2',
	'njets30': "7,-0.5,6.5",
	'eminuspt': "20,20,120",
	'eminuseta': "48,-2.4,2.4",
}
bins['abszy'] = bins['abs(zy)']
zpt_ticks = [30, 40, 60, 100, 140, 200, 400, 1000]
zpt_xlog = True

def lims(quantity):
	if "," in bins[quantity]:
		return map(float, bins[quantity].split(",")[1:])
	else:
		binlist = map(float, bins[quantity].split(" "))
		return binlist[::len(binlist)-1]


pdfsetdict = {
	'NNPDF23_nlo_as_0118': 'NNPDF 2.3 NLO',
	'NNPDF30_nlo_as_0118': 'NNPDF 3.0 NLO',
	'NNPDF21_100': 'NNPDF 2.1',
	'abm11_3n_nlo': 'ABM11',
	'cteq65': 'CTEQ 6.5',
	'cteq66': 'CTEQ 6.6',
	'MSTW2008nlo68cl': 'MSTW 2008',
	'CT10nlo': 'CT10 NLO',
	'HERAPDF15NLO_EIG': 'HeraPDF 1.5',
	'MMHT2014nlo68clas118': 'MMHT 2014',
}

nmembersdict = {
	'CT10': 51,
	'NNPDF23_nlo_as_0118': 101,
	'NNPDF30_nlo_as_0118': 101,
}

qdict = {
	'abs(zy)': 'abszy',
	'eminuspt': 'eminuspt',
	'eminuseta': 'eminuseta',
}

## Rapidity binning
ybins = np.arange(0, 2.8, 0.4)
ybin_labels = ["{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
ybin_weights = ["abs(zy)<{1} && abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])]
ybin_plotlabels = ["${0}<|y_Z|<{1}$".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])]


### Uncertainties
variations = ["", "_edown", "_eup", "_bkgrup", "_bkgrdown", "_ptup", "_ptdown"]  # for sys uncert estimation
uncertainties = ["_e", "_bkgr", "_unf", "_pt"]
uncertainties_with_lumi = uncertainties + ['_lumi']
unc_labelsdict = {
	'_e': 'Electron ID/Trigger Efficiency',
	'_bkgr': 'Background',
	'_unf': 'Unfolding',
	'_lumi': 'Luminosity',
	'_pt': 'Electron pT scale',
}


# workflow dirs
excaliburpath = os.environ['EXCALIBURPATH']
bkgr_path = excaliburpath

subtract_dir = "1_background-subtracted"
unfold_path = "2_unfolded"
divided_path = "3_divided"
systematic_path = "4_systematic"
pdf_dir = "5_pdfunc"

iterations_to_use = 1

mc = excaliburpath + "/work/mc_ee.root"
mc_raw = excaliburpath + "/work/mc_ee_raw.root"
data = excaliburpath + "/work/mc_ee.root"

bkgr_backgrounds = ['zz', 'wz', 'tt', 'tw', 'ww', 'wjets', 'dytautau', 'qcd']
backgrounds_merged = ['zz', 'wz', 'tt', 'others', 'others', 'others', 'others', 'others']
backgrounds_merged_short = ['zz', 'wz', 'tt', 'others']


lumi = 19.712
lumi_uncertainty = 0.026


#unfolding_variations = [0, -1, 1]
unfolding_variations = ['_unfdown', '_unfup']
