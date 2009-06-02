import combine

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, p in enumerate(combine.permute(a)) :
	if i == 999999 : 
		print i, p
		break