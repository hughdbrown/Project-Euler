def stripe(x, index, k, max_value) :
    max_i = int((float(max_value)/float(index)) ** 0.5) + 1
    mask = 1 << k
    for i in xrange(1,max_i) :
        ii = index * (i**2)
        max_j = int((max_value - ii) ** 0.5) + 1
        for j in xrange(1,max_j) :
            jj = j**2
            t = ii + jj
            if t < max_value :
                if t in x or (k == 0) :
                    x[t] |= mask
        if k == 0 : print i, len(x)

def remove(x, k) :
    if k :
        mask = (1 << (k+1)) - 1
        kk = [k for k,v in x.iteritems() if v != mask]
        for k in kk :
            del x[k]
    print len(x)

def euler_229(max_value) :
    import collections
    x = collections.defaultdict(int)
    indexes = (7,3,2,1)
    for k, index in enumerate(indexes) :
        stripe(x, index, k, max_value)
        remove(x, k)
    return len(x)

print euler_229(10*1000*1000)

