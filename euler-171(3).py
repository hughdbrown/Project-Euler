from __future__ import with_statement
import psyco
psyco.full()

import sys

def fact(n) :
	result = 1
	for i in xrange(2, n+1) :
		result *= i
	return result

def digitsum(d) :
	return sum(k*v for k, v in d.iteritems())

def digitcount(d) :
	return sum(v for v in d.itervalues())

def product(s) :
	result = 1
	for a in s :
		if a : result *= a
	return result

def combinations(d, digit_limit) :
	digitcounts = [a for a in d.itervalues()]
	n = sum(digitcounts)
	assert (n <= digit_limit)
	result = 0
	fn1 = fact(n - 1)
	for i, item  in enumerate(d.iteritems()) :
		k, v = item
		if k != 0 :
			digitcounts[i] -= 1
			result += fn1/product(fact(a) for a in digitcounts)
			digitcounts[i] += 1
	return result 

def createdict(line) :
	import collections
	d = collections.defaultdict(int)
	for c in line :
		d[int(c)] += 1 
	return d

def euler171(digit_limit) :
	with open("euler-171.txt") as f :
	#with open("euler-171(2).txt") as f :
		lines = [ line.strip() for line in f ]
	total = 0
	multiplier = 111111111
	multiplier = int("1" * digit_limit)
	for i, line in enumerate(lines) :
		print >> sys.stderr, i, line, "\r",
		d = createdict(line)
		nonzerocount = len(line)
		maxzerocount = digit_limit - nonzerocount
		ds = digitsum(d)
		assert(0 <= ds <= 9 * digit_limit)
		d[0] = maxzerocount
		cc = combinations(d, digit_limit)
		result = (cc * ds * multiplier) // digit_limit
		total += result
		#if total > 1000000000 :
		#	total %= 1000000000
	print
	print
	print
	print
	print total		

if __name__ == "__main__" :
	import time
	s = time.clock()
	digit_limit = 20
	euler171(digit_limit)
	e = time.clock()
	print "Elapsed: ", (e - s)
