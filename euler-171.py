import psyco
psyco.full()

import sys

max_items = 5

def compose(s, i, items, total) :
	if total <= 0 :
		yield []
	else :
		assert(items < max_items)
		for j in xrange(i, len(s)) :
			n = s[j]
			kk = n * n
			if kk <= total <= (max_items - items) * kk :
				for c in compose(s, j, items+1, total - kk) :
					yield [n] + c

def test(xx, sq) :
	if len(xx) > max_items :
		#print "Too long( ", len(xx), "): ", xx
		return False
	elif sum(c*c for c in xx) != sq :
		#print "Bad(", sq, "): ", xx
		return False
	else :
		return True

def euler171() :
	#s = "987654321"
	s=[9,8,7,6,5,4,3,2,1]
	top = 81*max_items
	t = int(0.5 + top ** 0.5)
	squares = [x * x for x in xrange(1, t) if x*x <= top ] 
	for sq in squares :
		x = [y for y in compose(s, 0, 0, sq)]
		print >> sys.stderr, sq, len(x)
		for xx in x :
			if test(xx, sq) :
				ss = "".join(str(c) for c in xx)
				print ss

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler171()
	e = time.clock()
	print >> sys.stderr, "Elapsed: ", (e - s)
