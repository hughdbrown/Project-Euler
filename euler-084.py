#!/usr/bin/env python
import psyco
psyco.full()

die_size = 4


class square(object) :
	def __init__(self, name, square_type) :
		self.name = name
		self.square_type = square_type


squares = [
	square("GO", ""),
	square("A1", "prop"),
	square("CC1", "CC"),
	square("A2", "prop"),
	square("T1", ""),
	square("R1", "RR"),
	square("B1", "prop"),
	square("CH1", "CH"),
	square("B2", "prop"),
	square("B3", "prop"),

	square("JAIL", "J"),
	square("C1", "prop"),
	square("U1", "U"),
	square("C2", "prop"),
	square("C3", "prop"),
	square("R2", "RR"),
	square("D1", "prop"),
	square("CC2", "CC"),
	square("D2", "prop"),
	square("D3", "prop"),

	square("FP", ""),
	square("E1", "prop"),
	square("CH2", "CH"),
	square("E2", "prop"),
	square("E3", "prop"),
	square("R3", "RR"),
	square("F1", "prop"),
	square("F2", "prop"),
	square("U2", "U"),
	square("F3", "prop"),

	square("GTJ", "GTJ"),
	square("G1", "prop"),
	square("G2", "prop"),
	square("CC3", "CC"),
	square("G3", "prop"),
	square("R4", "prop"),
	square("CH3", "CH"),
	square("H1", "prop"),
	square("T2", ""),
	square("H2", "prop"),
]

def search_square(s) :
	for i in xrange(40) :
		if s == squares[i].name :
			return i
	print "Something bad: %s" % s
	return -1

JAIL = search_square("JAIL")
GO = search_square("GO")
BOARDWALK = search_square("H2")
STCHARLES = search_square("C1")
READING = search_square("R1")
ILLINOIS = search_square("E3")
GTJ = search_square("GTJ")


def roll(n) :
	import random
	return random.randint(1,n)

def CC(position) :
	import random
	r = random.randint(1,16)
	if r == 1 :
		return GO
	elif r == 2 :
		return JAIL
	else :
		return position

def nextRailroad(position) :
	while (squares[position].square_type != "RR") :
		position = (position + 1) % 40
	return position

def nextUtility(position) :
	while (squares[position].square_type != "U") :
		position = (position + 1) % 40
	return position

def CH(position) :
	import random
	r = random.randint(1,16)
	if r == 1 :
		return GO
	elif r == 2 :
		return JAIL
	elif r == 3 :
		return STCHARLES
	elif r == 4 :
		return ILLINOIS
	elif r == 5 :
		return BOARDWALK
	elif r == 6 :
		return READING
	elif r in [7, 8] :
		return nextRailroad(position)
	elif r == 9 :
		return nextUtility(position)
	elif r == 10 :
		return (position - 3) % 40
	else :
		return position



outcome = [0] * 40
position = 0
turns = 100*1000*1000
rolls = [0] * (2 * die_size + 1)

def visit(pos) :
	outcome[pos] += 1

jail_doubles = 0
visit(0)
for i in xrange(turns + 1) :
	for j in xrange(3) :
		d1, d2 = roll(die_size), roll(die_size)
		if not (1 <= d1 <= die_size and 1 <= d2 <= die_size) :
			print "something bad"
		rolls[d1+d2] += 1

		double = (d1 == d2)
		if double and j == 2:
			visit(JAIL)
			position = JAIL
			jail_doubles += 1
			break
		else :
			new_pos = (position + d1 + d2) % 40

		if squares[new_pos].square_type == "CH" :
			new_pos2 = CH(new_pos)
			if new_pos2 != new_pos :
				visit(new_pos2)
				new_pos = new_pos2
			else :
				visit(new_pos)
		elif squares[new_pos].square_type == "CC" :
			new_pos2 = CC(new_pos)
			if new_pos2 != new_pos :
				visit(new_pos2)
				new_pos = new_pos2
			else :
				visit(new_pos)
		elif squares[new_pos].square_type == "GTJ" :
			#visit(new_pos)
			visit(JAIL)
			position = JAIL
			break
		else :
			position = new_pos
			visit(position)

		if not double :
			break

print outcome
print sum(outcome)

a = [ (outcome[i], squares[i].name, i) for i in xrange(40) ]
b = sorted(a)
b.reverse()
for x in b :
	print x

for i, r in enumerate(rolls) :
	if i > 0:
		print i, r

print "Jail doubles: %d" % jail_doubles
