
#def find_factor(n) :
#    for i in xrange(2, int(n**0.5 + 1)) :
#        if n % i == 0 :
#            return i
#    return n
    
#def find_factors(n) :
#    factors = []
#    while n != 1 :
#        fac = find_factor(n)
#        if fac not in factors :
#            factors.append(fac)
#        n /= fac
#    return factors

import psyco
psyco.full()

import primes
pt = primes.primeTable(1000*1000)

def find_factors(n) :
	factors = set()
	while pt[n] != 1 :
		factors.add(pt[n])
		n /= pt[n]
	factors.add(n)
	return factors

def totient(n) :
	num, denom = 1, 1
	for factor in find_factors(n) :
		num *= (factor - 1)
		denom *= factor
	return (n * num) / denom

import datetime
s = datetime.datetime.utcnow()
pt = primes.primeTable(1000*1000)
e = datetime.datetime.utcnow()
print e - s

s = datetime.datetime.utcnow()
print sum((i-1 if pt[i] == 1 else totient(i)) for i in xrange(2, 1000001))
e = datetime.datetime.utcnow()
print e - s
