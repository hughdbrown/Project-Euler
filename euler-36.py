
def palindrome_helper(s, n) :
	if n == 0 :
		yield s
	else :
		lower = (0 if n > 2 else 1)
		for i in range(lower, 10) :
			seed = str(i) + s + str(i)
			for x in palindrome_helper(seed, n - 2) :
				yield x
	return

def palindrome_10(n) :
	if n & 1 :
		lower = (0 if n > 1 else 1)
		for i in range(lower,10) :
			for x in palindrome_helper(str(i), n-1):
				yield x
	else :
		for x in palindrome_helper("", n):
			yield x
	return

def palindrome(s) :
	i,j = 0, len(s)-1
	while i < j :
		if s[i] != s[j] : return False
		i += 1; j -= 1
	else:
		return True

def is_palindrome_2(s) :
	x = int(s)
	tmp = ""
	while x :
		tmp = ("1" if x & 1 else "0") + tmp
		x >>= 1
	return palindrome(tmp)


s = []
for i in range(1,7) :
	for x in palindrome_10(i) :
		if is_palindrome_2(x) :
			s.append(x)
print sum(int(ss) for ss in s)
print s