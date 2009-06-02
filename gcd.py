
def gcd(a, b) :
	if b > a : a, b = b, a
	while b > 0 :
		a, b = b, a % b
	return a

def test_gcd() :
	data = [(5, 2), (7, 2),(7, 5),(16, 5),(16, 8),(16, 4),(16, 2),(16, 1)]
	for a,b in data :
		print "(%d, %d): %d" % (a, b, gcd(a, b))

if __name__ == "__main__" :
	test_gcd()
