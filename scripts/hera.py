#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir and all files, start herafitter in parallel with GC including all uncertainties
"""

import time, sys, os, glob, argparse, subprocess
import sherivf
import copy_herafitter_steering


class Hera(object):
	def __init__(self):
		self.default_mode = 'hera'
		self.default_config = "herafitter.conf"
		self.default_storage_path = '/storage/a/dhaitz/hera/'
		self.get_arguments()

	def run(self):
		self.create_output_dir()
		files_to_copy = [self.default_config, 'minuit.in.txt', 'herapdf_par.conf', 'ewparam.txt','run-herafitter.sh']
		self.list_of_gc_files = [sherivf.get_env('SHERIVFDIR') + '/hera-gc/' + f for f in files_to_copy]
		self.copy_gc_files()
		self.gctime = time.time()
		sherivf.run_gc(self.args.output_dir + "/" + self.args.config, self.args.output_dir)
		self.gctime = time.time() - self.gctime
	
		subprocess.call(['ln', '-sf', self.args.output_dir+"/output/", sherivf.get_env('SHERIVFDIR')+'/latest_herafitter_'+self.args.mode])


	def copy_gc_files(self):
		for gcfile in self.list_of_gc_files:
			sherivf.copyfile(gcfile, self.args.output_dir+'/'+os.path.basename(gcfile),{
				'@OUTDIR@': self.args.output_dir+'/output',
				'@MODE@': self.args.mode,
			})
		copy_herafitter_steering.copy_herafile(self.args.mode, True, self.args.output_dir)


	def create_output_dir(self):
		print "Output directory:", self.args.output_dir
		os.makedirs(self.args.output_dir + "/work." + self.args.config.replace(".conf", ""))
		os.makedirs(self.args.output_dir + "/output")


	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the main analysis program.", epilog="Have fun.")

		parser.add_argument('-m', '--mode', type=str, default=self.default_mode,
			help="mode (hera, heraZ)")
		parser.add_argument('-c', '--config', type=str, default=self.default_config,
			help="")
		parser.add_argument('-o', '--output-dir', type=str, default=None,
			help="")
		
		self.args = parser.parse_args()
		if self.args.output_dir is None:
			self.args.output_dir = (self.args.mode + "_" + time.strftime("%Y-%m-%d_%H-%M"))
		self.args.output_dir = self.default_storage_path + "/" + self.args.output_dir

if __name__ == "__main__":
	start_time = time.time()
	hera = Hera()
	hera.run()
	if hasattr(hera, "gctime"):
		print "---        Hera took {}  ---".format(sherivf.format_time(time.time() - start_time))
		print "--- GridControl took {}  ---".format(sherivf.format_time(hera.gctime))