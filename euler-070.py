import psyco
psyco.full()


import prime_cache
import primes

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

d = {}
min_so_far = 20000
k = 0
for i in xrange(1000*100*95, 10, -1) :
##for i in xrange(1000*1000*10 - 1, 10, -1) :
##for i in xrange(10, 1000*1000*10) :
	print i, k, min_so_far, "\r",
	if not prime_cache.isPrime(i) :
		p = primes.relativePrimes(i)
		phi = len(p)
		a = sorted(c for c in str(i))
		b = sorted(c for c in str(phi))
		if a == b :
			score = float(i)/float(phi)
			d[i] = phi
			if score < min_so_far :
				k, min_so_far = i, score
				print i, k, phi, min_so_far, primes.primeFactors(i)

print
min_score = min(float(k) / float(v) for k,v in d.iteritems())
for k,v in d.iteritems() :
	if v == min_score :
		print k, v