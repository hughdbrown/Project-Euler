#!/usr/bin/env python
import psyco
psyco.full()

import decimal

def euler80(limit) :
	sq = int(limit ** 0.5)
	s = set(range(limit)) - set(x*x for x in range(sq))
	decimal.getcontext().prec = 105
	ds = 0
	for i in sorted(s) :
	#for i in [2] :
		d = decimal.Decimal(i)
		sqrt_d = d.sqrt()
		s = str(sqrt_d).replace(".", "")[ : 100]
		ds += sum(int(c) for c in s)
		print i, sqrt_d, s
	return ds
	# 1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327
	# 1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501

if __name__ == "__main__" :
	#test_euler72()
	#c = euler72(1000*1000)
	c = euler80(100)
	print
	print c

