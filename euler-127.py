import sys

def prime_table(n) :
	n += 1
	x = list(range(n))
	for i in range(2,n) :
		if x[i] == i :
			x[i] = 1
			if i*i < n :
				for j in range(i*i, n, i) :
					x[j] = i
	return x

def primes(n) :
	x = prime_table(n)
	return [ i for i in range(2,n) if x[i] == 1 ]

def product(s) :
	import operator, functools
	return functools.reduce(operator.mul, s)

#def gcd(x,y) :
#	if 0 in (x,y) : return max(x,y)
#	else : return gcd(y, x - y*(x//y))

factor_table = {}
def factors(table, n) :
	import collections
	d = collections.defaultdict(int)
	while table[n] != 1 :
		x = table[n]
		d[x] += 1
		n //= x
	d[n] += 1
	return [k for k in sorted(d.keys())]

def create_factor_table(table, limit) :
	global factor_table
	for c in range(1, limit) :
		factor_table[c] = factors(table, c)

def rad(a,b,c) :
	global factor_table
	return product(tuple(sorted(set(factor_table[a] + factor_table[b] + factor_table[c]))))

def some_power(p, limit) :
	import math
	s = set()
	for pp in p :
		x = pp*pp
		if x >= limit :
			break
		powers = []
		while x < limit :
			powers.append(x)
			x *= pp
		for x in powers :
			j = int(limit / x)
			for k in range(1, j+1) :
				if k not in powers and k * x < limit :
					s.add(k * x)
	return sorted(s)
		
def ab_pairs(c, possible_b) :
	# Remove all numbers that share factors with c
	possibles = set(range(1, c))
	for i in factor_table[c] :
		possibles = possibles.difference(range(i, c, i))

	# Yield all possible pairs
	for b in reversed(sorted(possible_b)) :
		a = c - b
		if b <= a :
			break
		elif a in possibles :
			if not set(factor_table[a]).intersection(factor_table[b]) :
				yield (a, b)
	return

def euler127(limit) :
	global factor_table
	print ("Creating prime table({0})".format(limit), file=sys.stderr)
	table = prime_table(limit)

	print ("Creating primes({0})".format(limit), file=sys.stderr)
	p = [ i for i in range(2,len(table)) if table[i] == 1 ]

	print ("Creating factor table".format(), file=sys.stderr)
	create_factor_table(table, limit)
 
	print ("Creating powers".format(), file=sys.stderr)
	powers = some_power(p, limit)
	print ("{0} possible values for c".format(len(powers)), file=sys.stderr)
	print(file=sys.stderr)
	results = []
	ab_count = 0
	for i,c in enumerate(powers) :
		possibles = set(powers[:i])
		for a,b in ab_pairs(c, possibles) :
			if rad(a,b,c) < c :
				results.append((a,b,c))
				print ("{1} {0} {2}\r".format(c, len(results), ab_count), file=sys.stderr, end="")
			ab_count += 1

	print()
	total = sum(c for _,_,c in results)
	print (total)
	for i, t in enumerate(results) :
		print (i, t)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler127(110*1000)
	#euler127(1000)
	e = time.clock()
	print("Elapsed: {0}".format(e -s ))
