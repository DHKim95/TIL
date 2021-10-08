dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < N and 0 <= ny < N and (graph[nx][ny] == graph[x][y] + 1):
            return True
    return False


T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N+1)

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                visited[graph[i][j]] = 1

    print(visited)
