a = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
b = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
c = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
aa = sum(len(aaa) for aaa in a)
bb = sum(len(bbb) for bbb in b)
cc = sum(len(ccc) for ccc in c)

total = 10 * (9 * aa + bb) + 900 * len("hundred") + 900 * aa + len("onethousand") + 900 * len("and") + 100 * cc
print total

def printNumber(n) :
	result = ""
	thousands, remainder = divmod(n, 1000)
	if thousands == 1 :
		result = "%s%s" % ("one", "thousand")
		n = 0

	hundreds, remainder = divmod(n, 100)
	if hundreds >= 1 :
		result += ("%s%s%s") % (a[hundreds], "hundred", ("and" if remainder > 0 else ""))
		n = remainder

	tens, remainder = divmod(n, 10)
	if tens >= 2 :
		result += c[tens-2]
		n = remainder
	elif tens == 1 :
		result += b[remainder]
		n = 0

	#print remainder
	if n < 10 :
		result += a[n]
	return result

print sum(len(printNumber(i)) for i in range(1, 1001))
