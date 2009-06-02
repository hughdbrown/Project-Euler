import primes
import sys

count = 0

def _expandByTail(results, i, pp, limit) :
	global count
	prev, next = i, i * pp
	while next <= limit :
		assert (results[next] == 0)
		assert (results[prev] != 0)
		results[next] = results[prev] * pp
		#print "_expandByTail(%d,%d)" % (next, results[next])
		count += 1
		prev, next = next, next * pp

def _expandBy(results, i, pp, limit) :
	global count
	assert (results[i] == 0)
	results[i] = results[pp]
	#print "_expandBy(%d,%d)" % (i, results[i])
	count += 1
	_expandByTail(results, i, pp, limit)

def _expand(results, i, p, limit) :
	assert(0 == results[i])
	for pp in p :
		assert(pp < i)
		if i % pp == 0 :
			_expandBy(results, i, pp, limit)
			break
	assert(0 != results[i])

def _expandComposite(results, i, p, limit) :
	global count
	assert(0 == results[i])
	for pp in p :
		assert(pp < i)
		if i % pp == 0 :
			if (i/pp) % pp == 0 :
				results[i] = results[i/pp] * pp
			else :
				results[i] = results[i/pp] * results[pp]
			#print "_expandComposite(%d,%d)" % (i, results[i])
			count += 1
			break
	assert(0 != results[i])

def expandPrimes(results, p, limit) :
	global count
	print
	print >> sys.stderr, "Expand primes"
	for pp in p :
		if pp > limit : break
		print >> sys.stderr, pp, count, "\r",
		assert(results[pp] == 0)
		results[pp] = pp - 1
		count += 1
		_expandByTail(results, pp, pp, limit)

def expandComposites(results, p, limit) :
	global count
	print
	print >> sys.stderr, "Expand composites"
	for i in range(len(p)) :
		pi = p[i]
		print >> sys.stderr, pi, count, "\r",
		if pi*2 > limit: break
		for j in range(i+1, len(p)) :
			pj = p[j]
			pipj = pi*pj
			if pipj <= limit :
				assert(results[pi] != 0)
				assert(results[pj] != 0)
				assert(results[pipj] == 0)
				results[pipj] = results[pi] * results[pj]
				#print "Expand composites(%d,%d)" % (pipj, results[pipj])
				count += 1
				_expandByTail(results, pipj, pi, limit)
				_expandByTail(results, pipj, pj, limit)
			else : break

def expandEverythingElse(results, p, limit) :
	global count
	print
	print >> sys.stderr, "Expand everything else"
	for i in range(2,len(results)) :
		if results[i] == 0:
			print >> sys.stderr, i, count, "\r",
			_expandComposite(results, i, p, limit)

def euler72(limit) :
	global count
	print "*** %d" % limit
	count = 0
	p = primes.primes(limit+1)
	results = [0] * (limit+1)
	expandPrimes(results, p, limit)
	expandComposites(results, p, limit)
	expandEverythingElse(results, p, limit)

	print
	print [i for i,x in enumerate(results) if x == 0 and i >= 2]
	#for i,x in enumerate(results) :
	#	print i, x
	return sum(results)

def test_euler72() :
	a = [[5,9], [6,11], [7,17], [8,21], [9, 27], [10, 31], \
		[11, 41], [12,45], [13,57], [14,63], [15,71], [16,79], [17,95], [18,101], [19,119], [20,127], \
		[21,139], [22,149], [23, 171], [24, 179], [25, 199], [26, 211], [27, 229], [28, 241], [29, 269], \
		[30, 277], [31, 307], [32, 323], [33, 343], [34, 359], [35, 383], [36, 395], \
		[1000, 304191]]
	for r in a :
		result = euler72(r[0])
		if result != r[1] :
			print "%d: expecting %d, got %d" % (r[0], r[1], result)
		else : print "Success: %d" % r[0]

if __name__ == "__main__" :
	#test_euler72()
	r = euler72(1000*1000)
	#r = euler72(1000)
	print
	print r
