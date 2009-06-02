#!/usr/bin/env python
import math

class Convergent(object) :
	def __init__(self, root, whole, add, div) :
		self.root, self.whole, self.add, self.div = root, whole, add, div
		self.int_root = int(math.sqrt(self.root))
	def reduce(self) :
		if self.whole == 0 :
			whole = self.int_root
			add = - whole
			div = 1
		else :
			div = self.root - self.whole ** 2
			neg_add = - self.add
			whole = (self.root + neg_add) / div
			add = neg_add - (div * whole)
		return Convergent(self.root, whole, add, div)
	def __str__(self) :
		if self.whole == 0 :
			return "sqrt(%d)" % self.root
		else :
			return "%d + 1/(sqrt(%d) + %d)/%d" % (self.whole, self.root, self.add, self.div)

c = Convergent(23, 0, 0, 1)
print c

d = c.reduce()
print d

e = d.reduce()
print e

