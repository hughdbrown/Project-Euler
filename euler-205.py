#!/usr/bin/env python
import psyco
psyco.full()

def dice_collection_iterator(count, size) :
	if count == 0 :
		yield []
	else :
		for i in xrange(1, size+1) :
			for c in dice_collection_iterator(count-1, size) :
				yield [i] + c
	return

import collections
pp = collections.defaultdict(int)
for a in dice_collection_iterator(9, 4) :
	pp[sum(a)] += 1
dd = collections.defaultdict(int)
for a in dice_collection_iterator(6, 6) :
	dd[sum(a)] += 1

ppdivisor = sum(k for k in pp.itervalues())
dddivisor = sum(k for k in dd.itervalues())
divisor = ppdivisor * dddivisor

total = sum(v1 * v2 for k1, v1 in pp.iteritems() for k2, v2 in dd.iteritems() if k1 > k2)

print float(total) / float(divisor)
