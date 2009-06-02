
s = set()
f = open ("keylog.txt")
for i in f.readlines() :
	s.add(i.strip())

for i in sorted(s) :
	print i

73162890