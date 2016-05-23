#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir and all files, start xfitter in parallel with GC to calculate all uncertainties
"""

import time, sys, os, glob, argparse, subprocess
import sherivftools
import make_pdf_uncertainties


class Xfit(object):

	def __init__(self):
		self.mode = 'hera'
		self.default_mode = None
		self.config = "xfitter.conf"
		self.files_to_copy = [self.config, 'minuit.in.txt', 'ewparam.txt','run-xfitter.sh']
		self.default_storage_path = sherivftools.get_env('HERA_STORAGE_PATH')
		self.get_arguments()


	def get_arguments(self):
		parser = argparse.ArgumentParser(description="%(prog)s is the main analysis program.", epilog="Have fun.")
		parser.add_argument('mode', type=str, default=self.default_mode, help="Mode. Can be hera or cms", choices=['hera', 'cms'])
		self.args = parser.parse_args()
		self.output_dir = self.default_storage_path + "/" + self.mode +  "_" + time.strftime("%Y-%m-%d_%H-%M")


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
			})
		
		# put together steering.txt and copy
		steeringfile = os.path.join(os.environ['SHERIVFDIR'], "xfitter/steering.txt")
		target = os.path.join(self.output_dir, os.path.basename(steeringfile))
		datafiles = ["'{}'".format(os.path.join(os.path.join(os.environ['SHERIVFDIR'], "datafiles/hera/"), f)) for f in os.listdir(os.path.join(os.environ['SHERIVFDIR'], "datafiles/hera/"))]
		corrfiles = []
		if self.mode == 'cms':
			datafiles += [("'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_HFinput_{0}_{1}.txt'").format('zpt', ptbin) for ptbin in common.ybin_labels[:-1]]
			corrfiles += [("'" + os.environ['SHERIVFDIR'] + "/datafiles/zjet/CMS_Zee_correlation_{0}_{1}.corr'").format('zpt', ptbin) for ptbin in common.ybin_labels[:-1]]
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
			sherivftools.create_result_linkdir(self.output_dir, self.mode)
		
		# merge outputs to get exp/model/par uncertainties
		for q in make_pdf_uncertainties.q_values:
			base = self.output_dir+"/output/job_{}_hf_pdf__" + q + ".root"
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
