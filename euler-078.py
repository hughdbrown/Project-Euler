import psyco

psyco.full()

import collections
i = 2
q = collections.defaultdict(int)
q[1,1] = 1
while 1 :
	total = 0
	for j in xrange(1, i+1) :
		if j in (1, i, i-1) :
			x = 1
		elif j == 2 :
			x = i / 2
		else :
			if q[i, j, "all"] == 0 :
				q[i, j, "all"] = sum(q[i-j, k] for k in xrange(1, min(j, i-j)+1))
			x = q[i, j, "all"]
		q[i,j] = x
		total += x
		total %= 1000000
		#print i, j, x
	print i, total
	if total % 1000000 == 0 :
		break
	i += 1

			
