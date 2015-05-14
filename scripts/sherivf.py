#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is the GC wrapper"""

import sys, os, glob, shutil, time, subprocess, argparse, socket


def sherivf():
	"""Main function.
		1. Get configs.
		2. Check if a new workdir has to be created.
		3. Delete, resume or start new (default) run
	"""

	args = get_arguments()

	# config dir: new or existing one?
	if args.delete or args.resume:
		paths = glob.glob(args.output_dir + "/*")
		paths.sort()
		try:
			args.output_dir = paths[-1]
		except IndexError:
			sys.exit("No output directories exist!")
	else:
		args.output_dir += time.strftime("%Y-%m-%d_%H-%M")

	if args.delete:
		delete_latest_output_dir(args.output_dir, args.configfile)
	else:
		if not args.resume:
			create_output_dir(args.output_dir, args.configfile)
			copy_gc_configs(args.output_dir, args.list_of_gc_cfgs)
		run_gc(args.output_dir + "/" + args.configfile)


def delete_latest_output_dir(output_dir, configfile):
	try:
		subprocess.call(['go.py', output_dir + "/" + configfile, "-d all"])
	except:
		print "could not delete currently running jobs"
		exit(1)
	try:
		shutil.rmtree(output_dir)
		print "Directory {0} deleted.".format(output_dir)
	except:
		print "Could not delete output directory {0}".format(output_dir)


def get_arguments():
	parser = argparse.ArgumentParser(
		description="%(prog)s is the main analysis program.", epilog="Have fun.")

	if 'naf' in socket.gethostname().lower():
		default_config = 'naf'
		default_storage_path = '/afs/desy.de/user/d/dhaitz/nfs/sherivf'
	elif 'ekp' in socket.gethostname().lower():
		default_config = 'ekpcluster'
		default_storage_path = '/storage/a/dhaitz/sherivf/'

	parser.add_argument('-c', '--config', type=str, default=default_config,
		help="config to run. will be set automatically for naf")
	parser.add_argument('-d', '--delete', action='store_true',
		help="delete the latest output and jobs still running")
	parser.add_argument('-R', '--resume', action='store_true',
		help="resume the grid-control run.")

	parser.add_argument('--output-dir', type=str, help="output directory",
		default=default_storage_path)

	args = parser.parse_args()

	# define configs to use
	args.configfile = 'sherpa-rivet_{0}.conf'.format(args.config)
	args.list_of_gc_cfgs = [
		get_env('SHERIVFDIR') + '/' + 'sherpa-gc/sherpa-rivet_base.conf',
		get_env('SHERIVFDIR') + '/' + 'sherpa-gc/run-sherpa.sh',
		get_env('SHERIVFDIR') + '/' + 'sherpa-gc/sherpa-rivet_{0}.conf'.format(args.config)
	]
	if 'ekp' in socket.gethostname().lower():
		args.list_of_gc_cfgs.append(get_env('SHERIVFDIR') + '/' + 'sherpa-gc/sherpa-rivet_ekp-base.conf')

	return args


def create_output_dir(work, configfile):
	"""
		ensure that the output path exists and delete old outputs optionally)
		to save your outputs simply rename them without timestamp
	"""
	print "Output directory:", work
	os.makedirs(work + "/work." + configfile.replace(".conf", ""))


def copy_gc_configs(output_dir, list_of_gc_cfgs):
	for gcfile in list_of_gc_cfgs:
		shutil.copy(gcfile, output_dir)


def run_gc(config):
	commands = ['go.py', config]
	try:
		print " ".join(commands)
		subprocess.call(commands)
	except KeyboardInterrupt:
		exit(0)
	except:
		print "grid-control run failed"
		exit(1)


"""
def copyfile(source, target, replace={}):
	"""
# copy file with replace dict
"""
	with open(source) as f:
		text = f.read()
	for a, b in replace.items():
		text = text.replace(a, b)
	with open(target, 'wb') as f:
		f.write(text)
	return text
"""


def get_env(variable):
	try:
		return os.environ[variable]
	except:
		print variable, "is not in shell variables:", os.environ.keys()
		print "Please source scripts/ini.sh!"
		sys.exit(1)


if __name__ == "__main__":
	sherivf()
