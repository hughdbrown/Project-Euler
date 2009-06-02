upper = 5000

def pentagonal(n) :
	return (n*(3*n-1))/2

pp = [ pentagonal(n) for n in range(2*upper) ]
p = dict.fromkeys( pp, 1 )
#diff = [pp[i] - pp[i-1] for i in range(1, 2*upper - 1) ]

#print pp[0:10]
#print diff[0:10]
#for i in range(1, upper) :
#	for j in range(i+1, upper) :
#		print i, j, "\r",
#		if p[i] < diff[j-1] : break
#		else :
#			s = p[j] + p[i]
#			if s in pp:
#				d = p[j] - p[i]
#				if d in pp :
#					print "Found: %d %d %d %d" % (s, d, p[i], p[j])
#					break

def euler44() :
	for i in range(1, upper) :
		for j in range(i+1, upper) :
			#print i, j, "\r",
			su = pp[i] + pp[j]
			if p.has_key(su) :
				sd = pp[j] - pp[i]
				if p.has_key(sd) :
					return pp[i], pp[j], sd, su

print euler44()
