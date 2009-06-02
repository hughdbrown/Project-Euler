from __future__ import with_statement

import psyco
psyco.full()

def powerset(s) :
	length = len(s)
	for i in xrange(1, 1 << length) :
		yield [c for j, c in enumerate(s) if (1 << j) & i]
	return

def isSpecialSet(s) :
	for i in xrange(1,1+len(s)/2) :
		left, right = s[:i+1], s[-i:]
		if len(left) <= len(right) :
			break
		if sum(left) <= sum(right) :
			print left, right
			return False
	sset = set(s)
	for a in powerset(s) :
		diff = sset - set(a)
		suma = sum(a)
		for b in powerset(diff) :
			if suma == sum(b) :
				print suma, sorted(a), sorted(b)
				return False	
	return True

def test() :
	total = 0
	with open("sets-105.txt") as f :
		for line in f :
			print "-----"
			a = sorted(int(d) for d in line.strip().split(","))
			if isSpecialSet(a) :
				#print "Special: ", a
				total += sum(a)
			else :
				print "Not special: ", a
	print total

test()
