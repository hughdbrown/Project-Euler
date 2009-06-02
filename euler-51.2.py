#!/usr/bin/env python
import psyco
psyco.full()

import collections

def primes(x) :
	a = range(0,x+1)
	a[0], a[1] = 0, 0
	for i in xrange(2, x+1) :
		if a[i] == i :
			a[i] = 1
			if (x+1)/ i > i :
				for j in xrange(i*i, x+1, i) :
					a[j] = i
	return [x for x, aa in enumerate(a) if aa == 1]

def chooser(indexes, length) :
	if length == 0 :
		yield []
	elif len(indexes) == length :
		yield indexes
	else :
		for i, c in enumerate(indexes) :
			for a in chooser(indexes[i+1 : ], length-1) :
				yield [c] + a
	return

def keys(s, length) :
	result = []
	for c in set(s) :
		indexes = [ j for j in xrange(len(s)) if s[j] == c ]
		if len(indexes) >= length :
			for choose in chooser(indexes, length) :
				ss = s
				for k in choose :
					ss = ss[ : k] + "*" + ss[k+1 : ]
				result.append(ss)
			#for choose in chooser(indexes, length) :
			#	ss = "*" * len(s)
			#	for k in choose :
			#		ss = ss[ : k] + s[k] + ss[k+1 : ]
			#	result.append(ss)
	return result


"""
for a in [56003, 56113, 56333, 56443, 56663, 56773, 56993] :
	s = str(a)
	print s, keys(s, 2)
"""
#for a in [1801, 1811, 1831, 1861, 1871, 1877, 1889] :
#	s = str(a)
#	print s, keys(s, 2)

def test_euler51(set_len) :
	print "Generating primes"
	n = 6
	p = primes(10 ** n)

	#aa = dict()
	#for pp in p :
	#	s = str(pp)
	#	aa[pp] = max(s.count(str(i)) for i in range(10))

	for replace_len in range(2, n + 1) :
		print "Creating keys of length %d" % replace_len
		d = collections.defaultdict(set)
		for pp in p :
			#if aa[pp] >= replace_len :
			for x in keys(str(pp), replace_len) :
				d[x].add(pp)

		print "Finding solution in %d items" % len(d)
		for k in sorted(d.iterkeys()) :
			v = d[k]
			if len(v) == set_len :
				print k, sorted(v)
				return

if __name__ == "__main__" :
	import time
	s = time.clock()
	test_euler51(8)
	e = time.clock()
	print "Done: ", (e - s)
