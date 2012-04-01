

def pentagonal(n) :
	return (n * (3 * n - 1)) >> 1
def hexagonal(n) :
	return (n * (2 * n - 1))

p = 144; pc = pentagonal(p)
h = 144; hc = hexagonal(h)
while pc != hc :
	if pc > hc :
		h += 1
		hc = hexagonal(h)
	else :
		p += 1
		pc = pentagonal(p)
print "Hex: ", h, hc
print "Pent: ", p, pc
