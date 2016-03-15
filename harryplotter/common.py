# -*- coding: utf-8 -*-

import numpy as np
import os

import pdf_2_root


bkgr_labels = {
	'zz': "ZZ",
	'wz': "WZ",
	'tt': r"$t\\bar{t}$",
	'tw': "tW",
	'ww': "WW",
	'wjets': "W+jets",
	'dytautau': r"DY$\\rightarrow \\tau\\tau$",
	'qcd': "dijet",
	'others': "tW, WW, dijet,\nW+jets, "+r"DY$\\rightarrow \\tau\\tau$",
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

import Excalibur.Plotting.utility.labelsZJet as labelsZJet

labels = labelsZJet.LabelsDictZJet()

### main steering for quantities
data_quantities = ['zpt', 'abszy', 'zy', 'zmass']
###
quantities = data_quantities 
def root_quantity(quantity):
	return {'abszy': 'abs(zy)'}.get(quantity, quantity)

bins = {
	'zpt': "30 40 50 60 80 100 120 140 170 200 1000",
	'zy': "48,-2.4,2.4",
	'abs(zy)': "24,0,2.4",
	'zmass': "20,81,101",
	'zphi': '32,-3.2,3.2',
	'njets30': "7,-0.5,6.5",
	'eminuspt': "20,20,120",
	'eminuseta': "48,-2.4,2.4",
}
bins['abszy'] = bins['abs(zy)']
default_mc = 'madgraph'
mcs = [default_mc, 'powheg']

unfbins = {}
unfbins.update(bins)
unfbins['zpt'] = "0 " + unfbins['zpt']
unfbins.update({
	'abs(zy)': "26,0,2.6",
	'zy': "52,-2.6,2.6",
})
unfbins['abszy'] = unfbins['abs(zy)']
default_unfolding_method = 'inversion'
other_methods = ['dagostini', 'binbybin']
unfdict = {
	'zpt' : 'ptunfolding',
	'abszy': 'yunfolding',
	'zy': 'yunfolding',
}
unfdict['abs(zy)'] = unfdict['abszy']
def unffolder(quantity):
	return unfdict.get(quantity, 'zcuts')

zpt_ticks = [30, 40, 60, 100, 200, 400, 1000]
zpt_xlog = True
zpt_miny = 1e-5

def lims(quantity):
	if "," in bins[quantity]:
		return map(float, bins[quantity].split(",")[1:])
	else:
		binlist = map(float, bins[quantity].split(" "))
		return binlist[::len(binlist)-1]


pdfsetdict = {
	'NNPDF23_nlo_as_0118': 'NNPDF 2.3 NLO',
	'NNPDF30_nlo_as_0118': 'NNPDF 3.0 NLO',
	'NNPDF30_nlo_as_0118_nolhc': 'NNPDF 3.0 NLO (no LHC data)',
	'NNPDF30_nlo_as_0118_nolhc_1000': 'NNPDF 3.0 NLO (no LHC data, 1000 replicas)',
	'NNPDF21_100': 'NNPDF 2.1',
	'abm11_3n_nlo': 'ABM11 NLO',
	'cteq65': 'CTEQ 6.5',
	'cteq66': 'CTEQ 6.6',
	'MSTW2008nlo68cl': 'MSTW 2008',
	'CT10nlo': 'CT10 NLO',
	'CT14nlo': 'CT14 NLO',
	'HERAPDF15NLO_EIG': 'HeraPDF 1.5 NLO',
	'HERAPDF20_NLO_EIG': 'HeraPDF 2.0 NLO',
	'MMHT2014nlo68clas118': 'MMHT 2014 NLO',
	'PDF4LHC15_nlo_100': 'PDF4LHC15 NLO '
}

nmembersdict = {
	'CT10': 51,
	'NNPDF23_nlo_as_0118': 101,
	'NNPDF30_nlo_as_0118': 101,
	'NNPDF30_nlo_as_0118_nolhc': 101,
}

qdict = {
	'abs(zy)': 'abszy',
	'eminuspt': 'eminuspt',
	'eminuseta': 'eminuseta',
}

## Rapidity binning
ybins = np.arange(0, 2.8, 0.4)
ybin_labels = [r"{0:02d}y{1:02d}".format(int(10*low), int(10*up)) for low, up in zip(ybins[:-1], ybins[1:])]
ybin_weights = ["abs(zy)<{1}&&abs(zy)>{0}".format(low, up) for low, up in zip(ybins[:-1], ybins[1:])]
ybin_plotlabels = [(r"${0}\\leq|\\mathit{{y}}_Z|<{1}$".format(low, up) if (low > 0.) else r"      $\\,|\\mathit{{y}}_Z|<{0}$".format(up))  for low, up in zip(ybins[:-1], ybins[1:])]


### Uncertainties
variations = ["", "_edown", "_eup", "_bkgrup", "_bkgrdown", "_ptup", "_ptdown"]  # for sys uncert estimation
uncertainties = ["_e", "_bkgr", "_pt"]
uncertainties_with_lumi = uncertainties + ['_lumi']
unc_labelsdict = {
	'_e': 'Electron ID/trigger efficiency',
	'_bkgr': 'Background',
	'_lumi': 'Luminosity',
	'_pt': r'Electron p$_\\mathrm{T}$ scale',
}


# workflow dirs
excaliburpath = os.environ['EXCALIBURPATH']
bkgr_path = excaliburpath
sherpa_results = os.path.join(os.environ['SHERIVFDIR'], 'results/MCgrid_CMS_2015_Zee_zjet/')
sherivf_output_dir = sherpa_results

subtract_dir = "1_background-subtracted"
unfold_path = "2_unfolded"
divided_path = "3_divided"
systematic_path = "4_systematic"
pdf_dir = "5_pdfunc"

iterations_to_use = 1

algocorr = "ak5PFJetsCHSL1L2L3"

mc = excaliburpath + "/work/mc_ee.root"
mc_raw = excaliburpath + "/work/mc_ee_raw.root"
data = excaliburpath + "/work/mc_ee.root"

bkgr_backgrounds = ['zz', 'wz', 'tt', 'tw', 'ww', 'wjets', 'dytautau', 'qcd']
backgrounds_merged = ['zz', 'wz', 'tt', 'others', 'others', 'others', 'others', 'others']
backgrounds_merged_short = ['zz', 'wz', 'tt', 'others']

xseclabels = {
	'zpt': 'xsecpt',
	'abszy': 'xsecabsy',
	'zy': 'xsecy',
	'zmass': 'xsecm',
	'zphi': 'xsecphi'
}
xseclabels_bin = {
	'zpt': 'xsecpt_bin',
	'abszy': 'xsecabsy_bin',
	'zy': 'xsecy_bin',
	'zmass': 'xsecm_bin',
	'zphi': 'xsecphi_bin'
}

hera_title = "HERA 1+2"
hera_cms_title = hera_title + r" and CMS Z+jet"

lumi = 19.712
lumi_uncertainty = 0.026


# PDF
pdfq = "1_9_squared"
pdf_unc_flavours = [pdf_2_root.partondict[f].replace(' ', '_') for f in pdf_2_root.default_flavours]
results_dir = os.environ['SHERIVFDIR']+"/results/"

