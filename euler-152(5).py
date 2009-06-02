#!/usr/bin/env python
set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]
lcm = 4480842240000
##half = lcm/2
inverses = [ lcm/(x*x) for x in set_of_numbers ]
residuals = [ sum(inverses[i: -1]) for i in range(len(inverses)) ]

def real_numbers(x) :
	return [ set_of_numbers[j] for j in x ]

def find(remainder, start_index, factors) :
	if remainder == 0 :
		yield factors
	else :
		#if (start_index < len(inverses)) :
		#	print real_numbers(factors), set_of_numbers[start_index], remainder, "\r",
		for j in range(start_index, len(inverses)) :
			new_remainder = remainder - inverses[j]
			if (new_remainder >= 0) :
				new_factors = factors + [j]
				
				for factors_found in find(new_remainder, j+1, new_factors) :
					yield factors_found
			elif (remainder > residuals[j]) :
				break
	return

def euler_152() :
	import time
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	for i in range(len(inverses)) :
		x = inverses[i]
		for j, y in enumerate(find(x, i+1, [])) :
			print set_of_numbers[i], real_numbers(y)
	print "End ", time.strftime(fmt, time.gmtime())
	
if __name__ == "__main__" :
	euler_152()
