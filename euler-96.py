import psyco
psyco.full()

import Queue
import sys
import powerset

row = [None] * 9
col = [None] * 9
box = [None] * 9
neighbors = [None] * 81

def CandidateToRCB(c) :
	rowNum, colNum = c / 9, c % 9
	boxNum = 3 * (rowNum/3) + colNum/3
	return (rowNum, colNum, boxNum)

def setup() :
	for i in range(9) :
		row[i] = range(i*9,i*9+9)
		col[i] = range(i,81, 9)

	box[0] = [0,1,2,9,10,11,18,19,20]
	for i in range(1, 3) :
		box[i] = [(i*3 + a) for a in box[0] ]
	for i in range(6) :
		x = i % 3
		incr = (i / 3) + 1
		box[i+3] = [(incr*27 + a) for a in box[x] ]

	for me in range(0,81) :
		rn, cn, bn = CandidateToRCB(me)
		neighbors[me] = set(row[rn] + col[cn] + box[bn])
		neighbors[me].remove(me)

class Sudoku(object) :
	def __init__(self, a) :
		self.values = a
		self.unsolved = a.count(0)
		self.q = self.PopulatedQueue()
		self.possibleValues = [ self.Possibles(i) for i in range(81) ]
	def ScoreRowColBox(self, rcb) :
		#return sum((1 if self.values[x] == 0 else 0) for x in rcb)
		b = [self.values[x] for x in rcb]
		return b.count(0)
	def Score(self, s) :
		return [ self.ScoreRowColBox(a) for a in s ]
	def PopulatedQueue(self) :
		q = Queue.Queue()
		r = self.SortCandidates(n for n in range(81) if self.values[n] == 0)
		for n in r :
			q.put(n)
		return q
	def AppendToQueue(self, c) :
		#assert (self.values[c] == 0)
		self.q.put(c)
	def SortCandidates(self, s) :
		r = []
		for n in s :
			rn,cn,bn = CandidateToRCB(n)
			rc = self.ScoreRowColBox(row[rn])
			cc = self.ScoreRowColBox(col[cn])
			bc = self.ScoreRowColBox(box[bn])
			t = ( min(rc, cc, bc), n )
			r.append(t)
		return [ n for _, n in sorted(r) ]

	def AppendCandidatesToQueue(self, s) :
		r = self.SortCandidates(s)
		for n in r :
			self.AppendToQueue(n)

	def SetCandidate(self, c, v) :
		#print "Before", c, v
		#self.Print()
		#print self.values[c]
		#print self.possibleValues[c]

		rn, cn, bn = CandidateToRCB(c)

		self.values[c] = v
		self.possibleValues[c] = [v]
		for a in neighbors[c] :
			if v in self.possibleValues[a] :
				self.possibleValues[a].remove(v)

		more_candidates = []
		rc = self.ScoreRowColBox(row[rn])
		if rc == 1 :
			n = [ x for x in row[rn] if self.values[x] == 0 ]
			xx = n[0]
			more_candidates.append(xx)

		cc = self.ScoreRowColBox(col[cn])
		if cc == 1 :
			n = [ x for x in col[cn] if self.values[x] == 0 ]
			xx = n[0]
			more_candidates.append(xx)

		bc = self.ScoreRowColBox(box[bn])
		if bc == 1 :
			n = [ x for x in box[bn] if self.values[x] == 0 ]
			xx = n[0]
			more_candidates.append(xx)

		for affected in neighbors[c] :
			if self.values[affected] == 0 :
				more_candidates.append(affected)
		self.AppendCandidatesToQueue(more_candidates)

		#print "After"
		#for m in more_candidates :
		#	print m, self.possibleValues[m]
		#self.Print()
		#print self.values[c]
		#print self.possibleValues[c]

	def Solved(self) :
		return (self.values.count(0) == 0)
	def AllRelated(self, rcb, rcbNum) :
		return [ x for x in rcb[rcbNum] if self.values[x] == 0 ]
	def OtherValues(self, others) :
		return [ self.possibleValues[cn] for cn in others ]
	def ComplementSet(self,others, i) :
		return [ elem for k, elem in enumerate(others) if not ((1 << k) & i) ]
	def SetOfPossibleValues(self,r) :
		s = set()
		for j in r :
			for x in self.possibleValues[j] :
				s.add(x)
		return s
	def UsingSameBox(self, r) :
		boxes = [ CandidateToRCB(c) for c in r ]
		return all(bn == boxes[0] for bn in boxes)
	def UsingSameRow(self, r) :
		rows = [ self.CandidateToRCB(c) for c in r ]
		return all(rn == rows[0] for rn in rows)
	def UsingSameCol(self, r) :
		cols = [ self.CandidateToRCB(c) for c in r ]
		return all(cn == cols[0] for cn in cols)
	def RemoveTriples(self, rcb, rcbNum, twins) :
		i = 0
		sameBox = self.UsingSameBox(twins)
		# r is a powerset of integers (square numbers) for squares in a region that are not filled
		for r in powerset.powerset(twins) :
			if 1 < len(r) < len(twins) :
				others = self.AllRelated(rcb, rcbNum)
				cs = self.ComplementSet(others, i)
				rv = self.SetOfPossibleValues(r)
				csv = self.SetOfPossibleValues(cs)
	# This removes twins, triples, etc.
	def SolveOthers(self, rcb, rcbNum) :
		others = self.AllRelated(rcb, rcbNum)
		i = 0
		# r is a powerset of integers (square numbers) for squares in a region that are not filled
		for r in powerset.powerset(others) :
			if 0 < len(r) < len(others) :
				# s is a set of the possible values of squares indexed by r
				s = self.SetOfPossibleValues(r)
				if len(s) == len(r) :
					cs = self.ComplementSet(others, i)
					for c in cs :
						valuesToRemove = s.intersection(set(self.possibleValues[c]))
						if len(valuesToRemove) :
							for ss in valuesToRemove :
								self.possibleValues[c].remove(ss)
							self.AppendToQueue(c)
					if len(r) >= 3 :
						self.RemoveTriples(rcb, rcbNum, r)
			i += 1
	def Solve(self) :
		while (not self.q.empty()) and (not self.Solved()) :
			#for i in range(81) :
			#	solved = (self.values[i] != 0)
			#	if solved :
			#		if len(self.possibleValues[i]) != 1 :
			#			print "Error on %d" % i
			#			return
			c = self.q.get()
			p = self.possibleValues[c]
			if len(p) == 1 :
				self.SetCandidate(c, p[0])
			else :
				rn, cn, bn = CandidateToRCB(c)
				self.SolveOthers(row, rn)
				self.SolveOthers(col, cn)
				self.SolveOthers(box, bn)
		if not self.Solved() :
			print "Not solved: %d" % self.values.count(0)
			self.NotSolvedPrint()
	def Print(self) :
		for rowNum in range(9) :
			print rowNum, self.values[rowNum*9: rowNum*9+9]
		print
	def NotSolvedPrint(self) :
		self.Print()
		for i in range(81) :
			if len(self.possibleValues[i]) > 1 :
				print i, CandidateToRCB(i), self.possibleValues[i]
	def Possibles(self,c) :
		global row, col, box, neighbors
		if self.values[c] != 0 :
			return [ self.values[c] ]
		else :
			allValues = range(1,10)
			p = set(allValues)
			discardable = [ self.values[n] for n in neighbors[c] if self.values[n] != 0 ]
			p -= set(discardable)
			return [x for x in sorted(p)]

def loadSudoku(f) :
	header = f.readline()
	if not header :
		return None
	else :
		a = []
		for i in range(9) :
			line = f.readline().strip()
			for c in line:
				a.append(int(c))
		s = Sudoku(a)
		return s

def euler96(fileName) :
	print fileName
	f = open(fileName)
	i = 1
	while (1) :
		s = loadSudoku(f)
		if not s: break
		else:
			print "Puzzle %d" % i
			s.Solve()
		i += 1

if __name__ == "__main__" :
	setup()
	#euler96("sudoku-96.txt")
	euler96("sudoku-unsolved.txt")
	#euler96("sudoku.txt")
