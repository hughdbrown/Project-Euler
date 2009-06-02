import primes

s = set()
for i in range(12, 98) :
	si = "%02d" % i
	for j in range(123, 987) :
		r = i * j
		sj = "%03d" % j
		sr = "%04d" % r
		p = si + sj + sr
		if p.find("0") == -1 :
			c = primes.countset(p)
			if max(c.itervalues()) == 1 :
				print i, j, r, p
				s.add(r)

for i in range(1, 10) :
	si = "%01d" % i
	for j in range(1000, 10000) :
		r = i * j
		sj = "%04d" % j
		sr = "%04d" % r
		p = si + sj + sr
		if p.find("0") == -1 :
			c = primes.countset(p)
			if max(c.itervalues()) == 1 :
				print i, j, r, p
				s.add(r)



for pp in s :
	print pp
print sum(pp for pp in s)
