import string
def key(n) :
	if n == 0: yield []
	else :
		for c in string.lowercase:
			for k in key(n-1) :
				yield [ord(c)] + k
	return

f = open("cipher-59.txt")
data = []
for line in f.readlines() :
	a = line.strip().split(",")
	for aa in a :
		data.append(int(aa))
#print data

def brute_force()  :
	for k in key(3) :
		result = [ chr(d ^ k[i%3]) for i, d in enumerate(data) ]
		x = "".join(result)
		if (" " in x) and ("~" not in x) and ("`" not in x):
			print k, x

def answer ():
	k = [103, 111, 100]
	result = [ chr(d ^ k[i%3]) for i, d in enumerate(data) ]
	x = "".join(result)
	s = sum(ord(a) for a in x)
	print s

answer()
