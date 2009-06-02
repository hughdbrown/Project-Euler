import psyco
psyco.full()

import primes
import phi
import sys

"""
21 21 12 1.75 [3, 7]
291 291 192 1.515625 [3, 97]
2817 2817 1872 1.50480769231 [3, 3, 313]
2991 2991 1992 1.5015060241 [3, 997]
4435 4435 3544 1.25141083521 [5, 887]
20617 20617 20176 1.02185765266 [53, 389]
45421 45421 44512 1.02042145938 [53, 857]
69271 69271 67912 1.02001119095 [53, 1307]
"""

import primes
limit = 10*1000*1000
pt = primes.primeTable(limit)

def find_factors(n) :
	factors = set()
	while pt[n] != 1 :
		factors.add(pt[n])
		n /= pt[n]
	factors.add(n)
	return factors

def totient(n) :
	num, denom = 1, 1
	for factor in find_factors(n) :
		num *= (factor - 1)
		denom *= factor
	return (n * num) / denom

min_so_far = 20000
k = 0
#p = primes.primes(limit)
for i in xrange(2, limit) :
	print >> sys.stderr, i, k, min_so_far, "\r",
	x = totient(i) ## phi.phi_p(i, p)
	a = sorted(c for c in str(i))
	b = sorted(c for c in str(x))
	if a == b :
		score = float(i)/float(x)
		if score < min_so_far :
			k, min_so_far = i, score
			print
			print k, min_so_far
print
print k, min_so_far 