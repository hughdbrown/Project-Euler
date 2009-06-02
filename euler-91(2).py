#!/usr/bin/env python
#!/usr/bin/env python
import psyco
psyco.full()

def euler91(limit) :
	origin = (limit-1)*(limit-1)
	right = (limit-1)*(limit-1)
	left = (limit-1)*(limit-1)
	return origin + left + right

if __name__ == "__main__" :
	c = euler80(50)
	print
	print c

