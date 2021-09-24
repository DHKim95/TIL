from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 벽을 벗어나면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 방문했던곳 다시 가지 않기
            if visited[nx][ny] != -999:
                continue

            queue.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1

T = int(input())

# Test케이스
for tc in range(T):
    N, M = map(int, input().split()) # N개의 줄 M개의 길이
    graph = [list(input()) for _ in range(N)]
    visited = [[-999] * M for _ in range(N)] # 방문표시

    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'W':
                queue.append((i,j))
                visited[i][j] = 0

    bfs()
    cnt = 0
    for i in range(N):
        cnt += sum(visited[i])

    print("#{} {}".format(tc+1, cnt))