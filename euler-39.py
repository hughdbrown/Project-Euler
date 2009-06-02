import math
import collections
d = collections.defaultdict(lambda : 0)

for a in range(3, 997) :
	aa = a * a
	for b in range(a+1, 1000-a) :
		bb = b * b
		c = int(math.sqrt(aa + bb))
		p = a+b+c
		if p < 1000 :
			if (c*c == aa+bb):
				d[p] += 1
				print p, a,b,c, d[p]
		else : break
vv = max(d.itervalues())
for k,v in d.iteritems() :
	if v == vv :
		print k
		break

			
		