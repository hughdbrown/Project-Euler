#!/usr/bin/env python

def generator_iter(s) :
	for i, elem in enumerate(s) :
		yield s[:i], elem, s[i+1:]

def spanningsets(items):
	if len(items) == 1:
		yield [items]
	else:
		left_set, last = items[:-1], [items[-1]]
		for cc in spanningsets(left_set):
			yield cc + [last]
			for left, elem, right in generator_iter(cc):
				yield left + [elem + last] + right
