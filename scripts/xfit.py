#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir and all files, start xfitter in parallel with GC to calculate all uncertainties
"""

import time
import sys
import os
import glob
import argparse
import subprocess

import sherivftools
import make_pdf_uncertainties


class Xfit(object):
	
	def __init__(self):
		self.config = "xfitter.conf"
		self.files_to_copy = [self.config, 'minuit.in.txt', 'ewparam.txt','run-xfitter.sh']
		self.default_storage_path = sherivftools.get_env('HERA_STORAGE_PATH')
		self.get_arguments()
		# datafiles for HERA:
		self.datafiles_hera = ["'{0}'".format(os.path.join(os.path.join(os.environ['SHERIVFDIR'], "datafiles/hera/"), f)) for f in os.listdir(os.path.join(os.environ['SHERIVFDIR'], "datafiles/hera/"))]
		self.corrfiles_hera = []
		# datafiles for CMS: zpt in rapidity bins:
		self.rapidity_bins = ["{0:02d}".format(i) for i in range(0, 28, 4)]
		self.rapidity_bins_strings = ["{0}y{1}".format(a,b) for a,b in zip(rapidity_bins[:-1], rapidity_bins[1:])]
		self.datafiles += [("'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_HFinput_{0}_{1}.txt'").format('zpt', ptbin) for ptbin in rapidity_bins_strings[:-1]]
		self.corrfiles += [("'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_correlation_{0}_{1}.corr'").format('zpt', ptbin) for ptbin in rapidity_bins_strings[:-1]]
	
	
	def get_arguments(self):
		parser = argparse.ArgumentParser(description="%(prog)s is the main analysis program.", epilog="Have fun.")
		parser.add_argument('mode', type=str, default='hera', help="Mode. Can be hera or heracms", choices=['hera', 'heracms'])
		self.args = parser.parse_args()
		self.output_dir = self.default_storage_path + "/" + self.args.mode +  "_" + time.strftime("%Y-%m-%d_%H-%M")
	
	
	def run(self):
		# create gc-dirs
		print "Output directory:", self.output_dir
		os.makedirs(self.output_dir + "/work." + self.config.replace(".conf", ""))
		os.makedirs(self.output_dir + "/output")
		
		# copy GC files
		self.list_of_gc_files = [sherivftools.get_env('SHERIVFDIR') + '/xfitter/' + f for f in self.files_to_copy]
		for gcfile in self.list_of_gc_files:
			sherivftools.copyfile(gcfile, self.output_dir+'/'+os.path.basename(gcfile),{
				'@OUTDIR@': self.output_dir+'/output',
				'@SHERIVFDIR@': sherivftools.get_env('SHERIVFDIR'),
			})
		
		# put together steering.txt and copy
		steeringfile = os.path.join(os.environ['SHERIVFDIR'], "xfitter/steering.txt")
		target = os.path.join(self.output_dir, os.path.basename(steeringfile))
		datafiles = self.dataFiles_hera
		corrfiles = self.corrfiles_hera
		if self.args.mode == 'heracms':
			datafiles += self.datafiles_cms
			corrfiles += self.corrfiles_cms
		settings = {  # these values are replaced in the steering file
			'@NFILES@': str(len(datafiles)),
			'@FILES@': ",\n      ".join(datafiles),
			'@CORRFILES@': ",\n      ".join(corrfiles),
			'@NCORRFILES@': str(len(corrfiles)),
		}
		sherivftools.copyfile(steeringfile, target, settings)
		
		# run GC
		self.gctime = time.time()
		gc_exitcode= sherivftools.run_gc(self.output_dir + "/" + self.config, self.output_dir)
		self.gctime = time.time() - self.gctime
		if gc_exitcode == 0:
			sherivftools.create_result_linkdir(self.output_dir, self.args.mode)
		
		# merge outputs to get exp/model/par uncertainties
		for q in make_pdf_uncertainties.q_values:
			base = self.output_dir+"/output/job_{0}_hf_pdf__" + q + ".root"
			output_filename = self.output_dir+"/pdf_" + q + ".root"
			make_pdf_uncertainties.make_pdf_uncertainties(
				base.format("0"),
				[base.format(str(n)) for n in range(1, 9)+[18, 19]],
				[base.format(str(n)) for n in range(9, 18)],
				output_filename
			)


if __name__ == "__main__":
	start_time = time.time()
	xfit = Xfit()
	xfit.run()
	if hasattr(xfit, "gctime"):
		print "---     xFitter took {}  ---".format(sherivftools.format_time(time.time() - start_time))
		print "--- GridControl took {}  ---".format(sherivftools.format_time(xfit.gctime))
