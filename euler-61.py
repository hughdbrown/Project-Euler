#!/usr/bin/env python


import psyco
psyco.full()

import sys

def triangleNum(n) :
	return n*(n+1)/2
def pentagonNum(n) :
	return n*(3*n-1)/2
def hexagonNum(n) :
	return n*(2*n-1)
def heptagonNum(n) :
	return n*(5*n-3)/2
def octagonNum(n) :
	return n*(3*n-2)

triangles = [ triangleNum(n) for n in range(45, 141) ]
squares = [n*n for n in range(32,100) ]
pentagons = [ pentagonNum(n) for n in range(26,81) ]
hexagons = [ hexagonNum(n) for n in range(23,70) ]
heptagons = [ heptagonNum(n) for n in range(21,64) ]
octagons = [ octagonNum(n) for n in range(19,59) ]

allLists = [triangles, squares, pentagons, hexagons, heptagons, octagons]

def flatten(LL) :
	result = []
	for L in LL :
		result.extend(L)
	return result
def removeImpossibles() :
	for L in allLists :
		removeList = []
		for x in L :
			if (x % 100) < 10 :
				removeList.append (x)
		for y in removeList :
			L.remove(y)

def removeUnmatchableHead() :
	for i, L in enumerate(allLists) :
		otherList = allLists[ : i] + allLists[i+1 : ]
		joined = flatten(otherList)
		removeList = [ x for x in L if not any(y%100 == x/100 for y in joined) ]
		#removeList = []
		#for x in L :
		#	head = str(x)[2 : ]
		#	#if not any(str(y)[ : 2] == head for y in otherList) :
		#	if not any(str(y).endswith(head) for y in otherList) :
		#		#print "Removing ", x, " from ", L
		#		removeList.append (x)
		for y in removeList :
			L.remove(y)

def removeUnmatchableTail() :
	for i, L in enumerate(allLists) :
		otherList = allLists[ : i] + allLists[i+1 : ]
		joined = flatten(otherList)
		removeList = [x for x in L if not any(y/100 == x%100 for y in joined) ]
		#removeList = []
		#for x in L :
		#	tail = str(x)[ : 2]
		#	#if not any(str(y)[2 : ] == tail for y in otherList) :
		#	if not any(str(y).startswith(tail) for y in otherList) :
		#		#print "Removing ", x, " from ", L
		#		removeList.append (x)
		for y in removeList :
			L.remove(y)

def removeUnstringable() :
	for i, L in enumerate(allLists) :
		otherList = allLists[ : i] + allLists[i+1 : ]
		joined = flatten(otherList)
		for x in L :
			tail = x%100
			head = x/100
			if (not any(y/100 == tail for y in joined)) or (not any(y%100 == head for y in joined)) :
				L.remove(x)

def printLists () :
	for L in allLists :
		print L
	print "----"
def printListLen() :
	for L in allLists :
		print len(L)
	print "----"

printListLen()
removeImpossibles()
printListLen()

for j in range(2) :
	removeUnmatchableHead()
	removeUnmatchableTail()
	removeUnstringable()
	printListLen()
	#printLists()

solutions = set()
for i,L1 in enumerate(allLists) :
	for ii in L1 :
		h1 = ii / 100
		t1 = ii % 100
		for j,L2 in enumerate(allLists) :
			if j in [i] : continue
			for jj in L2 :
				h2 = jj / 100
				t2 = jj % 100
				if t1 == h2 :
					for k,L3 in enumerate(allLists) :
						if k in [i,j] : continue
						for kk in L3 :
							h3 = kk / 100
							t3 = kk % 100
							if t2 == h3 :
								for m,L4 in enumerate(allLists) :
									if m in [i,j,k] : continue
									for mm in L4 :
										h4 = mm / 100
										t4 = mm % 100
										if t3 == h4 :
											for n,L5 in enumerate(allLists) :
												if n in [i,j,k,m] : continue
												for nn in L5 :
													h5 = nn / 100
													t5 = nn % 100
													if t4 == h5 :
														for p,L6 in enumerate(allLists) :
															if p in [i,j,k,m,n] : continue
															for pp in L6 :
																h6 = pp / 100
																t6 = pp % 100
																if t5 == h6 :
																	if t6 == h1 :
																		if (ii, jj, kk, mm, nn, pp) not in solutions :
																			solutions.add( (ii, jj, kk, mm, nn, pp) )
																			#print
																			print ii, jj, kk, mm, nn, pp
