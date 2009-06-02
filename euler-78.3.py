import psyco

psyco.full()

def pentagonal(n) :
    return n*(3*n-1)/2

def generalised_pentagonal(n): # 0, 1, -1, 2, -2
    def pentagonal(n) :
        return n*(3*n-1)/2
    if n < 0: return 0
    #if n%2 == 0: return pentagonal(n/2+1)
    if (n & 1) == 0: return pentagonal(n/2+1)
    else: return pentagonal(-(n/2+1))

pt = [1]
#for n in range (1, 1000+1):
n = 1
while True :
    r = 0
    f = -1
    i = 0
    while True : # generalised_pentagonal(i) <= n:
        k = generalised_pentagonal(i)
        if k > n:
            break
        #if i%2==0: f = -f
        if (i & 1) == 0: f = -f
        r += f*pt[n - k]
        i += 1
    rr = r % (1000*1000)
    if rr == 0 :
	print n
	break
    else :
        print n, rr
        pt.append(r)
        n += 1



