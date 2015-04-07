#!/usr/bin/env python

"""
Script to calculate the correlation coefficient between PDFs and xs

originally by gsieber
https://gist.github.com/claria/da98570014514f0ada89
"""

import os
import sys
import argparse
import numpy as np

import lhapdf
import fastnlo
from fastnlo import fastNLOLHAPDF
lhapdf.setVerbosity(0)


partons = {0: 'gluon',
           -1: 'd antiquark',
           -2: 'u antiquark',
           #            -3 : 'sbar',
           #            -4 : 'cbar',
           #            -5 : 'bbar',
           #            -6 : 'tbar',
           1: 'd quark',
           2: 'u quark',
           #            3 : 'strange',
           #            4 : 'charm',
           #            5 : 'bottom',
           #            6 : 'top',
           7: 'd valence quark',
           8: 'u valence quark',
           9: 'sea quarks',
}

def main():
	#Parse Args
	parser = argparse.ArgumentParser(description='Calculates the correlation coefficient between PDFs and xs')
	parser.add_argument('-t', '--table', help='fastNLO table')
	parser.add_argument('-p', '--pdfset', help='LHAPDF PDF Filename', default='NNPDF21_100.LHgrid')
	kwargs = vars(parser.parse_args())
	get_corr(**kwargs)


def get_corr(table, pdfset, **kwargs):
	storage = get_fnlo(table, pdfset)
	kwargs['table_basename'] = os.path.basename(table)
	x = np.logspace(-4, -0.0001, 250)

	for parton in partons:
		print partons[parton]
		#Split after y-bins
		rap_bins = list(set(storage['y_low']))
		for rapbin in rap_bins:
			storage_bin = storage.copy()
			#Apply cuts
			filter_arr = storage_bin['y_low'].copy()
			cut_arr_1dim = (filter_arr == rapbin)
			for item in storage:
				storage_bin[item] = storage[item][cut_arr_1dim]
			nobsbins = len(storage_bin['xsnlo'])
			obsbins = range(0, nobsbins)
			corr = np.zeros((len(obsbins), len(x)))
			for nobbin, obbin in enumerate(obsbins):
				pdf = get_pdf(pdfset, parton, storage_bin['scale'][nobbin], x)
				for xi in range(0, len(x)):
					corr[nobbin][xi] = np.corrcoef([pdf.transpose()[xi], storage_bin['xsnlo'][obbin]])[0][1]
			print "\nkwargs", kwargs
			y = np.array(list(storage_bin['pt_low']) + [storage_bin['pt_high'][len(storage_bin['pt_high']) -1]])
			#if table == 'fnl2932bm3_strippedless.tab':
			#	y/=2.
			#print y
			print "\nx\n",x
			print "\ny\n", y
			print "\ncorr\n", corr
			print "\nstorage_bin\n", storage_bin
			print "\nparton\n", parton
			print "\npdfset\n", pdfset
			return


def get_fnlo(table, pdfset):
	xs_nlo = {}

	fnlo = fastNLOLHAPDF(table)
	fnlo.SetLHAPDFFilename(pdfset)

	fnlo.SetLHAPDFMember(0)
	fnlo.CalcCrossSection()

	npdfmember = fnlo.GetNPDFMembers()
	xs_nlo['xsnlo'] = np.zeros((npdfmember - 1, fnlo.GetNObsBin(),))
	xs_nlo['scale'] = np.array(fnlo.GetQScales(1))
	# xs_nlo['bi_lo'] = np.array([fnlo.GetObsBin(i)[1] for i in range(0,fnlo.GetNObsBin())]).transpose()[0]
	# xs_nlo['bi_hi'] = np.array([fnlo.GetObsBin(i)[1] for i in range(0,fnlo.GetNObsBin())]).transpose()[1]

	#########################

	#xs_nlo['pt_low'], xs_nlo['y_low'] = np.array(fnlo.GetLowBinEdge()).transpose()
	#xs_nlo['pt_high'], xs_nlo['y_high'] = np.array(fnlo.GetUpBinEdge()).transpose()

	xs_nlo['y_low'] = np.array(fnlo.GetLoBin(0))
	xs_nlo['y_high'] = np.array(fnlo.GetUpBin(0))

	xs_nlo['pt_low'] = xs_nlo['y_low']
	xs_nlo['pt_high'] = xs_nlo['y_high']

	#######################

	for i in range(1, npdfmember):
		fnlo.SetLHAPDFMember(i)
		fnlo.CalcCrossSection()
		xs_nlo['xsnlo'][i - 1] = fnlo.GetCrossSection()
	xs_nlo['xsnlo'] = xs_nlo['xsnlo'].transpose()

	return xs_nlo


def get_pdf(pdfset, parton, q, xs):
	"""get the PDF (xfx) for a certain set, parton, x and Q"""

	lhapdf.initPDFSetByName(pdfset)
	npdfs = lhapdf.numberPDF()
	pdf = np.zeros((npdfs, len(xs)))

	for member in range(1, npdfs + 1):
		lhapdf.initPDF(member)
		for (i, xi) in enumerate(xs):
			if parton < 7:
				pdf[member - 1][i] = lhapdf.xfx(xi, q, parton)
			elif parton == 7:
				#DVAL 1-(-1)
				pdf[member - 1][i] = lhapdf.xfx(xi, q, 1) - \
								 lhapdf.xfx(xi, q, -1)
			elif parton == 8:
				#UVAL 2-(-2)
				pdf[member - 1][i] = lhapdf.xfx(xi, q, 2) - \
								 lhapdf.xfx(xi, q, -2)
			elif parton == 9:
				#Light sea: xS=2(xubar + xdbar + xsbar)
				pdf[member - 1][i] = 2*(lhapdf.xfx(xi, q, -1) + \
								 lhapdf.xfx(xi, q, -2) + \
								 lhapdf.xfx(xi, q, -3))
			else:
				raise ValueError('Parton id not in range 0...9')
	return pdf


if __name__ == '__main__':
	sys.exit(main())
