import primes

def truncate_left(n) :
	ns = str(n)
	for i in range(len(ns)) :
		yield ns[i : ]

def truncate_right(n) :
	ns = str(n)
	for i in range(len(ns)) :
		yield ns[0 : len(ns)-i]

def test_truncate() :
	for a in truncate_left("123456") :
		print a
	for a in truncate_right("123456") :
		print a

def remove_candidates(cand, h) :
	r = []
	for k in cand :
		ss = str(k)
		if len(ss) > 2 :
			for c in ss :
				if c in "02468" :
					r.append(k)
					break
			else :
				if ss[0:2] not in h or ss[-2:] not in h :
					r.append(k)
				elif ss[0] == "19" or ss[-1] in "19":
					r.append(k)
	r.reverse()
	return r

def euler_37() :
	x = primes.primes(2000000)
	cand = dict.fromkeys (x[4 : ], 1 )
	h = [ str(p) for p in x[0:100] if 10 < p < 100 ]

	for k in remove_candidates(cand, h) :
		cand.pop(k)

	left  = set( p for p in cand if all(int(y) in x for y in truncate_left(p)) )
	right = set( p for p in cand if all(int(y) in x for y in truncate_right(p)) )
	#print left
	#print right
	truncatable_prime = left.intersection(right)
	for i, j in enumerate(sorted(truncatable_prime)) :
		print "%d %d" % ( i, j )
	print sum(truncatable_prime)

if __name__ == "__main__" :
	euler_37()
