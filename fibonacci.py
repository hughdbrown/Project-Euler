#!/usr/bin/env python

def build_fibber(n) :
	def fibber() :
		a, b = 0, 1
		while True :
			yield [ a + b, a, b ]
			a = a + b
			yield [ a + b, b, a ]
			b = a + b
		return
	d = dict()
	for (c, a, b) in fibber() :
		if c >= n : break
		d[c] = [a, b]
	return d

if __name__ == "__main__" :
	def test_fibber() :
		d = build_fibber(1000 * 1000 * 1000)
		print len(d)
		for k in sorted(d.iterkeys()) :
			print k, d[k]

	test_fibber()
