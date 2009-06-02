def collatz(c, n) :
	if not c.has_key(n) :
		x = ((n+(n<<1))+1 if n&1 else n>>1)
		c[n] = 1 + collatz(c,x)
	return c[n]

x = 0
c = {1:1}
for i in range(1000*1000-1, 77001, -2) :
	y = collatz(c,i) 
	##print i, y, len(c), "\r",
	if y > x :
		x,j = y, i
		print i, y ##, len(c)
print x, j
