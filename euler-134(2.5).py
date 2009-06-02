import psyco
psyco.full()

import sys

def prime_table(n) :
	n += 1
	x = list(range(n))
	for i in range(2,n) :
		if x[i] == i :
			x[i] = 1
			if i*i < n :
				for j in range(i*i, n, i) :
					x[j] = i
	return x

def primes(n) :
	x = prime_table(n)
	return [ i for i in range(2,len(x)) if x[i] == 1 ]

def compose(x, y) :
	base = 10 ** len(str(x))
	base_incr = base % y
	s = (base + x) % y

	i = 0
	while s != 0 :
		q = (y - s) // base_incr
		i += q
		s += q * base_incr
		if s < y :
			i += 1
			s += base_incr
		s -= y
		#assert(0 <= s < y)
	result = x + ((i+1) * base)
	print >> sys.stderr, "***", x, y, result, result//y, base_incr, "\r",

	#assert (i < y)
	#assert (0 == s)
	#assert (0 == result%y)
	#for j in xrange(1, i) :
	#	z = j * base + x
	#	assert(0 != (z % y))

	return result

def prime_pairs(p, limit) :
	for i in range(3,len(p)) :
		p1, p2 = p[i-1], p[i]
		if p1 < limit :
			yield p1, p2
	return

def euler_134(limit) :
	p = primes(limit + 5000)
	total = sum(compose(p1, p2) for p1, p2 in prime_pairs(p, limit))
	print total

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler_134(1000*1000)
	e = time.clock()
	print "Elapsed: ", (e - s)

