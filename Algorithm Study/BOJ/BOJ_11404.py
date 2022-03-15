import sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[10000001] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 10000001:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
