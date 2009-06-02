#!/usr/bin/env python
import math

def prime_factors(x) :
	factors = []
	while x % 2 == 0 :
		x /= 2
		factors.append(2)
	lowest = 3
	while x >= lowest :
		##y = int(math.floor(math.sqrt(x) + 2))
		added = False
		for z in range(lowest, x, 2) :
			while x % z == 0 :
				factors.append(z)
				lowest = z
				x /= z
				added = True
		if not added:
			factors.append(x)
			break
	return factors

def product(a) :
	prod = 1
	for x in a :
		prod *= x
	return prod

##print prime_factors(317584931803)

factors_required = []
##for i in range(1, 21) :
for i in [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80] :
	s = prime_factors(i*i)
	for x in s :
		while s.count(x) > factors_required.count(x) :
			factors_required.append(x)

print factors_required
print product(factors_required)
