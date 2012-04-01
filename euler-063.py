count = 0
for power in range(1, 100) :
	for digit in range(1, 10) :
		p = digit ** power
		if len(str(p)) == power :
			print power, digit, p
			count += 1
print count

