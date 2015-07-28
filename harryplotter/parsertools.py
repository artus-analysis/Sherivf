# -*- coding: utf-8 -*-

#TODO document this


import argparse

def parser_list_tool(args, arguments):
	parser = argparse.ArgumentParser()
	for argument in arguments:
		parser.add_argument('--no-{}'.format(argument), type=int, nargs='?', default=False, const=0)
	return parser.parse_known_args(**({'args': args} if args is not None else {}))

def get_list_slice(lists, arg):
	if arg is False:
		return lists
	else:
		return [[l[arg]] for l in lists]
