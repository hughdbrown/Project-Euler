import primes

d17 = [d for d in range(17, 1000, 17) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d13 = [d for d in range(13, 1000, 13) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d11 = [d for d in range(132, 1000, 11) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d7 = [d for d in range(7, 1000, 7) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d5 = [d for d in range(5, 1000, 5) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d3 = [d for d in range(3, 1000, 3) if max(primes.countset("%03d" % d).itervalues()) == 1 ]
d2 = [d for d in range(2, 1000, 2) if max(primes.countset("%03d" % d).itervalues()) == 1 ]

a = set()
b = set()
for i in d17 :
	s17 = "%03d" % i
	for j in d13 :
		s13 = "%03d" % j
		if s13[1:3] == s17[0:2] :
			a.add(i)
			b.add(j)
d17 = sorted([aa for aa in a])
d15 = sorted([bb for bb in b])

a = set()
b = set()
for i in d13 :
	s13 = "%03d" % i
	for j in d11 :
		s11 = "%03d" % j
		if s11[1:3] == s13[0:2] :
			a.add(i)
			b.add(j)
d13 = sorted([aa for aa in a])
d11 = sorted([bb for bb in b])


a = set()
b = set()
for i in d11 :
	s11 = "%03d" % i
	for j in d7 :
		s7 = "%03d" % j
		if s7[1:3] == s11[0:2] :
			a.add(i)
			b.add(j)
d11 = sorted([aa for aa in a])
d7 = sorted([bb for bb in b])


a = set()
b = set()
for i in d7 :
	s7 = "%03d" % i
	for j in d5 :
		s5 = "%03d" % j
		if s5[1:3] == s7[0:2] :
			a.add(i)
			b.add(j)
d7 = sorted([aa for aa in a])
d5 = sorted([bb for bb in b])

a = set()
b = set()
for i in d5 :
	s5 = "%03d" % i
	for j in d3 :
		s3 = "%03d" % j
		if s3[1:3] == s5[0:2] :
			a.add(i)
			b.add(j)
d5 = sorted([aa for aa in a])
d3 = sorted([bb for bb in b])


a = set()
b = set()
for i in d3 :
	s3 = "%03d" % i
	for j in d2 :
		s2 = "%03d" % j
		if s2[1:3] == s3[0:2] :
			a.add(i)
			b.add(j)
d3 = sorted([aa for aa in a])
d2 = sorted([bb for bb in b])


#print d17
#print d15
#print d13
#print d11
#print d7
#print d5
#print d3
#print d2


def pandigital() :
	for a2 in d2 :
		aa2 = "%03d" % a2
		for a3 in d3 :
			aa3 = "%03d" % a3
			if aa2[1:] != aa3[0:-1] : continue
			for a5 in d5 :
				aa5 = "%03d" % a5
				if aa3[1:] != aa5[0:-1] : continue
				for a7 in d7 :
					aa7 = "%03d" % a7
					if aa5[1:] != aa7[0:-1] : continue
					for a11 in d11 :
						aa11 = "%03d" % a11
						if aa7[1:] != aa11[0:-1] : continue
						for a13 in d13 :
							aa13 = "%03d" % a13
							if aa11[1:] != aa13[0:-1] : continue
							for a17 in d17 :
								aa17 = "%03d" % a17
								if aa13[1:] != aa17[0:-1] : continue
								trial = aa2 + aa3[2] + aa5[2] + aa7[2] + aa11[2] + aa13[2] + aa17[2]
								c = primes.countset(trial)
								if max(c.itervalues()) == 1 :
									for a in "0123456789" :
										if not c.has_key(a) :
											yield a + trial
											break
									else :
										print "error in %s" % trial


pp = [p for p in pandigital()]
print pp
print sum(int(p) for p in pp)


								