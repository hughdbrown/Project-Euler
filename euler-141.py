#try:
#    import psyco
#    psyco.full()
#except ImportError:
#    pass

import specialFactors
import primes

c = dict.fromkeys((i, i*i*i) for i in range(1,10000))
def CubeRoot(n) :
	if n < 0 :
		return None
	elif c.has_key(n) :
		return c[n]
	else :
		upper = long(n ** 0.333333333)
		for i in range(upper-2, upper+2) :
			cube = i*i*i
			if cube > n : return None
			elif cube == n: return i
		else : return None

def testSpecialFactors() :
	#f = primes.factors(37156)
	#f = primes.factors(576081)
	f = primes.factors(759)
	print f
	print specialFactors.specialFactors(f)

#pc = primes.primes(1000*1000)
#composites = set (range(2,1000*1000)) - set(pc)
#composites2 = sorted(composites)

def euler141() :
	## [3,102,130,312,759,2496,2706,3465,6072,6111,8424,14004,16005,36897,37156,92385,98640,112032,117708,128040,351260,740050]) :
	s = set()
	for sqr in xrange(2, 1000*1000) :
		if primes.isPrime(sqr) : continue
		i = sqr*sqr
		print sqr, i, "\r",
		f = primes.factors(sqr)
		sp = specialFactors.specialFactors(f, sqr)
		for r in sp :
			x = r * (i - r)
			cub = CubeRoot(x)
			if cub :
				q, r2 = divmod(i, cub)
				if r == r2 :
					a = [r, q, cub]
					print sqr, i, a
					s.add(i)
					break
	print sorted(s)
	print sum(s)


if __name__ == "__main__" :
	euler141()
	#testSpecialFactors()




		##print sp
		#sp = primes.factors(i)

		#for j in sp :
		#	r = j*j
		#	x = r * (i - r)
		#	cub = CubeRoot(x)
		#	if cub :
		#		q, r2 = divmod(i, cub)
		#		if r == r2:
		#			a = [q, r, cub]
		#			print sqr, i, a # sorted(a)
		#			s.add(i)
		#			break

		#for j in sp :
		#	y = j*j
		#	x = y * (i - y)
		#
		#	cub = CubeRoot(x)
		#	if not cub :
		#		y = j*j*j
		#		x = i - y
		#		cub = CubeRoot(x)
		#		if cub : cub *= j
		#	if cub :
		#		q, r = divmod(i, cub)
		#		if r == y :
		#			a = [q, r, cub]
		#			print sqr, i, sorted(a)
		#			s.add(i)
		#			break

		##set([k*k for k in range(1,sqr)] + [k*k*k for k in range(1,sqr) if k*k*k < sqr]))
		#b = sqr * sqr
		#c = sqr * b
		#squares_and_trips.add(b)
		#squares_and_trips.add(c)
		##for r in sorted(squares_and_trips) :
		#for r in range(2,sqr) :
		#for r in squareTripsIterator(sqr) :

#def primesTo(n) :
#	nn = binarySearch(pc, n)
#	return pc[ : nn]

#def nonPrimeIterator(n) :
#	for c in composites2 :
#		if c > n: return
#		else: yield c
#	return

#def squareTripsIterator(n) :
#	s1 = [ i*i for i in range(2,int(n ** 0.5)) ]
#	s2 = [ i*i*i for i in range(2,int(n ** 0.3333333333333)+5) ]
#	s = set(s1 + s2)
#	for k in sorted(s) :
#		yield k
#	return

#def isPerfectSquare(n) :
#	import math
#	sq = int(math.sqrt(n))
#	return sq*sq == n

#def SquareRoot(n) :
#	import math
#	sq = int(math.sqrt(n))
#	return (sq if sq*sq == n else None)

#def isPerfectCube(n) :
#	upper = long(n ** 0.5)
#	lower = long(upper ** 0.5)
#	for i in range(lower, upper) :
#		cube = i*i*i
#		if cube > n : return False
#		elif cube == n: return True
#	else : return False

