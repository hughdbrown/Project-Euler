import specialFactors
import primes


j = 4
max_so_far = -1
k = -1
while 1 :
	if not primes.isPrime(j) :
		f = primes.factors(j)
		sp = specialFactors.specialFactors(f, j)	
		L = len(sp)
		if L > max_so_far :
			pf = primes.primeFactors(j)
			max_so_far, k = L, j
			print k, max_so_far, pf
		if L > 1000 : break
		print j, L, "\r", 
	j += 1
print
print k, max_so_far