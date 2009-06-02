#!/usr/bin/env python
import math

def isPrime(val) :
	if val <= 3 : return True
	elif val % 2 == 0 : return False
	else :
		upper = math.sqrt(val)
		for i in range(3, int(upper) + 1, 2) :
			if val % i == 0 : return False
		return True

def nextPrime(primes) :
	x = primes[-1] + 2
	while not isPrime(x) :
		x += 2
	return x

primes = [2, 3, 5, 7]
while len(primes) < 10001 :
	n = nextPrime(primes)
	print n
	primes.append(n)
	
print primes