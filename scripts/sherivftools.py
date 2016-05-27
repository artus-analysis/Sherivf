# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import ROOT


def create_result_linkdir(outputdir, linkname):
	"""Create a link to a directory"""
	print "Output dir", outputdir
	linkdir = get_env('SHERIVFDIR')+'/results/'
	if not os.path.exists(linkdir):
		os.makedirs(linkdir)
	linkdir += linkname
	subprocess.call(['rm', '-f', linkdir])
	print "Create link to", linkdir
	subprocess.call(['ln', '-sf', outputdir, linkdir])


def run_gc(config, output_dir):
	"""Run grid control."""
	commands = ['go.py', config]
	try:
		return print_and_call(commands)
	except KeyboardInterrupt:
		print output_dir
		exit(1)
	except:
		print "grid-control run failed"
		exit(1)


def print_and_call(commands, **kwargs):
	print " ".join(commands)
	try:
		print subprocess.call(commands, **kwargs)
	except OSError as e:
		print e
		print "Command '{0}' could not be executed successfully! EXIT".format(" ".join(commands))
		sys.exit(1)


def copyfile(source, target, replace={}):
	"""copy file, use the replace-dictionary to replace values """
	try:
		with open(source) as f:
			text = f.read()
	except IOError:
		print "Couldnt open file", source
		sys.exit(1)
	for a, b in replace.items():
		text = text.replace(str(a), str(b))
	with open(target, 'wb') as f:
		f.write(text)
	return text


def get_env(variable):
	""" Read environmenr variable from shell."""
	try:
		return os.environ[variable]
	except:
		print variable, "is not in shell variables:", os.environ.keys()
		print "Please source scripts/ini_sherivf.sh!"
		sys.exit(1)


def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via raw_input() and return their answer.

	#http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is True for "yes" or False for "no".
	"""
	valid = {"yes": True, "y": True, "ye": True,
			 "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
							 "(or 'y' or 'n').\n")


def format_time(seconds):
	if seconds < 180.:
		return "{0:.0f} seconds".format(seconds)
	elif (seconds/60.) < 120.:
		return "{0:.0f} minutes".format(seconds/60.)
	else:
		return "{0:.0f} hours {1:.0f} minutes".format(int(seconds/3600.), (seconds/60. % 60))

def tgraph_get_point(tgraph, i):
	tmpX, tmpY = ROOT.Double(0), ROOT.Double(0)
	tgraph.GetPoint(i, tmpX, tmpY)
	return float(tmpX), float(tmpY)
