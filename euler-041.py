import combine, primes

for i in range(4, 10) :
	print "%d digits" % i
	p = primes.primes(10 ** i)
	a = range(1, i + 1)
	for s in combine.permute(a) :
		d = int(s)
		if d in p :
			print d

