import primes

for i in range(1, 100000) :
	s = str(1*i) + str(2*i)
	if len(s) == 9 :
		c = primes.countset(s)
		if max(c.itervalues()) == 1 and s.find("0") == -1 :
			print s
