import collections
d = collections.defaultdict(int)
d[0] = 1
numbers = [5,4,3,2,1]
for n in numbers :
    dk = reversed(sorted(d.iterkeys()))
    for k in dk :
        d[k+n] += d[k]
    print "----"
    for k in sorted(d.iterkeys()) :
        print k, d[k]
