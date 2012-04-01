d = {}
for i in range(1, 10000000) :
	i3 = i**3
	ss = sorted(str(i3))
	si3 = ""
	for a in ss :
		si3 += a
	print i, i3, si3, "\r",
	if d.has_key(si3) :
		li = d[si3]
		d[si3] = li + [i3]
	else :
		d[si3] = [i3]
	if len(d[si3]) == 5 :
		print d[si3]
		break