# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

def cal(a, c, b) :
	if c == '+' :
		return (a + b)
	elif c == '-' :
		return (a - b)
	elif c == '*' :
		return (a * b)
	elif c == '/' :
		return (a // b)

sum = 0
for _ in range(n):
	a, c, b = input().split()
	sum += cal(int(a), c, int(b))
print(sum)