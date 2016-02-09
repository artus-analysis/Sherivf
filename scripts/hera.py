#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir and all files, start herafitter in parallel with GC including all uncertainties
"""

import time, sys, os, glob, argparse, subprocess
import tools
import copy_herafitter_steering


class Hera(object):
	def __init__(self):
		self.default_mode = 'hera2'
		self.default_value = None
		self.default_config = "herafitter.conf"
		self.default_storage_path = '/storage/a/dhaitz/hera/'
		self.get_arguments()

	def run(self):
		# create gc-dir and copy necessary files
		self.create_output_dir()
		files_to_copy = [self.default_config, 'minuit.in.txt', 'herapdf_par.conf', 'ewparam.txt','run-herafitter.sh']
		self.list_of_gc_files = [tools.get_env('SHERIVFDIR') + '/hera-gc/' + f for f in files_to_copy]
		self.copy_gc_files()

		self.gctime = time.time()
		tools.run_gc(self.args.output_dir + "/" + self.args.config, self.args.output_dir)
		self.gctime = time.time() - self.gctime

		tools.create_result_linkdir(self.args.output_dir+"/output/", self.args.mode + ('_' + self.args.value if self.args.value else ''))


	def copy_gc_files(self):
		for gcfile in self.list_of_gc_files:
			tools.copyfile(gcfile, self.args.output_dir+'/'+os.path.basename(gcfile),{
				'@OUTDIR@': self.args.output_dir+'/output',
			})
		copy_herafitter_steering.copy_herafile(self.args.mode, self.args.value, True, self.args.output_dir, self.args.fast)


	def create_output_dir(self):
		print "Output directory:", self.args.output_dir
		os.makedirs(self.args.output_dir + "/work." + self.args.config.replace(".conf", ""))
		os.makedirs(self.args.output_dir + "/output")


	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the main analysis program.", epilog="Have fun.")

		parser.add_argument('-m', '--mode', type=str, default=self.default_mode, help="mode", choices=copy_herafitter_steering.modes.keys())
		parser.add_argument('-v', '--value', type=str, default=self.default_value, help="Value", choices=copy_herafitter_steering.values.keys())
		parser.add_argument('-c', '--config', type=str, default=self.default_config,
			help="default:" + self.default_config)
		parser.add_argument('-o', '--output-dir', type=str, default=None, help="")
		parser.add_argument('-f', '--fast', action="store_true", help="RT FAST scheme (instead of RT)")
		
		self.args = parser.parse_args()
		if self.args.output_dir is None:
			self.args.output_dir = (self.args.mode + ('_' + self.args.value if self.args.value else '') + "_" + time.strftime("%Y-%m-%d_%H-%M"))
		self.args.output_dir = self.default_storage_path + "/" + self.args.output_dir

if __name__ == "__main__":
	start_time = time.time()
	hera = Hera()
	hera.run()
	if hasattr(hera, "gctime"):
		print "---        Hera took {}  ---".format(tools.format_time(time.time() - start_time))
		print "--- GridControl took {}  ---".format(tools.format_time(hera.gctime))
