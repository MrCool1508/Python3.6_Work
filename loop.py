#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###for循环###
#sum = 0
#for x in range(101):
#	sum += x
#print(sum)

###while循环###
#sum = 0
#n = 99
#while n > 0:
#	sum += n
#	n -= 2
#print(sum)

###print list###
#L = ['Bart', 'Lisa', 'Adam']
#for name in L:
#	print(name)

###break###
n = 1
while n <= 100:
#	if n > 20:
#		break
	n += 1
	if n % 2 == 0:
		continue
	print(n)

print('END')
