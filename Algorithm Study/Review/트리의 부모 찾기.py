from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
lst = [0] * (N+1)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                lst[i] = x
                queue.append(i)
                visited[i] = True

BFS(graph, 1, visited)

for i in range(2, N+1):
    print(lst[i])