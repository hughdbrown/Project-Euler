import primes

def cumulative_sum(s) :
	a = [0] * (len(s)+1)
	sum = 0
	for i in range(len(s)) :
		sum += s[i]
		a[i] = sum
	return a
def calc_offset(a, limit) :
	lo, hi = 0, len(a)
	while lo < hi :
		mid = (lo + hi) >> 1
		if a[mid] > limit :
			hi = mid - 1
		else :
			lo = mid + 1
	result = [ (0, hi) ]
	lo = 1
	while hi < len(a) :
		d = a[hi] - a[lo]
		if d > limit :
			result.append( (lo, hi-1) )
			lo += 1
		else :
			hi += 1
	return result

limit = 1000 * 1000
p = primes.primes(limit)
a = cumulative_sum(p[0:4920])
offset = calc_offset(a, limit)
max_len, that_prime, starts_at = 0, -1, -1
for t in offset :
	lower, upper = t[0], t[1]
	length = upper-lower
	max_iters = length - max_len
	for j in range(max_iters) :
		v = a[upper-j] - a[lower]
		if v in p :
			cur_len = upper - lower - j
			max_len, that_prime, starts_at = cur_len, v, p[lower]
			break

print "Len of %d, sums to %d, starts at %d" % (max_len, that_prime, starts_at)
