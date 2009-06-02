import psyco
psyco.full()

def pandigital(n) :
	s = set (d for d in str(n))
	return len(s) == 9 and "0" not in s

a, b, i = 1, 1, 2
while i < 10*1000*1000 :
	i += 1
	print i, "\r",
	b, a = a+b, b

a10mil, b10mil, i19mil = a, b, i

pright = []
limit = 50*1000*1000
while i < limit :
	i += 1
	print i, "\r",
	b, a = a+b, b
	s = str(b)
	if len(s) >= 9 :
		right = s[-9:]
		if pandigital(right) :
			print "Right", i, right
			pright.append(i)
			#if pandigital(left) :
			#	print "Left", i, left
			#	#break
		a = int(str(a)[-9:])
		b = int(str(b)[-9:])

a, b, i = a10mil, b10mil, i10mil
j = 0
while i < limit :
	i += 1
	print i, "\r",
	b, a = a+b, b
	s = str(b)
	if b == pright[j] :
		left = s[ :9]
		if pandigital(left) :
			print i, left, pright[j], b
			break
		else : j += 1
	elif len(s) >= 16 :
		a = int(str(a)[:20])
		b = int(str(b)[:20])

print "Done"
	