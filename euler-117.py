memo = {}
def divide(total_len, block_size) :
	if total_len < 0 :
		yield 0
	elif total_len == 0 :
		yield 1
	else :
		if (total_len, block_size) in memo :
			yield memo[total_len, block_size]
		else :
			for block in block_size :
				s = 0
				for d in divide (total_len - block, block_size) :
					s += d
				memo[total_len - block, block_size] = s
				yield s
	return

def euler117(total_len) :
	block_size = (1,2,3,4)
	result = sum(divide(total_len, block_size))
	print (result)

if __name__ == "__main__" :
	import time
	s = time.clock()
	euler117(50)
	e = time.clock()
	print ("Elapsed: {0}".format(e - s))

