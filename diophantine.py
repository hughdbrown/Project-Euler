#!/usr/bin/env python
#import psyco
#psyco.full()

def part1(m,x,y,k) :
	return (float(m*x+y)/float(k)) ** 2
def part2(m,n,k) :
	return float(m*m - n) / float(k)
def part3(m,y,n,x,k) :
	return (float(m*y + n*x)/float(k)) ** 2
def solved (n, x, y, k, m) :
	p1 = part1(m,x,y,k)
	p2 = part2(m,n,k)
	p3 = part3(m,y,n,x,k)
	assert (int(p1) == p1)
	assert (int(p2) == p2)
	assert (int(p3) == p3)
	return (int(p1 ** 0.5), int(p2), int(p3 ** 0.5))

def minSolution(x, y, k, n) :
	k = abs(k)
	m = [ t * k + x for t in range(1,20)]
	mm = [abs(a**2 - n) for a in m]
	mmin = min(mm)
	for i, a in enumerate(mm) :
		if a == mmin :
			return m[i]

def solveDiophantine(n, k) :
	(x, y) = (1, int(n ** 0.5))
	kk = y*y - n
	while kk != k :
		print x, kk, y
		m = minSolution(x, y, kk, n)
		(x, kk, y) = solved(n, x, y, kk, m)
	return (x, y)

if __name__ == "__main__" :
	for D in [67] :
		print solveDiophantine(D, 1)
