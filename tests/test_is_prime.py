from prng.util.util import is_prime
import pytest

def test_is_prime_primes():
	try:
		# file with primes < 2,000
		with open("prime_nums_2k.txt") as f:
			primes = [int(line) for line in f.readlines()]
	except FileNotFoundError:
		primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

	assert all(is_prime(n) for n in primes)

def test_is_prime_not_prime():
	not_primes=[1,4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30]
	assert not any(is_prime(n) for n in not_primes)

def test_is_prime_negative_number():
    not_primes = [-2,-3,-5,-7,-11,-13,-17,-19,-23,-29,-31,-37,-41,-43,-47,-53,-59,-61,-67,-71]
    assert not any(is_prime(n) for n in not_primes)

def test_is_prime_zero():
    assert not is_prime(0)
