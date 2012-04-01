import primes

def rotate(n) :
	ns = str(n)
	for i in range(len(ns)) :
		ns = ns[1 : ] + ns[0]
		yield ns

x = primes.primes(1000*1000)
#x = primes.primes(100)

r = []
for i, s in enumerate(x) :
	if s > 20 :
		ss = str(s)
		for c in "02468" :
			if c in ss :
				r.append(i)
				break
r.reverse()
for rr in r :
	x.pop(rr)

circular_prime = 0
for p in x :
	print p, circular_prime, "\r",
	for y in rotate(p) :
		if int(y) not in x :
			break
	else :
		circular_prime += 1
		#print y
print circular_prime
