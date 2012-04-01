import string

def score(word) :
	
	return sum((1 + string.uppercase.index(c)) for c in word)

triangles = [ (n*(n+1))/2 for n in range(100) ]
words = {}
f = open ("words-42.txt")
for line in f.readlines() :
	for w in line.replace('"', "").strip().split(',') :
		words[w] = score(w)

result = sum(1 for k, v in words.items() if v in triangles)
print result
