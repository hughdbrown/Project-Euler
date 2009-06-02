#!/usr/bin/env,python

def load_triangle(fileName) :
	triangle = []
	f = open (fileName)
	for line in f.readlines() :
		t = [ int(s) for s in line.split(' ') ]
		triangle.append(t)
	return triangle

def triangle_add(x, y) :
	result = [x[i] + max(y[i], y[i + 1]) for i in range(len(x))]
	return result

if __name__ == "__main__" :
	triangle =load_triangle("triangle.txt")
	x = [0] * (len(triangle[-1]) + 1)
	for i in range(len(triangle)-1, -1, -1) :
		x = triangle_add(triangle[i], x)
	print x
	