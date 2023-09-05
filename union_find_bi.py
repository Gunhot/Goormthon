import sys
input = sys.stdin.readline
v_n, e_n = map(int, input().split())
parent = list(range(v_n + 1))

#입력 완료

def find_parent(x) :
	if parent[x] == x :
		return x
	else : 
		parent[x] = find_parent(parent[x])
		return parent[x]

def union(f, t) :
	f = find_parent(f)
	t = find_parent(t)
	if f != t :
		parent[t] = f

edges = [[] for _ in range(v_n + 1)]

for _ in range(e_n) :
	f, t = map(int, input().split())
	for v in edges[t]:
		if v == f:
			union(f, t)
			break
	edges[f].append(t)

for i in range(1, v_n+1) :
	find_parent(i)

answer = len(set(parent[1:]))
print(answer)