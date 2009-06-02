import factorial, powerset, primes

for i in range(1, 100000) :
	t = (i * (i + 1)) / 2
	pf = primes.factors(t)
	print i, t, len(pf)
	if len(pf) >= 500 :
		break

