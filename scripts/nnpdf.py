#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	create a workdir, copy needed files, start herafitter NNPDF reweighting
"""


import time, sys, os, glob, argparse, subprocess

import sherivftools
import copy_herafitter_steering
import pdf_2_root


class NNPDF(object):
	def __init__(self):
		self.default_value = 'abszy'
		self.get_arguments()
		self.hfiles = ['ewparam.txt', 'minuit.in.txt']

	def run(self):
		pdfset = 'NNPDF30_nlo_as_0118_nolhc_1000'
		newname = 'Zee'
		chi2_data = 'chi2'
		n_replicas = 1000
		newset = '_'.join([pdfset, newname, chi2_data])
		steering_dict = {'@PDFSET@': pdfset,'@NREPLICAS@': str(n_replicas), '@RUNNINGMODE@': 'LHAPDF Analysis'}
		
		# create dir and copy necessary files
		os.makedirs(self.args.output_dir + "/input_steering")
		copy_herafitter_steering.copy_herafile('nnpdf', self.args.value, False, self.args.output_dir, keys=steering_dict)
		for hfile in self.hfiles:
			sherivftools.copyfile('hera-gc/'+hfile, self.args.output_dir+'/'+os.path.basename(hfile),
			{
				'@MCHARM@': '1.4',
				'@MBOTTOM@': '4.75',
				'@BG@': 0,
				'@BG_S@': 0,
				'@CG@': 0,
				'@CG_S@': 0,
				'@DG_S@': 0,
				'@EG_S@': 0,
				'@APRIG@': 0,
				'@APRIG_S@': 0,
				'@BPRIG@': 0,
				'@BPRIG_S@': 0,
				'@CPRIG@': 0,
				'@CPRIG_S@': 0,
				'@BUV@': 0,
				'@BUV_S@': 0,
				'@CUV@': 0,
				'@CUV_S@': 0,
				'@DUV@': 0,
				'@DUV_S@': 0,
				'@EUV@': 0,
				'@EUV_S@': 0,
				'@BDV@': 0,
				'@BDV_S@': 0,
				'@CDV@': 0,
				'@CDV_S@': 0,
				'@DDV_S@': 0,
				'@EDV_S@': 0,
				'@BUBAR@': 0,
				'@BUBAR_S@': 0,
				'@CUBAR@': 0,
				'@CUBAR_S@': 0,
				'@DUBAR@': 0,
				'@DUBAR_S@': 0,
				'@EUBAR_S@': 0,
				'@ADBAR@': 0,
				'@ADBAR_S@': 0,
				'@BDBAR@': 0,
				'@BDBAR_S@': 0,
				'@CDBAR@': 0,
				'@CDBAR_S@': 0,
				'@DDBAR_S@': 0,
				'@EDBAR_S@': 0,
			})

		# Run fit
		os.chdir(self.args.output_dir)
		os.makedirs(newset)
		stdout_file = open("stdout.txt", "w")
		fit_success = sherivftools.print_and_call(["xfitter"], stdout=stdout_file)
		
		#second step: produce LHA file
		#
		stdout_process_file = open("stdout_process.txt", "w")
		fit_process_success = sherivftools.print_and_call(["xfitter-process", "reweight", str(n_replicas), "hera/pdf_BAYweights.dat", "/storage/a/dhaitz/PDFsets/"+pdfset, newset], stdout=stdout_process_file)


		# evaluate PDF
		#os.chdir('output/' + newset)
		#newset_rep = newset + '_nRep'+str(n_replicas)
		#with open(newset_rep + '/' + newset_rep + '.info', 'a') as pdf_info_file:
		#	pdf_info_file.write('ErrorType: replicas')
		print "Name of new PDF set:", newset
		for q, q2 in zip([91.2, 1.9, 10.0], [False, True, True]):
			pdf_2_root.main(
				newset,
				pdf_2_root.partondict.keys(),
				pdf_2_root.get_default_filename(newset, q, q2)+'.root',
				100,
				q,
				q2,
				n_replicas+1,
				os.getcwd()
			)

		# create link
		print "Output dir", self.args.output_dir
		linkdir = sherivftools.get_env('SHERIVFDIR')+'/results'
		if not os.path.exists(linkdir):
			os.makedirs(linkdir)
		linkdir += '/nnpdf_'+self.args.value
		subprocess.call(['rm', '-f', linkdir])
		print "Create link to", linkdir
		subprocess.call(['ln', '-sf', self.args.output_dir, linkdir])

	def get_arguments(self):
		parser = argparse.ArgumentParser(
			description="%(prog)s is the main analysis program.", epilog="Have fun.")
		parser.add_argument('-v', '--value', type=str, default=self.default_value,
			help="value (abszy, zpt")
		parser.add_argument('-o', '--output-dir', type=str, default=None, help="")
		
		self.args = parser.parse_args()
		if self.args.output_dir is None:
			self.args.output_dir = (self.args.value + "_" + time.strftime("%Y-%m-%d_%H-%M"))
		self.args.output_dir = sherivftools.get_env('SHERIVF_STORAGE_PATH') + 'nnpdf/' + self.args.output_dir


if __name__ == "__main__":
	start_time = time.time()
	nnpdf = NNPDF()
	nnpdf.run()
	print "---        NNPDF took {}  ---".format(sherivftools.format_time(time.time() - start_time))

