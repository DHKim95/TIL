from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def BFS(graph, v, visited):
    visited[v] = 1
    queue = deque([v])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

lst = [0]
for i in range(1, N+1):
    visited = [0] * (N + 1)
    BFS(graph, i, visited)
    lst.append(sum(visited))

max_value = max(lst)
for i in range(len(lst)):
    if max_value == lst[i]:
        print(i, end=' ')