from collections import deque

N, M, S, E = map(int, input().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1, N + 1):
    city = [True for _ in range(N + 1)]
    visited = [1 for _ in range(N + 1)]
    
    if i == S or i == E:
        print(-1)
    else:
        city[i] = False
        mincnt = 99999
        dq = deque()
        dq.append(S)        
        while dq:
            cur_v = dq.popleft()
            # print("*", cur_v)
            for next_v in edges[cur_v]:
                if visited[next_v] == 1 and city[next_v] == True:
                    visited[next_v] = visited[cur_v] + 1
                    if next_v == E:
                        # 어차피 한 번 밖에 안간다..! min은 한 번 바뀐다.
                        mincnt = visited[next_v]
                        break
                    else:
                        dq.append(next_v)
            
        if mincnt == 99999:
            print(-1)
        else:
            print(mincnt)
