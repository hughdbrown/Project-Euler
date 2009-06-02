import psyco
psyco.full()

import primes
import sys

dr = {}
def digitalRoot(n) :
	if n in dr :
		return dr[n]
	else :
		x = n
		while n >= 10 :
			sn = str(n)
			n = sum(int(d) for d in sn)
		dr[x] = n
		return n

def digitalRootSet(sp) :
	return sum(digitalRoot(a) for a in sp)

def primeTable(limit) :
	pt = [1] * (limit + 1)
	for i in range(2, limit + 1) :
		if pt[i] == 1 :
			for j in xrange(i+i, limit+1, i) :
				if pt[j] == 1 :
					pt[j] = i
	return pt

def product(s) :
	a = 1
	for x in s :
		a *= x
	return a

def specialPowerSet(s) :
	while s.count(3) >= 2 :
		s.remove(3)
		s.remove(3)
		s.append(9)
	while s.count(2) >= 3 :
		s.remove(2)
		s.remove(2)
		s.remove(2)
		s.append(8)
	if s.count(2) >= 1 and s.count(3) >= 1 :
		s.remove(2)
		s.remove(3)
		s.append(6)
	c = primes.countset(s)
	if all(a == 1 for a in c.itervalues()) :
		yield s
	else :
		L = len(s)
		xrl = xrange(L)
		ss = set()
		for i in xrange(1 << L):
			if i == 0 : continue
			a = product(s[j] for j in xrl if (i & (1 << j)))
			#if not a in ss :
			#ss.add(a)
			b = [ s[j] for j in xrl if (i & (1 << j)) == 0 ]
			yield sorted([a] + b)

def getFactors(pt, i) :
	a = []
	while pt[i] != 1 :
		a.append(pt[i])
		i /= pt[i]
	a.append(i)
	return a	

def euler159(limit) :
	result = 0
	pt = primeTable(limit)
	for i in xrange(2, limit) :
		print >> sys.stderr, i, result, "\r",
		if pt[i] != 1 :
			f = getFactors(pt, i)
			#print i, f
			m = max(digitalRootSet(sp) for sp in specialPowerSet(f))
			#m = 0
			#for sp in specialPowerSet(f) :
			#	a = digitalRootSet(sp) 
			#	print "\t", sp, a
			#	if a > m : m = a
			result += m
	return result

if __name__ == "__main__" :
	r = euler159(1000*1000)
	#r = euler159(100)
	print 
	print r

