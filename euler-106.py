import psyco
psyco.full()

def pairwiseCompare(x, y) :
	return sum((1 if x1 > y1 else 0) for x1, y1 in zip(x,y))

def choose(s, i) :
	if not i :
		yield []
	else :
		for j in xrange(len(s) - i + 1) :
			a, rest = [s[j]], s[j+1: ]
			for ss in choose(rest, i-1) :
				yield a + ss

def test_all(hi) :
	total = 0
	s = range(1, hi + 1)
	ss = set(s)
	for i in xrange(2, 1 + hi/2) :
		for x in choose(s, i) :
			diff = ss - set(x)
			diff -= set(a for a in diff if a < x[0])
			for y in choose(sorted(diff), i) :
				total += (1 if pairwiseCompare(x, y) not in [0, i] else 0)
	print hi, total

def euler_106() :
	import time
	s = time.clock()
	#test_all(4)
	#test_all(7)
	test_all(12)
	e = time.clock()
	print "Elapsed: %f" % (e - s)

euler_106()
