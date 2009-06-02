def permute(s) :
	if not len(s) : yield ""
	else :
		for i in range(len(s)) :
			left, mid, right = s[0 : i], s[i], s[i+1 : ]
			remainder = left + right
			for x in permute(remainder) :
				yield str(mid) + x
	return
