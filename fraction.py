import psyco
psyco.full()

import primes
import prime_cache

def product(s) :
	result = 1
	for ss in s :
		result *= ss
	return result

def reducedFraction(t) :
	num, denom = t[0], t[1]
	#if prime_cache.isPrime(num) or prime_cache.isPrime(denom) :
	if primes.isPrime(num) or primes.isPrime(denom) :
		return t
	else :
		pn = primes.primeFactors(num)
		pd = primes.primeFactors(denom)
		i, j = 0, 0
		remove = []
		while i < len(pn) and j < len(pd) :
			if pn[i] < pd[j] : i += 1
			elif pn[i] > pd[j] : j += 1
			else :
				remove.append( (i, j) )
				i += 1
				j += 1
		L = len(remove)
		for j in range(L) :
			t = remove.pop()
			pn.pop(t[0])
			pd.pop(t[1])
		return ( product(pn) , product(pd) )
