def DFS(x):
    global cnt
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            cnt += 1
            DFS(i)


N = int(input())
K = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1)

print(cnt)