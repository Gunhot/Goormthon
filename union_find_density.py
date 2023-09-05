import sys
input = sys.stdin.readline
v_n, e_n = map(int, input().split())
parent = list(range(v_n + 1))

count = [1 for _ in range(v_n + 1)]
member = [[] for _ in range(v_n + 1)]
#입력 완료

def find_parent(x) :
	if parent[x] == x :
		return x
	else : 
		parent[x] = find_parent(parent[x])
		return parent[x]


def union(f, t) :
	f_p = find_parent(f)
	t_p = find_parent(t)
	#나의 edge 그대에게로
	if f_p != t_p :
		parent[t_p] = f_p
		count[f_p] += count[t_p]
		count[t_p] = 0
	#밀도 반영
	else:
		count[f_p] += 1
	# print("f_p", f_p, "t_p", t_p)
	# print(count)

for _ in range(e_n) :
	f, t = map(int, input().split())
	union(f, t)
	
for c in range(1, v_n+1) :
	p = find_parent(c)
	member[p].append(c)
# print(member)

max_ratio = -1  
max_i = -1  

# 위에 대로 하면 하나씩 더 큰 값 나옴 <- 왠지 모름 ㅋㅋㄹㅃㅃ
for i in range(len(count)):
	if count[i] > 0:
		count[i] -= 1

# 가장 밀도가 높은 컴포너트를 출력한다.
for i in range(len(count)):
	if len(member[i]) > 0:  
		ratio = count[i] / len(member[i])
		if ratio > max_ratio:
			max_ratio = ratio
			max_i = i
		# 조건: 1을 만족하는 컴포넌트가 여러개라면
		elif ratio == max_ratio:
			if len(member[i]) < len(member[max_i]):
				max_ratio = ratio
				max_i = i
			# 조건: 2를 만족하는 컴포넌트가 여러개라면
			elif len(member[i]) == len(member[max_i]):
				if min(member[i]) < min(member[max_i]):
					max_ratio = ratio
					max_i = i
print(*member[max_i])
# m = max(parent)
