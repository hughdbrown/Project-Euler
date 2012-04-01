#!/usr/bin/env python
import psyco
import primes
import sys

psyco.full()

def generateCandidates2(pi, indexes, L, x) :
	mult = sum(10**(L - i) for i in indexes)
	pi -= x * mult
	return [ pi + i*mult for i in range(10) ]

def generateCandidates(spi, indexes, L) :
	spix = spi[0 : indexes[0] ] + "0" + spi[indexes[0]+1 : indexes[1] ] + "0" + spi[indexes[1]+1 : ]
	pi = int(spix)
	mult = 10**(L-indexes[0]) + 10**(L-indexes[1])
	return [pi] + [ pi + i*mult for i in range(1,10) ]
	#spix = spi[0 : indexes[0] ] + "X" + spi[indexes[0]+1 : indexes[1] ] + "X" + spi[indexes[1]+1 : ]
	#return [ int(spix.replace("X", str(i))) for i in range(10) ]
	#fmt = spi[0 : indexes[0] ] + "%d" + spi[indexes[0]+1 : indexes[1] ] + "%d" + spi[indexes[1]+1 : ]
	#return [ int(fmt % (i,i)) for i in range(10) ]

def testPrimes(x, lower_limit, minimum) :
	removeList = [ ]
	for i,y in enumerate(x) :
		if not primes.isPrime(y) :
			removeList.append(i)
			if len(removeList) > 10-minimum :
				return False
	else :
		for i in range(len(removeList)) :
			j = removeList[-1 - i]
			x.pop(j)
		return True
def test(pi) :
	spi = str(pi)
	L = len(spi) - 1
	for i,c in enumerate(spi) :
		j = spi.find(c, i+1)
		if j > 0 :
			#yield generateCandidates(spi, [i,j], L)
			yield generateCandidates2(pi, [i,j], L, int(c))
	return

def euler51(lower_limit) :
	import binarySearch
	upper_limit = 10 * lower_limit
	p = primes.primes(upper_limit + 50)
	lower = binarySearch.binarySearch(p, lower_limit)
	upper = binarySearch.binarySearch(p, upper_limit)

	minimum = 7

	for i in xrange(lower, upper) :
		pi = p[i]
		print >> sys.stderr, pi, "\r",
		for x in test(pi) :
			if testPrimes(x, lower_limit, minimum) :
				print pi, x
				if len(x) == 8 :
					sys.exit(0)
	p = None

if __name__ == "__main__" :
	a = [10*1000, 100*1000, 1000*1000, 10*1000*1000, 100*1000*1000]
	for aa in a :
		euler51(aa)
