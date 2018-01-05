#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'others:', kw)

person('Bob', 30, gender = 'M', city = 'Shanghai')
'''
'''
def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age:', age, 'other:', kw)

person('Cherry', 24, city = 'Beijing', addr = 'Haidian')
'''

def product(*args):
	pro = 1
	for n in args:
		pro = pro * n

	return pro

print(product(5, 6, 10))
