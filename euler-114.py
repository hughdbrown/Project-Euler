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
					#print (total_len, block)
					newsize = total_len - block
					if block != 1 and newsize > 0 :
						newsize -= 1
					s = sum(d for d in divide(newsize, block_size))
					memo[newsize] = s
					yield s
	return

def euler114(total_len) :
	global memo
	block_sizes = tuple([1]) + tuple(range(3, total_len + 1))
	memo = {}
	result = sum(divide(total_len, block_sizes))
	print (total_len)
	print (result)
	#print (memo)
	print ("-----")

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler114(50)
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))

