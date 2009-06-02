#import sys

scores = {}

def traverse(limit) :
	# Queue of tuples, implemented as list
	q = []

	# Seed q with initial values
	power_of_two = 2
	twos = [1]
	while power_of_two <= limit :
		twos += [power_of_two]
		q.append(twos)
		for i, n in enumerate(twos[:-1]) :
			candidate = power_of_two + n
			if candidate > limit :
				break
			new_s = twos + [candidate]
			q.append(new_s)
		power_of_two *= 2

	# Optimization: don't add tuples that have been examined before
	seen = set(tuple(qq) for qq in q)

	index = 0
	while(index < len(q)) :
		# Logically dequeue item
		# Copying parts of queue was expensive, so just use an index
		curr = q[index]
		#print ("{0} {1}".format(index,curr), file=sys.stderr)
		index += 1

		# Add all tuple elements to scores
		# Potentially modify score if better route found
		for i, x in enumerate(curr) :
			if (x not in scores) :
				scores[x] = i
			elif (i < scores[x]) :
				#print("Modify score[{0}] from {1} to {2}".format(x, scores[x], i))
				scores[x] = i

		# Create new set of high numbers to add to end of new tuple
		last = curr[-1]
		b = set(x+y for x in curr for y in curr if last < x+y <= limit)
		for bb in sorted(b) :
			assert(bb not in curr) 
			assert(bb > curr[-1])
			# Starve the queue by excluding tuples that cannot 
			# produce better results than already available
			if bb in scores and scores[bb] < len(curr) :
				continue

			candidate = curr+[bb]
			tcandidate = tuple(candidate)
			if tcandidate not in seen :
				q.append(candidate)
				seen.add(tcandidate)

def euler112(limit) :
	traverse(limit)
	print (scores)
	print(sum(scores.values()))

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler112(200)
	e = time.clock()
	print("Elapsed: {0}".format(e - s))
