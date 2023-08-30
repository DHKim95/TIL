N, M = map(int, input().split())

graph = [[1e9] * (N+1) for _ in range(N+1)]
visited = [[0] * (N+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     graph[i][i] = 0

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x][y] = cost
    graph[y][x] = cost
    visited[x][y] = y
    visited[y][x] = x

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                visited[a][b] = visited[a][k]

for i in range(1, N+1):
    visited[i][i] = '-'

for i in visited[1:]:
    print(*i[1:])
