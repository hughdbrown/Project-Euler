import psyco
psyco.full()

import gcd
import primes

def euler72(limit) :
	# 1 appears in all
	count = limit - 2 + 1
	p = primes.primes(limit + 1)
	p.append(limit + 50)
	p_counter = 0
	next_prime = p[p_counter]
	p25 = p[ : 25]
	#print "Limit: %d Count: %d" % (limit, count)
	g_fn = gcd.gcd
	for r in xrange(2, limit) :
		if r % 1000 == 0 :
			print r, count, "\r",
		leftover = limit%r
		multiples_of_r = (limit - r - leftover) / r
		x, y = 0, 0
		if r == next_prime :
			p_counter += 1
			next_prime = p[p_counter]
			x, y = (r-1), leftover
		else :
			r_temp = r
			rr = range(r)
			for pp in p25 :
				if r_temp % pp == 0 :
					for ccc in xrange(pp, r, pp) :
						rr[ccc] = 0
					while 1 :
						qq, rrr = divmod(r_temp, pp)
						if rrr != 0 : break
						r_temp = qq
					if r_temp == 1 or pp > r_temp : break
			for j in rr :
				if j :
					if g_fn(j, r) == 1 :
						x += 1
						if j <= leftover :
							y += 1
			#for j in range(1,r+1) :
			#	if g_fn(j, r) == 1 :
			#		x += 1
			#		if j <= leftover :
			#			y += 1
			#print r, gcd_range, multiples_of_r, leftover
		print r, (multiples_of_r * x) + y
		count += (multiples_of_r * x) + y
	return count

def test_euler72() :
	#a = [[5,9], [6,11], [7,17], [8,21], [9, 27], [10, 31], [11, 41], [12,45], [13,57], [14,63], [15,71]]
	a = [[5,9], [6,11], [7,17], [8,21], [9, 27], [10, 31], \
		[11, 41], [12,45], [13,57], [14,63], [15,71], [16,79], [17,95], [18,101], [19,119], [20,127], \
		[21,139], [22,149], [23, 171], [24, 179], [25, 199], [26, 211], [27, 229], [28, 241], [29, 269], \
		[30, 277], [31, 307], [32, 323], [33, 343], [34, 359], [35, 383], [36, 395] ]
	for r in a :
		result = euler72(r[0])
		if result != r[1] :
			print "%d: expecting %d, got %d" % (r[0], r[1], result)
		else : print "Success: %d" % r[0]

if __name__ == "__main__" :
	#test_euler72()
	#c = euler72(1000*1000)
	c = euler72(1000)
	print
	print c

