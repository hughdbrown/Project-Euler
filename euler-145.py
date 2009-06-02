#!/usr/bin/env python

import psyco
psyco.full()

import sys
#import gcd
#import primes

def reverseNumber(x) :
	c = 0
	while x :
		q, r = divmod(x, 10)
		c = 10*c + r
		x = q
	return c
def isReversibleNumber(x) :
	while x :
		q, r = divmod(x, 10)
		if r & 1 == 0:
			return False
		x = q
	return True

def test(x) :
	rev = reverseNumber(x)
	if (rev&1) ^ (x&1) :
		return isReversibleNumber(x + rev)
	else :
		return False
	#return isReversibleNumber(x + rev)
def reversibleNumberIterator(limit) :
	x = 0
	L = []
	while x <= limit :
		if not len(L) :
			x += 10
			d = int(str(x)[0])
			L = ([2,4,6,8] if d&1 else [1,3,5,7,9])
			if x + L[0] > limit :
				return
		yield x + L.pop(0)
	return
def euler145(limit) :
	count, j = 0, 2000
	for i in reversibleNumberIterator(limit) :
		if not j :
			print >> sys.stderr, i, count, "\r",
			j = 2000
		j -= 1
		if test(i) :
			count += 1
	return count

if __name__ == "__main__" :
	#c = euler145(10000)
	c = euler145(1000*1000*1000)
	print
	print c
