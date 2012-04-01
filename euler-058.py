try:
    import psyco
    psyco.full()
except ImportError:
    pass

limit = 1000*1000*10
#import primes
#p = primes.primes(limit)
#pp = dict.fromkeys((ppp for ppp in p), 1)

#def isPrime2(n) :
#	if pp.has_key(n) : return True
#	elif n > p[-1]*p[-1] : 
#		print "Not enough primes"
#		sys.exit(0)
#	else :
#		for ppp in p:
#			if n%ppp == 0:
#				return False
#		else :
#			return True

def isPrime3(n) :
	m = int(n ** 0.5)
	#return all(n % i for i in xrange(3, m, 2))	# 20 seconds
	#return not any(n % i == 0 for i in xrange(3, m, 2))	# 22 seconds
	for i in xrange(3, m, 2) :
		if n % i == 0:
			return False
	else :
		return True

def isPrime(n) :
	import rabinmiller
	return rabinmiller.is_prime(n)

def corners(n) :
	sq = n*n
	return [sq - (n-1), sq - 2*(n-1), sq - 3*(n-1)]

primes = 3
diag = 7
i = 3
while 10*primes >= diag :
	i += 2
	diag += 4
	primes += sum(isPrime(cc) for cc in corners(i))
	# 2.4 seconds
	#for cc in corners(i) :
	#	if isPrime(cc) : primes += 1

print i, float(primes) / float(diag)
