import collections
import random
import decimal

def init(size) :
	d = collections.defaultdict(int)
	one = decimal.Decimal(1)
	for i in range(size) :
		for j in range(size) :
			d[i,j] = one
	return d

def neighbors_of(i, j, size) :
	def legal(i, j) :
		return (0 <= i < size) and (0 <= j < size)
	results = []
	for p in [(-1,0), (1,0), (0,-1), (0,1)] :
		newi, newj = i + p[0], j + p[1]
		if legal(newi, newj) :
			results.append((newi, newj))
	return results

def odds_of(i, j, size) :
	def iscorner(i, j) :
		return i in [0, size-1] and j in [0, size-1]
	def isedge(i, j) :
		return i in [0, size-1] or j in [0, size-1]
	if iscorner(i, j) : return decimal.Decimal("0.5")
	elif isedge(i, j) : return decimal.Decimal(1)/decimal.Decimal(3)
	else : return decimal.Decimal("0.25")

def euler213(size, iterations) :
	d = init(size)
	neighbors = dict()
	odds = dict()
	for i in range(size) :
		for j in range(size) :
			neighbors[i, j] = neighbors_of(i, j, size)
			odds[i, j] = odds_of(i, j, size)

	for m in range(iterations) :
		dst = dict()
		for i in range(size) :
			for j in range(size) :
				dst[i, j] = sum(odds[n] * d[n] for n in neighbors[i, j])
		d = dst
	return sum(max(0, 1 - d[k]) for k in d)

if __name__ == "__main__" :
	import time

	s = time.clock()
	size = 30
	trial_iters = 50
	c = euler213(size, trial_iters)
	print ("{0} {1}".format(size, c))
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))
