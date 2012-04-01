from __future__ import with_statement

import psyco
psyco.full()

with open ("matrix-82.txt") as f:
	lines = [ line.strip().split(",") for line in f.readlines() ]

q = {}
for i in xrange(159) :
	for j in xrange(0,i+1) :
		x, y = j, i - j
		if (0 <= x < 80) and (0 <= y < 80) :
			if x == 0 and y == 0:
				z = 0
			elif x == 0 :
				z = q[x,y-1]
			elif y == 0 :
				z = q[x-1,y]
			else :
				z = min(q[x-1,y], q[x, y-1])
			q[x,y] = z + int(lines[x][y])
print q[79,79]
