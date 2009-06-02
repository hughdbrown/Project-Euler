#import psyco
#psyco.full()

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

#def inverse(x, y) :
#	return pow(x % y, y - 2, y)

def inverse(x, y) :
	m = y + 1
	while m % x :
		m += y
	return m // x

def compose(x, y) :
	base = 10 ** len(str(x))
	inv = inverse(base, y)
	assert (0 <= inv < y)
	a = ((y - x) * inv) % y
	assert (0 <= a < y)
	result = x + (a * base)
	assert (result % y == 0)
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
	print(total)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler_134(1000*1000)
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))

