# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def cal(w, r) :
	return (w * (1 + r/30))
w, r = map(int, input().split())
print(int(cal(w,r)))