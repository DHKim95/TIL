from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (N+1)

def DFS(graph, V, visited):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            DFS(graph, i, visited)

DFS(graph, V, visited)

print()
visited2 = [False] * (N+1)

def BFS(graph, start, visited2):
    queue = deque([start])
    visited2[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

BFS(graph, V, visited2)