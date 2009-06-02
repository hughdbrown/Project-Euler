#!/usr/bin/env python

import psyco
psyco.full()

import sys

def sumSeries(d, i) :
	count = 0
	ditem = d[i]
	for j in range(len(ditem)) :
		dd = ditem[j]
		count += dd[1]
	return count

def check(d, i, x) :
	count = 0
	ditem = d[i]
	for j in range(len(ditem)) :
		dd = ditem[j]
		if dd[0] <= x :
			count += dd[1]
	return count

def euler76(limit) :
	d = range(limit + 1)
	d[2] = [[1,1]]
	d[3] = [[2,1],[1,1]]
	d[4] = [[3,1],[2,2],[1,1]]
	d[5] = [[4,1],[3,2],[2,2],[1,1]]
	d[6] = [[5,1],[4,2],[3,3],[2,3],[1,1]]
	d[7] = [[6,1],[5,2],[4,2],[3,4],[2,3],[1,1]]
	d[8] = [[7,1],[6,2],[5,3],[4,5],[3,6],[2,4],[1,1]]

	for i in range(9, limit + 1) :
		print >> sys.stderr, i, "\r",
		dd = [[i-1, 1], [i-2, 2]]
		for j in xrange(i-2, 2, -1) :
			x = check(d, i-j, j)
			dd.append([j, x])
		dd.append([2,int(i/2)])
		dd.append([1,1])
		d[i] = dd
	print d[limit]
	return sumSeries(d, limit)

if __name__ == "__main__" :
	c = euler76(100)
	print
	print c
