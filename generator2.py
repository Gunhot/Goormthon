from collections import deque

n, k = map(int, input().split())
building = [0 for _ in range(31)]

maps = []
for _ in range(n):
	maps.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(y, x):
	q = deque()
	q.append((y,x))
	cur_t = maps[y][x]
	maps[y][x] = 0
	visited[y][x] = True
	dy = [-1, 0, 0, 1]
	dx = [0, -1, 1, 0]
	cnt = 1
	while q:
		cur_y, cur_x = q.popleft()
		for _ in range(4):
			new_y = cur_y + dy[_]
			new_x = cur_x + dx[_]
			if 0 <= new_y < n and 0 <= new_x < n:
				if maps[new_y][new_x] == cur_t and not visited[new_y][new_x]:
					q.append((new_y, new_x))
					visited[new_y][new_x] = True
					cnt+=1
	# print(cur_t, cnt)
	if cnt >= k:
		building[cur_t] += 1




for y in range(n):
	for x in range(n):
		if not visited[y][x]:
			bfs(y, x)

# print(building)
max_indices = [i for i, value in enumerate(building) if value == max(building)]
print(max_indices[-1])