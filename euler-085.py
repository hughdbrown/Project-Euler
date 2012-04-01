import sys
import psyco
psyco.full()

def solve(w,h) :
	count = 0
	for i in range(1,w+1) :
		for j in range(1,h+1) :
			c = (w-i+1)*(h-j+1)
			count += c
	return count

def euler85(upper) :
	m = 2000*1000
	w1, h1, c1 = 0, 0, 0
	for w in range(2,upper) :
		for h in range(w+1,upper) :
			print >> sys.stderr, w, h, "\r",
			c = solve(w,h)
			if abs(2000*1000 - c) < m :
				w1, h1, c1, m = w, h, c, abs(2000*1000 - c)
				print >> sys.stderr, w1, h1, c1, m
			if c > 2000*1000 :
				break
	print
	print w1, h1, m, w1*h1

if __name__ == "__main__" :
	euler85(100)
	#print solve(2,2)

