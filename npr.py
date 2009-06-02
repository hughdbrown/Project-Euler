import psyco
psyco.full()

def npf(dmax):
    "npf = sum(totient(n) for n in xrange(2, dmax + 1))"
    # calculate totient(n) for n=2..N
    N = dmax + 1; totient = range(N)
    for n in xrange(2, N):
        if totient[n] == n:
            for k in xrange(n, N, n):
                totient[k] *= (n - 1);
                totient[k] //=  n;
    # find number of reduced proper fraction
    return sum(totient[2:])

#main: It takes me ~3 seconds on P4 2GHz
if __name__ == "__main__" :
	import datetime
	s = datetime.datetime.utcnow()
	print npf(10**6)
	e = datetime.datetime.utcnow()
	print e - s

