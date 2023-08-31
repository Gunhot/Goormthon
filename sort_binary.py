# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())
a_list = list(map(int, input().split()))

def change_to_binary(a) :
	c = ""
	while a != 0 :
		if a % 2 == 1 :
			c = "1" + c
		else :
			c = "0" + c
		a = a // 2
	return c

def count_one(str) :
	cnt = 0
	for i in range(len(str)):
		if str[i] == '1':
			cnt += 1
	return cnt

def main(a_list, n, k):
	a_list.sort(key=lambda x : (count_one(change_to_binary(x)), x), reverse=True)
	# print(a_list)
	print(a_list[k - 1])

main(a_list, n, k)	
