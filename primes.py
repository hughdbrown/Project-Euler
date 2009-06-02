import math

smallPrimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
#setSmallPrimes = set(smallPrimes)

#prime_cache = None
#
#def primes(n) :
#	global prime_cache
#	if n <= 2 : return [2]
#	elif prime_cache != None and (prime_cache[-1] > n) :
#		for i in range(n) :
#			if prime_cache[i] > n :
#				return prime_cache[0 : i]
#	else:
#		x = int(math.sqrt(n)) + 1
#		p = primes(x)
#		cand = set(xrange(x, n))
#		for pp in p :
#			#c = set(range(pp, n + 1, pp))
#			#cand -=  c
#			for ppp in range(pp, n + 1, pp) :
#				cand.discard(ppp)
#		prime_cache = p + sorted(cand)
#		return prime_cache
def primes(n):
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
	return [2]+[x for x in s if x]


def isPrime(n) :
	#if n in smallPrimes :
	if any(n % y == 0 for y in smallPrimes):
		return False
	elif n < smallPrimes[-1]*smallPrimes[-1] :
		return True
	else :
		x = int(n ** 0.5) + 1
		return not any(n % y == 0 for y in primes(x))

def primeFactors(n) :
	result = []
	for y in smallPrimes :
		if y > n : break
		while n % y == 0 :
			result.append(y)
			n /= y
	else :
		x = int(n ** 0.5) + 1
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

def countset2(s) :
	import collections
	d = collections.defaultdict(list)
	for i,a in enumerate(s) :
		d[a].append(i)
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

def relativePrimes(n) :
	s = range(n)
	for p in set(primeFactors(n)) :
		for i in xrange(p, n, p) :
			s[i] = 0
	return [x for x in s if x]

def testRelativePrimes() :
	for i in range(2,15) :
		rp = relativePrimes(i)
		print i, rp

def testFactors() :
	for i in range(4, 100) :
		f = factors(i)
		print i, f

def testPrimeFactors() :
	for i in range(2, 200) :
		pf = primeFactors(i)
		print i, pf

def primeTable(n) :
	max_range = n + 1
	table = range(max_range)
	table[0] = table[1] = 0
	for pp in primes(n) :
		table[pp] = 1
		for j in xrange(pp+pp, max_range, pp) :
			if table[j] == j :
				table[j] = pp
	return table

def primeTable2(n) :
	max_range = n + 1
	table = range(max_range)
	table[0] =  table[1] = 0
	for pp in xrange(2,max_range) :
		if table[pp] == pp :
			table[pp] = 1
			#if pp*pp < max_range :
			for j in xrange(pp*pp, max_range, pp) :
				if table[j] == j :
					table[j] = pp
	return table

def primeTableIter(pt, n) :
	while pt[n] not in (0,1):
		i = pt[n]
		yield i
		n /= i
	yield n
	return

def primeFactors(n) :
	pt = primeTable2(n)
	s = [x for x in primeTableIter(pt, n)]
	return s

if __name__ == "__main__" :
	#testRelativePrimes()
	#testFactors()
	#testPrimeFactors()
	#for i, x in enumerate(primeTable(29)) :
	#	print i, x
	for x in [20,21,100,201,1001] :
		print x, primeFactors(x)
