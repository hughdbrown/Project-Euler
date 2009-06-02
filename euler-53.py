import factorial

count = 0
for n in range(4, 101) :
	for r in range(1, n+1) :
		f = factorial.choose(n, r)
		if f > 1000*1000:
			count += n - (2 * r - 1)
			break
print count
