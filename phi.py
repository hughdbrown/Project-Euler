import psyco
psyco.full()

import primes
import sys

def product(s) :
	a = 1
	for x in s:
		a *= x
	return a

def phi_p(n, p) :
	num, denom = [n], []
	for pp in p :
		if n < pp: break
		q, r = divmod(n, pp)
		if r == 0 :
			num.append(pp-1)
			denom.append(pp)
			while r == 0 :
				n = q
				q, r = divmod(n, pp)
	if n != 1 :
		num.append(n-1)
		denom.append(n)
	return product(num) / product(denom)

def phi(n) :
	p = primes.primes(n)
	return phi_p(n, p)

if __name__ == "__main__" :
	limit = 1000*1000+1
	p = primes.primes(limit)
	#p.append(limit + 1)
	ph = range(limit+1)
	ph[1] = 0
	# Do primes
	for pp in p :
		ph[pp] = pp - 1

	# Do squares
	sq_limit = int(limit ** 0.5)
	for i in range(2, sq_limit) :
		ph[i*i] = i * ph[i]

	# Do all other numbers
	for i in range(2,limit) :
		print >> sys.stderr, i, "\r",
		if ph[i] == 0 :
			ph[i] = phi_p(i, p)

	print
	print sum(ph)
