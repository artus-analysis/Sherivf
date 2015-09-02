#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdf_2_root

for q in [1, 1.9, 3, 10, 14, 91.2, 200]:
	pdf_2_root.main(
		'NNPDF30_nlo_as_0118',
		[0, 1, 2, -1, -2, 7, 8, 3, -3],
		"pdfs_for_plotting_{}.root".format(str(q).replace(".", "_")),
		100,
		q,
		"pdf_sets"
	)
