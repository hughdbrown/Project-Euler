#!/usr/bin/env python
import collections

squared = [ i * i for i in range(0, 10) ]
dsquares = {}
def chain_value(n) :
	a = []
	while n not in [1, 89] :
		if dsquares.has_key(n) :
			n = dsquares[n]
		else :
			a.append(n)
			n = sum(squared[int(x)] for x in str(n))
	for aa in a:
		dsquares[aa] = n
	return n

def foo(s, remainder, count) :
	if count == 0 :
		if remainder == 0:
			yield []
	else :
		for i in range(len(s)) :
			x = s[i]
			x_sq = x * x
			if remainder > count*x_sq :
				break
			else :
				new_remainder = remainder - x_sq
				if new_remainder >= 0:
					new_set = s[i : ]
					for j in foo(new_set, new_remainder, count-1) :
						yield [x] + j
	return

fact_lookup = {}
def fact(x) :
	if not fact_lookup.has_key(x) :
		result = 1
		for i in range(1, x+1) :
			result *= i
			fact_lookup[i] = result
	return fact_lookup[x]

def product(s) :
	return reduce(lambda a, b: a * b, s)

def score(x) :
	diff = collections.defaultdict(lambda: 0)
	for y in x :
		diff[y] += 1
	return fact(len(x)) / product(fact(diff[x]) for x in diff.keys())

if __name__ == "__main__" :
	import time
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	sum_of_one = 0
	for sq in [ i for i in range(1, 7 * 9*9 + 1) if chain_value(i) == 1 ] :
		sum_of_one += sum(score(x) for x in foo([9,8,7,6,5,4,3,2,1,0], sq, 7))
	print 9999999 - sum_of_one
	print "End ", time.strftime(fmt, time.gmtime())
