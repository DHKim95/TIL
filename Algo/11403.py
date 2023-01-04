N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(graph)

for k in range(N):
    for a in range(N):
        for b in range(N):
            # 둘다 이어져있으면 갈 수 있는 길이다.
            if graph[a][k] + graph[k][b] >= 2:
                graph[a][b] = 1
            # graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()
