"""
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. 

The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""

import primes

s = set()
upper = int(5000.0 * (6 ** 0.5))
primeset = primes.primes(400)
for i in xrange(2, 10, 2) : ## upper, 2) :
	j = i * i
	print i, upper, j, "\r",
	if j > primeset[-1] : break
	elif all((j+x) in primeset for x in [1,3,7,9,13,27]) :
		s.add(j)
		print j, "                  "
print i, s
print sum(s)

##primeset = primes.primes(150 * 1000 * 1000)
##for p in primeset :
#	print p, "\r",
#	n = int((p-1) ** 0.5)
#	if not(n & 1) and (n*n == (p-1)) :
#		if all((p+x) in primeset for x in [3,7,9,13,27]) :
#			set.add(p)
#			print p
#print s
#print sum(s)
