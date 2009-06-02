#!/usr/bin/env python
import psyco
import collections
def findSquareTriple2(limit) :
	c = collections.defaultdict(list)
	sq = [ x*x for x in xrange(1, limit)]
	count = 0
	for i in xrange(1, len(sq)) :
		print i, count
		for j in xrange(1 + (i & 1), i) :
			x, y = (sq[i] - sq[j]) >> 1, (sq[i] + sq[j]) >> 1
			#if (x + y == sq[i]) :
			c[y].append(x)
			count += 1
	print "Done first part"
	for x in sorted(c.iterkeys()) :
		for y in c[x] :
			if y in c :
				s = set(c[y]).intersection(set(c[x]))
				if len(s) :
					print x, y, s[0]
					return x, y, s[0]
	return None

if __name__ == "__main__" :
	limit = 10000
	print findSquareTriple2(limit)
