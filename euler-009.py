#!/usr/bin/env python

import math

def findTriplet() :
	sq = [i * i for i in range(0, 1001)]
	for i in range(1, 500) :
		for j in range(i, 500) :
			c2 = sq[i] + sq[j]
			if c2 in sq :
				c = int(math.sqrt(c2))
				print i, j, c
				s = i + j + c
				if s == 1000 :
					yield i, j, c, i*j*c
				else :
					factor = int(1000/s)
					if factor * s == 1000 :
						ii = i*factor; jj = j * factor; cc = c *factor
						yield ii, jj, cc, ii*jj*cc
	return

for x in findTriplet() :
	print x
