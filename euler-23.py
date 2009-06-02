#import psyco
#psyco.full()

#import primes, factorial

def euler23() :
	#upper = 28124
	#abundant = [i for i in range(12, upper) if sum(primes.factors(i)[0:-1]) > i]
	#
	#found = {}
	#for i in abundant :
	#	for j in abundant :
	#		a = i + j
	#		if a > 28123 : break
	#		else : found[a] = 1
	#missing = [ i for i in range(1, upper) if not found.has_key(i) ]
	#print missing
	#print sum(missing)

	def abundant_numbers(upper) :
		x = [1] * upper
		for i in range(2, upper) :
			for j in xrange(i+i, upper, i) :
				x[j] += i
		return set(i for i in xrange(1,upper) if x[i] > i)

	def summable(i) :
		return any(i - a in abundant for a in s_ab if a < i)

	upper = 28124
	print "Find abundant numbers"
	abundant = abundant_numbers(upper)
	s_ab = sorted(abundant)

	print "Find summable with abundant numbers"
	print sum(s for s in xrange(1, upper) if not summable(s))

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler23()
	e = time.clock()
	print "Elapsed: ", (e - s)
