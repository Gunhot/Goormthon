# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
H, M = map(int, input().split())
for _ in range(N):
	c = int(input())
	M += c
	while M >= 60 :
		H += 1
		if H >= 24 :
			H = 0
		M -= 60

print(H, M)