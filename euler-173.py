def euler173(limit) :
	n = 0
	for i in range(limit // 4, 1, -1) :
		length = i + 1
		used = 4 * i
		remainder = limit - used
		#print ("+ {0}x{0}: {1}".format(length, remainder))
		n += 1
		while (length >= 5) and (remainder >= 4*(length-3)) :
			length -= 2
			used = length**2 - (length-2)**2
			remainder -= used
			used += 4*(length-1)
			#print (" {0}x{0} {1}".format(length, remainder))
			n += 1
	print ("Total: {0}".format(n))

if __name__ == "__main__" :
	euler173(1000*1000)
	#euler173(100)
