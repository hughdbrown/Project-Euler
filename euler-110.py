import psyco

psyco.full()

import primes
import specialFactors

"""
2 3 [3]
3 4 [2, 2]
5 6 [2, 3]
8 12 [2, 2, 3]
11 24 [2, 2, 2, 3]
14 30 [2, 3, 5]
23 60 [2, 2, 3, 5]
32 120 [2, 2, 2, 3, 5]
37 180 [2, 2, 3, 3, 5]
40 210 [2, 3, 5, 7]
53 360 [2, 2, 2, 3, 3, 5]
67 420 [2, 2, 3, 5, 7]
68 720 [2, 2, 2, 2, 3, 3, 5]
95 840 [2, 2, 2, 3, 5, 7]
113 1260 [2, 2, 3, 3, 5, 7]
122 1680 [2, 2, 2, 2, 3, 5, 7]
157 2520 [2, 2, 2, 3, 3, 5, 7]
158 3780 [2, 2, 3, 3, 3, 5, 7]
202 4620 [2, 2, 3, 5, 7, 11]
"""



def doTest(n) :
	d = {}
	nFactors = primes.primeFactors(n)
	sp = specialFactors.specialFactors(nFactors)
	for i in sp :
		y = int((n * i)/(i - n))
		if (i+y) == (i * y) / n :
			if i not in d :
				d[y] = i
	return len(d)

if __name__ == "__main__" :
	max_so_far = 0
	j = 0
	for i in [3,4,6,12,24,30,60,120,180,210,360,420,720,840,1260,1680,2520,3780,4620] :
		x = doTest(i)
		print i, x, "\r",
		if x > max_so_far :
			max_so_far, j = x, i
			print max_so_far, j, primes.primeFactors(i)

	for i in xrange(j+1, 100*1000*1000) :
		x = doTest(i)
		print i, x, "\r",
		if x > max_so_far :
			max_so_far, j = x, i
			print max_so_far, j, primes.primeFactors(i)
			if max_so_far > 4*1000*1000 : break
	print
	print max_so_far, j
