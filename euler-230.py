#!/usr/bin/env python
import psyco
psyco.full()

def build_fibber(n) :
	def fibber() :
		a, b, i = 0, 1, 0
		while True :
			yield [ a + b, a, b, i ]
			a = a + b
			i += 1
			yield [ a + b, b, a, i ]
			b = a + b
			i += 1
		return
	d = dict()
	for (c, a, b, i) in fibber() :
		if c >= n : break
		d[c] = [a, b, i]
	return d

def find(d, n) :
	for k in sorted(d.iterkeys()) :
		if k > n :
			x = k
			break

	i = 0
	while n != 0 :
		left, right, i = d[x]
		if n < left :
			x = left
		else :
			n -= left
			x = right
	return i & 1

def find_digit_alt(dd) :
	#    123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
	A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
	B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
	result = [ A, B ]
	while (len(result[-1]) <= dd) :
		result.append(result[-2] + result[-1])
	return result[-1][dd]

def find_digit(d, dd) :
	#    123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
	A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
	B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
	div, rem = dd / 100, dd % 100
	j = find(d, div)
	digit = (A[rem] if j == 0 else B[rem])
	return digit

def test1() :
	digits = [ (127 + 19 * n) * 7**n for n in xrange(18) ]
	d = build_fibber(digits[-1])
	result = ""
	for i in xrange(101, 1000) :
		print i
		a = find_digit(d, i)
		b = find_digit_alt(i)
		if a != b :
			print i, a, b
	print "Done!"

def test2() :
	digits = [ (127 + (19 * n)) * (7**n) for n in xrange(18) ]
	d = build_fibber(digits[-1])
	result = ""
	for i, dd in enumerate(digits) :
		digit = find_digit(d, dd-1)
		result = digit + result
	print result

if __name__ == "__main__" :
	import time
	s = time.clock()
	#test1()
	test2()
	e = time.clock()
	print "Elapsed: %f" % (e - s)

