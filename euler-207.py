import math

def root(a,b,c) :
    x = math.sqrt(b * b - 4 * a * c)
    a2 = 2 * a
    return [ (-b + x) / a2, (-b - x) / a2 ]

def isInt(x) :
    return x == int(x)

def euler207() :
	intCount, nonIntCount = 0, 0
	log2 = math.log(2)
	root = 2
	mustFind = 0
	while True :
		kk = 2 * root - 1
		k = (kk*kk - 1) / 4
		t = math.log(root) / log2
		if isInt(t) :
			intCount += 1
			mustFind = 12344 * intCount
		else :
			nonIntCount += 1
		#print ("{0} {1} {2}: {3} {4} {5}".format(root, k, t, intCount, nonIntCount, mustFind))
		if mustFind < nonIntCount :
			print ("{0} {1}".format(intCount, nonIntCount))
			break
		root += 1


if __name__ == "__main__" :
	import time
	s = time.clock()
	euler207()
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))

