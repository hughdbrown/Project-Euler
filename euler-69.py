import psyco
psyco.full()


import prime_cache
import primes

d = {}
max_so_far = 0
k = 0
for i in xrange(10, 1000*1000) :
	print i, k, max_so_far, "\r",
	if not prime_cache.isPrime(i) :
		p = primes.relativePrimes(i)
		d[i] = len(p)
		score = float(i) / float(d[i])
		if score > max_so_far : 
			k, max_so_far = i, score
			print i, k, max_so_far

print
max_score = max(float(k) / float(v) for k,v in d.iteritems())
for k,v in d.iteritems() :
	if v == max_score :
		print k, v