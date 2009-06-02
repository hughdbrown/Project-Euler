#for i in range(10, 10**6) :
#	if i * 9**5 <= 10**(i-1) :
#		break
#print i

a = []
for i in range(2,10000000) :
	s = sum(int(j) ** 5 for j in str(i))
	if s == i :
		a.append(i)

print a
print sum(a)


