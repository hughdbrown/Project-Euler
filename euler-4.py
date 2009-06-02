#!/usr/bin/env python

#for i in range(999, 100, -1) :
#	s = str(i)
#	rs = s[2] + s[1] + s[0]
#	print int(s + rs)

def palindrome(x) :
	y = str(x)
	return (len(y) == 6 and (y[0] == y[5] and y[1] == y[4] and y[2] == y[3]))

pal = []
for i in range(100, 1000) :
	print i
	for j in range(i, 1000) :
		x = i * j
		if palindrome(x) :
			pal.append(x)
pp = sorted(pal)
print pp[-1]
