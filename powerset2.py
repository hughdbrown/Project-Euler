#import psyco
#psyco.full()

def powersetIterator(n) :
	while n :
		yield n ^ (n-1)
		n &= n-1

def powerset(s) :
	L = len(s)
	for i in xrange(1 << L):
		yield [ s[i] for i in powersetIterator(i) ]

if __name__ == "__main__" :
	import time, string
	fmt = "%Y-%m-%d %H:%M:%S"
	print "Start ", time.strftime(fmt, time.gmtime())
	for i, x in enumerate(powerset(string.lowercase[0:6])) :
		print i, x
	print "End ", time.strftime(fmt, time.gmtime())
