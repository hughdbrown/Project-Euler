import string
def score(name) :
	return sum(string.uppercase.index(a)+1 for a in name)

f = open ("names.txt")
names = []
for a in f.readlines() :
	names.extend(a.replace('"', '').split(','))
c = sorted(names)

print sum((i + 1) * score(d) for i, d in enumerate(c))
