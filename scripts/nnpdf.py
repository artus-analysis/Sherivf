#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir, copy needed files, start herafitter NNPDF reweighting
"""


import time, sys, os, glob, argparse, subprocess
import sherivf
import copy_herafitter_steering



class NNPDF(object):
	def __init__(self):
		self.default_mode = 'nnpdf'
		self.get_arguments()
		self.hfiles = ['ewparam.txt', 'minuit.in.txt']

	def run(self):
		pdfset = 'NNPDF23_nlo_as_0118'
		newname = 'Zee'
		chi2_data = 'chi2'
		newset = '_'.join([pdfset, newname, chi2_data])
		
		# create dir and copy necessary files
		os.makedirs(self.args.output_dir + "/output/"+newset)
		os.makedirs(self.args.output_dir + "/input_steering")
		copy_herafitter_steering.copy_herafile(self.args.mode, False, self.args.output_dir)
		for hfile in self.hfiles:
			sherivf.copyfile('hera-gc/'+hfile, self.args.output_dir+'/'+os.path.basename(hfile),{'@MCHARM@': '1.4','@MBOTTOM@': '4.75',})

		# 
		os.chdir(self.args.output_dir)
		os.makedirs(newset)

		sherivf.print_and_call(["FitPDF"])

		#os.chdir('output/')
		#cd output/${PDFSET}_${NEWNAME}_${CHI2_DATA}
		#echo "ErrorType: replicas" >> ${PDFSET}_${NEWNAME}_${CHI2_DATA}_nRep100/${PDFSET}_${NEWNAME}_${CHI2_DATA}_nRep100.info
		#eval_pdfs ${PDFSET}_${NEWNAME}_${CHI2_DATA}_nRep100
		#rename ${PDFSET}_${NEWNAME}_${CHI2_DATA}_nRep100 herapdf *.root
		print self.args.output_dir

		# link
		linkdir = sherivf.get_env('SHERIVFDIR')+'/latest_herafitter_'+self.args.mode
		subprocess.call(['rm', '-f', linkdir])
		print "Create link to", linkdir
		subprocess.call(['ln', '-sf', self.args.output_dir+"/output/"+newset, linkdir])

	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the main analysis program.", epilog="Have fun.")

		parser.add_argument('-m', '--mode', type=str, default=self.default_mode,
			help="mode (hera, heraZ)")
		parser.add_argument('-o', '--output-dir', type=str, default=None, help="")
		
		self.args = parser.parse_args()
		if self.args.output_dir is None:
			self.args.output_dir = (self.args.mode + "_" + time.strftime("%Y-%m-%d_%H-%M"))
		self.args.output_dir = 'nnpdf/' + self.args.output_dir


if __name__ == "__main__":
	start_time = time.time()
	nnpdf = NNPDF()
	nnpdf.run()
	print "---        NNPDF took {}  ---".format(sherivf.format_time(time.time() - start_time))

