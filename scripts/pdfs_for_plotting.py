#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdf_2_root

for q in [1, 1.9, 3, 10, 14, 91.2, 200]:
	pdf_2_root.main(
		'NNPDF23_nlo_as_0118_HighStat_chi2_nRep100',
		[0, 1, 2, -1, -2],
		"pdfs_for_plotting_{}.root".format(str(q).replace(".", "_")),
		100,
		q,
		"pdf_sets"
	)