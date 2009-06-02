#!/usr/bin/env python

import psyco
psyco.full()

import sys

def combinationIterator(y) :
	if not len(y) :
		yield []
	else :
		for i in range(len(y)) :
			x = y[i]
			rest = y[ : i] + y[i+1 : ]
			for z in combinationIterator(rest) :
				yield [x] + z
	return
def scoreSolution(a, scoreCard) :
	b = [ a[sc[0]] + a[sc[1]] + a[sc[2]] for sc in scoreCard ]
	return all(bb == b[0] for bb in b), b[0]
def printSolution(a, scoreCard) :
	i = a.index(min(a[:5]))
	result = "".join([str(a[s]) for j in range(5) for s in scoreCard[(j + i) % 5]])
	print result

def euler68() :
	a = [0] * 10
	a[0] = 10
	scoreCard = [[0,5,9],[1,6,5],[2,7,6],[3,8,7],[4,9,8]]

	j = 0
	for i in combinationIterator(range(1,10)) :
		a = [10] + i
		t = scoreSolution(a, scoreCard)
		if t[0]:
			print t[1], a
			printSolution(a, scoreCard)
			print
		#for k in range(5) :
		#	a = i[:k] + [10] + i[k: ]
		#	#print >> sys.stderr, a, "\r",
		#	t = scoreSolution(a, scoreCard)
		#	if t[0]:
		#		print t[1], a
		#		printSolution(a, scoreCard)
		#		print
		#	#a = i + [10]
		#	#if scoreSolution(a, scoreCard) :
		#	#	print a
		#	#	printSolution(a, scoreCard)
		#	#	print
		j += 1
	print
	print j

def test() :
	for i in combinationIterator(range(1,5)) :
		print i

if __name__ == "__main__" :
	euler68()
	#test()
