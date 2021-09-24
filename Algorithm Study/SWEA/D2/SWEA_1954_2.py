T = int(input())

for tc in range(T):
    N = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    graph = [[0] * N for _ in range(N)]  # 그래프
    idx = 0
    x, y = 0, -1 # 현재위치

    for num in range(1, N*N+1):
        new_X = x + dx[idx]
        new_Y = y + dy[idx]

        # 범위안에 있고 값이 0이면
        if (0 <= new_X) and (new_X < N) and (0 <= new_Y) and (new_Y < N) and graph[new_X][new_Y] == 0:
            graph[new_X][new_Y] = num
            x = new_X
            y = new_Y
        else: # 범위를 벗어나거나 값이 있으면
            idx = (idx+1) % 4
            x += dx[idx]
            y += dy[idx]
            graph[x][y] = num

    print("#{}".format(tc+1))
    for s in graph:
        print(*s)