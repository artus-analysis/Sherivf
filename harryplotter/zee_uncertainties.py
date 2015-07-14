# -*- coding: utf-8 -*-

import Excalibur.Plotting.harryZJet as harryZJet
import Excalibur.Plotting.harryinterface as harryinterface


def zee_unc(args=None):
	""" Plot of the systematic uncertainties of the Z->ee measurement."""

	weights = "1"
	bins = [30,40,60,80,100,120,140,170,200,1000]
	path = "/portal/ekpcms5/home/dhaitz/git/excalibur/"

	d = {
		"absolute_bin_contents": [
			"background", 
			"unfolding"
		], 
		"analysis_modules": [
			"StatisticalErrors", 
			"Unfolding", 
			"Divide", 
			"ShiftBinContents", 
			"AbsoluteBinContents", 
			"ScaleHistograms"
		], 
		"colors": [
			"black", 
			"lightskyblue", 
			"red", 
			"green"
		], 
		"divide_denominator_nicks": [
			"lumi_denum", 
			"backgroundunc", 
			"unfoldedup"
		], 
		"divide_numerator_nicks": [
			"lumi_num", 
			"data", 
			"unfolded"
		], 
		"divide_result_nicks": [
			"lumi", 
			"background", 
			"unfolding"
		], 
		"energy": "8", 
		"files": [
			path + "work/data_ee_corr.root", 
			path + "work/data_ee_corr.root", 
			path + "store/mc_ee_powheg_corr.root", 
			path + "store/mc_ee_powheg_corr.root", 
			path + "store/mc_ee_powheg_corr.root", 
			path + "store/background_ee_zz.root", 
			path + "store/background_ee_wz.root", 
			path + "store/background_ee_tt.root", 
			path + "store/background_ee_tw.root", 
			path + "store/background_ee_ww.root", 
			path + "store/background_ee_wjets.root", 
			path + "store/background_ee_dytautau.root", 
			path + "store/background_ee_zz.root", 
			path + "store/background_ee_wz.root", 
			path + "store/background_ee_tt.root", 
			path + "store/background_ee_tw.root", 
			path + "store/background_ee_ww.root", 
			path + "store/background_ee_wjets.root", 
			path + "store/background_ee_dytautau.root", 
			path + "work/data_ee_corr.root", 
			path + "work/data_ee_corr.root", 
			path + "work/data_ee_corr.root"
		], 
		"folders": 
			["zcuts_AK5PFJetsCHSL1L2L3Res"]*2 + 
			["zcuts_AK5PFJetsCHSL1L2L3", "zcuts_AK5PFJetsCHSL1L2L3"] +["zcuts_AK5PFJetsCHSL1L2L3"]*15 + 
			["zcuts_AK5PFJetsCHSL1L2L3Res"]*3,
		"weights": 
			[weights]*3 + 
			["genzpt>30 && {}".format(weights)] +[weights]*18,
		"filename": "sys-errors", 
		"formats": [
			"png"
		], 
		"legend": "upper left", 
		"libRooUnfold": "~/home/RooUnfold-1.1.1/libRooUnfold.so", 
		"linestyles": [
			"-", 
			"-", 
			"-", 
			"-"
		], 
		"lumi": 19.8, 
		"markers": [
			"o", 
			"*", 
			".", 
			"d"
		], 
		"nicks": [
			"statistical", 
			"data", 
			"mc", 
			"responsematrix", 
			"gen", 
			"data", 
			"data", 
			"data", 
			"data", 
			"data", 
			"data", 
			"data", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"backgroundunc", 
			"lumi_num", 
			"lumi_denum"
		], 
		"nicks_blacklist": [
			"responsematrix", 
			"backgroundunc", 
			"gen", 
			"data", 
			"mc", 
			"lumi_", 
			"unfolded"
		],
		"relative_error": True, 
		"title": "own work", 
		"scale": 100, 
		"scale_nicks": [
			"background", 
			"unfolding"
		], 
		"scale_factors": [
			1, 
			1, 
			1, 
			1, 
			1, 
			-1, 
			-1, 
			-1, 
			-1, 
			-1, 
			-1, 
			-1, 
			-1.5, 
			-1.5, 
			-1.5, 
			-1.5, 
			-1.5, 
			-1.5, 
			-1.5, 
			1, 
			2.6, 
			1
		], 
		"shift": -1, 
		"shift_bin_contents": [
			"background", 
			"unfolding"
		], 
		"stat_error": [
			"statistical"
		], 
		"unfolding": "data", 
		"unfolding_mc_gen": "gen", 
		"unfolding_mc_reco": "mc", 
		"unfolding_new_nicks": [
			"unfolded", 
			"unfoldedup"
		], 
		"unfolding_responsematrix": "responsematrix", 
		"unfolding_variation": [
			0, 
			1
		], 
		"x_bins": bins, 
		"x_errors": None, 
		"x_expressions": [
			"zpt", 
			"zpt", 
			"zpt", 
			"genzpt", 
			"genzpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt", 
			"zpt"
		], 
		"x_label": "zpt", 
		"x_lims": [
			30, 
			250
		], 
		"y_bins": bins, 
		"y_errors": None, 
		"y_expressions": [
			None, 
			None, 
			None, 
			"zpt", 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None, 
			None
		], 
		"y_label": "relative error [%]", 
		"y_lims": [
			0, 
			5
		]
	}
	harryinterface.harry_interface([d], args)


if __name__ == '__main__':
	zee_unc()
