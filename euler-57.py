

def expand(n) :
	num, denom = 1, 2
	for i in range(n) :
		num, denom = denom, 2 * denom + num
	num += denom
	return (num, denom)

count = 0
for i in range(1000) :
	t = expand(i)
	if len(str(t[0])) > len(str(t[1])) :
		count += 1
print count
