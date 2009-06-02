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

def euler123(limit) :
	print ("Creating prime table({0})".format(limit), file=sys.stderr)
	table = prime_table(limit)

	print ("Creating primes({0})".format(limit), file=sys.stderr)
	p = [ i for i in range(2,len(table)) if table[i] == 1 ]

	for i, pp in enumerate(p) :
		i += 1
		if i & 1 :
			if (i * pp * 2) >= 10*1000*1000*1000 :
				x, y, m = 1, 1, pp * pp
				for _ in range(i) :
					x = x * (pp-1) % m
					y = y * (pp+1) % m
				n = (x + y) % m
				print("Trying {0} {1} {2}".format(i, pp, n))
				if n >= 10*1000*1000*1000 :
					print (n)
					print (i, pp)
					break

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler123(1000*1000)
	e = time.clock()
	print("Elapsed: {0}".format(e -s ))
