from prng.util.util import relatively_prime
import pytest

def test_relatively_prime():
	rel_primes = [
		[5,7],
		[263, 71],
		[4, 17],
		[9, 4],
		[2789, 8],
		[6, 8941],
		[8, 9],
		[1, 234],
		[5, 27],
		[18, 143],
	]

	assert all(relatively_prime(a,b) for a,b in rel_primes)

def test_relatively_prime_not_relatively_prime():
	not_rel_primes = [
		[37, 185],
		[12, 42],
		[144, 192],
		[24, 138],
		[0, 55],
		[136, 196],
		[20, 124],
		[8, 48],
		[154, 38],
		[48, 58]
	]

	assert not any(relatively_prime(a,b) for a,b in not_rel_primes)
