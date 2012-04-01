import psyco
psyco.full()

import sys

def testSolution(d, values) :
	print >> sys.stderr, "Testing ", values, "\r",
	for i,k in enumerate(values) :
		v = values[ : i] + values[i+1 : ]
		if any(x not in d[k] for x in v) :
			break
	else :
		print
		print values

def testAllKeys(d) :
	for i in sorted(d.keys()) :
		for j in d[i] :
			if j > i :
				for m in d[j] :
					if m > j and m in d[i] :
						for n in d[m] :
							if n > m and n in d[j] :
								for p in d[n] :
									if p > n :
										testSolution(d, [i,j,m,n,p])
#def testFourKeys(d) :
#	for i in sorted(d.keys()) :
#		for j in d[i] :
#			if j > i :
#				for m in d[j] :
#					if m > j and m in d[i]:
#						for p in d[m] :
#							if p > m  and p in d[j] :
#								testSolution(d, [i,j,m,p])

def euler60(upper) :
	import primes
	import collections
	print "Testing up to %d" % upper
	p = primes.primes(upper)
	d = collections.defaultdict(list)
	base = 10
	for i in xrange(1, len(p)) :
		pi = p[i]
		while pi > base : base *= 10
		print >> sys.stderr, pi, len(d), "\r",
		base2 = base
		for j in xrange(i+1, len(p)) :
			pj = p[j]
			while pj > base2 : base2 *= 10
			pipj = pi*base2 + pj
			if primes.isPrime(pipj) :
				pjpi = pj*base + pi
				if primes.isPrime(pjpi) :
					d[pi] += [pj]
					d[pj] += [pi]

	testAllKeys(d)

if __name__ == "__main__" :
	euler60(8400)
