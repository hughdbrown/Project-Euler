t = [0] * (101)
t[0] = 1
total = 0
for i in range (0, len(t)) :
	for j in range(i,0,-1) :
		t[j] = t[j] + t[j-1]
	print(t)
	total += sum(1 for j in range(i) if t[j] % 7 != 0)
print (total)

