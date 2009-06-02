x = 0
for i in range(2, 100) :
	print i, "\r", 
	for j in range(2, 100) :
		m = sum(int(c) for c in str(i**j))
		if m > x : a, b, x = i, j, m
print i, j, x
