R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]

alpha_set = set(graph[0][0])
max_value = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, cnt):
    global max_value
    max_value = max(max_value, cnt)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in alpha_set:
                alpha_set.add(graph[nx][ny])
                DFS(nx, ny, cnt+1)
                alpha_set.remove(graph[nx][ny])

DFS(0, 0, max_value)
print(max_value)