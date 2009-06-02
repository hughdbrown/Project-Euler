#!/usr/bin/env python
set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]
set_of_squares = [a*a for a in set_of_numbers]
primes = [3,5,7]
d = {}
for p in primes :
	a = [ x for x in set_of_numbers if int(x/p)*p == x ]
	d[p] = a
	
#for k,v in d.iteritems() :
#	print k, v

def sumsq(values, factors) :
	return sum(values[a]*values[a] for a in factors)

def sum_of_factors_is_square(values, factors) :
	import math
	sq = sumsq(values, factors)
	sqr = int(math.sqrt(sq))
	return sqr*sqr == sq

def find(values, start_index, factors) :
	if len(factors) > 1 and sum_of_factors_is_square(values, factors) :
		yield factors
	else :
		for j in range(start_index, len(values)) :
			new_factors = factors + [j]
			for factors_found in find(values, j + 1, new_factors) :
				yield factors_found
	return

for k, v in d.iteritems() :
	print k, v
	for i, x in enumerate(find(v, 0, [])) :
		print i, [ v[j] for j in x ]

