def hash(i, c) :
	return ((int(i) * 37) + c) & 0xFFFFFFFF

def hashR(low, high) :
	hashC = 0
	for i in range(low, high) :
		hashC = hash(hashC, i)
	return hashC

d = {}
x = 0
for i in range(1, 1000*1000) :
	if i % 1000 == 0 :
		print ".",
	x = hash(x, i)
	if x in d.keys() :
		print "Seen %08x: %d %d" % (x, d[x], i)
		break
	else :
		d[x] = i
