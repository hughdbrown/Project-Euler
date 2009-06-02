#!/usr/bin/env python
def factorial(n) :
	x = 1
	for i in range(1, n + 1) :
		x *= i
	return x

print sum(int(s) for s in str(factorial(100)) )
