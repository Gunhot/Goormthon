# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
s, b = map(int, input().split())

if s > b :
	s, b = b, s

b_cnt = n // b
s_pie = n % b
s_cnt = 0
while (True):
	if s_pie % s == 0:
		s_cnt = s_pie // s
		print(b_cnt + s_cnt)
		break
	else :
		b_cnt -= 1
		s_pie += b
		if (b_cnt < 0):
			print(-1)
			break