import primes

r, s, m = 0, 0, 0
p = primes.primes(1000*1000)

def test(i, j) :
	for n in range(0, 1000) :
		pp = n**2 + i*n + j
		if pp not in p :
			break
	return n


for i in range(-999, 1000) :
	for j in p :
		print i,j,m,"\r",
		if j >= 1000: break
		else :
			t = test(i, j)
			if t > m :
				r, s, m = i, j, t
				print r,s,m
print r,s,m