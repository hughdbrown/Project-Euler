#!/usr/bin/env python
import psyco
psyco.full()

def find_diophantine(n, lower_limit, upper_limit) :
	for y in xrange(lower_limit,upper_limit+1) :
		t = n * y * y
		t += 1
		x = long(t ** 0.5)
		if x * x == t :
			return x, y
	return None

d = [ x* x for x in xrange(1,32)]
s = [ y for y in xrange(1,1000) if y not in d ]
#limits = [ 10**i for i in range(1,8)]
max_seen, j = 0, 0
lower_limit = 1L
upper_limit = 10L
while len(s) :
	print "------- %d, %d items" % (upper_limit, len(s))
	new_s = []
	for x in s :
		p = find_diophantine(x, lower_limit, upper_limit)
		if p != None :
			print x, p
			if p[0] > max_seen :
				max_seen = p[0]
				j = x
		else :
			new_s.append(x)
	print max_seen, j
	s = new_s
	lower_limit = upper_limit
	upper_limit *= 10

print max_seen, j
