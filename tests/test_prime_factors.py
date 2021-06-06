from prng.util.util import prime_factors
import pytest

def test_prime_factors():
	prime_factor_sets = [
		[8, [2]],
		[280, [2,5,7]],
		[2349281, [11,17,739]],
		[3934, [2,7,281]],
		[57309, [3,7,2729]],
		[3453924534, [2,3,29,19850141]],
		[17, [17]],
		[174985, [5,79,443]],
		[974621, [59,16519]],
		[991, [991]]
	]

	assert all(sorted(prime_factors(a)) == pfs for a,pfs in prime_factor_sets)
