#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is the GC wrapper

sherivf.py
"""

import argparse
import getpass
import glob
import multiprocessing
import os
import shutil
import socket
import subprocess
import sys
import time

import sherivftools


class Sherivf(object):

	def __init__(self, rivet_analysis, sherpa_runcard):
		self.rivet = rivet_analysis
		self.sherpa = sherpa_runcard
		self.sherivf_path = sherivftools.get_env('SHERIVFDIR')
		self.compile_path = sherivftools.get_env('COMPILE')
		self.mode_dict = {
			"compile":self.compile_rivet_plugin,
			"integrate": self.sherpa_integration_run,
			"warmup": self.warmup,
			"local": self.local,
			"batch": self.batch
		}
		self.get_arguments()
		self.fastnlo_outputs = [os.path.basename(f).replace('.txt', ('.txt' if (self.args.mode == 'warmup') else '.tab')) for f in glob.glob(os.path.join(self.sherivf_path,'fastnlo', '*.txt' ))]


	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the wrapper for Monte Carlo production and generation of fastNLO tables.", epilog="Have fun.")

		parser.add_argument('mode', type=str, choices=self.mode_dict.keys(),
			help="mode. [Default: %(default)s]")

		# for batch mode
		parser.add_argument('-d', '--delete', action='store_true',
			help="delete the latest output and jobs still running")
		parser.add_argument('-r', '--resume', action='store_true',
			help="resume the grid-control run.")
		parser.add_argument('-j', '--n-jobs', type=str, default='1',
			help="n jobs [Default: %(default)s]")
		parser.add_argument('--output-dir', type=str, help="output directory [Default: %(default)s]",
			default=sherivftools.get_env('SHERIVF_STORAGE_PATH'))
		parser.add_argument('-b', '--batch', type=str, default='ekpcluster', choices=['ekpcluster'],
			help="batch config. [Default: %(default)s]")

		# for local and batch
		parser.add_argument('-n', '--n-events', type=str, default='1000000',
			help="n events [Default: %(default)s]")

		self.args = parser.parse_args()

		# define configs to use
		self.args.configfile = 'sherpa-rivet_{0}.conf'.format(self.args.batch)
		self.args.list_of_gc_cfgs = [
			self.sherivf_path + '/' + 'sherpa/sherpa-rivet_base.conf',
			self.sherivf_path + '/' + 'sherpa/run-sherpa.sh',
			self.sherivf_path + '/' + 'sherpa/sherpa-rivet_{0}.conf'.format(self.args.batch)
		]
		if self.args.batch == 'ekpcloud':  # jobs on cloud can only write on ekpcloud_local, not regular storage
			path_list = self.args.output_dir.split('/')
			path_list[path_list.index('storage')+1] = 'ekpcloud_local'
			self.args.output_dir = "/".join(path_list)


	def run(self):
		"""Main function. Decide between compilation, integration, local production or batch production mode."""
		start_time = time.time()
		self.mode_dict[self.args.mode]()  # start mode
		print "---	 Sherivf took {0} ---".format(sherivftools.format_time(time.time() - start_time))
		if hasattr(self, "gctime"):
			print "--- GridControl took {0} ---".format(sherivftools.format_time(self.gctime))


	def batch(self):
		""" Check if a new workdir has to be created.  Delete, resume or start new (default) run"""
		# config dir: already existing or create new one?
		if self.args.delete or self.args.resume:
			paths = glob.glob("{0}/{1}*".format(self.args.output_dir, self.args.batch))
			paths.sort()
			try:
				self.args.output_dir = paths[-1]
				self.args.configfile = filter(lambda x: "work.sherpa-rivet" in x, glob.glob(paths[-1] + "/*"))[0].split("work.")[-1] + ".conf"
			except IndexError:
				sys.exit("No output directories exist!")
		else:
			self.args.output_dir += (self.args.batch + "_" + time.strftime("%Y-%m-%d_%H-%M"))

		# delete, normal run or warmup?
		if self.args.delete:
			self.delete_latest_output_dir()
		else:
			if not self.args.resume:
				self.create_output_dir()
				self.copy_gc_configs()
			self.gctime = time.time()
			gc_exitcode = sherivftools.run_gc(self.args.output_dir + "/" + self.args.configfile, self.args.output_dir)
			if gc_exitcode > 0:
				print "grid-control run not successful!"
				sys.exit(1)
			self.gctime = time.time() - self.gctime

			outputs = self.merge_outputs()
			print "\nOutput files:\n", "\n".join(outputs)

			# create link to latest output:
			link_dir = os.path.join(self.sherivf_path, 'results')
			if not os.path.exists(link_dir):
				os.makedirs(link_dir)
			link = link_dir+'/'+self.rivet + '_' + self.sherpa
			subprocess.call(['rm', '-f', link])
			subprocess.call(['ln', '-sf', self.args.output_dir, link])


	def delete_latest_output_dir(self):
		try:
			subprocess.call(['go.py', self.args.output_dir + "/" + self.args.configfile, "-d all"])
		except OSError as e:
			print "could not delete currently running jobs ({0}): {1}".format(e.errno, e.strerror)
			exit(1)
		try:
			shutil.rmtree(self.args.output_dir)
			print "Directory {0} deleted.".format(self.args.output_dir)
		except OSError as e:
			print "Could not delete output directory {0} ({1}): {2}".format(self.args.output_dir, e.errno, e.strerror)


	def local(self, warmup=False):
		"""LOCAL EXECUTION (for Testing)"""
		test_dir = os.path.join(self.sherivf_path, 'test', time.strftime("%Y-%m-%d_%H-%M-%S"))
		print "Create directory", test_dir

		# copy Sherpa/Rivet/fastNLO files to test directory
		for filelist, function in zip([
			['sherpa', self.sherpa],
			['rivet', 'Rivet_{0}.so'.format(self.rivet)],
			['fastnlo', self.rivet+'.str'],
		], ["copytree", "copy", "copy"]):
			try:
				getattr(shutil, function)(os.path.join(self.sherivf_path, *filelist), test_dir)
			except IOError:
				print "Could not copy", os.path.join(self.sherivf_path, *filelist)

		os.chdir(test_dir)
		for _dir in ["MCGRID_OUTPUT_PATH", "MCGRID_PHASESPACE_PATH"]:
			os.environ[_dir] = test_dir

		# paths for mc grid and Rivet
		ph_path = os.path.join(test_dir, self.rivet, "phasespace")
		ph_target_dir = os.path.join(self.sherivf_path, 'fastnlo')
		os.environ["RIVET_ANALYSIS_PATH"] = test_dir

		# copy warmupfiles and event count file
		if not warmup:
			try:
				shutil.copy(os.path.join(ph_target_dir, self.rivet+".str.evtcount"), test_dir)
			except IOError:
				print "could not copy", os.path.join(ph_target_dir, self.rivet+".str.evtcount")
			warmupfiles = glob.glob(os.path.join(ph_target_dir, "*.txt"))
			if not os.path.exists(ph_path):
				os.makedirs(ph_path)
			for wfile in warmupfiles:
				shutil.copy(wfile, ph_path)
		
		# execute Sherpa
		sherivftools.print_and_call(["Sherpa", "-e "+str(self.args.n_events)])
		
		# copy warmup and event count files
		if warmup:
			for f in glob.glob(ph_path+"/*.txt"):
				if not os.path.exists(ph_target_dir):
					os.makedirs(ph_target_dir)
				shutil.copy(f, ph_target_dir)
			shutil.copy(os.path.join(test_dir, self.rivet+".str.evtcount"), ph_target_dir)
			print "Copied warmup files to", ph_target_dir

		print "Sherpa was run in", test_dir

	def warmup(self):
		self.local(warmup=True)

	def create_output_dir(self):
		"""
			ensure that the output path exists and delete old outputs optionally)
			to save your outputs simply rename them without timestamp
		"""
		print "Output directory:", self.args.output_dir
		os.makedirs(self.args.output_dir + "/work." + self.args.configfile.replace(".conf", ""))
		os.makedirs(self.args.output_dir + "/output")


	def copy_gc_configs(self):

		# files to be copied by gc to workdir
		inputfiles = [
			os.path.join(self.sherivf_path, 'rivet', 'Rivet_{0}.so'.format(self.rivet)),
			os.path.join(self.sherivf_path, 'sherpa', self.sherpa, '*.*'),
			os.path.join(self.sherivf_path, 'fastnlo', '*.*'),
		]

		for gcfile in self.args.list_of_gc_cfgs:
			sherivftools.copyfile(gcfile, self.args.output_dir+'/'+os.path.basename(gcfile),{
				'@NEVENTS@': self.args.n_events,
				'@NJOBS@': self.args.n_jobs,
				'@OUTDIR@': self.args.output_dir+'/output',
				'@WARMUP@': ("rm *.txt"if (self.args.mode == 'warmup') else ""),
				'@OUTPUT@': "Rivet.yoda " + ' '.join(self.fastnlo_outputs),
				'@CONFIG@': self.sherpa,
				'@ANALYSIS@': self.rivet,
				'@INPUTFILES@': "\n\t".join(inputfiles),
				'@SHERIVFDIR@': sherivftools.get_env('SHERIVFDIR'),
			})


	def merge_outputs(self):
		outputs = []
		# DISABLE RIVET.YODA MERGING UNTIL FIXED
		#try:
		#	#merge yoda files
		#	yoda_files = glob.glob(self.args.output_dir+'/output/'+'*.yoda')
		#	commands = ['yodamerge'] + yoda_files + ['-o', self.args.output_dir+'/Rivet.yoda'
		#	sherivftools.print_and_call(commands)
		#	outputs.append(self.args.output_dir+'/Rivet.yoda')
		#except OSError as e:
		#	print "Could not merge Rivet outputs ({0}): {1}".format(e.errno, e.strerror)
		try:
			#merge fastNLO files: gather commands
			commands_list = []
			for quantity in [item.replace(".tab", "") for item in self.fastnlo_outputs]:
				commands = ['fnlo-tk-merge'] + glob.glob(self.args.output_dir+'/output/'+'{0}*.tab'.format(quantity)) + [self.args.output_dir+'/{0}.tab'.format(quantity)]
				commands_list.append(commands)
				outputs.append(self.args.output_dir+'/{0}.tab'.format(quantity))
			# DISABLE FASTNLO PARALLEL MERGING UNTIL FIXED
			#pool = multiprocessing.Pool(processes=len(commands_list))
			#results = pool.map_async(sherivftools.print_and_call, commands_list)
			#res = results.get(9999999) # 9999999 is needed for KeyboardInterrupt to work: htt
			for commands in commands_list:
				sherivftools.print_and_call(commands)
		except OSError as e:
			print "Could not merge fastNLO outputs ({0}): {1}".format(e.errno, e.strerror)

		return outputs


	def compile_rivet_plugin(self):
		""" compile the Rivet plugin via rivet-buildplugin"""
		print "Compiling Rivet Plugin {0}".format(self.rivet)
		os.chdir(os.path.join(self.sherivf_path, 'rivet'))
		sherivftools.print_and_call([
			'rivet-buildplugin', 
			"{path}/Rivet_{analysis}.so {path}/{analysis}.cc".format(
				analysis=self.rivet,
				path=os.path.join(self.sherivf_path, 'rivet')
			),
			"-std=c++0x -Wl,--export-dynamic,-z,defs -I"+self.compile_path+"/include -L"+self.compile_path+"/lib -lmcgrid -lYODA"
		])


	def sherpa_integration_run(self):
		"""Switch to sherpa dir, delete files other than Run.dat, integrate"""
		directory = os.path.join(self.sherivf_path, 'sherpa', self.sherpa)
		try:
			print "Preparing for integration run in directory", directory
			os.chdir(directory)
			files_to_delete = os.listdir(os.getcwd())
			files_to_delete.remove('Run.dat')
			if len(files_to_delete) > 0:
				rm_command = ["rm", "-rf"] + files_to_delete
				if sherivftools.query_yes_no("Delete {0}?".format(" ".join(files_to_delete))):
					sherivftools.print_and_call(rm_command)
			if sherivftools.print_and_call(["Sherpa", "-e "+str(self.args.n_events)]):
				print "Sucessfully ran Sherpa in directory", directory

			#check for 'makelibs' (produced by AMEGIC)
			if os.path.isfile('makelibs') and sherivftools.query_yes_no("Compile makelibs?"):
				if sherivftools.print_and_call(["./makelibs"]):
					print "Sucessfully compiled libraries with './makelibs'"

		except OSError:
			print "ERROR: could not switch to directory", directory
		return


if __name__ == "__main__":
	sherivf = Sherivf(rivet_analysis='MCgrid_CMS_2015_Zee', sherpa_runcard='zjet')
	sherivf.run()
