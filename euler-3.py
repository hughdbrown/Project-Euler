#!/usr/bin/env python
import math
import psyco
psyco.full()

def prime_factors(x) :
	primes = [2,3,5,7,11,13,17,19]
	lowest = 2
	factors = []
	for z in primes :
		while x % z == 0 :
			factors.append(z)
			x /= z
			if x < lowest and x != 1: factors.append(x)
	return factors

def test2() :
	from time import clock
	s = clock()
	n = prime_factors(317584931803)
	e = clock()
	print n
	print "found %d in %f" % (n, (e - s))

test2()

#for i in range(2, 21) :
#	s = prime_factors(i)
#	print i, s
