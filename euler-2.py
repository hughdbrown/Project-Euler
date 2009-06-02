#!/usr/bin/env python
def fibonacci(x) :
	i, a = 1, [1, 1]
	while (a[i-1] + a[i] < x) :
		a.append(a[i-1] + a[i])
		i += 1
	return a

#for x in fibonacci(1000000) :
#	print x
	
print sum(x for x in fibonacci(1000000) if (x % 2 == 0))
