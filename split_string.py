# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
s = input()

scores = set()
cases = []

def divide_string(s, parts, result=[]):
    if parts == 0:
        if not s:
            cases.append(result)
            for _ in range(len(result)):
                scores.add(result[_])
        return
    for i in range(1, len(s) + 1):
        divide_string(s[i:], parts - 1, result + [s[:i]])

divide_string(s, 3)
scores = sorted(scores)


cases_score = []
for i in range(len(cases)):
	sum = 0
	for j in range(len(cases[i])):
		sum += scores.index(cases[i][j])
	cases_score.append(sum)
print(max(cases_score) + 3)