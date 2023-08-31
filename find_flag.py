n,k = map(int, input().split())
M = []
for _ in range(n):
	temp = list(map(int, input().split()))
	M.append(temp)


def cal(y, x) :
	options = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	result = 0
	if M[y][x] != 1 :
		for op in options:
			new_y = y + op[0]
			new_x = x + op[1]
			if 0 <= new_y <= n-1 and 0 <= new_x <= n-1:
				if M[new_y][new_x] == 1:
					result += 1
	return result

F = [[0 for _ in range(n)] for _ in range(n)]

ans = 0
for i in range(n):
	for j in range(n):
		if cal(i, j) == k:
			ans += 1
print(ans)