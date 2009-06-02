memo = {}
def divide(total_len, block_size) :
	if total_len < 0 :
		yield 0
	elif total_len == 0 :
		yield 1
	else :
		if total_len in memo :
			yield memo[total_len]
		else :
			for block in block_size :
				if block <= total_len :
					newsize = total_len - block
					if block != 1 and newsize > 0 :
						newsize -= 1
					s = sum(d for d in divide(newsize, block_size))
					memo[newsize] = s
					yield s
	return

def euler115(block, total_len) :
	global memo
	block_sizes = tuple([1]) + tuple(range(block, total_len+1))
	memo = {}
	return sum(divide(total_len, block_sizes))

if __name__ == "__main__" :
	import time
	s = time.clock()
	m = 50
	for i in range(m, 6000) :
		x = euler115(m, i)
		print(i, x)
		if x > 1000*1000 :
			break
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))

