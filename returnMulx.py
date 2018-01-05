#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(120, 132, 24, math.pi / 6)
print(x, y)
'''

import math
def quadratic(a, b, c):
	temp = math.sqrt(b * b - 4 * a * c)
	x_1 = (-b + temp) / (2 * a)
	x_2 = (-b - temp) / (2 * a)
	return x_1, x_2

x, y = quadratic(1, 5, 4)
print(x, y)
