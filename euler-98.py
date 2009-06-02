import collections
import string

def x(v) :
	y = len(v[0])
	lower, upper = 10**(y-1), 10**y
	lx = int(lower ** 0.5) - 1
	ly = int(upper ** 0.5) + 1
	squares = [ i*i for i in range(lx, ly) if len(str(i*i)) == y ]
	for sq in squares :
		ssq = str(sq)
		if len(set(ssq)) == y :
			t = string.maketrans(v[0], ssq)
			tt = v[1].translate(t)
			if int(tt) in squares :
				print v[0], v[1], ssq, tt				
	

def euler98() :
	f = open("words-98.txt")
	words = []
	for line in f.readlines() :
		words.extend(line.strip().replace('"', "").split(","))

	d = collections.defaultdict(list)
	for i, w in enumerate(words) :
		a = sorted(w)
		sa = "".join(a)
		d[sa].append(w)

	deletions = [ key for key in d.keys() if len(d[key]) == 1 ]
	for delete in deletions :
		d.pop(delete)

	print d
	for k, v in d.iteritems() :
		x(v)

euler98()
