from __future__ import with_statement
import psyco
psyco.full()

import sys

digit_limit = 20

fact_table = [0] * (digit_limit + 1)
def fact(n) :
	if not fact_table[n]:
		result = 1
		for i in xrange(2, n+1) :
			result *= i
		fact_table[n] = result
	#return result
	return fact_table[n]

def digitsum(d) :
	return sum(k*v for k, v in d.iteritems())

def digitcount(d) :
	return sum(v for v in d.itervalues())

def product(s) :
	result = 1
	for a in s :
		if a : result *= a
	return result

def combinations(d) :
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

def euler171() :
	with open("euler-171.txt") as f :
		lines = [ line.strip() for line in f ]
	total = 0
	for i, line in enumerate(lines) :
		print >> sys.stderr, i, line, "\r",
		d = createdict(line)
		nonzerocount = len(line)
		maxzerocount = digit_limit - nonzerocount
		ds = digitsum(d)
		assert(0 <= ds <= 9 * digit_limit)
		for zerocount in xrange(maxzerocount + 1) :
			d[0] = zerocount
			cc = combinations(d)
			result = cc * ds
			length = nonzerocount + zerocount
			if length > 1 :
				fc = result / nonzerocount
				otherc = (result - fc) / (length - 1)
				assert (otherc == int(otherc))
				if length > 9 :
					result = 111111111 * otherc
				else :
					result = (10**length * fc) + (int("1" * (length-1)) * otherc)
			total += result
			if total > 1000000000 :
				total %= 1000000000
	print
	print
	print
	print
	print total		

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler171()
	e = time.clock()
	print "Elapsed: ", (e - s)
