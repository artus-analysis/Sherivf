# -*- coding: utf-8 -*-

import os
import subprocess
import sys

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
