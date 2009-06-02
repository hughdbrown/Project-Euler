import psyco
psyco.full()

def reverseString(s) :
	return "".join(s[-i-1] for i in range(len(s)))

def isPalindrome(s) :
	return all(s[i] == s[len(s) - i - 1] for i in range(len(s) >> 1))

def palindromicNumber(n) :
	if n & 1 :
		x = (n - 1) >> 1
		lower = int(10 ** (x-1))
		upper = int(10 ** x)
		for j in range(lower, upper) :
			s = str(j)
			x = int(s + "0" + reverseString(s))
			for i in range(0, 10*upper, upper) :
				yield x + i
	else :
		x = n >> 1
		lower = int(10 ** (x-1))
		upper = int(10 ** x)
		for j in range(lower, upper) :
			s = str(j)
			yield int(s + reverseString(s))
	return

def cumulativeSeries(s) :
	a = [0]
	sum = 0
	for ss in s :
		sum += ss
		a.append(sum)
	return a

def euler125(upper) :
	print "Getting palindromes..."
	p = {}
	for i in range(1,upper+1) :
		for x in palindromicNumber(i) :
			p[x] = 1

	print "Getting squares..."
	upper_ten = int(int(10 ** upper) ** 0.5)
	#print upper_ten
	squares = [i * i for i in range(1,upper_ten + 1)]
	#print len(squares)

	print "Generating cumulative series..."
	cum_squares = cumulativeSeries(squares)
	#print len(cum_squares)

	results = set()
	for i in range(len(cum_squares)) :
		#print i, "\r",
		for j in range(i+2, len(cum_squares)) :
			v = cum_squares[j] - cum_squares[i]
			if v > 10**upper : break
			elif v in p : 
				results.add(v)
				#print len(results), v, "[%d,%d]" %(i+1,j+1) #, squares[i:j]
	print
	print len(results), sum(results)
	#print results

def testPalindromes() :
	p = {}
	for i in range(1,upper+1) :
		for x in palindromicNumber(i) :
			p[x] = 1
	count = 0
	for i in range(10**7, 10**8) :
		if (i % 10000 == 0) : print i, "\r",
		b1, b2 = isPalindrome(str(i)), (i in p)
		if (b1 and not b2) :
			print
			print "Missed a palindrome: %d" % i
		elif (not b1 and b2) :
			print
			print "Added a non-palindrome: %d" % i
		elif b1 == b2 :
			count += 1
	print "Equal %d times" % count


if __name__ == "__main__" :
	#upper = 4
	upper = 8
	euler125(upper)
	#testPalindromes()
