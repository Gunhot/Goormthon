n, m, k = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range (m):
	a, b = map(int, input().split())
	edge[a].append(b)
	edge[b].append(a)

visited = [False for _ in range(n + 1)]
cur = k
visited[cur] = True
while True:
	targets = []
	for i in edge[cur]:
		if visited[i] == False:
			targets.append(i)
	if len(targets) == 0:
		print(visited.count(True), cur)
		exit()
	target = min(targets)
	visited[target] = True
	cur = target
