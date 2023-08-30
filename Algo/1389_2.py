N, M = map(int, input().split())

graph = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(N):
    graph[k][k] = 0
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_value = float('inf')
answer = 0
for idx in range(N):
    hap = sum(graph[idx])
    if min_value > hap:
        min_value = hap
        answer = idx

print(answer+1)