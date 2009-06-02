#!/usr/bin/env python
set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]
lcm = 4480842240000
inverses = [ lcm/(x*x) for x in set_of_numbers ]
half = lcm/2

def find(remainder, start_index, factors) :
	if remainder == 0 :
		yield factors
	else :
		#print factors, start_index, remainder
		for j in range(start_index, len(inverses)) :
			if (inverses[j] <= remainder) :
				trial = remainder - inverses[j]
				new_factors = factors + [j]
				for factors_found in find(trial, j+1, new_factors) :
					yield factors_found
	return

import time
fmt = "%Y-%m-%d %H:%M:%S"
print "Start ", time.strftime(fmt, time.gmtime())
for i, x in enumerate(find(half, 0, [])) :
	print i, time.strftime(fmt, time.gmtime()), [ set_of_numbers[j] for j in x ]
print "End ", time.strftime(fmt, time.gmtime())
