#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""copy herafitter steering file and replace certain parameters according to fit mode"""

import argparse
import os

import sherivf


def main():
	"""main"""
	heradir = os.environ['HERADIR']
	steeringfile = os.path.join(os.environ['SHERIVFDIR'], "herafitter/steering.txt")

	heradict = {
		'nnpdf': [1, "'{}/herafitter/CMS_Zee_HFinput.txt'".format(os.environ['SHERIVFDIR']), 'True'],

		'hera': [4, """'{hera}/datafiles/hera/H1ZEUS_NC_e-p_HERA1.0.dat',
      '{hera}/datafiles/hera/H1ZEUS_NC_e+p_HERA1.0.dat'
      '{hera}/datafiles/hera/H1ZEUS_CC_e-p_HERA1.0.dat'
      '{hera}/datafiles/hera/H1ZEUS_CC_e+p_HERA1.0.dat'""".format(hera=heradir),'False'],

		'heraZ': [5, """'{hera}/datafiles/hera/H1ZEUS_NC_e-p_HERA1.0.dat',
      '{hera}/datafiles/hera/H1ZEUS_NC_e+p_HERA1.0.dat'
      '{hera}/datafiles/hera/H1ZEUS_CC_e-p_HERA1.0.dat'
      '{hera}/datafiles/hera/H1ZEUS_CC_e+p_HERA1.0.dat'
      '{sh}/herafitter/CMS_Zee_HFinput.txt'""".format(hera=heradir, sh=os.environ['SHERIVFDIR']), 'False'],
	}

	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--mode', type=str, default='nnpdf',
		help="mode", choices=heradict.keys())
	parser.add_argument('-d', '--dir', type=str, default=heradir, help="dir to copy steering file to")
	args = parser.parse_args()

	print "Preparing Herafitter for {} mode".format(args.mode)


	# copy
	values = heradict[args.mode]
	target = os.path.join(args.dir, os.path.basename(steeringfile))
	print "Copy steering file to", target
	sherivf.copyfile(steeringfile, target, {
				'@NFILES@': str(values[0]),
				'@FILES@': values[1],
				'@DOREWEIGHTING@': values[2],
				'@OUTDIRNAME@': args.mode,
			})


if __name__ == "__main__":
	main()
