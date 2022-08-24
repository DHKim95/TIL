from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def BFS(i, j):
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 0:
                    cnt[x][y] += 1
    return 1


queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day_cnt = 0

while True:
    visited = [[0] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    arr = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == 0:
                arr.append(BFS(i, j))

    for i in range(N):
        for j in range(M):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(arr) == 0:
        print(0)
        break
    if len(arr) >= 2:
        print(day_cnt)
        break
    day_cnt += 1