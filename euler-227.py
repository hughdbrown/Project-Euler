#!/usr/bin/env python

import psyco
psyco.full()

def euler227(size, iterations) :
	import random
	accum = 0
	for _ in xrange(iterations) :
		counter = 0
		pos = [0, size // 2]
		while pos[0] != pos[1] :
			for i in (0, 1) :
				a = random.randint(1, 6)
				pos[i] = (pos[i] + (1 if a == 1 else (-1 if a == 6 else 0))) % size
			counter += 1
		accum += counter
	print size, float(accum) / float(iterations)

if __name__ == "__main__" :
	import time
	s = time.clock()
	for i in range(4, 30, 2) :
		euler227(i, 100*1000*1000)
	e = time.clock()
	print "Elapsed: ", (e - s)
