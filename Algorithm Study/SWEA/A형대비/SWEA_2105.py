dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def DFS(x, y, count, direction):
    global cnt
    if x == i and y == j and direction == 3:
        if cnt < count:
            cnt = count
        return

    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < N and 0 <= ny < N and visited[graph[nx][ny]] == 0:
        visited[graph[nx][ny]] = 1
        DFS(nx, ny, count + 1, direction)
        visited[graph[nx][ny]] = 0

    if direction < 3:
        direction += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < N and 0 <= ny < N and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            DFS(nx, ny, count + 1, direction)
            visited[graph[nx][ny]] = 0
    return


T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * 101
    cnt = 0

    for i in range(N):
        for j in range(N):

            DFS(i, j, 0, 0)

    if cnt > 0:
        print("#{} {}".format(tc+1, cnt))
    else:
        print("#{} {}".format(tc+1, -1))