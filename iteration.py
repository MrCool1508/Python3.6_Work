#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
	min = L[0]
	max = L[0]	
	for n in L:
		if n < min:
			min = n
#		print(min)
		if n > max:
			max = n
#		print(max)
		#print(n, min, max)
#	print(min, max)
	if len(L) == 0:		
		return (None, None)
	return(min, max)


L = input( )
Llist = L.split(", ")
print(Llist)
intLlist = list(map(int, Llist))
#print(list(intLlist))
print(findMinAndMax(intLlist))
