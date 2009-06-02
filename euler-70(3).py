import psyco
psyco.full()

import sys

def euler70(dmax):
    "npf = sum(totient(n) for n in xrange(2, dmax + 1))"
    # calculate totient(n) for n=2..N
    N = dmax + 1; totient = range(N)
    for n in xrange(2, N):
        print >> sys.stderr, n, "\r",
        if totient[n] == n:
            totient[n] = n-1
            for k in xrange(n+n, N, n):
                totient[k] *= (n - 1);
                totient[k] //=  n;

    min_so_far = 20000
    k = 0
    score = 6
    # find number of reduced proper fraction
    for n in xrange(2, N):
        print >> sys.stderr, n, score, k, "\r",
	score = float(n)/float(totient[n])
	if score < min_so_far :
		a = sorted(c for c in str(totient[n]))
		b = sorted(c for c in str(n))
		if a == b :
			k, min_so_far = n, score
			print
			print k, totient[n], min_so_far
    return k

if __name__ == "__main__" :
	import datetime
	s = datetime.datetime.utcnow()
	x = euler70(10**7)
	print 
	print x
	e = datetime.datetime.utcnow()
	print e - s

