for r in range(995000, 2000000) :
	print r, "\r",
	x = r * (1000*1000*1000*1000 - r)
	y = x ** 0.33333333333333
	if r > y :
		print r, y
		break