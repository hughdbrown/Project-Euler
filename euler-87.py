import psyco
psyco.full()

import prime_cache
import primes

squares, cubes, fourth = [], [], []
upper = 50*1000*1000

for i in range(2, int(upper ** 0.5)+1) :
	if primes.isPrime(i) :
		sq = i * i
		if sq < upper :
			squares.append(sq)
		else :
			break
		tr = i * sq
		if tr < upper :
			cubes.append(tr)
		fo = i * tr
		if fo < upper :
			fourth.append(fo)

#print squares
#print cubes
#print fourth

s = set()
for x4 in fourth :
	remainder4 = upper - x4
	for x3 in cubes :
		remainder3 = remainder4 - x3
		if remainder3 > 0 :
			for x2 in squares :
				remainder2 = remainder3 - x2
				if remainder2 >= 0 :
					a = [x2, x3, x4]
					s.add(sum(a))
					print sum(a), a

#print s
print len(s)
