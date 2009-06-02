#!/usr/bin/env python

def product(a) :
	return reduce(lambda x, y: x * y, a)

def factorial(n) :
	return (1 if n <= 1 else product(range(1, n + 1)))
	
def choose(n, r) :
	if n == r: return 1
	elif (n-1) == r : return r
	else :
		k = n - r
		x = min(k, r)
		y = max(k, r)
		return product(range(y+1, n+1)) / factorial(x)



