def primes(limit) :
	limit += 1
	x = range(limit)
	for i in xrange(2,limit) :
		if x[i] ==  i:
			x[i] = 1
			for j in xrange(i*i, limit, i) :
				x[j] = i
	return [j for j in xrange(2, limit) if x[j] == 1]

def factors(limit) :
	limit += 1
	x = range(limit)
	for i in xrange(2,limit) :
		if x[i] ==  i:
			x[i] = 1
			for j in xrange(i*i, limit, i) :
				x[j] = i
	result = []
	y = limit-1
	while x[y] != 1 :
		divisor = x[y]
		result.append(divisor)
		y /= divisor
	result.append(y)
	return result


#print primes(20)
#print primes(100)
#print primes(1000)

for i in xrange(2, 50) :
	print i, factors(i)

