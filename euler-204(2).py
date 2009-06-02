#!/usr/bin/env python

class LazyList:
	def __init__(self, g):
		self.sofar = []
		self.fetch = g.next

	def __getitem__(self, i):
		sofar, fetch = self.sofar, self.fetch
		while i >= len(sofar):
			sofar.append(fetch())
		return sofar[i]

def times(n, g):
	for i in g:
		yield n * i

def merge(g, h):
	ng = g.next()
	nh = h.next()
	while 1:
		if ng < nh:
			yield ng
			ng = g.next()
		elif ng > nh:
			yield nh
			nh = h.next()
		else:
			yield ng
			ng = g.next()
			nh = h.next()

def m235():
	yield 1
	# Gack:  m235 below actually refers to a LazyList.
	me_times2 = times(2, m235)
	me_times3 = times(3, m235)
	me_times5 = times(5, m235)
	for i in merge(merge(me_times2, me_times3), me_times5):
		yield i

m235 = LazyList(m235())
limit = 100*1000*1000
i = 0
while m235[i] <= limit :
	#print m235[i]
	i += 1
print i
