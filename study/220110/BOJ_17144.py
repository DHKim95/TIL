from collections import deque

R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dust_lst = deque()
air_machine = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_machine.append((i, j))
            air_machine.append((i+1, y))
            break

# 미세먼지 담기
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                dust_lst.append((i, j, graph[i][j]))

    while dust_lst:
        x, y, dus = dust_lst.popleft()
        cnt = 0
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                graph[nx][ny] += dus // 5
                graph[x][y] -= dus // 5

    graph2 = [l[:] for l in graph]
    for x in range(R):
        for j in range(C):
            if x == air_machine[0][0] and air_machine[0][1] < y < C:
                graph[x][y] = graph2[x][y-1]