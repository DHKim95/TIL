from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def BFS(k, v):
    visited = [0] * (N+1)
    queue = deque()
    queue.append(v)
    visited[v] = 1
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # 방문안했고 추천 이상이면
            if not visited[i[0]]:
                if i[1] >= k:
                    queue.append(i[0])
                    cnt += 1
                    visited[i[0]] = 1
    return cnt

for _ in range(Q):
    K, V = map(int, input().split())
    answer = BFS(K, V)
    print(answer)