#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cmptwostrings(str1,str2):
	len1 = len(str1)
	len2 = len(str2)
	b = True
	if len1 != len2:
		print('两个字符串不同')
		b = False
	elif len1 == len2:
		for i in range(len1):
			if str1[i] != str2[i]:
				b = (b and False)
				break
			else:
				b = (b and True)
	if b == True:
		print('两个字符串相同')
	elif b == False:
		print('两个字符串不同')

if __name__ == "__main__":
	cmptwostrings('baby','baby')
