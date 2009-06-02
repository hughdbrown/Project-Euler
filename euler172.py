try:
    import psyco
    psyco.full()
except ImportError:
    pass

import collections

def euler172(lower, upper) :
	count = 0
	for i in xrange(lower, upper) :
		#d = collections.defaultdict(int)
		d = [0] * 10
		for c in str(i):
			d[int(c)] += 1
		if max(d) <= 3 :
			count += 1
	return count

if __name__ == "__main__" :
	import time
	s = time.clock()
	for n in range(2, 9) :
		lower, upper = 10**n, 10**(n+1)
		x = euler172(lower, upper)
		print (lower, upper, x)
	e = time.clock()
	#print("Elapsed: {0}".format(e - s))
	print "Elapsed: ", (e - s)


