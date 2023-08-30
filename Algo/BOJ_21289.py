N, M = map(int, input().split())

graph = [[987654321] * (N+1) for _ in range(N+1)]
min_value = 987654321
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자신 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N):
    for j in range(2, N+1):
        if i == j:
            continue
        value = 0
        for k in range(1, N+1):
            value += min(graph[k][i], graph[k][j]) * 2
        if value < min_value:
            min_value = value
            answer = [i, j, min_value]

print(*answer)