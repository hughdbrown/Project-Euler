def spanningSet(s) :
	#print s
	if not len(s) :
		yield []
	else :
		ss = set(s)
		for i in xrange(1, len(s)+1) :
			for c in choose(s, i) :
				rest = [x for x in (ss - set(c)) ]
				for sp in spanningSet(rest) :
					yield [c] + sp
	return

def choose(s, n) :
	if n == 0:
		yield []
	else :
		for i,c in enumerate(s) :
			rest = s[i+1:]
			for ch in choose(rest, n-1) :
				yield [c] + ch
	return

def testChoose(s) :
	for ch in choose(s, 1) :
		print ch
	for ch in choose(s, 2) :
		print ch
	for ch in choose(s, 3) :
		print ch
	for ch in choose(s, 4) :
		print ch

def testSpanningSet(s) :
	a = sorted(sorted(ss) for ss in spanningSet(s))
	for i,aa in enumerate(a) :
		print i, aa

if __name__ == "__main__" :
	s = [1,2,3,4]
	#s = "1234"
	testSpanningSet(s)

"""
1 2 3 4
1 2 34
1 23 4
1 3 24
12 3 4
13 2 4
14 2 3
12 34
13 24
14 23
123 4
124 3
134 2
234 1
1234
"""
"""
123
1 2 3
1 23
12 3
13 2
1 2 3
"""
"""
12
1 2
"""
"""
f(1) = 1
f(2) = 2
f(3) = 6
f(4) = 15
"""
