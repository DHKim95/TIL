from collections import deque

K = int(input())
W, H = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ddx = [-2, -2, -1, -1, 1, 1, 2, 2]
ddy = [-1, 1, -2, 2, -2, 2, -1, 1]

def BFS():
    queue = deque()
    queue.append((0, 0, K))

    visited = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]
    while queue:
        x, y, k = queue.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != 1and visited[nx][ny][k] == 0:
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx, ny, k))
        if k > 0:
            for i in range(8):
                nx = x + ddx[i]
                ny = y + ddy[i]
                if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != 1 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k-1))
    return -1

print(BFS())