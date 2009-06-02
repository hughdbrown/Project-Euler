#!/usr/bin/env python
set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]
##set_of_numbers = [2,3,4,5,6, 7,9,10,12, 15,20, 28, 30,35,36,40, 45] ##,48,49,50, 54,56,60,63,64, 70,72,75,80]
lcm = 4480842240000
inverses = [ lcm/(x*x) for x in set_of_numbers ]
half = lcm/2

residuals = [ sum(inverses[i: -1]) for i in range(len(inverses)) ]

def searchNextInverse (startIndex, remainder) :
	for k in range(startIndex, len(inverses)) :
		if remainder >= inverses[k] :
			return k
	else :
		return -1
	
def real_numbers(x) :
	return [ set_of_numbers[j] for j in x ]

def find(remainder, start_index, factors) :
	if remainder == 0 :
		yield factors
	else :
		##print real_numbers(factors), set_of_numbers[start_index], remainder
		##start_index = max(j for j in range(start_index, len(inverses)) if remainder >= inverses[j] )
		for j in range(start_index, len(inverses)) :
			##print set_of_numbers[j]
			new_remainder = remainder - inverses[j]
			if (new_remainder >= 0) :
				new_factors = factors + [j]
				
				for factors_found in find(new_remainder, j+1, new_factors) :
					yield factors_found
			elif (remainder > residuals[j]) :
				##print set_of_numbers[j], remainder, residuals[j], inverses[j]
				break
	return

def euler_154() :
	import time
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	for i, x in enumerate(find(half, 0, [])) :
		print i, time.strftime(fmt, time.gmtime()), real_numbers(x)
	print "End ", time.strftime(fmt, time.gmtime())
	
if __name__ == "__main__" :
	euler_154()
