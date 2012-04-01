#!/usr/bin/env python
def squares(r) :
	return [a * a for a in r]

a = sum (range(1, 101))
a2 = a * a
b = squares(range(1, 101))
b2 = sum(b)

print a2, b2, b2 - a2