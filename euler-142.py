from collections import defaultdict
UPPER = 1000
squares = [x * x for x in range(1, UPPER)]
set_squares = set(squares)

def create_d():
    d = defaultdict(list)
    for i, x in enumerate(squares):
        for j, y in enumerate(squares):
            if i > j and ((i & 1) == (j & 1)):
                d[x - y].append((x, y))
    return d

def filter_d(d):
    return dict((k, v) for k, v in d.iteritems() if len(v) >= 2)

def search_d(d):
    for k, v in d.iteritems():
        z = k // 2
        for i in range(0, len(v) - 1):
            tu = v[i]
            x = sum(tu) // 2
            for j in range(i + 1, len(v)):
                vw = v[j]
                y = sum(vw) // 2
                x, y = max(x, y), min(x, y)
                #print tu, vw, x, y, z
                #print "\tx + z:", x + z
                #print "\tx - z:", x - z
                #print "\ty + z:", y + z
                #print "\ty - z:", y - z
                #print "\tx + y?", x + y
                #print "\tx - y?", x - y
                if (x + y) in set_squares and (x - y) in set_squares:
                    return (x, y, z)

if __name__ == '__main__':
    d = create_d()
    print "len(d):", len(d)
    e = filter_d(d)
    print "len(e):", len(e)
    print "max pairs to search:", max(len(v) for v in e.values())
    print search_d(e)
