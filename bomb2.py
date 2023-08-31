n, k = map(int, input().split())
maps = []
for _ in range(n):
	maps.append(list(input().split()))
bombs = [[0 for _ in range(n)] for _ in range(n)]

def change(y, x):
	if maps[y][x] == '@':
		bombs[y][x] += 2
	if maps[y][x] == '0':
		bombs[y][x] += 1

def bomb(y, x):
	options = [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)]
	for o in options:
		new_y = y + o[0]
		new_x = x + o[1]
		if 0 <= new_y < n and 0 <= new_x < n:
			if maps[new_y][new_x] != '#':
				change(new_y, new_x)

for _ in range(k):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	bomb(y, x)

flat_list = [value for row in bombs for value in row]

# 최댓값 찾기
max_value = max(flat_list)

print(max_value)