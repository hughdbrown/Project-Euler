#!/usr/bin/env python
import psyco
psyco.full()

#def primes(x) :
#	a = range(0,x+1)
#	a[0], a[1] = 0, 0
#	for i in xrange(2, x+1) :
#		if a[i] == i :
#			a[i] = 1
#			if (x+1)/ i > i :
#				for j in xrange(i*i, x+1, i) :
#					a[j] = i
#	#return [x for x, aa in enumerate(a) if aa == 1]
#	return a
#
#def prime_factors(a) :
#	global p
#	if a > len(p) :
#		return [ a ]
#	else :
#		result = []
#		while p[a] != 1 :
#			result.append(p[a])
#			a /= p[a]
#		result.append(a)
#		return result
#
#def product(s) :
#	result = 1
#	for ss in s :
#		result *= ss
#	return result
#
#def choose(s, i) :
#	if i == 0 :
#		yield []
#	else :
#		for x in xrange(len(s)) :
#			c = s[x]
#			temp = s[x+1 : ]
#			for cc in choose(temp, i - 1) :
#				yield [c] + cc
#	return
#
#def proper_divisors(i, pf) :
#	results = [1]
#	for j in xrange(1, len(pf)) :
#		for x in choose(pf, j) :
#			px = product(x)
#			results.append(px)
#	return set(results)

def create_proper_divisors(limit):
    table = [1] * limit
    for n in xrange(2, limit):
        for m in xrange(n + n, limit, n):
            table[m] += n
    return table

def test() :
	m = 1000 * 1000

	print "Generating prime factors and proper divisors"
	pd = create_proper_divisors(m)

	print "Creating chains"
	chains = []
	for i, p in enumerate(pd) :
		#if i % 1000 == 0 :
		#	print ".",
		if p != 1 :
			chain = []
			while True :
				chain.append(i)
				i = pd[i]
				if i > m : break
				elif i in chain :
					j = chain.index(i)
					cc = chain[j : ]
					if len(cc) > 1 :
						chains.append(cc)
						for j in cc :
							pd[j] = 1
					break

	print "writing out chains"
	sc = [ (len(chain), min(chain), chain) for chain in chains ]
	for scc in sorted(sc) :
		print scc

if __name__ == "__main__" :
	import time
	s = time.clock()
	test()
	e = time.clock()
	print "Elapsed time: ", (e - s)
