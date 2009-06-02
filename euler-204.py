#!/usr/bin/env python
import psyco
psyco.full()

import math

def primes(n) :
	n += 1
	x = list(range(n))
	for i in xrange(2,n) :
		if x[i] == i :
			x[i] = 1
			if i*i < n :
				for j in xrange(i*i, n, i) :
					x[j] = i
	return [ i for i in xrange(2,n) if x[i] == 1 ]

def hamming(p, so_far, max_total) :
	assert(so_far <= max_total)
	if so_far == max_total :
		return 1
	else:
		left_p, right_p = p[0], p[1:]
		if not len(right_p) :
			max_iters = 0
			tmp = so_far
			while tmp <= max_total :
				tmp *= left_p
				max_iters += 1
			#max_iters = 1 + int(math.log(max_total/so_far) / math.log(left_p))
			return max_iters
		else :
			count = 0
			while so_far <= max_total :
				count += hamming(right_p, so_far, max_total)
				so_far *= left_p
			return count

def euler_204() :
	limit = 100
	p = primes(limit)
	upper = 1000*1000*1000
	start = 1
	print hamming(p, start, upper)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler_204()
	e = time.clock()
	print "Elapsed: ", (e - s)
