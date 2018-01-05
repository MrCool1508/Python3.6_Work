#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def trim(s):
	n = 0
	while s[0] == ' ':
		s = s[1:]
	while s[-1] == ' ':
		s = s[:-1]
	return s

s = input()
print(trim(s))

