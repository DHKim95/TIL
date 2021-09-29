from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    queue.append((0,0,1))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while queue:
        x, y, h = queue.popleft()
        # 최종 도착 지점에 도달하면 반환
        if x == N-1 and y == M-1:
            return visited[x][y][h]

        # 4가지 방향 탐색
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 범위안에 있으면
            if 0 <= nx < N and 0 <= ny < M:
                # 벽일 경우에 벽 하나 부수고 하기
                if graph[nx][ny] == 1 and h == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                # 벽이 아닐 경우에 방문안했으면 방문
                elif graph[nx][ny] == 0 and visited[nx][ny][h] == 0:
                    visited[nx][ny][h] = visited[x][y][h] + 1
                    queue.append((nx, ny, h))
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

print(BFS())