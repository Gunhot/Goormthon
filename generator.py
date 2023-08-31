from collections import deque

n = int(input())
maps = []
for _ in range(n):
	maps.append(list(map(int, input().split())))
	
def install(y, x):
	dy = [1, 0, 0, -1]
	dx = [0, 1, -1, 0]
	q = deque()
	q.append((y,x))
	maps[y][x] = 0
	while q:
		cur_y, cur_x = q.popleft()
		for k in range(4):
			new_y = cur_y + dy[k]
			new_x = cur_x + dx[k]
			if 0 <= new_y < n and 0 <= new_x < n:
				if maps[new_y][new_x] == 1:
					q.append((new_y, new_x))
					maps[new_y][new_x] = 0
	
ans = 0
for y in range(n):
	for x in range(n):
		if maps[y][x] == 1:
			install(y, x)
			ans += 1			
print(ans)