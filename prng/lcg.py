from util._helpers import is_prime
from typing import Generator

def lcg(m:int, a:int, c:int, n:int) -> Generator[int, None, None]:
	"""
	Linear Congruential Generator (LCG)

	Parameters:
		m (int): modulus
		a (int): multiplier
		c (int): increment
		n (int): starting value, usually referred to as "seed"

	Yields:
		(int): pseudorandom number
	"""
	while True:
		n = (a*n+c) % m
		yield n

