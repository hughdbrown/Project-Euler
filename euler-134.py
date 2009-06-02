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
	return [ i for i in range(2,len(x)) if x[i] == 1 ]

def compose(x, y) :
	base = 10 ** len(str(x))
	base_incr = base % y
	ss = base + x
	s = ss % y

	print("{0} {1}\r".format(x, y), file=sys.stderr, end="")
	#i = 0
	#while s != 0 :
	#	i += 1
	#	s += base_incr
	#	if s >= y :
	#		s -= y
	i = 0
	q = y // base_incr
	r = q * base_incr
	while s != 0 :
		i += q
		s += r - y
		if s < 0 :
			i += 1
			s += base_incr
	result = ss + (i * base)
	#assert (0 == result%y)
	return result

def euler_134(limit) :
	p = primes(limit)
	total = sum(compose(p[i-1], p[i]) for i in range(3,len(p)))
	print()
	print(total)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler_134(1000*1000)
	#euler_134(30)
	e = time.clock()
	print("Elapsed: {0}".format(e - s))
