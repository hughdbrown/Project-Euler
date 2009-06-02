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
	result = 1
	for ss in s :
		result *= ss
	return result

def factor_count(table, n) :
	import collections
	d = collections.defaultdict(int)
	while table[n] != 1 :
		x = table[n]
		d[x] += 1
		n //= x
	d[n] += 1
	return product(v+1 for k,v in d.items())

def euler187(limit) :
	p = prime_table(limit // 2)
	n = 0
	for i in range(2, len(p)) :
		if p[i] == 1 :
			x = p[i : 1 + limit//i].count(1)
			n += x
		if i % 20000 == 0:
			print("{0}\r".format(i), file=sys.stderr, end="")
	print()
	print(n)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler187(100*1000*1000)
	#euler187(10*1000)
	#euler187(30)
	e = time.clock()
	print("Elapsed: {0}".format(e - s))
