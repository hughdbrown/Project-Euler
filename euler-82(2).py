from __future__ import with_statement

import psyco
psyco.full()

def cheapest_way_to_get_here(r, vals, row, sum_vals) :
	left = [ (r[i] + (sum_vals[row+1] - sum_vals[i])) for i in xrange(0, row) ]
	straight = r[row] + vals[row]
	right = [ (r[i] + (sum_vals[i+1] - sum_vals[row])) for i in xrange(row+1, len(vals)) ]
	return min(left + [straight] + right)

def calc_sum_vals(vals) :
	sum_vals, a = [0], 0
	for vv in vals :
		a += vv
		sum_vals.append(a)
	return sum_vals

def euler_82() :
	with open ("matrix-82.txt") as f:
		lines = [ line.strip().split(",") for line in f.readlines() ]

	size = len(lines)
	q = [0] * size
	for col in xrange(size) :
		vals = [ int(lines[row][col]) for row in xrange(size) ]
		sum_vals = calc_sum_vals(vals)
		r = [ qq for qq in q ]
		q = [ cheapest_way_to_get_here(r, vals, row, sum_vals) for row in xrange(size) ]
	print min(q)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler_82()
	e = time.clock()
	print "Elapsed: ", (e - s)
