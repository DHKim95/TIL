T = int(input())
for tc in range(T):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    cnt = 0
    for i in range(N//2):
        for j in range(i+1):
            if j == 0:
                cnt +=  graph[i][N//2]
            else:
                cnt += graph[i][N//2 + j]
                cnt += graph[i][N//2 - j]

    for i in range(N):
        cnt += graph[N//2][i]

    for i in range(N//2+1, N):
        for j in range(N-i):
            if j == 0:
                cnt += graph[i][N//2]
            else:
                cnt += graph[i][N // 2 + j]
                cnt += graph[i][N // 2 - j]


    print("#{} {}".format(tc+1, cnt))