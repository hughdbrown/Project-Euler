#!/usr/bin/env python
from __future__ import with_statement

import psyco
psyco.full()

def primes(x) :
	a = range(0,x+1)
	a[0], a[1] = 0, 0
	limit = int((x + 1) ** 0.5)
	for i in xrange(2, limit+1) :
		if a[i] == i :
			a[i] = 1
			for j in xrange(i*i, x+1, i) :
				a[j] = i
	for i in xrange(limit, x + 1) :
		if a[i] == i :
			a[i] = 1
	return [x for x, aa in enumerate(a) if aa == 1]

def key_gen(n) :
	k = sorted(str(n))
	if k[0] == "0" :
		return None
	if any(k[i] == k[i+1] for i in xrange(len(k) - 1)) :
		return None
	return "".join(k)

def powerkey(s) :
	global d
	def balance(s, ks) :
		return sorted(set(s) - set(ks))
	def key(s, i) :
		result, balance = "", ""
		for j in xrange(len(s)) :
			mask = 1 << j
			if mask & i :
				result += s[j]
			else :
				balance += s[j]
		return "".join(sorted(result)), "".join(sorted(balance))
	x = len(s)
	if not x :
		yield []
	else :
		for i in xrange (1, 2 ** x + 1) :
			ks, rest = key(s, i)
			if ks in d :
				for y in powerkey(rest) :
					yield [ks] + y
	return
def product(s) :
	global d
	total = 1
	for ss in s :
		total *= len(d[ss])
	return total
def drkey(r) :
	return ".".join(str(rr) for rr in sorted(r))

def load_primes(n) :
	with open ("primes-100000000.txt") as f :
		results = [ ]
		for line in f.readlines() :
			line = line.strip()
			if key_gen(line) :
				x = int(line)
				if x > n : break
				results.append(x)
		return results

def test(start) :
	import time
	import collections
	global d, p
	print "Generating primes: ", time.clock() - start
	limit = 100 * 1000 * 1000
	p = load_primes(limit)
	print "%d primes" % len(p)

	print "Generating possible prime keys: ", time.clock() - start
	d = collections.defaultdict(set)
	for pp in p :
		kp = key_gen(pp)
		if kp :
			d[kp].add(pp)
	p = []
	print "%d buckets" % len(d)
	print "primes: %d" % sum(len(v) for v in d.itervalues())

	print "Counting combinations: ", time.clock() - start
	dr = {}
	for r in powerkey("123456789") :
		drk = drkey(r)
		if drk not in dr :
			dr[drk] = r

	for drk in sorted(dr.iterkeys()) :
		print drk, sorted(dr[drk])
	print "combinations: ", len(dr)
	total = sum(product(r) for r in dr.itervalues())
	print total

if __name__ == "__main__" :
	import time
	s = time.clock()
	test(s)
	e = time.clock()
	print "Elapsed: ", (e - s)
