#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""copy xfitter steering file and replace certain parameters according to fit mode"""

import argparse
import os
import common

import sherivftools

steeringfile = os.path.join(os.environ['SHERIVFDIR'], "xfitter/steering.txt")

xdir = os.path.join(os.environ['SHERIVFDIR'], "datafiles/hera/")
modes = {
	'hera2':["'{}'".format(os.path.join(xdir, f)) for f in os.listdir(xdir)],
}

valuefile = "'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_HFinput_{0}_{1}.txt'"
values = {
	'abszy': [valuefile.format('abszy', 'inclusive')],
	'zpt': [valuefile.format('zpt', 'inclusive')],
	'zy': [valuefile.format('zy', 'inclusive')],
	'zpt_bins': [valuefile.format('zpt', ptbin) for ptbin in common.ybin_labels[:-1]],
}
corrfile = "'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_correlation_{0}_{1}.corr'"
corrs = {
	'abszy': [corrfile.format('abszy', 'inclusive')],
	'zpt': [corrfile.format('zpt', 'inclusive')],
	'zy': [corrfile.format('zy', 'inclusive')],
	'zpt_bins': [corrfile.format('zpt', ptbin) for ptbin in common.ybin_labels[:-1]],
}


def main():
	"""main"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--mode', type=str, default='hera2', help="mode", choices=modes.keys())
	parser.add_argument('-v', '--value', type=str, default=None, help="Value", choices=values.keys())
	parser.add_argument('-b', '--batch', action="store_true", help="batch mode, i.e. dont copy defaults", )
	parser.add_argument('-f', '--fast', action="store_true", help="RT FAST scheme (instead of RT)")
	parser.add_argument('-d', '--dir', type=str, default=os.getcwd(), help="dir to copy steering file to")
	args = parser.parse_args()
	copy_herafile(args.mode, args.value, args.batch, args.dir, args.fast)


def copy_herafile(mode, value, batch, targetdir, fast=False, keys={}):

	print "Preparing xfitter for {0} mode {1} ".format(mode, ('with {0} values'.format(value) if value else ''))

	# copy
	target = os.path.join(targetdir, os.path.basename(steeringfile))
	print "Copy steering file to", target

	datafiles = modes[mode] + (values[value] if value else [])
	corrfiles = (corrs[value] if value else [])
	settings = {
		'@NFILES@': str(len(datafiles)),
		'@FILES@': ",\n      ".join(datafiles),
		'@CORRFILES@': ",\n      ".join(corrfiles),
		'@NCORRFILES@': str(len(corrfiles)),
		# NNPDF Rew.
	}
	settings.update(keys)
	sherivftools.copyfile(steeringfile, target, settings)


if __name__ == "__main__":
	main()
