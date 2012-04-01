def find(remainder, s) :
	if remainder == 0 :
		yield []
	else :
		for i, x in enumerate(s) :
			new_remainder = remainder - x
			if new_remainder >= 0 :
				new_set = s[i : ]
				for y in find(new_remainder, new_set) :
					yield [x] + y
	return

s = [200, 100, 50, 20, 10, 5, 2, 1]
for i, x in enumerate(find(200, s)) :
	print i, x
