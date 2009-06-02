
def quadratic(a,b,c) :
	import math
	r0 = math.sqrt(b*b - 4*a*c)
	r1 = (-b + r0) / 2.0
	r2 = (-b - r0) / 2.0
	return (r1, r2)
