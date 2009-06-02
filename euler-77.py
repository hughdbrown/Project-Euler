

try:
    import psyco
    psyco.full()
except ImportError:
    pass


"""
4 [[2,1]]
5 [[3,1]]
6 [[4,1],[3,1]]
7 [[4,1]]
8 [[5,1], [4,2]]
9 [[7,1],[5,2]]
10 [[7,1], [
"""

import primes
import sys

def x(i, n, a) :
	y = n - i
	b = a[y]
	if i <= 1 : return 0
	if i >= y :
		s = sum(t[1] for t in b) + (1 if primes.isPrime(y) else 0)
	else :
		s = sum(t[1] for t in b if t[0] <= i)
	return s

def score(aa) :
	count = 0
	for i in range(len(aa)) :
		j, x = aa[i]
		count += x
	return count
def euler76(limit) :
	p = primes.primes(limit)
	p.append(limit+2)
	a = [ [[0,0]], [[1,0]], [[2,0]] ]
	p_counter = 1
	for i in range(3, limit+1) :
		print >> sys.stderr, i, "\r",
		d = []
		for j in range(p_counter, -1, -1) :
			pp = p[j]
			if pp >= i : continue
			y = x(pp, i, a)
			if y :
				d.append( [pp, y] )
		if i == p[p_counter] :
			p_counter += 1
		if score(d) >= 5000 :
			return i
		a.append(d)
	#s = sum(t[1] for t in a[limit])
	#return s
	return 0

if __name__ == "__main__" :
	c = euler76(1000*1000)
	print 
	print c
