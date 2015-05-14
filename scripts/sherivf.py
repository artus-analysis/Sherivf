#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is the GC wrapper"""

import sys, os, glob, shutil, time, subprocess, argparse


def sherivf():
	"""Main function."""

	# define variables
	list_of_gc_cfgs = [
		'sherpa-gc/sherpa-rivet_base.conf',
		'sherpa-gc/run-sherpa.sh'
	]
	if True:  # ekp
		list_of_gc_cfgs += [
			'sherpa-gc/sherpa-rivet_ekp-base.conf',
			'sherpa-gc/sherpa-rivet_ekpcluster.conf',
		]
		configfile = 'sherpa-rivet_ekpcluster.conf'
	else: # NAF, others
		pass
	
	output_dir = "/storage/a/dhaitz/sherivf/" 
	args = get_arguments()

	# delete?
	if args.delete:
		delete_latest_output_dir(output_dir, configfile)
	else:
		output_dir += time.strftime("%Y-%m-%d_%H-%M")

	if not args.resume:
		create_output_dir(output_dir, configfile)
		copy_gc_configs(output_dir, list_of_gc_cfgs)
	run_gc(output_dir + "/" + configfile)


def delete_latest_output_dir(output_dir, configfile):
	paths = glob.glob(output_dir + "/*")
	paths.sort()
	output_dir = paths[-1]

	try:
		subprocess.call(['go.py', output_dir + "/" + configfile, "-d all"])
	except:
		print "could not delete currently running jobs"
		exit(1)
	try:
		shutil.rmtree(output_dir)
		print "Directory {0} deleted.".format(output_dir)
	except:
		print "Could not delete output directory {}".format(output_dir)
	exit(0)

def get_arguments():
	parser = argparse.ArgumentParser(
		description="%(prog)s is the main analysis program.", epilog="Have fun.")

	parser.add_argument('-d', '--delete', action='store_true',
		help="delete the latest output and jobs still running")
	parser.add_argument('-R', '--resume', action='store_true',
		help="resume the grid-control run.")

	return parser.parse_args()


def create_output_dir(work, configfile):
	"""
		ensure that the output path exists and delete old outputs optionally)
		to save your outputs simply rename them without timestamp
	"""
	if work[-1] == '/':
		work = work[:-1]
	if "_20" in work:
		paths = glob.glob(work[:-17]+"_20*")
		paths.sort()
		if paths:
			paths.pop()
	else:
		paths = glob.glob(work + "_20*")
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



def copyfile(source, target, replace={}):
	""" copy file with replace dict"""
	with open(source) as f:
		text = f.read()
	for a, b in replace.items():
		text = text.replace(a, b)
	with open(target, 'wb') as f:
		f.write(text)
	return text


def getEnv(variable):
	try:
		return os.environ[variable]
	except:
		print variable, "is not in shell variables:", os.environ.keys()
		print "Please source scripts/ini.sh!"
		sys.exit(1)


if __name__ == "__main__":
	sherivf()
