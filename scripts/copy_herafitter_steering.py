#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""copy herafitter steering file and replace certain parameters according to fit mode"""

import argparse
import os
import common

import tools

heradir = os.environ['HERADIR']
steeringfile = os.path.join(os.environ['SHERIVFDIR'], "herafitter/steering.txt")

herafiles = ["'{}/datafiles/hera/H1ZEUS_{}_HERA1.0.dat'".format(heradir, i) for i in ["NC_e-p", "NC_e+p", "CC_e-p", "CC_e+p"]]
datafiles_y = ["'{}/herafitter/CMS_Zee_HFinput_{}_inclusive.txt'".format(os.environ['SHERIVFDIR'], "abszy")]
datafiles_pt = ["'{}/herafitter/CMS_Zee_HFinput_{}_inclusive.txt'".format(os.environ['SHERIVFDIR'], "zpt")]
datafiles_bins = ["'{}/herafitter/CMS_Zee_HFinput_zpt_{}.txt'".format(os.environ['SHERIVFDIR'], ybin) for ybin in common.ybin_labels]

heradict = {
	'nnpdf': [len(datafiles_pt), datafiles_pt, 'True'],
	'hera': [len(herafiles), herafiles, 'False'],
	'heraZ': [len(datafiles_y)+len(herafiles), datafiles_y+herafiles, 'False'],
	'heraZ_pt': [len(datafiles_pt)+len(herafiles), datafiles_pt+herafiles, 'False'],
	'heraZ_bins': [len(datafiles_bins)+len(herafiles), datafiles_bins+herafiles, 'False'],
}

valuefile = "'" + os.environ['SHERIVFDIR'] + "/herafitter/CMS_Zee_HFinput_{0}_{1}.txt'"
modes = {
	'hera': herafiles,
	#'hera2': [len(herafiles), herafiles],
	'nnpdf':[],
}

values = {
	'abszy': [valuefile.format('abszy', 'inclusive')],
	'zpt': [valuefile.format('zpt', 'inclusive')],
	'zpt_bins': [valuefile.format('zpt', ptbin) for ptbin in common.ybin_labels[:-1]],
}



def main():
	"""main"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--mode', type=str, default='hera', help="mode", choices=modes.keys())
	parser.add_argument('-v', '--values', type=str, default='abszy', help="Value", choices=values.keys())
	parser.add_argument('-b', '--batch', action="store_true", help="batch mode, i.e. dont copy defaults", )
	parser.add_argument('-f', '--fast', action="store_true", help="RT FAST scheme (instead of RT)")
	parser.add_argument('-d', '--dir', type=str, default=heradir, help="dir to copy steering file to")
	args = parser.parse_args()
	copy_herafile(args.mode, args.batch, args.dir, args.fast)


def copy_herafile(mode, value, batch, targetdir, fast=False, keys={}):

	print "Preparing Herafitter for {0} mode with {1} values".format(mode, value)

	defaults_local = {
		# for HERA Fit
		'@Q02@': '1.9',
		'@Q2MIN@': '7.5',
		'@HF_SCHEME@': 'RT'+(' FAST' if fast else ''),
		'@PDFStyle@': '13p HERAPDF',
		'@DOBANDS@': 'True',
		'@ALPHAS@': '0.1176',
		'@ALPHAS_S@': '0.0',
		'@FS@': '0.31',
		'@FC@': '0.',
	}
	defaults_global = {
	}

	# copy
	target = os.path.join(targetdir, os.path.basename(steeringfile))
	print "Copy steering file to", target

	datafiles = modes[mode] + values[value]
	settings = {
		'@NFILES@': str(len(datafiles)),
		'@FILES@': ",\n   ".join(datafiles),
		'@DOREWEIGHTING@': str((mode == 'nnpdf')),
		'@PDFSET@': 'NNPDF23_nlo_as_0118',
		# NNPDF Rew.
	}
	settings.update(defaults_global)
	if not batch:  # for GC, dont replace the HF values
		settings.update(defaults_local)
	settings.update(keys)
	tools.copyfile(steeringfile, target, settings)


if __name__ == "__main__":
	main()
