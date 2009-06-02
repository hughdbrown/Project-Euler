

try:
    import psyco
    psyco.full()
except ImportError:
    pass

def x(i, n, a) :
	y = n - i
	if y == 1 :
		return 1
	elif i == 1 :
		return 1
	else :
		b = a[y]
		if i >= y :
			s = sum(t[1] for t in b) + 1
		else :
			s = sum(t[1] for t in b if t[0] <= i)
		return s

def euler76(limit) :
	a = [ [[0,0]], [[1,0]] ]
	for i in range(2, limit+1) :
		d = [ [j, x(j, i, a)] for j in range(i-1, 0, -1) ]
		a.append(d)
	print a[limit]
	s = sum(t[1] for t in a[limit])
	return s

if __name__ == "__main__" :
	c = euler76(100)
	print 
	print c
