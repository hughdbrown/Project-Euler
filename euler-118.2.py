import psyco
psyco.full()

def isprime(x) :
	if x > 2 and (x & 1) :
		i = 3
		sqrt_x = int(x ** 0.5) + 1
		while i <= sqrt_x :
			if x % i == 0 :
				return False
			i += 2
		return True
	else :
		return x == 2

#def primes(x) :
#	a = range(0,x+1)
#	a[0], a[1] = 0, 0
#	for i in xrange(2, x+1) :
#		if a[i] == i :
#			a[i] = 1
#			if (x+1)/ i > i :
#				for j in xrange(i*i, x+1, i) :
#					a[j] = i
#	return [x for x, aa in enumerate(a) if aa == 1]
#
#p = primes(1000*1000)
#
#def isprime(x) :
#	global p
#	if x > 2 and (x & 1) :
#		sqrt_x = int(x ** 0.5) + 1
#		for pp in p:
#			if pp > sqrt_x : return True
#			elif x % pp == 0: return False
#		return True
#		#i = 3
#		#while i*i <= x :
#		#	if x % i == 0 :
#		#		return False
#		#	i += 2
#		#return True
#	else :
#		return x == 2


def generator_iter(s) :
	for i, elem in enumerate(s) :
		yield s[:i], elem, s[i+1:]
def permute(s) :
	if not len(s) :
		yield []
	else :
		for left, elem, right in generator_iter(s) :
			rest = left + right
			for x in permute(rest) :
				yield [elem] + x

def powerset(s) :
	length = len(s)
	for i in xrange(1, 1 << length) :
		yield [c for j, c in enumerate(s) if (1 << j) & i]

	return

def product(primes, d) :
	total = 1
	for prime in primes :
		total *= len(d[prime])
	return total

def spanningsets(items):
	if len(items) == 1:
		yield [items]
	else:
		left_set, last = items[:-1], [items[-1]]
		for cc in spanningsets(left_set):
			yield cc + [last]
			for left, elem, right in generator_iter(cc):
				yield left + [elem + last] + right

def list_to_int(s) :
	return int("".join(str(x) for x in s))
def int_to_list(x) :
	return [int(a) for a in str(x)]
def prime_permutations() :
	import collections

	print "Calculating prime permutations"
	d = collections.defaultdict(set)
	digits = range(1,10)
	for x in powerset(digits) :
		if sum(x) % 3 or x == [3] :
			kx = list_to_int(x)	# Known to be sorted
			for n in permute(x) :
				i = list_to_int(n)
				if isprime(i) :
					d[kx].add(i)
	print "Prime count:", len(d)
	return d

def list_to_str(s) :
	return ".".join(str(x) for x in s)
def used_unused_pairs(d, digits) :
	for prime in d :
		sa = set(int_to_list(prime))
		unused_digits = sorted(x for x in (digits - sa))
		yield prime, unused_digits
	return
def spanning_sets(d) :
	print "Calculating spanning sets"
	solutions = {}
	digits = set(range(1,10))
	for p, unused_digits in used_unused_pairs(d, digits) :
		for ss in spanningsets(unused_digits) :
			j = [list_to_int(aa) for aa in ss] # aa known to be sorted
			if all((aa in d) for aa in j) :
				k = sorted([p] + j)
				sol_key = list_to_str(k)
				if sol_key not in solutions :
					solutions[sol_key] = k
	print "Solution count: %d" % len(solutions)
	return solutions

def calculate_solutions(d, solutions) :
	print "Calculating number of solutions"
	return sum(product(solution, d) for solution in solutions.itervalues())

def test() :
	d = prime_permutations()
	solutions = spanning_sets(d)
	total = calculate_solutions(d, solutions)
	print "Total: %d" % total

if __name__ == "__main__" :
	import time
	s = time.clock()
	test()
	e = time.clock()
	print "Elapsed: ", (e - s)
