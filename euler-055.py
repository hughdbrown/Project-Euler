try:
    import psyco
    psyco.full()
except ImportError:
    pass

def lychrel(n) :
	t = [c for c in str(n)]
	t.reverse()
	m = int("".join(t))
	return m + n

def palindrome(n) :
	ns = str(n)
	fulllen = len(ns)
	halflen = fulllen / 2
	return all(ns[i] == ns[fulllen - i - 1] for i in range(halflen))

def test() :
	for i in [44, 74, 77, 47, 477, 447, 444, 777] :
		print i, palindrome(i)

def do_all():
	count = 0
	for i in range(1,10000) :
		x = i
		for j in range(50) :
			x = lychrel(x)
			if palindrome(x) :
				break
		else :
			count += 1
	print count

if __name__ == "__main__" :
	do_all()

		