#!/usr/bin/env python
#!/usr/bin/env python
import psyco
psyco.full()

import sys

class Point(object) :
	def __init__(self, _x, _y) :
		self.x, self.y = _x, _y
	def square(self) :
		return self.x**2 + self.y**2
	def squareDist(self, p2) :
		return (self.x-p2.x)**2 + (self.y-p2.y)**2
	def __str__(self) :
		return "[%d,%d]" % (self.x, self.y)
	def __cmp__(self, other) :
		if self.x == other.x and self.y == other.y :
			return 0
		else :
			return 1

def pointIterator(limit) :
	for i in range(limit+1) :
		for j in range(limit+1) :
			yield Point(i, j)
	return

def euler91(limit) :
	#origin = limit*limit
	#right = limit*limit
	#left = limit*limit
	#diagonal = limit
	#return origin + left + right + diagonal
	origin = Point(0,0)
	count = 0
	for p1 in pointIterator(limit) :
		if p1 == origin : continue
		for p2 in pointIterator(limit) :
			if p2 == origin : continue
			if p1 != p2 :
				pyth = [ p1.square(), p2.square(), p1.squareDist(p2) ]
				pyth.sort()
				if pyth[0] + pyth[1] == pyth[2] :
					print >> sys.stderr, p1, p2, count, "\r",
					count += 1
	return count / 2

if __name__ == "__main__" :
	c = euler91(50)
	#c = euler91(2)
	print
	print c

