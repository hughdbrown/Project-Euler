
def merge(s1, s2) :
	return sorted(s1 + s2)

def euler225() :
	#limit = 180*1000
	limit = 150*1000
	t = [0] * limit
	a,b,c = 1,1,1
	t[0:3] = a,b,c
	try :
		for i in range(3, limit) :
			x = sum((a,b,c))
			t[i] = x
			a,b,c = b,c,x
	except MemoryError as mem :
		import sys
		print(i)
		sys.exit(1)
	t.reverse()

	r = range(1, 2*124+1, 2)
	i = 1
	j = 0
	sieve = []
	m = 10000
	found = False
	while j <= 124 and i < m :
		if i in sieve :
			found = True
		elif not any(a%i == 0 for a in t) :
			sieve = merge(sieve, [i * rr for rr in r if (i * rr) < m])
			sieve = sieve[:130]
			if len(sieve) > 124 :
				m = sieve[124]
				print(m)
			found = True
		if found :
			print("{0}: {1}".format(j, i))
			j += 1
			found = False
		i += 2

	for x in sieve :
		if not any(a%x != 0 for a in t) :
			print ("Bad: {0}".format(x))

	print ("m = {0}".format(m))
	print (sieve)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler225()
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))
