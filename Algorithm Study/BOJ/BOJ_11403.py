N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                # print(i, j, k)
                graph[i][j] = 1
                # print(graph)

for i in range(N):
    print(*graph[i])