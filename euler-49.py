import primes
import collections

p = primes.primes(10000)
d = collections.defaultdict(list)
for pp in p :
	if pp > 1000:
		s = str(pp)
		ss = "".join(sorted(s))
		d[ss].append(pp)

#m = max(len(d[key]) for key in d.keys())
for k, v in d.iteritems() :
	for i in range(len(v)) :
		for j in range(i+1, len(v)) :
			diff = v[j] - v[i]
			x = v[j] + diff
			#y = v[j] + 2*diff
			if x in v  :
				print k, v
				print "Found: ", v[i], v[j], x

				

