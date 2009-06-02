import psyco
psyco.full()

import primes
import sys

def euler70(limit) :
	sq = 2 * int(limit ** 0.5)
	p = primes.primes(sq)
	best, phi, n = 6, 0, 0
	for i,x in enumerate(p) :
		pi = p[i]
		print >> sys.stderr, pi, best, "\r",
		for j in range(i+1, len(p)) :
			pj = p[j]
			x = (pi - 1) * (pj - 1)
			y = pi * pj
			if y > limit : continue
			a = sorted(c for c in str(y))
			b = sorted(c for c in str(x))
			if a == b :
				score = float(y) / float(x)
				if score < best :
					best, phi, n = score, x, y
					print 
					print best, phi, n, pi, pj
	return n

if __name__ == "__main__" :
	x = euler70(10*1000*1000+1)
	print
	print x