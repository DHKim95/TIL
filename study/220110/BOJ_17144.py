R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

time = 0
while time < T:
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                cnt = 0
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]
                    if 0 <= nx <= R and 0 <= ny <= C and graph[i][j] != -1:
                        visited[nx][ny] += (graph[i][j] // 5)
                        cnt += 1

                graph[i][j] -= (graph[i][j] // 5) * cnt

    # 확산 미세먼지 합치기
    for i in range(R):
        for j in range(C):
            graph[i][j] += visited[i][j]




    time += 1


print(graph)
print(visited)