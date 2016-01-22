#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is the GC wrapper

sherivf.py
"""

import sys, os, glob, shutil, time, subprocess, argparse, socket, multiprocessing
from tools import run_gc, print_and_call, copyfile, get_env, query_yes_no, format_time


class Sherivf(object):

	def __init__(self):

		if 'naf' in socket.gethostname().lower():
			self.default_config = 'naf'
		elif 'ekp' in socket.gethostname().lower():
			self.default_config = 'ekpcluster'
		self.default_storage_path = get_env('SHERIVF_STORAGE_PATH')
		self.sherivf_path = get_env('SHERIVFDIR')
		self.get_arguments()
		self.fastnlo_outputs = [os.path.basename(f).replace('.txt', '.tab') for f in glob.glob(os.path.join(self.sherivf_path,'fastnlo',self.args.rivet, '*.txt' ))]


	def run(self):
		"""Main function."""
		if self.args.compile:  # compilation
			self.compile_rivet_plugin()
			return
		elif self.args.integrate:  # integration run
			self.sherpa_integration_run()
		elif self.args.batch is None:  # local
			self.local()
			return
		else:  # batch
			self.batch()


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
			run_gc(self.args.output_dir + "/" + self.args.configfile, self.args.output_dir)
			self.gctime = time.time() - self.gctime

			outputs = self.merge_outputs()
			print "\nOutput files:\n", "\n".join(outputs)

			# create link to latest output:
			link_dir = os.path.join(self.sherivf_path, 'outputs')
			if not os.path.exists(link_dir):
				os.makedirs(link_dir)
			link = link_dir+'/'+self.args.rivet + '_' + self.args.sherpa
			subprocess.call(['rm', '-f', link])
			subprocess.call(['ln', '-sf', self.args.output_dir, link])
			subprocess.call(['yoda_2_root.py', link + '/Rivet.yoda'])


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


	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the main analysis program.", epilog="Have fun.")

		# for batch mode
		parser.add_argument('-b', '--batch', type=str, nargs="?", const=self.default_config,
			help="batch mode. cfg optional")
		parser.add_argument('-d', '--delete', action='store_true',
			help="delete the latest output and jobs still running")
		parser.add_argument('-r', '--resume', action='store_true',
			help="resume the grid-control run.")
		parser.add_argument('-j', '--n-jobs', type=str, default='1',
			help="n jobs")

		# cfgs: sherpa, analysis
		parser.add_argument('-s', '--sherpa', type=str, default='zjet',
			help="sherpa config in folder sherpa. [Default: %(default)s]")
		parser.add_argument('-i', '--integrate', action="store_true",
			help="Integration run for Sherpa. [Default: %(default)s]")
		parser.add_argument('--rivet', type=str, default='MCgrid_CMS_2015_Zee',
			help="name of rivet analysis")
		parser.add_argument('-c', '--compile', action='store_true',
			help="if set, compile analysis")

		parser.add_argument('-w', '--warmup', action='store_true', default=False,
			help="if set, do warmup run")
		parser.add_argument('-n', '--n-events', type=str, default='1000',
			help="n events")
		parser.add_argument('--output-dir', type=str, help="output directory",
			default=self.default_storage_path)

		self.args = parser.parse_args()

		# define configs to use
		self.args.configfile = 'sherpa-rivet_{0}.conf'.format(self.args.batch)
		self.args.list_of_gc_cfgs = [
			self.sherivf_path + '/' + 'gc_configs/sherpa-rivet_base.conf',
			self.sherivf_path + '/' + 'gc_configs/run-sherpa.sh',
			self.sherivf_path + '/' + 'gc_configs/sherpa-rivet_{0}.conf'.format(self.args.batch)
		]
		if 'ekp' in socket.gethostname().lower():
			self.args.list_of_gc_cfgs.append(self.sherivf_path + '/' + 'gc_configs/sherpa-rivet_ekp-base.conf')
		if self.args.batch == 'ekpcloud':
			self.args.output_dir = self.args.output_dir.replace("/a/", "/ekpcloud_local/")


	def local(self):
		"""LOCAL EXECUTION (for Testing)"""
		test_dir = os.path.join(self.sherivf_path, 'test', time.strftime("%Y-%m-%d_%H-%M-%S"))
		print "Create directory", test_dir

		# copy Sherpa/Rivet/fastNLO files to test directory
		for filelist, function in zip([
			['sherpa', self.args.sherpa],
			['rivet', self.args.rivet, 'Rivet_{0}.so'.format(self.args.rivet)],
			['fastnlo', self.args.rivet, self.args.rivet+'.str'],
		], ["copytree", "copy", "copy"]):
			try:
				getattr(shutil, function)(os.path.join(self.sherivf_path, *filelist), test_dir)
			except IOError:
				print "Could not copy", os.path.join(self.sherivf_path, *filelist)

		os.chdir(test_dir)
		for _dir in ["MCGRID_OUTPUT_PATH", "MCGRID_PHASESPACE_PATH"]:
			os.environ[_dir] = test_dir

		# paths for mc grid and Rivet
		ph_path = os.path.join(test_dir, self.args.rivet, "phasespace")
		ph_target_dir = os.path.join(self.sherivf_path, 'fastnlo', self.args.rivet)
		os.environ["RIVET_ANALYSIS_PATH"] = test_dir

		# copy warmupfiles and event count file
		if not self.args.warmup:
			try:
				shutil.copy(os.path.join(ph_target_dir, self.args.rivet+".str.evtcount"), test_dir)
			except IOError:
				print "could not copy", os.path.join(ph_target_dir, self.args.rivet+".str.evtcount")
			warmupfiles = glob.glob(os.path.join(ph_target_dir, "*.txt"))
			if not os.path.exists(ph_path):
				os.makedirs(ph_path)
			for wfile in warmupfiles:
				shutil.copy(wfile, ph_path)
		
		print_and_call(["Sherpa", "-e "+str(self.args.n_events)])
		
		# copy warmup and event count files
		if self.args.warmup:
			for f in glob.glob(ph_path+"/*.txt"):
				if not os.path.exists(ph_target_dir):
					os.makedirs(ph_target_dir)
				shutil.copy(f, ph_target_dir)
			shutil.copy(os.path.join(test_dir, self.args.rivet+".str.evtcount"), ph_target_dir)
			print "Copied warmup files to", ph_target_dir

		# convert yoda to root
		if os.path.isfile('Rivet.yoda'):
			print "Convert Rivet output from YODA to ROOT"
			print_and_call(['yoda_2_root.py', 'Rivet.yoda'])

		print "Sherpa was run in", test_dir


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
			os.path.join(self.sherivf_path, 'rivet', self.args.rivet, 'Rivet_{0}.so'.format(self.args.rivet)),
			os.path.join(self.sherivf_path, 'sherpa', self.args.sherpa, '*.*'),
			os.path.join(self.sherivf_path, 'fastnlo', self.args.rivet, '*.*'),
		]

		for gcfile in self.args.list_of_gc_cfgs:
			copyfile(gcfile, self.args.output_dir+'/'+os.path.basename(gcfile),{
				'@NEVENTS@': self.args.n_events,
				'@NJOBS@': self.args.n_jobs,
				'@OUTDIR@': self.args.output_dir+'/output',
				'@WARMUP@': ("rm *.txt"if self.args.warmup else ""),
				'@OUTPUT@': "Rivet.yoda " + ' '.join(self.fastnlo_outputs),
				'@CONFIG@': self.args.sherpa,
				'@ANALYSIS@': self.args.rivet,
				'@INPUTFILES@': "\n\t".join(inputfiles),
			})


	def merge_outputs(self):
		outputs = []
		try:
			#merge yoda files
			yoda_files = glob.glob(self.args.output_dir+'/output/'+'*.yoda')
			commands = ['yodamerge'] + yoda_files + ['-o', self.args.output_dir+'/Rivet.yoda']
			print_and_call(commands)
			#apply scalefactor
			scalefactor = 1./len(yoda_files)
			commands = ['yodascale', '-c', "'.* {0}x'".format(scalefactor), '-i', self.args.output_dir+'/Rivet.yoda']
			print_and_call(commands)
			outputs.append(self.args.output_dir+'/Rivet.yoda')
		except OSError as e:
			print "Could not merge Rivet outputs ({0}): {1}".format(e.errno, e.strerror)

		try:
			#merge fastNLO files: gather commands
			commands_list = []
			for quantity in [item.replace(".tab", "") for item in self.fastnlo_outputs]:
				commands = ['fnlo-tk-merge'] + glob.glob(self.args.output_dir+'/output/'+'{0}*.tab'.format(quantity)) + [self.args.output_dir+'/{0}.tab'.format(quantity)]
				commands_list.append(commands)
				outputs.append(self.args.output_dir+'/{0}.tab'.format(quantity))
			# merge in parallel
			pool = multiprocessing.Pool(processes=len(commands_list))
			results = pool.map_async(print_and_call, commands_list)
			res = results.get(9999999) # 9999999 is needed for KeyboardInterrupt to work: http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
		except OSError as e:
			print "Could not merge fastNLO outputs ({0}): {1}".format(e.errno, e.strerror)

		return outputs


	def compile_rivet_plugin(self):
		""" compile the Rivet plugin via rivet-buildplugin. compiler flags are
		read in via env var RIVET_COMPILER_FLAGS"""
		os.chdir(os.path.join(self.sherivf_path, 'rivet'))
		print "Compiling Rivet Plugin {0}".format(self.args.rivet)
		print_and_call([
			'rivet-buildplugin', 
			"{path}/Rivet_{analysis}.so {path}/{analysis}.cc".format(
				analysis=self.args.rivet,
				path=os.path.join(self.sherivf_path, 'rivet', self.args.rivet)
			),
			get_env("RIVET_COMPILER_FLAGS")
		])


	def sherpa_integration_run(self):
		"""Switch to sherpa dir, delete files other than Run.dat, integrate"""
		directory = os.path.join(self.sherivf_path, 'sherpa', self.args.sherpa)
		try:
			print "Preparing for integration run in directory", directory
			os.chdir(directory)
			files_to_delete = os.listdir(os.getcwd())
			files_to_delete.remove('Run.dat')
			if len(files_to_delete) > 0:
				rm_command = ["rm", "-rf"] + files_to_delete
				if query_yes_no("Delete {0}?".format(" ".join(files_to_delete))):
					print_and_call(rm_command)
			print_and_call(["Sherpa", "-e "+str(self.args.n_events)])
			print "Sucessfully ran Sherpa in directory", directory

			#check for 'makelibs' (produced by AMEGIC)
			if os.path.isfile('makelibs') and query_yes_no("Compile makelibs?"):
				print_and_call(["./makelibs"])
				print "Sucessfully compiled libraries with './makelibs'"

		except OSError:
			print "ERROR: could not switch to directory", directory
		return


if __name__ == "__main__":
	start_time = time.time()
	sherivf = Sherivf()
	sherivf.run()
	if hasattr(sherivf, "gctime"):
		print "---	 Sherivf took {0} ---".format(format_time(time.time() - start_time))
		print "--- GridControl took {0} ---".format(format_time(sherivf.gctime))
