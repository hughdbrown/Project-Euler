import psyco
psyco.full()

import primes
import fraction

def lowerPrimeIterator(lower, upper, mult, L) :
	while lower < upper :
		yield L, lower
		lower *= mult
		L *= mult
	return
def currentPrimeIterator(lower, upper, mult, L) :
	while lower < upper :
		yield L, lower
		lower *= mult
		L *= mult
	return

def euler72(upper) :
	p = primes.primes(upper)
	d = [-1] * upper

	for j, pn in enumerate(p) :
		#print pn, "\r",
		if pn >= upper: break
		L = pn - 1
		#d[pn] = L
		a = [pn]
		for val, k in currentPrimeIterator(pn, upper, pn, L) :
			d[k] = val
			a.append(k)
		for x in a :
			for i in xrange(j) :
				px = p[i]
				for val, k in lowerPrimeIterator(x*px, upper, x, L*x) :
					if not k in d :
						d[k] = val
	print

	#for i,v in enumerate(d):
	#	if v == -1 :
	#		print i
	#print sum(v for k,v in d.iteritems())
	print sum(d)
	for i,v in enumerate(d):
		print i,v
	#for k,v in d.iteritems() :
	#	print k, v
	#print visited - len(p), sum((1 if e == 0 else 1) for e in d)
	print

def bruteForceEuler72(upper) :
	s = set()
	for j in range(2, upper) :
		print j, len(s), "\r",
		for i in range(1, j) :
			f = (i, j)
			rf = fraction.reducedFraction (f)
			s.add(rf)
	print
	print len(s)


if __name__ == "__main__" :
	upper = 1000*1000+1
	##upper = 2000
	#euler72(upper)
	bruteForceEuler72(upper)
