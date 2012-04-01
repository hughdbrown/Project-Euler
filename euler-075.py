
import psyco
psyco.full()

import collections
import gcd
import sys

def triangleTest(a,b,c) :
	p = a+b+c
	return all(i < (p-i) for i in [a,b,c])

def pythagoreanIterator(limit) :
	sq_limit = int((limit + 1) ** 0.5)
	for i in range(1, sq_limit) :
		print >> sys.stderr, i, "\r",
		for j in range(i+1, sq_limit) :
			i_sq, j_sq = i**2, j**2
			a = j_sq - i_sq
			b = 2*i*j
			c = i_sq + j_sq
			p = a+b+c
			if p > limit : break
			if not triangleTest(a,b,c) : break
			if (i&1 == 0 or j&1 == 0) and gcd.gcd(i,j) == 1 :
				yield sorted( (a,b,c) )
	return

def euler75(limit) :
	d = collections.defaultdict(set)
	for t in pythagoreanIterator(limit) :
		a,b,c = t
		p = a+b+c
		for i in range(1, 1+ limit/p) :
			r, x, y, z = i * p, i * a, i * b, i * c
			#print "\t", "%d [%d,%d,%d]" % (r,x,y,z)
			d[r].add( (x,y,z) )
			
	count = sum( 1 for _,v in d.iteritems() if len(v) == 1 )
	return count


if __name__ == "__main__" :
	c = euler75(1000*1000)
	#c = euler75(150)
	print
	print c