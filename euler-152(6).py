#!/usr/bin/env python
import psyco
psyco.full()

import gc

def product(list_of_numbers) :
	result = 1
	for x in list_of_numbers:
		result *= x
	return result

def setup_values() :
	set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]  # + range(11,80,11) +range(13,80,13) +range(17,80,17) +range(19,80,19) +range(23,80,23)+range(29,80,29)+range(31,80,31)+range(37,80,37)
	set_of_numbers.sort()

	a = [64,27,25,49,17] #11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
	lcm = product(a + a)
	half = lcm/2
	inverses = [ lcm/(x*x) for x in set_of_numbers ]
	remainders = [ sum(inverses[i+1:]) for i in xrange(len(inverses)) ]
	return set_of_numbers, inverses, remainders, half

def euler_152() :
	import collections
	set_of_numbers, inverses, remainders, half = setup_values()
	#print inverses
	#print remainders
	d = collections.defaultdict(int)
	d[0] = 1
	for i, r, n in zip(inverses, remainders, set_of_numbers) :
		# Delete the keys that cannot contribute to a sum of 'half'
		lower_limit = half-r-i
		deletable = [k for k in d.iterkeys() if k < lower_limit]
		for k in deletable :
			del d[k]
		deleted = len(deletable)
		deletable = None
		gc.collect()

		# Add i to all candidate keys
		dk = [k for k in d.iterkeys() if (half - r) <= (k + i) <= half]
		dk.sort()
		dk.reverse()
		s1 = len(d)
		for k in dk:
		        d[k + i] += d[k]
		dk = None
		added = len(d) - s1
		print n, len(d), d[half], deleted, added
		gc.collect()
	return d[half]
	
if __name__ == "__main__" :
	import time
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	print euler_152()
	print "End ", time.strftime(fmt, time.gmtime())
