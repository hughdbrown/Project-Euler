import psyco
psyco.full()

import fraction
import prime_cache

def test(n) :
	s = set()
	for i in range(1,n) :
		print i, "\r",
		m = prime_cache.isPrime(i)
		for j in range((i+1)/4, (i+1)/2 + 1) :
			if 2*j < i < 3*j :
				k = (j, i)
				if m :
					s.add(k)
				else :
					s.add(reducedFraction(k))
	#print sorted(s)
	print len(s)

def fullTest() :
	test(10001)

def testReducedFractions() :
	test(21)

if __name__ == "__main__" :
	fullTest()
	#testReducedFractions()
