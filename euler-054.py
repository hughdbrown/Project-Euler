#!/usr/bin/env python

ranks = { "A":14, "K":13, "Q":12, "J":11, "T":10}
for i in range(2, 11) :
	ranks[str(i)] = i

class Card(object) :
	def __init__(self, s) :
		self.suit = s[1]
		self.rank = ranks[s[0]]
	def Rank(self) :
		return self.rank
	def Suit(self) :
		return self.suit
	def __str__(self) :
		return "%d.%s" % (self.Rank(), self.Suit())
class PokerHand(object) :
	def __init__(self, c) :
		self.cards = c
	def __cmp__(self, other) :
		return cmp(self.eval(), other.eval())
	def __str__(self) :
		return ",".join(str(c) for c in self.cards)
	def Flush(self) :
		for i in range(1, 5) :
			if self.cards[i].Suit() != self.cards[0].Suit() :
				return False
		return True
	def eval(self) :
		r = [c.Rank() for c in self.cards]
		r = sorted(r)
		flush = self.Flush()

		d = {}
		for rr in r :
			if not d.has_key(rr) :
				d[rr] = 1
			else :
				d[rr] += 1
		kind = max(d.itervalues())
		rr2 = [k for k, v in d.items() if v == 2]
		rr3 = [k for k, v in d.items() if v == 3]
		rr1 = [k for k, v in d.items() if v == 1]

		straight = ((min(r)+4) == max(r)) and (len(rr1) == 5)

		if flush :
			if min(r) == 10 and max(r) == 14 :
				print "Royal Flush"
				return 1000 # Royal Flush
			elif straight :
				print "Straight Flush"
				return 900 + min(r) # Straight Flush
			else :
				print "Flush"
				return 600
		elif straight :
			print "Straight"
			return 500 + min(r) # Straight
		else :
			if kind == 4 :
				print "Four of a kind"
				return 800 + max(r) # Four of a kind
			elif kind == 3 :
				if len(rr2) == 1 :
					print "Full house"
					return 700 + rr3[0] # Full house
				else :
					print "Three of a kind"
					return 400 + rr3[0] # Three of a kind
			elif kind == 1 :
				print "High card"
				return 100 + max(r)	# High card
			else :
				if len(rr2) == 2 :
					print "Two pair"
					return 300 + rr2[1]	# Two pair
				else :
					print "One pair"
					return 200 + rr2[0]	# One pair


if __name__ == "__main__" :
	f = open ("poker.txt")
	w1, w2 = 0, 0
	for line in f.readlines() :
		print line.rstrip()
		cards = [ Card(a) for a in line.split(' ') ]
		h1 = PokerHand(cards[0 : 5])
		h2 = PokerHand(cards[5 : 10])
		e1, e2 = h1.eval(), h2.eval()
		if (e1 > e2) :
			w1 += 1
		elif (e1 < e2) :
			w2 += 1
		else :
			print e1, h1, e2, h2
	print w1

