#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir and all files, start herafitter in parallel with GC including all uncertainties
"""

import time, sys, os, glob, argparse, subprocess
import sherivftools
import copy_herafitter_steering
import make_pdf_uncertainties


class Hera(object):

	def __init__(self):
		self.mode = 'hera2'
		self.default_value = None
		#self.config = "herafitter_scan.conf"
		self.config = "herafitter.conf"
		self.files_to_copy = [self.config, 'minuit.in.txt', 'herapdf_par.conf', 'ewparam.txt','run-herafitter.sh']
		#self.files_to_copy = [self.config, 'minuit.in.txt', 'herapdf_par_scan.conf', 'ewparam.txt','run-herafitter.sh']
		self.default_storage_path = sherivftools.get_env('HERA_STORAGE_PATH')
		self.get_arguments()


	def get_arguments(self):
		parser = argparse.ArgumentParser(description="%(prog)s is the main analysis program.", epilog="Have fun.")
		parser.add_argument('-v', '--value', type=str, default=self.default_value, help="Value", choices=copy_herafitter_steering.values.keys())
		self.args = parser.parse_args()
		self.output_dir = self.default_storage_path + "/" + (self.mode + ('_' + self.args.value if self.args.value else '') + "_" + time.strftime("%Y-%m-%d_%H-%M"))


	def run(self):
		# create gc-dirs
		print "Output directory:", self.output_dir
		os.makedirs(self.output_dir + "/work." + self.config.replace(".conf", ""))
		os.makedirs(self.output_dir + "/output")
		
		# copy necessary files
		self.list_of_gc_files = [sherivftools.get_env('SHERIVFDIR') + '/hera-gc/' + f for f in self.files_to_copy]
		for gcfile in self.list_of_gc_files:
			sherivftools.copyfile(gcfile, self.output_dir+'/'+os.path.basename(gcfile),{
				'@OUTDIR@': self.output_dir+'/output',
			})
		copy_herafitter_steering.copy_herafile(self.mode, self.args.value, True, self.output_dir)
		
		# run GC
		self.gctime = time.time()
		gc_exitcode= sherivftools.run_gc(self.output_dir + "/" + self.config, self.output_dir)
		self.gctime = time.time() - self.gctime
		if gc_exitcode == 0:
			sherivftools.create_result_linkdir(self.output_dir, self.mode + ('_' + self.args.value if self.args.value else ''))

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
	hera = Hera()
	hera.run()
	if hasattr(hera, "gctime"):
		print "---        Hera took {}  ---".format(sherivftools.format_time(time.time() - start_time))
		print "--- GridControl took {}  ---".format(sherivftools.format_time(hera.gctime))
