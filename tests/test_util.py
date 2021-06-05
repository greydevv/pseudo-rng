from prng.util import is_prime, relatively_prime, prime_factors



def test_is_prime():
	try:
		# file with primes < 2,000
		with open("prime_nums_2k.txt") as f:
			primes = [int(line) for line in f.readlines()]
	except FileNotFoundError:
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

	assert all(is_prime(n) for n in primes)



def test_is_prime_not_prime():
	not_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
	assert not any(is_prime(n) for n in not_primes)



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

print(prime_factors(280))