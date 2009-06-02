def powerset(s) :
	L = len(s)
	for i in xrange(1 << L):
		yield [ s[j] for j in xrange(L) if (i & (1 << j)) ]

if __name__ == "__main__" :
	import psyco
	psyco.full()
	import time, string
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	for i, x in enumerate(powerset(string.lowercase[0:6])) :
		print i, x
	print "End ", time.strftime(fmt, time.gmtime())
