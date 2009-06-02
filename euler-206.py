#!/usr/bin/env python

import psyco
psyco.full()

d = 10203040506070809

[0,1,2,3,4,5,6,7,8,9]
[0,1,2,3,4,5,6,7,8,9]
[0,1,2,3,4,5,6,7,8,9]
[0,2,4,6,8]
for i in xrange(100*1000*1000) :
	s = "".join((d + "0") for d in "%08d" % i)
	candidate = d + int(s)
	r = int(candidate ** 0.5)
	if r * r == candidate :
		print s
		break

for i in xrange(1000*1000*100,1000*1000*1000) :
	if  str(i)[-1] in "37" :
		j = i * i
		sj = str(j)
		if sj[-1] == "9" and sj[-3] == "8" and sj[-5] == "7" and sj[-7] == "6" and sj[-9] == "5" and sj[-11] == "4" and sj[-13] == "3" and sj[-15] == "2"  and sj[-17] == "1":
			print j

