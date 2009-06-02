def score(b) :
	return sum(bb * bb for bb in b)


a = [1]
for i in range(20) :
	b = [1] * (len(a)+1)
	for j in range(1, len(b)-1) : 
		b[j] = a[j-1] + a[j]
	print b, score(b)
	a = b
