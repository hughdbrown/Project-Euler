def binary(n) :
	r = []
	while n :
		r.append ("1" if n & 1 else "0")
		n >>= 1
	r.reverse()
	return "".join(c for c in r)

def add(a) :
	if not len(a) : return "0"
	else :
		result = ""
		max_len = len(a[-1])
		carry = 0
		for i in range(max_len) 
			count = carry
			carry = 0
			for j in range(len(a)) :
				s = a[j]
				decimalplace = len(s) - i - 1
				if decimalplace >= 0 :
					count += (1 if s[decimalplace] == "1" else 0) 
			result = ("1" if count & 1 else "0") + result
			carry = count >> 1
		while carry :
			result = ("1" if carry & 1 else "0") + result
			carry >>= 1
		return result

def multiply(a,b) :
	result = []
	b2 = list(b)
	b2.reverse()
	for i in range(len(b2)) :
		if b2[i] == "1" :
			result.append(a + "0"*i)
	return add(result)

def decimal(s) :
	result, mask = 0, 0
	t = list(s)
	t.reverse()
	for d in t :
		result += ((1 if d == "1" else 0) << mask)
		mask += 1
	return result

def euler97() :
	a = "1" + "0" * 7830457
	b = binary(28433)
	c = decimal(multiply(a, b)) + 1
	print str(c)[-10]

def test1() :
	for i in range(16) :
		b1 = binary(i)
		for j in range(16) :
			b2 = binary(j)
			c = multiply(b1, b2)
			d = decimal(c)
			print i, j, b1, b2, c, d



if __name__ == "__main__" :
	euler97()
	#test1()
	#print multiply("10011", "101")
	#print add (["111", "11111"])
