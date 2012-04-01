from __future__ import division

import psyco

psyco.full()

def operators() :
	s = ('+', '-', '*', '/')
	for i in s :
		for j in s :
			for k in s :
				yield i + j + k

def apply_op(x, y, op) :
	if   op == '+' : return x + y
	elif op == '-' : return x - y
	elif op == '*' : return x * y
	elif op == '/' : return float(x) / float(y)
	else           : raise "Bad op"

def eval_stack(s) :
	import copy
	#aa = copy.deepcopy(s)
	ss = []
	try :
	 	while len(s) :
			a, s = s[0], s[1 : ]
			if a in "+-/*" :
				x = ss.pop()
				y = ss.pop()
				z = apply_op(x, y, a)
				ss.append(z)
			else :
				ss.append(int(a))
		assert (len(ss) == 1)
		return (ss[0] if (ss[0] == int(ss[0])) else -1)
	except ZeroDivisionError, detail:
		#print 'Handling run-time error: ', detail
		pass
	except Exception, e :
		#print "Exception: ", e
		pass
	return -1

def generator_iter(s) :
	for i, elem in enumerate(s) :
		yield s[:i], elem, s[i+1:]

def permute(s) :
	if not len(s) :
		yield []
	else :
		for left, elem, right in generator_iter(s) :
			rest = left + right
			for x in permute(rest) :
				yield [elem] + x

def build_pattern(digits, ops, p) :
	result = []
	x, y = 0, 0
	for i in xrange(7) :
		if i in p :
			result.append(digits[x])
			x += 1
		else :
			result.append(ops[y])
			y += 1
	return "".join(result)

def eval_set(s) :
	import sys
	print >> sys.stderr, s, "\r",
	patterns = [[0,1,2,3], [0,1,2,4], [0,1,2,5], [0,1,3,4], [0,1,3,5], [0,1,4,5]]
	d = set()
	for ops in operators() :
		for p in patterns :
			for digits in permute(s) :
				ss = build_pattern(digits, ops, p)
				x = eval_stack(ss)
				if x > 0 :
					d.add(x)
	return sorted(d)

def score(d) :
	if not len(d) :
		return 0
	else :
		i = 1
		for e in d :
			if e != i :
				return i - 1
			i += 1
		return i

def digit_set() :
	for i in range(1,10) :
		for j in range(i+1, 10) :
			for k in range(j+1, 10) :
				for l in range(k+1, 10) :
					yield "".join(str(x) for x in (i, j, k, l))
	return

def big_test() :
	best_score, best = 0, [0,0,0,0]
	for t in digit_set() :
		x = eval_set(t)
		xs = score(x)
		if xs > best_score :
			print "-----"
			print xs, t, x
			best_score, best = xs, t
	print best_score, best

def small_test() :
	x = eval_set("5689")

if __name__ == "__main__" :
	import time
	s = time.clock()
	big_test()
	#small_test()
	e = time.clock()
	print "Elapsed: %f" % ( e - s)

