#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is the GC wrapper"""

import sys, os, glob, shutil, time, subprocess, argparse, socket

class Sherivf(object):

	def __init__(self):
		quantities = ['abszy', 'zpt', 'zmass']
		quantities += ['y0_zpt', 'y1_zpt', 'y2_zpt', 'y3_zpt', 'y4_zpt']
		self.analysis = "MCgrid_CMS_2015_Zee"

		if 'naf' in socket.gethostname().lower():
			self.default_config = 'naf'
			self.default_storage_path = '/nfs/dust/cms/user/dhaitz/sherivf/'
		elif 'ekp' in socket.gethostname().lower():
			self.default_config = 'ekpcluster'
			self.default_storage_path = '/storage/a/dhaitz/sherivf/'
		self.get_arguments()
		suffix = (".txt" if self.args.warmup else ".tab")
		self.fastnlo_outputs = [quantity + suffix for quantity in quantities]


	def run(self):
		"""Main function.
			1. Get configs.
			2. Check if a new workdir has to be created.
			3. Delete, resume or start new (default) run
		"""

		# config dir: new or existing one?
		if self.args.delete or self.args.resume:
			paths = glob.glob("{0}/{1}*".format(self.args.output_dir, self.args.config))
			paths.sort()
			try:
				self.args.output_dir = paths[-1]
				self.args.configfile = filter(lambda x: "work.sherpa-rivet" in x, glob.glob(paths[-1] + "/*"))[0].split("work.")[-1] + ".conf"
			except IndexError:
				sys.exit("No output directories exist!")
		else:
			self.args.output_dir += (self.args.config + "_" + time.strftime("%Y-%m-%d_%H-%M"))

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
			if not self.args.warmup:
				outputs = self.merge_outputs()
				print "\nOutputs:\n", "\n".join(outputs)
				subprocess.call(['rm', '-f', 'latest_sherivf_output'])
				subprocess.call(['ln', '-sf', self.args.output_dir, 'latest_sherivf_output'])
				subprocess.call(['yoda_2_root.py', 'latest_sherivf_output/Rivet.yoda'])
			else:
				self.merge_warmup_files()
				for warmupfile in [item.replace(".", "_warmup.") for item in self.fastnlo_outputs]:
					subprocess.call(['mv', warmupfile, warmupfile.replace('_warmup', '')])
				subprocess.call(['mv', self.args.output_dir + "/" + self.analysis+".str.evtcount", "."])

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

		parser.add_argument('-c', '--config', type=str, default=self.default_config,
			help="config to run. will be set automatically for naf")
		parser.add_argument('-d', '--delete', action='store_true',
			help="delete the latest output and jobs still running")
		parser.add_argument('-r', '--resume', action='store_true',
			help="resume the grid-control run.")
		parser.add_argument('--rivet-only', action='store_true',
			help="only recover rivet outputs, not fastNLO.")
		parser.add_argument('-s', '--sherpa', type=str, default='fo',
			help="sherpa config in folder sherpa-cfg. [Default: %(default)s]")

		parser.add_argument('-n', '--n-events', type=str, default='1',
			help="n events")
		parser.add_argument('-j', '--n-jobs', type=str, default='1',
			help="n jobs")

		parser.add_argument('--output-dir', type=str, help="output directory",
			default=self.default_storage_path)

		parser.add_argument('-w', '--warmup', action='store_true', default=False,
			help="if set, do warmup run")

		self.args = parser.parse_args()

		# define configs to use
		self.args.configfile = 'sherpa-rivet_{0}.conf'.format(self.args.config)
		self.args.list_of_gc_cfgs = [
			get_env('SHERIVFDIR') + '/' + 'gc_configs/sherpa-rivet_base.conf',
			get_env('SHERIVFDIR') + '/' + 'gc_configs/run-sherpa.sh',
			get_env('SHERIVFDIR') + '/' + 'gc_configs/sherpa-rivet_{0}.conf'.format(self.args.config)
		]
		if 'ekp' in socket.gethostname().lower():
			self.args.list_of_gc_cfgs.append(get_env('SHERIVFDIR') + '/' + 'gc_configs/sherpa-rivet_ekp-base.conf')
		if self.args.config == 'ekpcloud':
			self.args.output_dir = self.args.output_dir.replace("/a/", "/ekpcloud_local/")


	def create_output_dir(self):
		"""
			ensure that the output path exists and delete old outputs optionally)
			to save your outputs simply rename them without timestamp
		"""
		print "Output directory:", self.args.output_dir
		os.makedirs(self.args.output_dir + "/work." + self.args.configfile.replace(".conf", ""))
		os.makedirs(self.args.output_dir + "/output")


	def copy_gc_configs(self):
		if self.args.rivet_only:
			output = (' '.join(self.fastnlo_outputs) if self.args.warmup else "Rivet.yoda")
		else:
			output = (' '.join(self.fastnlo_outputs) if self.args.warmup else "Rivet.yoda " + ' '.join(self.fastnlo_outputs))
		if self.args.warmup:
			output += " " + self.analysis + ".str.evtcount"

		for gcfile in self.args.list_of_gc_cfgs:
			copyfile(gcfile, self.args.output_dir+'/'+os.path.basename(gcfile),{
				'@NEVENTS@': self.args.n_events,
				'@NJOBS@': self.args.n_jobs,
				'@OUTDIR@': self.args.output_dir+'/output',
				'@WARMUP@': ("rm *.txt"if self.args.warmup else ""),
				'@OUTPUT@': output,
				'@CONFIG@': self.args.sherpa,
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

		if self.args.rivet_only:
			return outputs

		try:
			#merge fastNLO files
			for quantity in [item.replace(".tab", "") for item in self.fastnlo_outputs]:
				commands = ['fnlo-tk-merge'] + glob.glob(self.args.output_dir+'/output/'+'{0}*.tab'.format(quantity)) + [self.args.output_dir+'/{0}.tab'.format(quantity)]
				print_and_call(commands)
				outputs.append(self.args.output_dir+'/{0}.tab'.format(quantity))
		except OSError as e:
			print "Could not merge fastNLO outputs ({0}): {1}".format(e.errno, e.strerror)

		return outputs


	def merge_warmup_files(self):
		for scenario in [item.replace(".txt", "") for item in self.fastnlo_outputs]:
			commands = [
				"/usr/users/dhaitz/home/qcd/fastnlo_toolkit_fredpatches/fastNLO/trunk/tools/fnlo-add-warmup.pl",
				"-w",
				self.args.output_dir+"/output/",
				scenario
			]
			print_and_call(commands)

def run_gc(config, output_dir):
	commands = ['go.py', config]
	try:
		print_and_call(commands)
	except KeyboardInterrupt:
		print output_dir
		exit(1)
	except:
		print "grid-control run failed"
		exit(1)


def print_and_call(commands):
	print " ".join(commands)
	subprocess.call(commands)


def copyfile(source, target, replace={}):
	# copy file with replace dict
	try:
		with open(source) as f:
			text = f.read()
	except IOError:
		print "Couldnt open file", source
		sys.exit(1)
	for a, b in replace.items():
		text = text.replace(a, b)
	with open(target, 'wb') as f:
		f.write(text)
	return text


def get_env(variable):
	try:
		return os.environ[variable]
	except:
		print variable, "is not in shell variables:", os.environ.keys()
		print "Please source scripts/ini.sh!"
		sys.exit(1)

def format_time(seconds):
	if seconds < 180.:
		return "{0:.0f} seconds".format(seconds)
	elif (seconds/60.) < 120.:
		return "{0:.0f} minutes".format(seconds/60.)
	else:
		return "{0:.0f} hours {1:.0f} minutes".format(int(seconds/3600.), (seconds/60. % 60))

if __name__ == "__main__":
	start_time = time.time()
	sherivf = Sherivf()
	sherivf.run()
	if hasattr(sherivf, "gctime"):
		print "---     Sherivf took {} ---".format(format_time(time.time() - start_time))
		print "--- GridControl took {} ---".format(format_time(sherivf.gctime))
