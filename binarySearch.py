def binarySearch(a, v) :
	lo, hi = 0, len(a)-1
	if v > a[-1] : return len(a)
	elif v < a[0] : return -1
	while lo <= hi :
		mid = lo + ((hi - lo) >> 1)
		if a[mid] > v : hi = mid - 1
		elif a[mid] < v : lo = mid + 1
		else: return mid
	return hi +1

if __name__ == "__main__" :
	import string

	def testBinarySearch(a, v) :
		i = binarySearch(a,v)
		print v, i, (a[i] if (0 <= i < len(a)) else "")

	s = string.uppercase
	for a in string.uppercase :
		testBinarySearch(s, a)
	testBinarySearch(string.uppercase, 'a')
	testBinarySearch(string.uppercase, '0')

	s = [string.uppercase[i] for i in range(0, len(string.uppercase), 2) ]
	#s = string.uppercase
	for a in (string.uppercase[i] for i in range(0, len(string.uppercase), 2)) :
		testBinarySearch(s, a)
	for a in (string.uppercase[i] for i in range(1, len(string.uppercase), 2)) :
		testBinarySearch(s, a)


