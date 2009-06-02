# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/410681
#import random
#import sys

#def ipow(a,b,n):
#    #calculates (a**b)%n via binary exponentiation, yielding itermediate
#    #results as Rabin-Miller requires
#    A = a = long(a%n)
#    yield A
#    t = 1L
#    while t <= b:
#        t <<= 1
#    
#    #t = 2**k, and t > b
#    t >>= 2
#    
#    while t:
#        A = (A * A)%n
#        if t & b:
#            A = (A * a) % n
#        yield A
#        t >>= 1
#
#def RabinMillerWitness(test, possible):
#    #Using Rabin-Miller witness test, will return True if possible is
#    #definitely not prime (composite), False if it may be prime.
#    
#    return 1 not in ipow(test, possible-1, possible)


# Modified from C code
# http://www.projecteuler.net/index.php?section=forum&id=58&page=1
def apower(a, n, mod) :
	power, result = a, 1
   
	while n :
		if(n%2) : result = (result*power) % mod
		power = (power*power) % mod;
		n/=2
	return result;
   
def witness(a, n) :
	u = n >> 1
	t = 1
	while (u%2 == 0) :
		u >>= 1
		t += 1
	prev = apower(a,u,n)
	for i in xrange(1, t+1) :
		curr = (prev*prev) % n;
		if ((curr==1) and (prev != 1) and (prev != n-1)) :
			return True
		prev = curr

	return (curr != 1)
   
def is_prime(n) :
	if(witness(2,n)) : return False
	elif(witness(7,n)) : return False
	elif(witness(61,n)) : return False
	return True
