import primes, powerset, factorial

max_elem = 10000
lowest = 2
d = {}
for i in range(max_elem-1, lowest-1, -1) :
	pf = primes.factors(i)
	d[i] = sum(pf[0: -1])

s = []
for i in range(lowest, max_elem) :
	p = d[i]
	if lowest < p < max_elem :
		if i == d[p] and p < d[p] :
			s.append ( (p, d[p]) )

a = 0
for x in s :
	a += x[0] + x[1]
	print x
print a

