from collections import deque

N, M, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = deque()
queue.append((0, 0, 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 987654321

while queue:
    # 공주 찾으면 끝
    x, y, t = queue.popleft()
    if (x, y) == (N-1, M-1):
        cnt = min(cnt, t)
        break

    # 시간 지나면 그냥 끝
    if t+1 > T:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, t+1))
            elif graph[nx][ny] == 2:
                visited[nx][ny] = 1
                now = t + 1 + abs(nx-(N-1)) + abs(ny-(M-1))
                if now <= T:
                    cnt = now

if cnt > T:
    print("Fail")
else:
    print(cnt)
