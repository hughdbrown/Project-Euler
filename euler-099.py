import math

f = open ("base_exp_99.txt")
lines = [ line.strip().split(",") for line in f.readlines() ]

greatest, base, exp, lineno = 0.0, 0, 0, -1
for i, a in enumerate(lines) :
	test = float(a[1]) * math.log(float(a[0]))
	if test > greatest :
		greatest, base, exp, lineno = test, a[0], a[1], i
print greatest, base, exp, lineno
