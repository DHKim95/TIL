# BFS 시간초과 ㅠ
M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

visited = [[-1] * N for _ in range(M)]

# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    # 한가지 경로의 수 도달
    if x == M-1 and y == N-1:
        return 1

    # 이미 방문한 곳 패스
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < M and 0 <= ny < N and graph[x][y] > graph[nx][ny]:
            # 지금까지 살아온거 다 더해주기
            visited[x][y] += DFS(nx, ny)

    return visited[x][y]

print(DFS(0, 0))

# 시간을 줄이기 위한 새로운 방법 -> DFS + DP