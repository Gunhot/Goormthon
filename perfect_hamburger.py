# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
ingre = list(map(int,input().split()))

max_index = ingre.index(max(ingre))
if ingre[0:max_index] == sorted(ingre[0:max_index]) :
	if ingre[max_index:] == sorted(ingre[max_index:], reverse=True):
		print(sum(ingre))
		exit()
print(0)