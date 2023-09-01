from collections import deque

N = int(input())

a, b = map(int, input().split()) # 촌수계산사람

M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x]+1
                queue.append(i)

BFS(a)

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)