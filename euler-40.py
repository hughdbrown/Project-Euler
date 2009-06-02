
s = ""
for i in range(1, 200000) :
	s += str(i)

i, j, k, l, m, n, o = int(s[1-1]), int(s[10-1]), int(s[100-1]), int(s[1000-1]), int(s[10*1000-1]), int(s[100*1000-1]), int(s[1000*1000-1])

print i, j, k, l, m, n, o
print i * j * k * l * m * n * o