import psyco
psyco.full()

def test(n) :
	for d in [2,3] :
		while n%d==0:
			n/=d
	while d*d <= n:
		d += 2
		while n%d==0:
			n/=d
		d += 2
		while n%d==0:
			n/=d
		d += 2
	return n

def test2() :
	from time import clock
	s = clock()
	#n = test(600851475143)
	n = test(6857)
	e = clock()
	print "found %d in %f" % (n, (e - s))

test2()

