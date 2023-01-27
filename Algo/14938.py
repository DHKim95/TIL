N, M, R = map(int, input().split())

item_list = [0] + list(map(int, input().split()))
graph = [[1e7] * (N+1) for _ in range(N+1)]

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# print(graph)
max_cnt = 0
for value in graph:
    cnt = 0
    for i in range(1, N+1):
        if value[i] <= M:
           cnt += item_list[i]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)