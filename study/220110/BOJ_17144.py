from collections import deque

R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

air_machine = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_machine.append([i, j])

for time in range(T):
    arr = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 공기청정기가 아니면
            if graph[i][j] != -1:
                cnt = 0
                # 4방향 탐색
                for direction in range(4):
                    nx, ny = i + dx[direction], j + dy[direction]


                    if 0 <= nx < R and 0 <= ny < C:
                        if graph[nx][ny] != -1:
                            cnt += 1
                            arr[nx][ny] += (graph[i][j] // 5)

                arr[i][j] += (graph[i][j] - (graph[i][j] // 5) * cnt)
            else:
                arr[i][j] = -1

    graph = arr

    for i in reversed(range(1, air_machine[0][0] + 1)):
        graph[i][0] = graph[i-1][0]

