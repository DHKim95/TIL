T = int(input())

for tc in range(T):
    N = int(input())
    graph = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0 or i == j:
                graph[i][j] = 1
            else:
                graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

    print("#{}".format(tc + 1))
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                continue
            else:
                print(graph[i][j], end=' ')
        print()


