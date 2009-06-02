import psyco

psyco.full()

"""
1 1
2 2
3 3
4 5
5 7
6 11
7 15
8 22
9 30
10 42
11 56
12 77
13 101
14 135
15 176
16 231
17 297
18 385
19 490
"""

#def gen(x) :
#	if x == 1 :
#		yield [1]
#	else :
#		yield [x]
#		for i in xrange(1, 1 + x/2) :
#			elem = [i]
#			for n in gen(x-i) :
#				if i <= n[0] :
#					yield elem + n

#def gen_set(x) :
#	#def x_str(n) :
#	#	return ".".join(str(i) for i in n)
#	#return set(x_str(n) for n in gen(x))
#	#return len([n for n in gen(x)])
#	for n in gen(x) :
#		print n

d = dict()
OneMillion = 1000*1000
TenMillion = 10*OneMillion
def fn(x,y) :
	if (x - y) in [0,1] or y == 1:
		return 1
	else :
		k = (x, y)
		if k not in d : 
			#d[k] = sum(fn(x-y, i) % OneMillion for i in xrange(1, y+1)) % OneMillion
			total = 0
			new_x = x - y
			limit = min(y, new_x) + 1
			for i in xrange(1, limit) :
				total += fn(new_x, i)
				if total >= TenMillion :
					total %= OneMillion
			d[k] = total % OneMillion
		return d[k]

def gen_sum(x) :
	#return sum(fn(x, i) % OneMillion for i in xrange(1, x+1))
	total = 0
	for i in xrange(1, x+1) :
		total += fn(x, i)
		if total >= TenMillion :
			total %= OneMillion
	return total % OneMillion

def small_test() :
	for i in xrange(1,20) :
		g = gen_sum(i)
		print i, g

def big_test() :
	i = 1
	while True :
		g = gen_sum(i) % OneMillion
		print i, g
		if not g : break
		i += 1
	print i, g
 
def test() :
	import time
	s = time.clock()
	#small_test()
	big_test()
	e = time.clock()
	print "%f" % (e - s)

test()
