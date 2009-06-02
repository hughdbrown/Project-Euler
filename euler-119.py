import math

x=[]
i = 10
while len(x) < 30:
	ss = sum(int(s) for s in str(i))
	if ss > 1 :
		y = int(math.log(i) / math.log(ss))
		if ss ** y == i :
			x.append(i)
			print ("{0} {1} = {2} ** {3}".format(len(x), x[-1], ss, y))
	i += 1