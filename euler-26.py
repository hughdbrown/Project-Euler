def lastDigit(j, i) :
	curr = int(10**j % i)
	return curr

d = {}
for i in range(2, 1000) :
	digits = []
	count, prev, j = 0, -1, 1
	while 10**j < i :
		j += 1
	y = lastDigit(j, i)
	digits.append(y)
	j += 1
	while 1 :
		curr = lastDigit(j, i)
		if curr in digits : break
		else :
			digits.append(curr)
			count += 1
			j += 1
	d[i] = count

m = max(d.itervalues())
for k, v in d.iteritems() :
	if v == m :
		print k, v
