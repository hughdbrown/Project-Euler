scores = {}

def traverse(limit, s) :
	q = []
	power_of_two = 2
	k = 1
	twos = [1]
	while power_of_two <= limit :
		twos.append(power_of_two)
		q.append((twos, k)
		n, i = 1, 1
		while n < power_of_two :
			candidate = power_of_two + n
			if candidate > limit :
				break
			q.append((twos + [candidate], k + i)
			n *= 2
			i += 1
		power_of_two *= 2
		k += 1

	result = []
	index = 0
	while(index < len(q)) :
		curr = q[index]
		index += 1
		depth, s = curr

		x = s[-1]
		b = set(x+y for y in s[:-1] if x+y <= limit)
		#print ("New value: {0}".format(bb))
		bb = sorted(list(b))
		bb.reverse()
		for score in bb :
			if score not in scores :
				scores[score] = depth + 1
				print("scores[{0}] = {1}; {2}".format(score, scores[score], limit - len(scores)))
		if len(scores) == limit :
			break
		for bbbb in bb :
			if bbbb not in s :
				ss = sorted(s+[bbbb])
				ss.reverse()
				t = (depth+1, ss)
				q.append(t)

def euler112(limit) :
	base = [1]
	traverse(limit, base)
	print (scores)
	print(sum(scores.keys()))

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler112(200)
	e = time.clock()
	print("Elapsed: {0}".format(e - s))
