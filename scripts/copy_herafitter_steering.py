#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""copy herafitter steering file and replace certain parameters according to fit mode"""

import argparse
import os
import common

import sherivf

heradir = os.environ['HERADIR']
steeringfile = os.path.join(os.environ['SHERIVFDIR'], "herafitter/steering.txt")

herafiles = ["'{}/datafiles/hera/H1ZEUS_{}_HERA1.0.dat'".format(heradir, i) for i in ["NC_e-p", "NC_e+p", "CC_e-p", "CC_e+p"]]
datafiles = ["'{}/herafitter/CMS_Zee_HFinput_{}_inclusive.txt'".format(os.environ['SHERIVFDIR'], "abszy")]
datafiles_bins = ["'{}/herafitter/CMS_Zee_HFinput_zpt_{}.txt'".format(os.environ['SHERIVFDIR'], ybin) for ybin in common.ybin_labels]

heradict = {
	'nnpdf': [len(datafiles), datafiles, 'True'],
	'hera': [len(herafiles), herafiles, 'False'],
	'heraZ': [len(datafiles)+len(herafiles), datafiles+herafiles, 'False'],
	'heraZ_bins': [len(datafiles_bins)+len(herafiles), datafiles_bins+herafiles, 'False'],
}



def main():
	"""main"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--mode', type=str, default='nnpdf',
		help="mode", choices=heradict.keys())
	parser.add_argument('-b', '--batch', action="store_true", help="batch mode, i.e. dont copy defaults", )
	parser.add_argument('-d', '--dir', type=str, default=heradir, help="dir to copy steering file to")
	args = parser.parse_args()
	copy_herafile(args.mode, args.batch, args.dir)


def copy_herafile(mode, batch, targetdir):

	print "Preparing Herafitter for {} mode".format(mode)

	defaults = {
		'@Q02@': '1.9',
		'@HF_SCHEME@': 'RT FAST', # TODO Use 'RT' for final results
		'@PDFStyle@': '13p HERAPDF',
		'@DOBANDS@': 'True',
		'@ALPHAS@': '0.1176',
		'@ALPHAS_S@': '0.0',
		'@FS@': '0.31',
		'@FC@': '0.',
	}

	# copy
	dataset = heradict[mode]
	target = os.path.join(targetdir, os.path.basename(steeringfile))
	print "Copy steering file to", target

	values = {
		'@NFILES@': str(dataset[0]),
		'@FILES@': ",\n   ".join(dataset[1]),
		'@DOREWEIGHTING@': dataset[2],
		#'@OUTDIRNAME@': mode,
	}
	if not batch:  # for GC, dont replace the HF values
		values.update(defaults)
	sherivf.copyfile(steeringfile, target, values)


if __name__ == "__main__":
	main()
