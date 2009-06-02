#!/usr/bin/env python
#import psyco
#psyco.full()

def primes(x) :
	a = range(0,x+1)
	a[0], a[1] = 0, 0
	for i in xrange(2, x+1) :
		if a[i] == i :
			a[i] = 1
			if (x+1)/ i > i :
				for j in xrange(i*i, x+1, i) :
					a[j] = i
	#return [x for x, aa in enumerate(a) if aa == 1]
	return a

def prime_factors(a) :
	global p
	if a > len(p) :
		return [ a ]
	else :
		result = []
		while p[a] != 1 :
			result.append(p[a])
			a /= p[a]
		result.append(a)
		return result

def product(s) :
	result = 1
	for ss in s :
		result *= ss
	return result

def reduce(a, b) :
	ap = prime_factors(a)
	bp = prime_factors(b)

	c = []
	for aa in ap :
		if aa in bp :
			bp.remove(aa)
			c.append(aa)
	for cc in c :
		ap.remove(cc)
	return product(ap), product(bp)

def convergent_pair(n) :
	a, b = 1, 1
	while True :
		print a, b
		yield a, b
		a, b = a + n * b, a + b
		a, b = reduce(a, b)
	return

def find_diophantine(n) :
	for a in convergent_pair(n) :
		x, y = a[0], a[1]
		t = n * y * y + 1
		x = long(t ** 0.5)
		if x * x == t :
			return x, y
def test() :
	squares = [ x* x for x in xrange(1,32)]
	s = [ y for y in xrange(1,1000) if y not in squares ]
	max_seen, j = 0, 0

	for x in s :
		d = find_diophantine(x)
		print x, d
		if d[0] > max_seen :
			max_seen = d[0]
			j = x
	print max_seen, j

if __name__ == "__main__" :
	global p
	p = primes(10*1000*1000)
	test()

"""
p = primes(1000)
print reduce(36,16)
"""
