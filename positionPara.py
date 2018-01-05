#!/usr/bin/env python3
# -*- coding: utf-8  -*-

def power(x, n = 2):  
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s
	
x = 3
n = 5
print(power(x))
