# -*- coding: utf-8 -*-

import math


def get_pdf_uncertainty_for_bin(central_value, other_values):
	"""according to sieber thesis Eq. 5.15"""
	upper_error = 0
	lower_error = 0
	for value in other_values:
		upper_error += (max(value-central_value,0))**2
		lower_error += (min(value-central_value,0))**2
	return math.sqrt(lower_error), math.sqrt(upper_error)
