import math

prime_cache = None
def primes(n): 
	if prime_cache : return prime_cache
	if n==2: return [2]
	elif n<2: return []
	s = range(3,n+1,2)
	mroot = int(n ** 0.5)
	half = ((n+1) >> 1) - 1
	m = 1
	for i in range(0, int(mroot >> 1)) :
		m += 2
		if s[i]:
			for j in range((m*m-3) >> 1, half, m) :
				s[j]=0
	prime_cache = [2]+[x for x in s if x]
	return prime_cache


def isPrime(n) :
	x = int(math.sqrt(n)) + 1
	return all(n % y != 0 for y in primes(x) if y < n)

def primeFactors(n) :
	result = []
	x = int(math.sqrt(n)) + 1
	for y in primes(x) :
		if y > n : break
		while n % y == 0 :
			result.append(y)
			n /= y
	if not len(result) : result.append(n)
	elif n != 1 : result.append(n)
	return result

def countset(s) :
	import collections
	d = collections.defaultdict(lambda : 0)
	for a in s :
		d[a] += 1
	#print s, max(d.itervalues())
	return d

def factors(n) :
	import powerset, factorial
	f = primeFactors(n)
	result = [1, n] + f
	if len(f) :
		for s in powerset.powerset(f) :
			if len(s) :
				p = factorial.product(s)
				result.append(n/p)
	return sorted(set(result))

