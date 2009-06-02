import primes, powerset
import binarySearch

def product(s) :
	result = 1
	for ss in s:
		result *= ss
	return result

def specialIterator(f, i) :
	for j, x in enumerate(f) :
		yield x
		for y in f[j: ] :
			prod = x * y
			if prod > i : break
			yield prod
			pp = prod ** 2
			if pp <= i : yield pp
	return

def specialFactors(f, p) :
	m = f[-1]
	max_val = int(p / f[1])
	x = binarySearch.binarySearch(f, max_val) + 1
	result = set(pse for pse in specialIterator(f[1:x], p) if pse < p )
	result.add(1)
	return sorted(result)

def testSpecialFactors() :
	for i in range(4, 100) :
		if not primes.isPrime(i) :
			f = primes.factors(i)
			sp = specialFactors(f, i)
			print i, sp

def testSpecialFactors2() :
	d = {3:1,102:36,130:25,312:8,759:81,2496:512,2706:1936,3465:1225,6072:5184,6111:3969,8424:5832,14004:432,16005:1089,36897:21609,37156:12544,92385:50625,98640:50625,112032:27648,117708:41616,128040:69696} ## ,351260,740050}
	for k,v in sorted(d.iteritems()) :
		f = primes.factors(k)
		sp = specialFactors(f, k)
		if v not in sp :
			print k, v, sp
			print

if __name__ == "__main__" :
	testSpecialFactors()
	#testSpecialFactors2()
