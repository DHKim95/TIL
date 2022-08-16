from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            x, y = i, j
            break

queue = deque()
queue.append((x, y))
visited[x][y] = 0

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx, ny = x + direction[k][0], y + direction[k][1]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            if graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            elif graph[nx][ny] == 0:
                visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()