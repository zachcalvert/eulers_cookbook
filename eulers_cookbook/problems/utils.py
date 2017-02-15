"""
Utility functions that may be used across different solutions.
"""

import math

def is_prime(x):
	"""
	Determines whether an integer x is prime or not.
	"""
	if x % 2 == 0 and x > 2:
		return False
	return all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))