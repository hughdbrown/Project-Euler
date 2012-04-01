try:
    import psyco
    psyco.full()
except ImportError:
    pass
import math

def isPerfectSquare(n) :
	sq = long(math.sqrt(n))
	return (sq ** 2) == n

def fn1(n) :
	return sum([3*n*n,-2*n,-1])
def fn2(n) :
	return sum([3*n*n,2*n,-1])

def euler94() :
	s = 0
	ans1 = []

	for i in (long(j*j+1) for j in xrange(1, 18257)) :
		sss = fn1(i)
		if isPerfectSquare(sss) and ((i-1) % 4 == 0) :
			ans1.append(i)
	s += sum((3*i + 1) for i in ans1)

	ans2 = []
	for i in (long((j*j*2+1)/3) for j in xrange(3, 31630)) : 
		sss = fn2(i)
		if isPerfectSquare(sss) and ((i-1) % 4 == 0):
			ans2.append(i)
	s += sum((3*i - 1) for i in ans2)

	print s
	print ans1
	print ans2


if __name__ == "__main__" :
	euler94()
