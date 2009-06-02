import primes

prime_cache = None
def isPrime(n) :
	global prime_cache
	if not prime_cache :
		prime_cache = dict.fromkeys( (p,1) for p in primes.primes(1000*1000*10) )
	return n in prime_cache
