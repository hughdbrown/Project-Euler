try:
    import psyco
    psyco.full()
except ImportError:
    pass

a = 128
j = 7
m = 10**11
for i in xrange(1,783046) :
	print i, a, "\r",
	a *= 1024
	j += 10
	if a > m : a %= m

print j
result = str(28433 * a + 1)[-10 : ]
print result
