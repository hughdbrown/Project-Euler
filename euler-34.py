import factorial

f = [ factorial.factorial(i) for i in range(10) ]

results = []
for i in range(9, 1000000) :
	s = sum(f[int(j)] for j in str(i))
	if s == i :
		results.append(i)
print results
print sum(results)
