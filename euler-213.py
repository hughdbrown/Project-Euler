import collections
import random

def init(size) :
	d = collections.defaultdict(int)
	for i in range(size) :
		for j in range(size) :
			d[i,j] = 1
	return d

LEFT, RIGHT, UP, DOWN = range(4)
alldirs = (LEFT, RIGHT, UP, DOWN)

def directions(i, j, size) :
	if i not in (0, size-1) and j not in (0, size-1) :
		return alldirs
	else :
		results = set(alldirs)
		if i == 0 :
			results -= set([UP])
		if i == size-1 :
			results -= set([DOWN])
		if j == 0 :
			results -= set([LEFT])
		if j == size-1 :
			results -= set([RIGHT])
		return tuple(ss for ss in results)

def newPos(i, j, jump, size) :
	if jump == LEFT :
		j -= 1
	elif jump == RIGHT :
		j += 1
	elif jump == UP :
		i -= 1
	elif jump == DOWN :
		i += 1
	return (i, j)

def euler213(size, iterations) :
	d = init(size)
	for m in range(iterations) :
		dst = collections.defaultdict(int)
		for i in range(size) :
			for j in range(size) :
				dirs = directions(i, j, size)
				for x in range(d[i,j]) :
					jumpint = random.randint(0, len(dirs)-1)
					newi, newj = newPos(i, j, dirs[jumpint], size)
					dst[newi, newj] += 1
		d = dst
	return size*size - len(d)

if __name__ == "__main__" :
	import time
	iters, trial_iters = 1000, 50
	
	for size in range(6, 24, 2) :
		s = time.clock()
		c = sum(euler213(size, trial_iters) for _ in range(iters))
		print ("{0} {1} {2}".format(size, c, iters))
		e = time.clock()
		print ("Elapsed: {0}".format(e - s))
