class Point(object) :
	def __init__(self, xx, yy) :
		self.x, self.y = xx, yy
	def __str__(self) :
		return "[%f,%f]" % (self.x, self.y)

def sign(x) :
	return (1 if x > 0 else (-1 if x < 0 else 0))
def calcCrossingY(p1,p2) :
	deltaY = p2.y - p1.y
	deltaX = p2.x - p1.x
	newY = p1.y - (float(p1.x) * (float(deltaY) / float(deltaX)))
	return Point(0.0, newY)
def calcCrossingX(p1,p2) :
	deltaY = p2.y - p1.y
	deltaX = p2.x - p1.x
	newX = p1.x - (float(p1.y) * (float(deltaX) / float(deltaY)))
	return Point(newX, 0.0)

def crossing(p1, p2) :
	c = []
	if sign(p1.x) != sign(p2.x) :
		c.append(calcCrossingY(p1, p2))
	if sign(p1.y) != sign(p2.y) :
		c.append(calcCrossingX(p1, p2))
	return (c if len(c) else None)

def euler102(fileName) :
	f = open(fileName)
	count = 0
	for line in f.readlines() :
		d = [int(a) for a in line.strip().split(",")]
		points = [ Point(d[0], d[1]), Point(d[2], d[3]), Point(d[4], d[5]) ]
		crossings = []
		for first,second in [(0,1), (1,2), (2,0)] :
			b = crossing(points[first], points[second])
			if b :
				for bb in b :
					crossings.append(bb)

		if len(crossings) :
			minX = min(a.x for a in crossings)
			maxX = max(a.x for a in crossings)
			minY = min(a.y for a in crossings)
			maxY = max(a.y for a in crossings)
			print "[%f,%f] [%f,%f]" % (minX,maxX, minY,maxY)
			if minX < 0 and maxX > 0 and minY < 0 and maxY > 0 :
				count += 1
	print count

def testIncludesPoint() :
	pass

if __name__ == "__main__" :
	import sys
	for arg in sys.argv[1 : ] :
		euler102(arg)
	#testIncludesPoint()
