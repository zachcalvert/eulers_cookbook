"""
Utility functions that may be used across different solutions.
"""

import math

def is_palindrome(x):
	"""
	Determines if a string of letters (or numbers!) is the same backwards as forwards
	"""
	return str(x) == str(x)[::-1]

def is_prime(x):
	"""
	Determines whether an integer x is prime or not.
	"""
	if x % 2 == 0 and x > 2:
		return False
	return all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))

def rotate_list(l, n):
	"""
	Rotates a list l from left to right by n spots.

	In [1]: l = [1,2,3]

	In [2]: rotate_list(l, 1)
	Out[2]: [2, 3, 1]

	In [3]: rotate_list(l, 2)
	Out[3]: [3, 1, 2]
	"""
	return l[n:] + l[:n]