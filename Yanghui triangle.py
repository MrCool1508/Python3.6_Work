#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles(max):
	L = [1]
	n = 0
	print(list(L))
	while n < max:
		yield L
		L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
		L.insert(0, 1)
		L.append(1)
		n += 1
		print(list(L))
	return 'done'
#		if len(L) > 10:
#			break


g = triangles(20)
while True:
	try:
		x = next(g)
#		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

#print(list(triangles(5)))
