def fill(d, k):
    if not k % 2:
        if k/2 not in d:
            fill(d,k/2)
        d[k] = 1 + d[k/2]
    else:
        o = 3*k+1
        if o not in d:
            fill(d,o)
        d[k] = 1 + d[o]
d = {1:1}
for i in range(2,1000000):
    fill(d,i)
highkey = 0
highv = 0
for (k,v) in d.iteritems():
    if v > highv and k < 1000000:
        highv = v
        highkey = k
print highkey
