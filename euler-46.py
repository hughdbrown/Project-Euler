import primes

def isSquare(t) :
	import math
	if t < 0: return False
	else :
		s = int(math.sqrt(t))
		return s*s == t
	
def test(x, p) :
	for pp in p :
		t = (x - pp) / 2
		if isSquare(t) :
			#print x, pp
			return True
	return False


def euler46() :
	p = primes.primes(1000*1000)
	for i in range(1,len(p)) :
		y = p[1: i+1]
		for x in range(p[i] + 1, p[i + 1]) :
			if (x&1) and (not test(x, y)) :
				#print y
				return x

print euler46()




