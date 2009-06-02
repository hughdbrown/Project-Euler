#!/usr/bin/env python

import psyco
psyco.full()

import collections

def prime_table(n) :
	n += 1
	x = list(range(n))
	for i in xrange(2,n) :
		if x[i] == i :
			x[i] = 1
			if i*i < n :
				for j in xrange(i*i, n, i) :
					x[j] = i
	return x

def primes(n) :
	x = prime_table(n)
	return [ i for i in xrange(2,n) if x[i] == 1 ]

def factors(table, n) :
	f = []
	while table[n] != 1 :
		x = table[n]
		f.append(x)
		n /= x
	f.append(n)
	return f

def comb(n,r) :
	m1 = max(r, n-r)
	m2 = min(r, n-r)
	num = list(range(m1+1, n+1))
	denom = list(range(1, m2+1))

	#print "Generating prime table"
	p = prime_table(n)

	#print "Generating denominator factors"
	denom_factors = []
	for j in xrange(len(denom)) :
		if denom[j] > 1 :
			denom_factors += factors(p, denom[j])

	dd = collections.defaultdict(int)
	for d in denom_factors :
		dd[d] += 1

	#print "Generating numerator factors"
	num_factors = []
	for j in xrange(len(num)) :
		num_factors += factors(p, num[j])

	nd = collections.defaultdict(int)
	for d in num_factors :
		nd[d] += 1

	#print "Removing denominator factors from numerator factors"
	remove_list = []
	for k in dd.iterkeys() :
		nd[k] -= dd[k]
		if not nd[k]:
			remove_list.append(k)
	for k in remove_list :
		del nd[k]

	return nd

def product(s) :
	result = 1
	for elem in s :
		result *= elem
	return result

def euler203() :
	s = set()
	for i in range(51) :
		for j in range(i+1) :
			a = comb(i, j)
			print product(k**v for k,v in a.iteritems()),
			for v in a.itervalues() :
				if v >= 2 :
					break
			else :
				x = product(a.iterkeys())
				s.add(x)
		print
	print sum(s)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler203()
	e = time.clock()
	print "Elapsed: ", (e - s)
