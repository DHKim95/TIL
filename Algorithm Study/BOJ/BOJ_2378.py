N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
graph_b = [list(map(int, input().split())) for _ in range(N)]

arr = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = graph[i][j] + graph_b[i][j]

for i in range(N):
    print(*arr[i])