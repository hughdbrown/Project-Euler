try:
    import psyco
    psyco.full()
except ImportError:
    pass

import primes

def euler47() :
	limit = 200 * 1000

	print "Generating primes"
	p = primes.primes(limit)
	x = [0] * limit

	print "Generating factor counts"
	for pp in p:
		for j in xrange(pp, limit, pp) :
			x[j] += 1

	for i in xrange(2, limit) :
		if all(4 == x[i-j] for j in range(0, 4)) :
			print i-3
			break


	#run_length = 4
	#pf = [0,0]
	#for i in range(run_length) :
	#	pf.append(len(set(primes.primeFactors(2+i))))
	#
	#i = 2
	#while not all(pf[i+j] == run_length for j in range(run_length)) :
	#	pf.append(len(set(primes.primeFactors(i+run_length))))
	#	i += 1
	#
	#for k in range(i,i+run_length) :
	#	print k, pf[k], primes.primeFactors(k)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler47()
	e = time.clock()
	print "Elapsed: ", (e - s)
	
